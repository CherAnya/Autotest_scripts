from selenium import webdriver
import time
import math

# функция для расчета у
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для переменной х
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex') 
    y = calc(x)

    # заполняем поле
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    # выбираем checkbox
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()

    # выбираем radiobutton
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

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