import logging
from config import Config
from bot import updater, dp, browser
from telegram.ext import CommandHandler, run_async
from telegram import ChatAction
import os
import pickle
import time
from os import execl
from sys import executable


@run_async	
def zoom(update, context):
	logging.info("DOING")

	def students(context):
		browser.find_element_by_xpath('//*[@id="wc-container-left"]/div[4]/div/div/div/div[1]').click()
		number = browser.find_element_by_xpath('//*[@id="wc-footer"]/div/div[2]/button[1]/div/div/span').text
		print(number)
		if(int(number) <10):
			context.bot.send_message(chat_id=451311925, text="Your Class has ended!")
			browser.find_element_by_xpath('//*[@id="wc-container-left"]/div[4]/div/div/div/div[1]').click()
			browser.find_element_by_xpath('//*[@id="wc-footer"]/div/div[3]/div/button').click()
			browser.quit()
			execl(executable, executable, "chromium.py")
	try:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		
		usernameStr = Config.GUSERNAME
		passwordStr = Config.GPASSWORD

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

			browser.get('https://zoom.us/google_oauth_signin')
			time.sleep(7)

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

		time.sleep(5)
		browser.find_element_by_xpath('//*[@id="voip-tab"]/div/button').click()

		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="wc-footer"]/div/div[2]/button[1]').click()

		time.sleep(2)
		# browser.find_element_by_xpath('//*[@id="participant-window"]/div[2]/div/div/div[2]/div/button[2]').click()
		browser.find_element_by_xpath('//*[@id="wc-container-right"]/div/div[2]/div/button[2]').click()

		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Attending you lecture. You can chill :v")
		logging.info("STAAAAPH!!")

	
	except Exception as e:
		browser.quit()
		context.bot.send_message(chat_id=update.message.chat_id, text="Error occurred! Fix error and retry!")
		context.bot.send_message(chat_id=update.message.chat_id, text=str(e))
		execl(executable, executable, "chromium.py")

	j = updater.job_queue
	j.run_repeating(students, 1000, 20)