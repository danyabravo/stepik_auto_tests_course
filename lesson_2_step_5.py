import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
browser=webdriver.Chrome()

try:
    # заходим на сайт
    browser.get("http://suninjuly.github.io/math.html")
    # находим значение x
    x_element = browser.find_element_by_css_selector('span#input_value.nowrap')
    x = x_element.text
    # вычисляем значение
    y = calc(x)

    # вводим получившееся значение
    input1=browser.find_element_by_css_selector('input#answer.form-control')
    input1.send_keys(y)
    # отмечаем чек-бокс 'I'm the robot'
    option1 = browser.find_element_by_css_selector("label.form-check-label[for='robotCheckbox']")
    option1.click()
    # отмечаем radiobutton 'Robots rule'
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    # нажимаем кнопку 'submit'
    option3 = browser.find_element_by_css_selector("button.btn.btn-default")
    option3.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()