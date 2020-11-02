import os
class Config(object):
	BOT_TOKEN = os.environ.get('BOT_TOKEN', ' 1234567890:Paste_BotTokenHereI')
	USERNAME = os.environ.get('USER_NAME', 'your@email.com')
	PASSWORD = os.environ.get('PASSWORD', 'password')
