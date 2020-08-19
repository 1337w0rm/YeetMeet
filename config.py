import os
class Config(object):
	HEROKU_APP_NAME = os.environ['HEROKU_APP_NAME']
	BOT_TOKEN = os.environ['BOT_TOKEN']