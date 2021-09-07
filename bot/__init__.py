import os
from telegram.ext import Updater
from config import Config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

try:
	BASE_DIR = os.path.dirname(os.path.realpath(__file__))
	print(BASE_DIR)
	s = BASE_DIR + '/Profile/'
	w = '/app/bot/Profile/'
#	g = /app/vendor/geckodriver/geckodriver
	print (s)
#	b = BASE_DIR + '/firefox/firefox/firefox'
	q = '/app/vendor/firefox/firefox'
	binary = FirefoxBinary(q)
	updater = Updater(token = Config.BOT_TOKEN, use_context=True)
	dp = updater.dispatcher
	options = webdriver.FirefoxOptions()
	options.add_argument("-profile")
	options.add_argument(w)
	#profile = FirefoxProfile()
	#profile.set_preference("dom.webdriver.enabled", False)
	#profile.set_preference('useAutomationExtension', False)
	#profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/60.0.3112.50 Safari/537.36")
	#profile.update_preferences()
	desired = DesiredCapabilities.FIREFOX
	options.add_argument("--disable-infobars")
	options.add_argument("--headless")
	#options.add_argument("--window-size=1200,800")
	options.add_argument("--disable-blink-features=AutomationControlled")
	#browser = webdriver.Firefox(options=options, firefox_profile=profile, desired_capabilities=desired, service_args=["--marionette-port", "2828"])
	browser = webdriver.Firefox(options=options, executable_path='/app/vendor/geckodriver', firefox_binary=binary, desired_capabilities=desired, service_args=["--marionette-port", "2828"])
	#browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
except Exception as e:
	print(e)
