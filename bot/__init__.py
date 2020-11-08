import logging
from telegram.ext import Updater
from config import Config

from selenium import webdriver

#Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token = Config.BOT_TOKEN, use_context=True)
dp = updater.dispatcher

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