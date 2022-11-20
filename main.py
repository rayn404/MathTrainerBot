from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
import time
import math

oper = {
    "+": lambda argums: argums[0]+argums[1],
    "−": lambda argums: argums[0]-argums[1],
    "×": lambda argums: argums[0]*argums[1],
    "÷": lambda argums: argums[0]/argums[1]
}

open_prcoess = subprocess.Popen(
    r'"C:\Program Files\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9014 --user-data-dir="C:\test\Chrome_Test_Profile"')

options = webdriver.ChromeOptions()
options.add_experimental_option('debuggerAddress', 'localhost:9014')
driver = webdriver.Chrome(options=options)
driver.get("https://mathtrainer.io")


def start_new():
    driver.implicitly_wait(10)
    button = driver.find_element(By.CLASS_NAME, "start")
    button.click()


def type_number(number):
    driver.find_element(By.TAG_NAME, "body").send_keys(math.ceil(number))


def calculate(question):

    for key in oper:
        if key in question:
            type_number(oper[key]([int(arg)
                        for arg in question.replace("\n", "").split(key)]))
            return

    if ("\t" in question):
        answer_list = [int(arg) for arg in question[:-5].split("\n")]
        if len(answer_list) == 1:
            answer_list.append(answer_list[0])
            answer_list[0] = 2
        answer = answer_list[1]**(1/answer_list[0])
    else:
        answer_list = [int(arg) for arg in question[:-1].split("\n")]
        answer = answer_list[0]**answer_list[1]
    type_number(answer)


def play_round():
    driver.implicitly_wait(3)
    question = driver.find_element(By.CLASS_NAME, "math").get_attribute(
        "innerText")[:-1].replace(",", "")
    calculate(question)


while True:
    try:
        if (driver.find_element(By.CLASS_NAME, "answer").get_attribute("innerText") == "?"):
            play_round()
            time.sleep(0.2)
    except:
        start_new()
