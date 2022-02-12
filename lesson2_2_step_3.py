import time
from selenium.webdriver.support.ui import Select


from selenium import webdriver

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    sum1 = str(num1 + num2)

    Select(browser.find_element_by_tag_name("select")).select_by_value(sum1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()