from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("#book")
    WebDriverWait(browser, 15, 0.5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(str(y))
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
