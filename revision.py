# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/?stype=lo&jlou=AffjgGX4DMzgwoK0XaipoWQnSMaMVdJSG7jz9SDKHDXpDL3fPuERGT9uuuWo671cgWmHXsaBdNdcX3taaOsTlNAwSwzX8eLuK1GOweAV0izEYw&smuh=19993&lh=Ac9DtZCc-dbX3oUSYlo")
# driver.maximize_window()
# time.sleep(2)
# driver.minimize_window()
# print(driver.title)
# print(driver.current_url)       ##print url in output
# driver.close()
# driver.quit()
import time

# driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_nxqtetlae_e&adgrpid=60571832564&hvpone=&hvptwo=&hvadid=486387378181&hvpos=&hvnetw=g&hvrand=17347261584313486042&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040235&hvtargid=kwd-296458789801&hydadcr=14452_2154371&gclid=CjwKCAjwkaSaBhA4EiwALBgQaOTCn5l1RGzC_AentIyZs-kzi7ykfemUO7PRBpWz9zi-XD-j6ZIcpRoCZpEQAvD_BwE")
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)

# abc=driver.find_element(By.XPATH,"//input[@id='email']")
# abc.send_keys('rushi@123')
# cde=driver.find_element(By.ID,"pass")
# cde.send_keys("12345")
# time.sleep(2)
# fgh=driver.find_element(By.NAME,'login')
# fgh.click()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
# find=driver.find_element(By.ID,"placeholderText")
# print(find.get_attribute('placeholder'))


#####=================================================

# intt=driver.find_element(By.ID,"dropOption2")
# print(intt.is_displayed())

##===================================================
# ddriver=driver.find_element(By.ID,"radioButton1")
# print(ddriver.is_selected())

# ##==================================================
# inputElement = driver.find_element(By.ID, "myTextInput2")
# print("Is enabled :", inputElement.is_enabled())

##---------------------------------------------------

#ORANGE HRMS

# from selenium import webdriver

# driver=webdriver.Chrome()
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# driver.maximize_window()
# time.sleep(2)
# pilot=driver.find_element(By.NAME,"username")
# pilot.send_keys("Admin")
# time.sleep(2)
# pilot1=driver.find_element(By.NAME,"password")
# pilot1.send_keys("admin123")
# driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()


###Dropdown options

# driver=webdriver.Chrome()
# driver.get('https://seleniumbase.io/demo_page')
# driver.maximize_window()
# slc=driver.find_element(By.ID,'mySelect')
#
# slc.click()
#
# open=Select(slc)
# time.sleep(3)
# open.select_by_visible_text('Set to 50%')
# time.sleep(3)
#
# open.select_by_index(2)
# time.sleep(3)
#
# open.select_by_value("100%")
#
# print(len(open.options))         ##4 dropdown optionns

###====================================================================

#=======Alerts==========================================================

from selenium import  webdriver

driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button').click()
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
driver.switch_to.alert.send_keys('hello')
driver.switch_to.alert.accept()

##=============================================================================



