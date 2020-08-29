# YEET MEET

YEET MEET is a telegram bot which can be deployed to a server, heroku or on your local machine. It can attend your google meet classes for you.

## Deploy to Local Machine and Server

> Replace the variables in [config.py](https://github.com/1337w0rm/YeetMeet/blob/master/config.py)

    BOT_TOKEN = Your Telegram Bot Token
    USERNAME = Your google username or email through which you want to join the meeting
    PASSWORD = Your google account password

	
 1. Download and Install Google Chrome and Chromedriver.
 2. `git clone https://github.com/1337w0rm/YeetMeet`
 3. `cd YeetMeet`
 4. `pip install -r requirements.txt`
 5. `python chromium.py` 

## Deploy to Heroku
**One Click Deploy**

> Note: In one click deploy you will have to re-login every day.
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/1337w0rm/YeetMeet)

**Conventional Deploy**

> Note: Login to your Google account from your local machine first, so that you don't have to re-login again and again on Heroku.


> Replace the variables in config.py

    BOT_TOKEN = Your Telegram Bot Token
    USERNAME = Your google username or email through which you want to join the meeting
    PASSWORD = Your google account password

1. Download and Install Google Chrome and Chromedriver.
 2. `git clone https://github.com/1337w0rm/YeetMeet`
 3. `cd YeetMeet`
 4. `pip install -r requirements.txt`
 5. `python chromium.py`
 6. Login to your Google Account.
 7. Now through Heroku-CLI login to your Heroku account
 8. Create a Heroku App `heroku create appname`
 9. Select this app in your Heroku-CLI `heroku git:remote -a appname`
 10. Commit the changes `git commit -am "Your commit message"`
 11. Push Code to Heroku `git push heroku master`
 12. Scale the dynos `heroku ps:scale worker=1`