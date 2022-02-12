from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element_by_name("firstname")
    fname.send_keys('Иван')

    lname = browser.find_element_by_name("lastname")
    lname.send_keys('Иванов')

    email = browser.find_element_by_name("email")
    email.send_keys('Иванов@mail.ru')

    current_dir=os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path=os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла

    select_file = browser.find_element_by_id("file")
    select_file.send_keys(file_path) # отправляем файл

    submit = browser.find_element_by_tag_name("button")
    submit.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()