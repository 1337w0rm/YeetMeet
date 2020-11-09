import logging
import os
from telegram.ext import CommandHandler, run_async
from telegram import ChatAction
from config import Config
from os import execl
from sys import executable
from bot import updater, dp, browser
from bot.meet import meet
from bot.zoom import zoom

@run_async
def restart(update, context):
    restart_message = context.bot.send_message(chat_id=update.message.chat_id, text="Restarting, Please wait!")
    # Save restart message object in order to reply to it after restarting
    browser.quit()
    execl(executable, executable, "chromium.py")

@run_async
def status(update, context):
	browser.save_screenshot("ss.png")
	context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
	mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
	os.remove('ss.png')

@run_async
def meetexit(update,context):
	context.bot.send_message(chat_id=update.message.chat_id, text="Exiting meeting")
	browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[9]/div[2]/div[2]/div').click()
	browser.quit()
	execl(executable, executable, "chromium.py")

@run_async
def zoomexit(update,context):
	context.bot.send_message(chat_id=451311925, text="Exiting Zoom Meeting")
	browser.find_element_by_xpath('//*[@id="wc-container-left"]/div[4]/div/div/div/div[1]').click()
	browser.find_element_by_xpath('//*[@id="wc-footer"]/div/div[3]/div/button').click()
	browser.quit()
	execl(executable, executable, "chromium.py")

def main():
	dp.add_handler(CommandHandler("zoom", zoom))
	dp.add_handler(CommandHandler("meet", meet))
	dp.add_handler(CommandHandler("restart", restart))
	dp.add_handler(CommandHandler("status", status))
	dp.add_handler(CommandHandler("meetexit", meetexit))
	dp.add_handler(CommandHandler("zoomexit", zoomexit))
	logging.info("Bot started")

	updater.start_polling()

if __name__ == '__main__':
    main()