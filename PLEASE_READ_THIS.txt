Install firefox browser on your pc,

Go to link about:profiles

Click make new profile,

Give it a name that you can remember 

Click "Launch the profile in new window"

Change preferences and settings of that profile according to video i sent in telegram
( You can skip the theme and looks changing stuff i did in the video, except that do everything else i did in the video )

Then, close both the browser windows entirely,

then open firefox again as you normally would,

Go to about:profiles again,

You will notice that your default profile has changed to the one you've just made,
we dont want that 

So, choose your old default profile as default again, restart the browser

Open about:profiles again, you will find yourself back to the old profile.

Click "Launch profile in new window" in your profile you just made for yeetmeet

Go to zoom.us

Scroll down to last,

Find "Cookie Preference"

Click it, slide it to "Advertising Cookies"

Click save, then click close.

Then, head to zoom.us/signin

Sign in to your account, before that make sure to tick the checkbox "Keep me Signed in"

After logging in, never open any zoom link ever again except zoom.us on that profile ( through 
opening zoom.us you can verify if you're still logged in on your that profile, 
by seeing at the top right corner of page, you know ) 


I'm asking to not open any other link again, because zoom very often clear the cookies.


So, after zoom login, go normally login to google too, just like you do 


After that, attend one zoom and one google meet meetings, it can just be 
your own meeting.


After that, your profile is ready, close that profile window

Head to about:profiles again, 
Click "Open Directory" on your yeetmeet profile ( make sure you are NOT opening the ".cache" one )

After that , file manager will pop up, select ALL files and folder, and copy.

Go to YeetMeetCode/bot/Profile folder and paste it ALL there.

After that, Click "Remove profile" on that profile you made after copying, so you won't mess up with it again

Open bot/zoom.py with a code editor ONLY, and find for word "Vansh Santoshi" , replace it with your name



Now, make new app on heroku, you can use old one too,

Go to App Settings --> Reveal Config Variables --> Add :
BOT_TOKEN   ( You can get this from @BotFather on telegram )
USERID      ( You can get this from @userinfobot )
SCHEDULE    ( Set to either True or False, according to your needs )

Variables with their respective value.

Click "Add Buildback", under the same setting page, and add this:

https://github.com/buitron/firefox-buildpack
http://github.com/buitron/geckodriver-buildpack
heroku/python

Now, head to your YeetMeetSourceCode folder in terminal and enter these commands

heroku login -i
rm .git -rf
git init
heroku git:remote -a <Your Heroku App Name Here>
git add .
git commit -am "YeetMeet Deploy"
heroku buildpacks:add --index 1 heroku-community/apt
git push heroku master
heroku ps:scale worker=1

It'll take time to deploy, and i guess I'm not forgetting something to tell. Just send a message on YeetMeet telegram
if you got any problems 

There are video tutorials for it both in Linux and Windows, on the telegram group
