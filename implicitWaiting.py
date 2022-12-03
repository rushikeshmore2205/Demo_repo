import time

from selenium import webdriver
from selenium.webdriver.common.by import By

atom=webdriver.Chrome()
atom.get('https://the-internet.herokuapp.com/dynamic_loading/2')
atom.find_element(By.XPATH,'//*[@id="start"]/button').click()
time.sleep(6)
# print(atom.find_element(By.XPATH,'//*[@id="finish"]/h4').text)    #............method1

atom1=atom.find_element(By.XPATH,'//*[@id="finish"]/h4').text     #..............method2
# print(atom1)



