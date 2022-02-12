from selenium import webdriver
from math import *

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_class_name('btn.btn-primary')
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x=browser.find_element_by_id('input_value').text
    a=calc(x)

    input1=browser.find_element_by_id('answer')
    input1.send_keys(a)

    submit = browser.find_element_by_class_name('btn.btn-primary')
    submit.click()


finally:
    print(browser.switch_to.alert.text)
    browser.quit()