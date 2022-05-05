"""
Created by: louisenaud on 5/5/22 at 12:29 PM for python_toold.
"""
from selenium import webdriver
from time import sleep

website = 'https://www.pythonguides.com'

driver = webdriver.Firefox()
driver.get(website)
sleep(2)
driver.get_screenshot_as_file("screenshots/capture.png")