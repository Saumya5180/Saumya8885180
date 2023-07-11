# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.indeed.jobs/")
time.sleep(5)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("xpath","/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/select")
time.sleep(3)
search_bar.send_keys("canada")
time.sleep(4)
# Submitting the search query
find_icon = driver.find_element("xpath", "/html/body/div[1]/div/div/div/main/div/article/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/button")
find_icon.click()
time.sleep(5)

city_icon = driver.find_element("xpath", "/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/form/div/div[2]/div/div/span/input")
time.sleep(5)
city_icon.send_keys("Kitchener")
time.sleep(5)

job_icon = driver.find_element("xpath", "/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/form/div/button")
job_icon.click()
time.sleep(5)
# Closing the webdriver
driver.close()