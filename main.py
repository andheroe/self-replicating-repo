import os

from flask import Flask, redirect, url_for
from flask_api import status
from flask_dance.contrib.github import github, make_github_blueprint
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "youllnevercrackme")

app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")

app.register_blueprint(blueprint=make_github_blueprint(),
                       url_prefix="/login")

host_username = os.environ.get("GITHUB_USERNAME", 'mykhaly')
repo_name = os.environ.get("REPOSITORY_NAME", "self-replicating-repo")


def get_link_to_repo(username, repo):
    return f"https://github.com/{username}/{repo}"

@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))

    user_resp = github.get("/user")
    if not user_resp.ok:
        return "Something went wrong when trying to get logged user's data. " \
               "Try refreshing a page. If it doesn't help - write to " \
               "yurkamykhalchuk@gmail.com"

    link_to_repo = get_link_to_repo(user_resp.json()["login"], repo_name)

    fork_resp = github.post(f'/repos/{host_username}/{repo_name}/forks')

    if not fork_resp.ok:
        if fork_resp.status_code == status.HTTP_404_NOT_FOUND:
            return f"You are trying to fork your own repo or the repo does not exist. {host_username}/{repo_name}. " + \
                   "user data: {}".format(user_resp.json())
        return "Something went wrong when trying to fork the repo. Try refreshing a page. " \
               "If it doesn't help - write to yurkamykhalchuk@gmail.com. "

    return f"You have successfully cloned a repository. URL: {link_to_repo}"


if __name__ == "__main__":
    app.run()
