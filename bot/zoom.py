import logging
from config import Config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bot import updater, browser
from telegram.ext import run_async
from telegram import ChatAction
import os
import pickle
import time
from os import execl
from sys import executable

userId = Config.USERID

def joinZoom(context, url_meet, passStr):

    def students(context):
        print("Running Student Check")

        browser.find_element_by_xpath('//*[@id="wc-container-left"]/div[4]/div/div/div/div[1]').click()
        number = WebDriverWait(browser, 2400).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wc-footer"]/div/div[2]/button[1]/div/div/span'))).text
        print(number)
        if(int(number) <10):
            context.bot.send_message(chat_id=userId, text="Your Class has ended!")
            browser.quit()
            execl(executable, executable, "chromium.py")
    try:
        name = "Vansh Santoshi"
        browser.get('https://zoom.us')
        browser.get('https://zoom.us/wc/join/'+ url_meet)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#inputname"))).click()
        for i in range(0, 20):
            browser.find_element(By.CSS_SELECTOR, "#inputname").send_keys(Keys.BACK_SPACE)
        browser.find_element(By.CSS_SELECTOR, "#inputname").send_keys(name)
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#joinBtn"))).click()
        print("Clicked on join button")

        try:
            logout = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "SIGN IN")))
            print("User is logged out. Logging in them again")
            browser.get("https://zoom.us/google_oauth_signin")
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wLBAL"))).click()
            time.sleep(10)
            browser.get('https://zoom.us')
            browser.get('https://zoom.us/wc/join/'+ url_meet)
            WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#inputname"))).click()
            for i in range(0, 20):
                browser.find_element(By.CSS_SELECTOR, "#inputname").send_keys(Keys.BACK_SPACE)
            browser.find_element(By.CSS_SELECTOR, "#inputname").send_keys(name)
            WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#joinBtn"))).click()
            print("Clicked on join button after logging in")

        except NoSuchElementException:
            print("User is already logged in. Continuing")
        except Exception as e:
            print(e)
            print("Probably, Terms and policies agreement isnt asked for.")
        try:
            for button in WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(., 'Continue')]"))):
                 button.click()
                 print("Trying to click the continue button")
        except Exception as e:
            print(e)
            print("Is it a good error, or a bad error ? Sore wa.... yami no nakae")
        try:
            WebDriverWait(browser, 2400).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputpasscode"]'))).send_keys(passStr)
            print("Entered the code")
        except:
            context.bot.send_message("Meeting didn't start. Probably Cancelled")

        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#joinBtn"))).click()
        print("Clicked join after entering passcode")
        time.sleep(15)
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid  = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
        context.bot.send_message(chat_id=userId, text="Attending you lecture. You can chill :v")
        logging.info("STAAAAPH!!")
#Join Audio Part
        try:
             action = webdriver.ActionChains(browser)
             action.move_by_offset(100, 100).perform()
             WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".join-audio-container__btn"))).click()
             WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".join-audio-by-voip"))).click()
             WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".join-dialog__close"))).click()
        except Exception as e:
             print(e)
             print("Maybe the dialog got closed by itself, or the website layout has changed ?")
#########
#        context.bot.delete_message(chat_id=userId ,message_id = mid)
#        browser.save_screenshot("ss.png")
#        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
#        mid = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
#        os.remove('ss.png')

        WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="voip-tab"]/div/button'))).click()

        WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wc-footer"]/div/div[2]/button[1]'))).click()

        WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="wc-container-right"]/div/div[2]/div/button[2]'))).click()


    except Exception as e:
        browser.save_screenshot("ss.png")
        context.bot.send_chat_action(chat_id=userId, action=ChatAction.UPLOAD_PHOTO)
        mid  = context.bot.send_photo(chat_id=userId, photo=open('ss.png', 'rb'), timeout = 120).message_id
        os.remove('ss.png')
        context.bot.send_message(chat_id=userId, text="Got some error, forward this to telegram group along with pic")
        context.bot.send_message(chat_id=userId, text=str(e))

    j = updater.job_queue
    j.run_repeating(students, 20, 1000)

@run_async
def zoom(update, context):
    logging.info("DOING")

    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)

    url_meet = update.message.text.split()[1]
    passStr = update.message.text.split()[2]
    joinZoom(context, url_meet, passStr)
