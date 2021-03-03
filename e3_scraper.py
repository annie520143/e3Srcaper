from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import time


from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

"""options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument('user-agent={userAgent}')
options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
#options.add_argument('--user-data-dir')"""

#driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver.exe')
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

#login
driver.get("https://portal.nycu.edu.tw/#/login?redirect=%2F")
driver.find_element_by_id('account').send_keys('0616308')
driver.find_element_by_id('password').send_keys('159357456Annie')
driver.find_element_by_class_name('login').click()

portal_handle = driver.current_window_handle

#find e3
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/a[1]/li').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="pane-全部"]/div[4]/div/div[1]/a').click()

time.sleep(3)

handles = driver.window_handles

for handle in handles:
    if handle != portal_handle:
        e3_handle = handle

driver.switch_to.window(e3_handle)

soup = BeautifulSoup(driver.page_source, 'html.parser')

time.sleep(10)
driver.quit()