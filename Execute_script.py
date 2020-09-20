from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time
import math

# функция для расчета у
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для переменной х
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text 
    y = calc(x)

    # скроллим вниз
    browser.execute_script('window.scrollBy(0, 100);')

    # заполняем поле
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(y))

    # отмечаем checkbox
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()

    # отмечаем radiobutton
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    # отправка формы
    button = browser.find_element_by_tag_name('button') 
    button.click() 

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()