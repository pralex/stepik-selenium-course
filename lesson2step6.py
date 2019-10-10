from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from math import *


try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text
    result = log(abs(12*sin(int(x))))

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(str(result))    
    
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    
    option = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option)
    option.click() 
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()