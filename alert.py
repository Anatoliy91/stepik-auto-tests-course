from selenium import webdriver
import math
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/alert_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)
  button=browser.find_element_by_xpath("//button[@type='submit']")
  button.click()
  confirm = browser.switch_to.alert
  confirm.accept()

  find_value=browser.find_element_by_xpath("//span[@id='input_value']")
  x=find_value.text
  y = calc(x)
  input1 = browser.find_element_by_xpath("//input[@id='answer']")
  input1.send_keys(y)
  button=browser.find_element_by_xpath("//button[@type='submit']")
  button.click()






  # alert = browser.switch_to.alert
  # alert.accept()
  #
  # alert_text = alert.text
  # confirm = browser.switch_to.alert
  # confirm.accept()
  # confirm.dismiss()
  #
  # prompt = browser.switch_to.alert
  # prompt.send_keys("My answer")
  # prompt.accept()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()