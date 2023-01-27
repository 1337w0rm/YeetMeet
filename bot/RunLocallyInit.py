import os
from telegram.ext import Updater
from config import Config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

try:
	BASE_DIR = os.path.dirname(os.path.realpath(__file__))
	print(BASE_DIR)
	s = BASE_DIR + '/Profile/'
	print (s)
	updater = Updater(token = Config.BOT_TOKEN, use_context=True)
	dp = updater.dispatcher
	options = webdriver.FirefoxOptions()
	options.add_argument("-profile")
	options.add_argument(s)
	#profile = FirefoxProfile()
	#profile.set_preference("dom.webdriver.enabled", False)
	#profile.set_preference('useAutomationExtension', False)
	#profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74  Safari/537.36")
	#profile.update_preferences()
	desired = DesiredCapabilities.FIREFOX
	options.add_argument("--disable-infobars")
	#options.add_argument("--headless")
	#options.add_argument("--window-size=1200,800")
	options.add_argument("--disable-blink-features=AutomationControlled")
	#browser = webdriver.Firefox(options=options, firefox_profile=profile, desired_capabilities=desired, service_args=["--marionette-port", "2828"])
	browser = webdriver.Firefox(options=options, desired_capabilities=desired, service_args=["--marionette-port", "2828"])
	#browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
except Exception as e:
	print(e)
