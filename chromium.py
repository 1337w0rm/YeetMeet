import logging
import os
from telegram.ext import CommandHandler, Job, run_async
from telegram import ChatAction
from config import Config
from os import execl
from sys import executable
from bot import updater, dp, browser

# if(Config.SCHEDULE == False):
from bot.meet import meet
from bot.zoom import zoom
# else:
from bot.meet_schedule import mJobQueue
from bot.zoom_schedule import zJobQueue

@run_async
def restart(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Restarting, Please wait!")
    # Save restart message object in order to reply to it after restarting
    browser.quit()
    execl(executable, executable, "chromium.py")

@run_async
def status(update, context):
    browser.save_screenshot("ss.png")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120)
    os.remove('ss.png')

def main():
    
    j = updater.job_queue

    # if Config.SCHEDULE == False:
    dp.add_handler(CommandHandler("zoom", zoom))
    dp.add_handler(CommandHandler("meet", meet))
    # else:
    # mJobQueue()
    zJobQueue()
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CommandHandler("status", status))

    logging.info("Bot started")

    updater.start_polling()

if __name__ == '__main__':
    main()
