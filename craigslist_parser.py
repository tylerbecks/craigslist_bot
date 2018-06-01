import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
# from selenium.webdriver.chrome.options import Options

from selenium import webdriver
service = webdriver.chrome.service.Service('./chromedriver')
service.start()
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options = options.to_capabilities()
# driver = webdriver.Remote(service.service_url, options)
# driver.get("https://www.youtube.com")


class CraigslistParser(object):
    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
        service = webdriver.chrome.service.Service('./chromedriver')
        service.start()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options = options.to_capabilities()
        self.driver = webdriver.Remote(service.service_url, options)
        # self.driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'), chrome_options=chrome_options)

    def parse(self, url):
        self.driver.get(url)
        reply_button = self.driver.find_element_by_css_selector('.reply_button')
        reply_button.click()
        time.sleep(3)
        t = self.driver.page_source
        print (t)

        if reply_button.is_displayed():
            #wait = WebDriverWait(self.driver, 100)
            #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'reply-email-address')))
            email_address = self.driver.find_elements_by_xpath("//*[contains(text(), 'sale.craigslist')]")
            print('email' + str(email_address))
            for address in email_address:
                print (address.text)
        else:
            print('I fucked up')

        # self.driver.close()

c = CraigslistParser()
c.parse('https://sfbay.craigslist.org/nby/for/d/10-piece-ceramic-duck-napkin/6489910463.html')
