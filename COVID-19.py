from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import sys

sys.stdout = open('result.txt', 'w')


driver = webdriver.Chrome("chromedriver")
driver.get("https://kosis.kr/covid/covid_index.do")

def situ():
    cl = driver.find_element(By.CSS_SELECTOR, '#byDateTab')
    cl.click()
    today = driver.find_elements(By.CLASS_NAME, 'DashboardBox.Type3')[1].text
    today = re.sub(r"[^0-9\s]", "", today)
    tmp = today.split('\n')
    result = []
    for idx in range(len(tmp)):
        if not tmp[idx] == '':
            result.append(tmp[idx])
    print(result)

situ()