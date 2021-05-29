# [NOTE] If you get Couldn't Sign In or App not Secure error while logging in. Create and use a fresh google account.


# YEET MEET (Telegram Group: https://t.me/YeetMeetTG)

YEET MEET is a telegram bot which can be deployed to a server, heroku or on your local machine. It can attend your Google Meet and Zoom classes for you. You can also schedule meetings and it will automatically join at the given time.

## Bot Commands

    /mlogin - Login to Meet
    /zlogin - Login to Zoom
    /meet - Command to join Google Meet classes or metting
    /zoom - Command to join Zoom Meeting
    /status - Sends screenshot of the web page
    /exit - Exit Meeting
    /timatable - Shows todays meeting schedule
    
## Usage
	
	Join Google Meeting
    /meet https://meet.google.com/agr-ghts-ade
    
    Join Zoom Meeting
    /zoom 12354674654 ax56rR
	
    Get screenshot of the web page
    /status

    Exit Google Meet or Zoom Meeting
    /exit

	If you've set SCHEDULER in config.py to True

	Use /timetable to get todays schedule



## [config.py](https://github.com/1337w0rm/YeetMeet/blob/schedule/config.py) Explained

**BOT_TOKEN** : You can get the BOT TOKEN from Bot Father on Telegram. [Here is a guide on how to create and new bot and get it's BOT_TOKEN](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)

**GUSERNAME**  : Your Email/Google username. 
				Example: `aditya@gmail.com/aditya`

**GPASSWORD** : Your Gmail/Google password

**SCHEDULER** :  If you want to use scheduler on bot set this to `TRUE` else set it to `False

**USERID**` : Set this to your Telegram User ID. [Guide to get your Telegram User ID](https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android#Finding-Your-Personal-Chat-ID) 

## Setup Scheduler
> If you want to use Scheduler set SCHEDULER to True in [config.py](https://github.com/1337w0rm/YeetMeet/blob/schedule/config.py)

1. cd YeetMeet
2. cd bot
3. python [schedule.py](https://github.com/1337w0rm/YeetMeet/blob/schedule/bot/schedule.py)

The scheduler.py script will guide you to setup schedule for your meetings. It stores the schedule in a CSV file. 


## Deploy to Linux Machine and Linux Server

> Set ENVIRONMENT VARIABLES according to VARIABLES in [config.py](https://github.com/1337w0rm/YeetMeet/blob/master/config.py)
 OR
See [How to edit config.py](https://github.com/1337w0rm/YeetMeet/issues/3#issuecomment-694277739)
	
 1. Download and Install Google Chrome and Chromedriver.
 2. `git clone https://github.com/1337w0rm/YeetMeet`
 3. `cd YeetMeet`
 4. `pip install -r requirements.txt`
 5. `python chromium.py` 

## Deploy to Heroku

> Note: Login to your Google account from your local machine first by sending /mlogin or /zlogin command to your bot on Telegram, so that you don't have to re-login again and again on Heroku. This will create a meet.pkl or zoom.pkl file in your YeetMeet directory depending on the command sent to Telegram Bot respectively 

For Zoom, logging in is kinda buggy right now. Will try to fix it in some weeks.

> Set ENVIRONMENT VARIABLES according to VARIABLES in [config.py](https://github.com/1337w0rm/YeetMeet/blob/master/config.py)
 OR
See [How to edit config.py](https://github.com/1337w0rm/YeetMeet/issues/3#issuecomment-694277739)

**Prerequisite**
 
 1. You need to have Python3 installed.
 2. You need Heroku-CLI installed on your system. [Installation Guide Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
 3. You need to have Google Chrome and Chromedriver installed and in your PATH Environment Variable.
 
**Deployment**
1. Download and Install Google Chrome and Chromedriver.
 2. `git clone https://github.com/1337w0rm/YeetMeet`
 3. `cd YeetMeet`
 4. `pip install -r requirements.txt`
 5. `python chromium.py`
 6. Login to your Google Account using `/mlogin`  for meet and `/zlogin` for Zoom. Wait till you get `Logged In` message from your bot.
 7. Now through Heroku-CLI login to your Heroku account. 
 `heroku login -i`
 8. Create a Heroku App `heroku create appname --buildpack heroku/python`
 9. Set Chromedriver Builpack `heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver -a appname`
 10. Set Google Chrome buildpack `heroku buildpacks:add https://github.com/1337w0rm/heroku-buildpack-google-chrome -a appname`
 11. **Optional** If you've set SCHEDULE to `True` you need to set your timezone on Heroku. `heroku config:add TZ="Asia/Kolkata"` change it to your timezone by using TZ="Your timezone". For India it is TZ="Asia/Kolkata"
 
 13. Initialize git repository  `git init`
 14. Select this app in your Heroku-CLI `heroku git:remote -a appname`
 15. Add all files to `git add .`
 16. Commit the changes `git commit -am "Your commit message"`
 17. Push Code to Heroku `git push heroku master`
 18. Scale the dynos `heroku ps:scale worker=1`

