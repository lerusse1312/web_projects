from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

PATH = "/usr/bin/geckodriver"

driver = webdriver.Firefox(executable_path=PATH)

#Open the page
driver.get("http://www.google.com")

#Get searchbar
search = driver.find_element_by_name("q")

search.send_keys("quebecsocialist")
search.submit()
time.sleep(5)
driver.find_element_by_partial_link_text("QuebecSocialist").click()

time.sleep(10)
driver.quit()