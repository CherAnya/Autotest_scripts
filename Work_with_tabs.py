from selenium import webdriver
import time
import math

# функция для расчета у
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    # нажимаем на кнопку
    button = browser.find_element_by_tag_name('button') 
    button.click() 

    second_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(second_window)

    # считываем значение для переменной х
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # заполняем поле
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)   

    # отправка формы
    button = browser.find_element_by_class_name('btn')
    button.click() 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла