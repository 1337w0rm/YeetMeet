## Setting up local browser
 1. Install **Firefox** browser on your PC.
 2. Open **Firefox** and enter **about:profiles** in the URL bar.
 3. Click make new profile.
 4. Give it a name that you can remember .
 5. Click "Launch the profile in new window"
 6. Change preferences and settings of that profile according to video i sent in telegram( You can skip the theme and looks changing stuff i did in the video, except that do everything else i did in the video )
 7. Now, restart **Firefox**
 8. Go to **about:profiles** again.
 9. You will notice that your default profile has changed to the one you've just made. **We dont want that** 
 10. So, choose your old default profile as default again, restart the browser
 11. Open about:profiles again, you will find yourself back to the old profile.
 12. Click "Launch profile in new window" in your profile you just made for **YeetMeet**
 
## Setting up Accounts
 1. Now, go to Google and **login** to your **Google Account**.
 2. After that open `https://zoom.us`   
 3. Scroll down to last and find **Cookie Preference**
 4. Click on it. A pop up box will open.
 5. Slide the slider  present inside the pop up box to **Advertising Cookies**
 6. Click save, then click close the pop up box.
 7. Then, head to https://zoom.us/signin
 8. Sign in to your account using **Google**.

**Note:** After logging in, never open any zoom link ever again except zoom.us on that profile ( through 
opening zoom.us you can verify if you're still logged in on your that profile, 
by seeing at the top right corner of page, you know ) 

I'm asking to not open any other link again, because zoom very often clear the cookies.


9. After all the above steps, attend one zoom and one google meet meetings. It can  be your own meeting.


10. After that, your browser profile is ready, close that profile window
11. Head to **about:profiles** again. Click **Open Directory** on your **YeetMeet** profile ( make sure you are NOT opening the ".cache" one )
12. File manager will pop up, from there **select all files and folder** and copy.
13. Now, go to YeetMeetCode/bot/Profile folder and paste the files that you just copied.
14. Click "Remove profile" on that profile you made after copying, so you can't mess up with it again

Open bot/zoom.py with a code editor ONLY, and find for word "Vansh Santoshi" , replace it with your name

# Setting up Heroku

 1. Now, go to **Heroku** make new app or you can use old one.
 2. Go to App Settings --> Reveal Config Variables --> Add :

BOT_TOKEN   ( You can get this from @BotFather on telegram )
USERID      ( You can get this from @userinfobot )
SCHEDULE    ( Set to either True or False, according to your needs )

## First Deploy

3. Now, open your terminal and `cd` to your **YeetMeet** code directory.
4. Now Login to Heroku ->`heroku login -i`
5. Delete **.git** folder ->`rm .git -rf`
6. Initialize git repository  with ->`git init`
7. Select on which app to push the code.

    `heroku git:remote -a <Your Heroku App Name Here>`
    **Note**: Your Heroku App Name Here is the name that you gave while creating the app on Heroku.

8. Add files for pushing -> `git add .`
9. Commit Files -> `git commit -am "YeetMeet Deploy"`
10. Push the code -> `git push heroku master`
11. Turn on Worker Dyno -> `heroku ps:scale worker=1`


## Second and final deploy

12. Click **Add Buildback**, under the setting page of your heroku app, and add these:

    `https://github.com/buitron/firefox-buildpack`

    `http://github.com/buitron/geckodriver-buildpack`

13. Make an empty text file inside YeetMeet code folder, and name it anything.

14. Now, enter these on same terminal where you just did your first deploy.

    `git add .`

    `git commit -am "Commit"`

    `heroku buildpacks:add --index 1 heroku-community/apt`

    `git push heroku master`

15. Check if build and app launch was successful

    `heroku logs --tail`

If you face any problem send a text on Just  YeetMeet Telegram Group.
