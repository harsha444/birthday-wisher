import webbrowser
import requests, bs4
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time

# function for connecting to browser
def browser_connect():
    browser = webdriver.Firefox()
    browser.get('http://www.facebook.com')
    return browser

# Fixing notification error(call it depending on time it is appearing)
def check_notification():
    wait = ui.WebDriverWait(browser, 10)
    noti_res = wait.until(lambda browser: browser.find_element_by_css_selector('.layerCancel'))
    if noti_res:
        noti_res.click()


# Authenticating user
def authenticate():
    elem = browser.find_element_by_tag_name('#email')
    # Asking for user email or phone number
    elem.send_keys('<Your Facebook ID/Mobile number here>')
    # ASking for password
    elem2 = browser.find_element_by_tag_name('#pass')
    elem2.send_keys('<Your password here>')
    elem2.submit()


def check_css_selector(val):
    wait = ui.WebDriverWait(browser, 10)
    result = wait.until(lambda browser: browser.find_element_by_css_selector(val))
    return result

# For finding and clicking events bar
def find_events_bar():
    results = check_css_selector('#navItem_2344061033')
    results.click()

# For finding and clicking birthday bar
def find_birthday_bar():
    results = check_css_selector('div._2yaa:nth-child(3) > a:nth-child(1) > span:nth-child(1)')
    results.click()

# Checking if there are any birthdays
def check_for_birthdays():
    results = check_css_selector('#birthdays_today_card')
    return results

def wish_happy_bday(results):
    if results:
        i=1
        wish = results.find_elements_by_xpath("//*[@id='birthdays_content']/div[1]/div[2]/ul/li[1]");
        # find_element_by_xpath('.//textarea[@aria-label="Write a birthday wish on his Timeline..."]')
        while(len(wish) > 0 ):
            wish1 = wish[0].find_elements_by_xpath(".//textarea")
            if(len(wish1) > 0):
                wish1[0].send_keys("Happy b'day..!!")
                #wish1.submit()
                time.sleep(0.5)
            else:
                pass
            i=i+1
            wish = results.find_elements_by_xpath("//*[@id='birthdays_content']/div[1]/div[2]/ul/li["+str(i)+"]");

        browser.quit()
        print("Done for the day..!!")
    else:
        browser.quit()


browser = browser_connect()
authenticate()
find_events_bar()
check_notification()
find_birthday_bar()
results = check_for_birthdays()
wish_happy_bday(results)