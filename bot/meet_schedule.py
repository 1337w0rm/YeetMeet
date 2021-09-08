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
from bot.meet import joinMeet

meeting_list = list()

def convertTime(string_time):
    hour = string_time.split(':')[0]
    minute = string_time.split(':')[1]

    datetime_str = f'{datetime.date.today().strftime("%m/%d/%y")} {hour}:{minute}:00'
    datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

    return datetime_object


class Meeting():
    def __init__(self, name, day, time, link):
        self.name = name
        self.time = convertTime(time)
        self.link = link

def getTodayMeetings():
    try:
        with open('bot/meet.csv') as file:
            read = csv.reader(file, delimiter=',')
            meet_count = 0
            for row in read:
                meet_count += 1
                if row[1] == datetime.datetime.today().strftime('%A'):
                    meeting = Meeting(row[0], row[1], row[2], row[3])
                    meeting_list.append(meeting)
    except:
        print("Google meet schedule not found. Run schedule.py to add schedule or change SCHEDULE environment variable to 'False to turn off schedule'")

def meet(context):
    logging.info("DOING")
    userId = 451311925
    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
    url_meet = context.job.context[0]
    context.bot.send_message(chat_id=userId, text="Attending " + str(context.job.context[1]))
    joinMeet(context, url_meet)

def timeTable(update, context):
    userId = Config.USERID
    
    text = "Today's meeting \n"
    for row in meeting_list:   
        text+=str(row.name) + " at " + str(row.time).split()[1] + "\n"
    context.bot.send_message(chat_id=userId, text=text)


def mJobQueue():
    logging.info("Adding Google Meet meetings to schedule")
    getTodayMeetings()

    j = updater.job_queue
    
    for row in meeting_list:
        secs = (row.time - datetime.datetime.now()).total_seconds()
        if(secs > 0):
            print(secs)
            j.run_once(meet, secs, context=(row.link, row.name))

