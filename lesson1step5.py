from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(str(y))
    
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    
    option = browser.find_element_by_css_selector("#robotsRule")
    option.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()