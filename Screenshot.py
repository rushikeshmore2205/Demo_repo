import time

from selenium import webdriver

yz=webdriver.Chrome()
yz.get('https://www.flipkart.com/')

time.sleep(3)

yz.get_screenshot_as_file("C:\\Users\\rushi\\OneDrive\\Pictures\\Screenshots\\.screenshot.png")










