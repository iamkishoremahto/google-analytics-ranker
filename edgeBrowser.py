from selenium import webdriver
import time
import requests

import undetected_chromedriver as  uc
from undetected_chromedriver.options import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_random_joke():
   return requests.get("https://official-joke-api.appspot.com/random_joke").json()['setup']


def handle_search(profile):
    options = uc.ChromeOptions()
    options.add_argument("--user-data-dir=/home/kishorekumarmahto/.config/google-chrome/") 
    options.add_argument(f"--profile-directory={profile}") 

    driver = uc.Chrome(options=options, version_main=121)
    count = 0
    while count<40:
        driver.get("https://www.bing.com/")
        driver.find_element(By.ID,"sb_form_q").send_keys(get_random_joke())
        driver.find_element(By.ID,"sb_form_q").send_keys(Keys.ENTER)
        time.sleep(10)
        count = count +1
        print(count)
    driver.quit()

if __name__ == "__main__":  

    # 
    profileList = ["Profile 51","Profile 54","Profile 55"]
    for profile in profileList:
        handle_search(profile)
