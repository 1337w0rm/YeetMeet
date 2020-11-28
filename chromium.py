import logging
import os
from telegram.ext import CommandHandler, Job, run_async
from telegram import ChatAction
from config import Config

from os import execl
from sys import executable
from bot import updater, dp, browser

from bot.meet_login import mlogin
from bot.zoom_login import zlogin

from bot.meet import meet
from bot.zoom import zoom

if Config.SCHEDULE == True:
    from bot.meet_schedule import mJobQueue, timeTable
    from bot.zoom_schedule import zJobQueue

userId = Config.USERID

@run_async
def exit(update, context):
    context.bot.send_message(chat_id=userId, text="Restarting, Please wait!")
    browser.quit()
    execl(executable, executable, "chromium.py")

@run_async
def status(update, context):
    browser.save_screenshot("ss.png")
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120)
    os.remove('ss.png')

def main():    
    j = updater.job_queue

    dp.add_handler(CommandHandler("zoom", zoom))
    dp.add_handler(CommandHandler("meet", meet))
   
    if Config.SCHEDULE == True:
        mJobQueue()
        zJobQueue()
        dp.add_handler(CommandHandler("timetable", timeTable))

    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CommandHandler("status", status))
    
    dp.add_handler(CommandHandler("mlogin", mlogin))
    dp.add_handler(CommandHandler("zlogin", zlogin))

    logging.info("Bot started")

    updater.start_polling()

if __name__ == '__main__':
    main()
