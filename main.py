from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import time
import math

options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress', 'localhost:9014')

open_prcoess = subprocess.Popen(r'"C:\Program Files\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9014 --user-data-dir="C:\test\Chrome_Test_Profile"')

driver = webdriver.Chrome(options=options)
driver.get("https://mathtrainer.io")
driver = webdriver.Chrome(options=options)

def start_new():
    driver.implicitly_wait(10)
    button = driver.find_element(By.CLASS_NAME, "start")
    button.click()

def play_round():
    driver.implicitly_wait(3)
    question = driver.find_element(By.CLASS_NAME, "math").get_attribute("innerText")
    question=question[:-1].replace(",", "")
    if (any([oper in question for oper in["+","−","×", "÷"]])):
        question = question.replace("\n","")
        if "+" in question:
            answer_list = [int(arg) for arg in question.split("+")]
            answer = answer_list[0]+answer_list[1]
        elif "−" in question:
            answer_list = [int(arg) for arg in question.split("−")]
            answer = answer_list[0]-answer_list[1]
        elif "×" in question:
            answer_list = [int(arg) for arg in question.split("×")]
            answer = answer_list[0]*answer_list[1]
        else:
            answer_list = [int(arg) for arg in question.split("÷")]
            answer = answer_list[0]/answer_list[1]
    else:
        if ("\t" in question):
            answer_list = [int(arg) for arg in question[:-5].split("\n")]
            if len(answer_list)==1:
                answer_list.append(answer_list[0])
                answer_list[0]=2
            answer = answer_list[1]**(1/answer_list[0])
        else:
            answer_list=[int(arg) for arg in question[:-1].split("\n")]
            answer = answer_list[0]**answer_list[1]          
    
    driver.find_element(By.TAG_NAME, "body").send_keys(math.ceil(answer))
    
      
while True:
    try:
        if(driver.find_element(By.CLASS_NAME, "answer").get_attribute("innerText")=="?"):
            play_round()
            time.sleep(0.2)
    except:
        start_new()