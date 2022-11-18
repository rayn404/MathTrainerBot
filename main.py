from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress', 'localhost:9014')
"""
"C:\Program Files\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9014 --user-data-dir="C:\test\Chrome_Test_Profile"
"""
driver = webdriver.Chrome(options=options)

def start_new():
    button = driver.find_element(By.CLASS_NAME, "start")
    button.click()

start_new()