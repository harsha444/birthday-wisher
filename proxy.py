import webbrowser
import requests, bs4
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

browser = webdriver.Chrome()
browser.get('http://www.facebook.com')
elem = browser.find_element_by_tag_name('#email')
elem.send_keys('9493083847')

elem2 = browser.find_element_by_tag_name('#pass')
elem2.send_keys('harsha@shm')
elem2.submit()

wait = ui.WebDriverWait(browser, 10)

results = wait.until(lambda browser: browser.find_element_by_css_selector('#navItem_2344061033'))
results.click()

wait = ui.WebDriverWait(browser, 10)
results = wait.until(lambda browser: browser.find_element_by_css_selector('div._2yaa:nth-child(3) > a:nth-child(1) > span:nth-child(1)'))
results.click()


wait = ui.WebDriverWait(browser, 10)
results = wait.until(lambda browser: browser.find_element_by_css_selector('#birthdays_today_card'))

if results:
    i=1
    wish = results.find_element_by_xpath("//*[@id='birthdays_content']/div[1]/div[2]/ul/li[1]");
    # find_element_by_xpath('.//textarea[@aria-label="Write a birthday wish on his Timeline..."]')
    while(wish):
        wish1 = wish.find_element_by_xpath(".//textarea")
        if(wish1):
            wish1.send_keys("Happy b'day ra..!!")
            wish1.submit()
            time.sleep(3)
        i=i+1
        wish = results.find_element_by_xpath("//*[@id='birthdays_content']/div[1]/div[2]/ul/li["+str(i)+"]");

# post = browser.find_element_by_css_selector('.notranslate > div:nth-child(1) > div:nth-child(1)')
# post.send_keys('testing automation')
# post.submit()
