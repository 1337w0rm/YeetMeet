from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pause
import os
import logging
from telegram.ext import Updater, CommandHandler
from telegram import ChatAction
from config import Config
import threading

#######YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# pause.until(datetime(2020, 3, 27, 11, 29))
# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)

#Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token = Config.BOT_TOKEN, use_context=True)
dp = updater.dispatcher


mode="dev"

if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=Config.BOT_TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(Config.HEROKU_APP_NAME, Config.BOT_TOKEN))


def shutdown():
    updater.stop()
    updater.is_idle = False
    updater.start_polling()

def meet(update,context):
	logging.info("DOING")
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	usernameStr = os.environ['USERNAME']
	passwordStr = os.environ['PASSWORD']
	url_meet = update.message.text.split()[-1]
	options = webdriver.ChromeOptions()
	# options.add_argument("--headless")
	options.add_argument("--disable-infobars")
	options.add_argument("--window-size=1200,800")
	options.add_argument("user-agent='User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'")
	options.add_experimental_option("prefs", { \
	    "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
	    "profile.default_content_setting_values.media_stream_camera": 2,
	     "profile.default_content_setting_values.notifications": 2
	  })
	browser = webdriver.Chrome(options=options)

	# browser.get('https://accounts.google.com/ServiceLogin?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&')

	browser.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
	browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
	
	username = browser.find_element_by_id('identifierId')
	username.send_keys(usernameStr)
	nextButton = browser.find_element_by_id('identifierNext')
	nextButton.click()
	time.sleep(7)

	browser.save_screenshot("ss.png")
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
	mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
	print(mid)
	os.remove('ss.png')

	password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
	password.send_keys(passwordStr)
	signInButton = browser.find_element_by_id('passwordNext')
	signInButton.click()
	time.sleep(7)

	context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

	browser.save_screenshot("ss.png")
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
	mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
	os.remove('ss.png')

	if(browser.find_elements_by_xpath('//*[@id="authzenNext"]/div/button/div[2]')):
		
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Need Verification. Please Verify")
		browser.find_element_by_xpath('//*[@id="authzenNext"]/div/button/div[2]').click()
		time.sleep(5)

		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')
		time.sleep(20)

	browser.get(url_meet)
	time.sleep(3)

	context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

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
	
	browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
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
	threading.Thread(target=shutdown).start()

def main():
	dp.add_handler(CommandHandler("meet", meet))
	logging.info("Bot started")
	run(updater)

if __name__ == '__main__':
    main()