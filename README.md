# YEET MEET

YEET MEET is a telegram bot which can be deployed to a server, heroku or on your local machine. It can attend your Google Meet and Zoom classes for you.



## Bot Commands

    /meet - Command to join Google Meet classes or metting
    /zoom - Command to join Zoom Meeting
    /status - Sends screenshot of the web page
    /restart - exit meeting before meeting end
    
    
	

## Usage
	
    Join Google Meeting
    /meet https://meet.google.com/agr-ghts-ade
    
    Join Zoom Meeting
    /zoom 12354674654 ax56rR
	
    Get screenshot of the web page
    /status

    Restarts Script and exits meeting before end
    /restart


## DIRECT METHOD by One Click Deploy - NOT RECOMMENDED

> Use only if you don't understand anything here and only want to use for google meet.

> [Create an heroku account](https://signup.heroku.com/) if you don't have one and set up the basics. Click on Deploy To Heroku.


NOTE: In Direct Method, you will have to re-login every day. Also One Click Deploy only works for Google meet somewhat. Zoom not working currently in one click deploy. Use MAIN METHOD for Zoom. Will Update Soon.



[![One Click Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/1337w0rm/YeetMeet)


## MAIN METHOD - USE THIS

1. If you are installing on linux skip to step 4, windows and mac (maybe)  need to set up few things first.
2. Make sure to have installed Git and python on your system . Search for it on internet. Figure it out yourself.
3. You need to install Build Tools in [Microsoft Visual Studio](https://visualstudio.microsoft.com/downloads/) . It requires ample data to be downloaded.
4. [Download](https://www.google.com/intl/en_in/chrome/) and Install Latest Google chrome.
5. Open your Command Line Interface CLI . Terminal for Linux and Mac. Command Prompt for Windows. Now follow the commands.
6. `git clone https://github.com/1337w0rm/YeetMeet`
7. `cd YeetMeet` Now Create Telegram Bot 



## Creating Telergam Bot and Config.py modifications
	
Open your Telegram App and Search for Botfather (blue tick). 

Type /newbot. Type Name for your bot and bot username. 

Copy  Bot token from there . It should be like this 1234567890:BUnhFbjGmmy_EcOk

Open YeetMeet user directory, the folder path that appears on your CLI. It should be somewhere on your user folder.

>Edit config.py using text editor or your choice. Replace and Set values of  variables bot token, username and password with you and save it. 


>Follow Further Instructions.



8. `pip install -r requirements.txt` if this gives some error , see fix on net or send screenshot in create new issue in github repo.
9.  Minimise CLI and Download Chrome Driver for your particular version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) .
10. Extract and paste the driver file on the YeetMeet user directory.
11. run `python chromium.py` to start Bot server on Local Machine. Chrome Brower Should open automatically here.
12. Now set Up meet.pkl and zoom.pkl files from your telegram bot. Send /zoom or /meet whatever you want to use to your bot on telegram.
13. After that send /restart to bot. 
14. If any error occurs , check config.py file or delete meet.pkl or/and zoom.pkl from your YeetMeet directory and try again.
15. You can use your bot through your local machine by sending /meet https://meet.google.com/agr-ghts-ade or /zoom 12354674654 ax56rR to join meetings on your Local Machine. See Usage and commands above.
    


## For using bot wirelessly without local machine and offline
	
16. First, Create and join a test zoom or meet meeting automatically  from local machine.
17. meet.pkl or zoom.pkl should be present in YeetMeet directory.
18. Make Sure Everything is working properly properly without errors , then only proceed next steps. For help, see above steps.
19. Make Sure [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) is installed on your Local Machine.
20. [Create an heroku account](https://signup.heroku.com/) if you don't have one and set up the basics. Now run following commands on command line.
21. Use `heroku login -i` to login to your Heroku account on command line.
22. Create a Heroku App `heroku create appname --buildpack heroku/python` Replace appname with any unique namein this and folllowing steps.
23. Set Chromedriver Builpack `heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver -a appname`
24. Set Google Chrome buildpack `heroku buildpacks:add https://github.com/1337w0rm/heroku-buildpack-google-chrome -a appname`
25. Initialize git repository  `git init`
26. Select this app in your Heroku-CLI `heroku git:remote -a appname`
27. Commit the changes `git commit -am "Commit message"`
28. Push Code to Heroku `git push heroku master`
29. Scale the dynos `heroku ps:scale worker=1`
30. The bot is now All set on Heroku sever. You can use the bot commands on telegram to join zoom or meet meetings automatically.
 
> If any error comes run `heroku apps:destroy appname` , check all previous step from 1. Then Continue from Step 22.


> For issues feel free to ask for help on github page.


