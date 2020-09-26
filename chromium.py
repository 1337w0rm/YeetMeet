from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pause
import os
import logging
from telegram.ext import Updater, CommandHandler, run_async
from telegram import ChatAction
from config import Config
from os import execl
from sys import executable
import pickle

#Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token = Config.BOT_TOKEN, use_context=True)
dp = updater.dispatcher


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--disable-infobars")
options.add_argument("--window-size=1200,800")
options.add_argument("user-agent='User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,
     "profile.default_content_setting_values.notifications": 1
  })

browser = webdriver.Chrome(options=options)



@run_async
def restart(update, context):
    restart_message = context.bot.send_message(chat_id=update.message.chat_id, text="Restarting, Please wait!")
    # Save restart message object in order to reply to it after restarting
    browser.quit()
    with open('restart.pickle', 'wb') as status:
        pickle.dump(restart_message, status)
    execl(executable, executable, "chromium.py")

def status(update, context):
	browser.save_screenshot("ss.png")
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
	mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
	os.remove('ss.png')
	
def zoom(update, context):
	logging.info("DOING")
	try:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		
		usernameStr = Config.USERNAME
		passwordStr = Config.PASSWORD

		url_meet = update.message.text.split()[1]
		passStr = update.message.text.split()[2]

		if os.path.exists("zoom.pkl"):
			cookies = pickle.load(open("zoom.pkl", "rb"))
			browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow')
			for cookie in cookies:
				browser.add_cookie(cookie)
		else:
			browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow')
			username = browser.find_element_by_id('identifierId')
			username.send_keys(usernameStr)
			nextButton = browser.find_element_by_id('identifierNext')
			nextButton.click()
			time.sleep(7)

			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')

			password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
			password.send_keys(passwordStr)
			signInButton = browser.find_element_by_id('passwordNext')
			signInButton.click()
			time.sleep(7)


			browser.get('https://zoom.us/google_oauth_signin')
			time.sleep(7)

			if(browser.find_elements_by_xpath('//*[@id="authzenNext"]/div/button/div[2]')):
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
				context.bot.send_message(chat_id=update.message.chat_id, text="Need Verification. Please Verify")
				browser.find_element_by_xpath('//*[@id="authzenNext"]/div/button/div[2]').click()
				time.sleep(5)

				browser.save_screenshot("ss.png")
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
				mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
				os.remove('ss.png')
				time.sleep(20)

			pickle.dump( browser.get_cookies() , open("zoom.pkl","wb"))

			context.bot.send_message(chat_id=update.message.chat_id, text="Logged In!")

		browser.get('https://zoom.us/wc/join/'+ url_meet)

		time.sleep(5)
		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid  = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), caption="Test", timeout = 120).message_id
		os.remove('ss.png')

		browser.find_element_by_xpath('//*[@id="joinBtn"]').click()
		time.sleep(5)
		browser.find_element_by_xpath('//*[@id="inputpasscode"]').send_keys(passStr)
		browser.find_element_by_xpath('//*[@id="joinBtn"]').click()

		time.sleep(10)

		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')

		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Attending you lecture. You can chill :v")
		pause
		logging.info("STAAAAPH!!")

	
	except:
		browser.quit()
		context.bot.send_message(chat_id=update.message.chat_id, text="Some error occurred retry!")

def meet(update,context):
	logging.info("DOING")
	try:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		usernameStr = Config.USERNAME
		passwordStr = Config.PASSWORD
		url_meet = update.message.text.split()[-1]

		if os.path.exists("meet.pkl"):
			cookies = pickle.load(open("meet.pkl", "rb"))
			browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow')
			for cookie in cookies:
				browser.add_cookie(cookie)
		else:
			browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow')
			username = browser.find_element_by_id('identifierId')
			username.send_keys(usernameStr)
			nextButton = browser.find_element_by_id('identifierNext')
			nextButton.click()
			time.sleep(7)

			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')

			password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
			password.send_keys(passwordStr)
			signInButton = browser.find_element_by_id('passwordNext')
			signInButton.click()
			time.sleep(7)


			browser.get('https://meet.google.com')
			time.sleep(7)


			if(browser.find_elements_by_xpath('//*[@id="authzenNext"]/div/button/div[2]')):
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
				context.bot.send_message(chat_id=update.message.chat_id, text="Need Verification. Please Verify")
				browser.find_element_by_xpath('//*[@id="authzenNext"]/div/button/div[2]').click()
				time.sleep(5)

				browser.save_screenshot("ss.png")
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
				mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
				os.remove('ss.png')
				time.sleep(20)

			pickle.dump( browser.get_cookies() , open("meet.pkl","wb"))
			context.bot.send_message(chat_id=update.message.chat_id, text="Logged In!")
		
		browser.get(url_meet)
		time.sleep(3)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid  = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), caption="Test", timeout = 120).message_id
		os.remove('ss.png')

		if(browser.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')):
			browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div').click()
			time.sleep(3)

			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
		try:
			browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
			time.sleep(10)
		except:
			browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]").click()
			time.sleep(10)

		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')
		time.sleep(5)

		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		time.sleep(10)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')

		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Attending you lecture. You can chill :v")
		pause
		logging.info("STAAAAPH!!")
	except:
		browser.quit()
		context.bot.send_message(chat_id=update.message.chat_id, text="Some error occurred retry!")


def main():
	dp.add_handler(CommandHandler("zoom", zoom))
	dp.add_handler(CommandHandler("meet", meet))
	dp.add_handler(CommandHandler("restart", restart))
	dp.add_handler(CommandHandler("status", status))
	logging.info("Bot started")
	updater.start_polling()

if __name__ == '__main__':
    main()