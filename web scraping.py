from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycondsjjbbdfghj")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(20)
driver.close()