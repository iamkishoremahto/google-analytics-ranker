import random
import undetected_chromedriver as  uc
from undetected_chromedriver.options import ChromeOptions
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
from selenium.webdriver.common.by import By
import time
import pandas as pd
from retry import retry
import json



def get_random_proxy():

    # proxies = [
    #     "http://digitalmarketingteam:freeKoal37@179.61.156.210:12345",
    #     "http://digitalmarketingteam:freeKoal37@165.231.97.92:12345",
    #     "http://digitalmarketingteam:freeKoal37@154.16.20.167:12345",
    #     "http://digitalmarketingteam:freeKoal37@179.61.156.74:12345",
    #     "http://digitalmarketingteam:freeKoal37@102.165.54.234:12345",
    #     "http://digitalmarketingteam:freeKoal37@154.16.20.253:12345",
    #     "http://digitalmarketingteam:freeKoal37@102.165.54.252:12345",
    #     "http://digitalmarketingteam:freeKoal37@102.165.54.61:12345",
    #     "http://digitalmarketingteam:freeKoal37@154.16.20.220:12345",
    #     "http://digitalmarketingteam:freeKoal37@185.158.106.72:12345"
    # ]

    proxies = ["https://brd-customer-hl_17b04146-zone-datacenter_proxy1:i6qiwe32e0n1@brd.superproxy.io:22225",
               "http://brd-customer-hl_17b04146-zone-datacenter_proxy1:i6qiwe32e0n1@brd.superproxy.io:22225"]
    return random.choice(proxies)

def initialize_driver():

    options = uc.ChromeOptions()
    options.page_load_strategy = 'eager'
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

  

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-images")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--disable-popup-blocking")
    proxy = get_random_proxy()

    proxy_helper = SeleniumAuthenticatedProxy(proxy_url= proxy)

    proxy_helper.enrich_chrome_options(options)

    driver = uc.Chrome(options=options, version_main=121)
    driver.set_page_load_timeout(120)

    return driver,proxy
# @retry()
def open_website(website,timeout = 0):
    print(f"Opening website: {website}")
    
    driver,proxy = initialize_driver()
    
   
 
    start_time = time.time()
    driver.get(website)
    print(driver.title)
    if timeout > 0:
        time.sleep(timeout)
    end_time = time.time()

    driver.get("https://api.ipify.org/?format=json")

    proxyElement = driver.find_element(By.XPATH,"//pre")
    
    ip = json.loads(proxyElement.text)['ip']
    driver.quit()
    
    with open('reportData.txt', 'a') as fl:
         fl.write(f"\n{website},{ip},{timeout},{end_time - start_time}")
    return {"website":website,"proxy":ip,"sleep_time":timeout,"total_time":end_time - start_time}



if __name__ == "__main__":
        
        websites = [
             "https://www.helenzysdent.com/",
             "https://www.helenzysdent.com/dental-website/",
             "https://www.helenzysdent.com/social-media-post/",
             "https://www.helenzysdent.com/search-engine-optimization/",
             "https://www.helenzysdent.com/social-media-management/"
        ]

       
        timeDict = []
        count = 0
        while True:
            
            website = random.choice(websites)    
            data = open_website(website = website,timeout=2)
            timeDict.append(data)
        



        # websiteList = []
        # proxyList = []
        # sleepTimeList = []
        # totalTimeList = []
        # for item in timeDict:
        #      print(item)
        #      websiteList.append(item["website"])
        #      proxyList.append(item["proxy"])
        #      sleepTimeList.append(item["sleep_time"])
        #      totalTimeList.append(item["total_time"])
        # df = pd.DataFrame({"Website": websiteList, "Proxy": proxyList, "Sleep Time": sleepTimeList, "Total Time": totalTimeList})
        # df.to_excel("Report.xlsx")







