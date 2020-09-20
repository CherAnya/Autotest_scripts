from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# функция для расчета у
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    # нажимаем на кнопку 
    price = WebDriverWait(browser, 12).until(
    		EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    	)
    button1 = browser.find_element(By.ID, 'book')
    button1.click()

    # считываем значение для переменной х
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # заполняем поле
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)   

    # отправка формы
    button2 = browser.find_element_by_id('solve')
    button2.click() 

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла