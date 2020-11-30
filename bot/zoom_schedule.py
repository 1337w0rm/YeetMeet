import logging
from config import Config
from bot import updater, browser
from telegram.ext import run_async
from telegram import ChatAction
import os
import pickle
import time
from os import execl
from sys import executable
import csv
import datetime
from bot.zoom import joinZoom

meeting_list = list()

def convertTime(string_time):
    hour = string_time.split(':')[0]
    minute = string_time.split(':')[1]

    datetime_str = f'{datetime.date.today().strftime("%m/%d/%y")} {hour}:{minute}:00'
    datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

    return datetime_object


class Meeting():
    def __init__(self, name, day, time, mid, mpass):
        self.name = name
        self.time = convertTime(time)
        self.mid = mid
        self.mpass = mpass

def getTodayMeetings():
    try:
        with open('bot/zoom.csv') as file:
            read = csv.reader(file, delimiter=',')
            for row in read:
                if row[1] == datetime.datetime.today().strftime('%A'):
                    meeting = Meeting(row[0], row[1], row[2], row[3], row[4])
                    meeting_list.append(meeting)
    except:
        print("Zoom schedule not found. Run schedule.py to add schedule or change SCHEDULE environment variable to 'False' to turn off schedule")

def zoom(context):
    logging.info("DOING") 
    userId = Config.USERID
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING) 

    url_meet = context.job.context[0]
    passStr = context.job.context[1]
    context.bot.send_message(chat_id=userId, text="Attending " + str(context.job.context[2]))
    joinZoom(context, url_meet, passStr)

def zJobQueue():
    logging.info("Adding Zoom meetings to schedule")
    getTodayMeetings()

    j = updater.job_queue
    
    for row in meeting_list:
        secs = (row.time - datetime.datetime.now()).total_seconds()
        if(secs > 0):
            print(secs)
            j.run_once(zoom, secs, context=(row.mid, row.mpass, row.name))
