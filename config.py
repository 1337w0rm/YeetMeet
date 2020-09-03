import os
class Config(object):
	BOT_TOKEN = os.environ.get('BOT_TOKEN')
	USERNAME = os.environ.get('USERNAME')
	PASSWORD = os.environ.get('PASSWORD')