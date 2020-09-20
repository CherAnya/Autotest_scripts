from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для переменной х
    x_element = browser.find_element_by_id('num1')
    x = x_element.text 
    z_element = browser.find_element_by_id('num2')
    z = z_element.text    
    y = calc(x + z)

    # выбор значения из списка
    select = Select(browser.find_element_by_tag_name("select")) select.select_by_value(str(y))

    # отправка формы
    button = browser.find_element_by_class_name('btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()