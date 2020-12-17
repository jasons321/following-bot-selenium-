from selenium import webdriver
from time import sleep 
driver = webdriver.Chrome(executable_path="-")
driver.get("https://instagram.com")
sleep(4)
driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
    .send_keys(("-"))
driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
    .send_keys(("-"))
driver.find_element_by_xpath(('//button[@type="submit"]'))\
    .click()
sleep(3)
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
     .click()
sleep(3)
driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")\
     .click()
sleep(3)


for x in range(10):
    for i in range(3):
        driver.find_element_by_xpath('//button[text()="Follow"]')\
            .click()        
        sleep(2)
    driver.refresh()



