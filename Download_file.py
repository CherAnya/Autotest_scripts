from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    # заполняем поле
    input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    input1.send_keys('Anna')
    input2 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    input2.send_keys('Cheresova')
    input3 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    input3.send_keys('a@yandex.ru')

    # загрузка файла
    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'Element_search.txt')  
    element.send_keys(file_path)

    # отправка формы
    button2 = browser.find_element_by_class_name('btn')
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()