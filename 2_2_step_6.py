from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим значение x
    x = int(browser.find_element_by_id("input_value").text)
    #подставляем x в выражение
    y = calc(x)

    #находим поле для ввода текста
    input_string = browser.find_element_by_id("answer")
    #перематываем к этому полю
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_string)
    #вставляем получившееся значение в поле
    input_string.send_keys(y)

    #находим checkbox i'm the robot
    imrobot = browser.find_element_by_id('robotCheckbox')
    #нажимаем на него
    imrobot.click()

    # находим radiobutton "Robots rule!"
    robotsrule = browser.find_element_by_id('robotsRule')
    # нажимаем на него
    robotsrule.click()

    #находим кнопку "Submit"
    submit = browser.find_element_by_css_selector('button[type = "submit"]')
    # нажимаем на неё
    submit.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()