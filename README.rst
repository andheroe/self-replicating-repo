Self replicating repository
=======================================

This repository is created only to fork itself by own code. 
The code is located mainly in ``main.py`` all the other files 
in this repository are just configuration files. You can run this
code locally, or deploy it to Heroku for free to have a personal instance.

Heroku Installation
```````````````````

Step 1: Deploy to Heroku
------------------------

- Click on button: |heroku-deploy|

- Log in to Heroku if you are not logged in yet.

- Come up with a name for your application and fill the corresponding field with it.

- Do not close the page. Go to the step 2.

Step 2: Get OAuth credentials from GitHub
-----------------------------------------

- Visit https://github.com/settings/applications/new to register an
  application on GitHub. 

- Fill applicationg name field with any name. It is not required to be the
  same as Heroku app name.

- Fill homepage URL with ``https://APPNAME.herokuapp.com`` where 
  APPNAME is the same as app name from Heroku (if Heroku app name is 
  ``peaceful-lake``, homepage URL will be 
  ``https://peaceful-lake.herokuapp.com``).

- Fill the GitHub application's authorization callback URL field with 
  ``https://APPNAME.herokuapp.com/login/github/authorized`` where 
  APPNAME is the same as app name from Heroku (if Heroku app name is 
  ``peaceful-lake``, authorization callback URL will be 
  ``https://peaceful-lake.herokuapp.com/login/github/authorized``).

- You may leave description field empty, it is not required for further usage.

- Register application

Step 3: Give OAuth credentials to your app on Heroku
----------------------------------------------------

- Take client ID and client secret from your GitHub application and fill the
corresponding fields on Heroku site. 

- Click the "Deploy app".

Step 4: Visit your app and login with GitHub!
---------------------------------------------

- Click on the "View" button or visit the ``https://APPNAME.herokuapp.com``. 

- Log in to Github.

- Done! Now you have your own fork of this repo.

Local Installation
``````````````````

Step 1: Get OAuth credentials from GitHub
-----------------------------------------

- Visit https://github.com/settings/applications/new to register an
  application on GitHub. 

- Fill applicationg name field with any name. It is not required to be the
  same as Heroku app name.

- Fill homepage URL with ``http://127.0.0.1:5000``

- Fill the GitHub application's authorization callback URL field with 
  ``http://127.0.0.1:5000/login/github/authorized`` 

- You may leave description field empty, it is not required for further usage.

- Register application

Step 2: Install code and dependencies
-------------------------------------

Run the following commands on your computer::

    git clone https://github.com/mykhaly/self-replicating-repo.git
    cd self-replicating-repo
    pip3 install virtualenv
    python3 -m venv venv
    . venv/bin/activate
    pip3 install -r requirements.txt

Step 3: Set environment variables
---------------------------------

Run the following commands on your computer:

- Client id and client secret you should take from the Github applicationg you 
  registered on step 1; flask secret key is a phrase which will be used for 
  signing cookies on server, you should not reveal it to your users::

    export GITHUB_OAUTH_CLIENT_ID=YOU_SHOULD_INSERT_YOUR_VALUE_HERE
    export GITHUB_OAUTH_CLIENT_SECRET=YOU_SHOULD_INSERT_YOUR_VALUE_HERE
    export FLASK_SECRET_KEY=YOU_SHOULD_INSERT_YOUR_VALUE_HERE
    export OAUTHLIB_INSECURE_TRANSPORT=1

Step 4: Run your app and login with GitHub!
-------------------------------------------

- Run the following command on your computer::
    python github.py

- Go to http://127.0.0.1:5000/

- Log in to Github

- Done! Now you have your own fork of this repo.

How this is working:
1) User logs in using Github account
2) Github OAuth application requests access to user's data
3) The repository is forked to logged user's profile

Thanks to @singingwolfboy for his tutorial flask-dance-github, code
is massively borrowed from there.


.. |heroku-deploy| image:: https://www.herokucdn.com/deploy/button.png
   :target: https://heroku.com/deploy
   :alt: Deploy to Heroku
