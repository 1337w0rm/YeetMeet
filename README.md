# YEET MEET

YEET MEET is a telegram bot which can be deployed to a server, heroku or on your local machine. It can attend your Google Meet and Zoom classes for you. You can also schedule meetings and it will automatically join at the given time.

## Bot Commands

    /meet - Command to join Google Meet classes or metting
    /zoom - Command to join Zoom Meeting
    /status - Sends screenshot of the web page
    /exit - Exit Meeting
    /timatable - Shows todays meeting schedule
    
## Usage
	
	Join Google Meeting
    /meet https://meet.google.com/agr-ghts-ade
    
    Get list of commands
    /help
    
    Join Zoom Meeting
    /zoom 12354674654 ax56rR
	
    Get screenshot of the web page
    /status

    Exit Google Meet or Zoom Meeting
    /exit

	If you've set SCHEDULER in config.py to True

	Use /timetable to get todays schedule

**BOT_TOKEN** : You can get the BOT TOKEN from Bot Father on Telegram. [Here is a guide on how to create and new bot and get it's BOT_TOKEN](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)

**SCHEDULER** :  If you want to use scheduler on bot set this to `TRUE` else set it to `False`

**USERID** : Set this to your Telegram User ID. ( You can use @userinfobot on Telegram for that )

## Setup Scheduler
> If you want to use Scheduler set SCHEDULER to True in [config.py](https://github.com/1337w0rm/YeetMeet/blob/schedule/config.py)

1. cd YeetMeet
2. cd bot
3. python3 [schedule.py](https://github.com/1337w0rm/YeetMeet/blob/schedule/bot/schedule.py)

The scheduler.py script will guide you to setup schedule for your meetings. It stores the schedule in a CSV file. 


## Deploy to Linux Machine and Linux Server
(  I will add support for running it in local machine, please wait for some days )

## Deploy to Heroku


You would need :
1. Firefox, for making a profile your YeetMeet app will use.
2. [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and [Heroku Account](https://www.heroku.com). 
3. Git installed.
4. Some patience.
5. For remaining instructions, please read [this](https://github.com/vanshsantoshi/YeetMeet/blob/master/PLEASE_READ_THIS.txt). or, watch the videos.
