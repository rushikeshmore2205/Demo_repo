import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

atom=webdriver.Chrome()
atom.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

time.sleep(3)
###page scroll by pixel
atom.execute_script('window.scrollBy(0,3000)')


time.sleep(3)
###page scroll by upto specific element

none=atom.find_element(By.ID,'Design_philosophy_and_features')
atom.execute_script("arguments[0].scrollIntoView()",none)


###Scroll till the end page
time.sleep(2)
atom.execute_script("window.scrollBy(0,document.body.scrollHeight)")

###scroll to top by pixel
# time.sleep(3)
# atom.execute_script('window.scrollBy(0,-document.body.scrollHeight)')

###scroll to top by pixel
time.sleep(3)
atom.execute_script("window.scrollTo(0,0)")

#diff between scrollBy and scrollTo
# It is not same as scrollTo behavior. It means scrollBy always scrolls up or down further from current position.
# Or you can say scrollBy scrolls by distance from current pixels.
# Or you can say scrollBy consider current position as (0,0) and scroll further.




















###:HW:--try with another Webside

