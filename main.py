from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentials import email, senha
from time import sleep
from pandas import Series

s = Service('C:/geckodriver/geckodriver.exe')
browser = webdriver.Firefox(service=s)

url = 'https://www.linkedin.com/login'

option = Options()
option.headless = False
browser.get(url)
sleep(3)

input_email = browser.find_element(By.ID, "username")
input_email.send_keys(email)

input_senha = browser.find_element(By.ID, "password")
input_senha.send_keys(senha)

browser.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()

browser.get('https://www.linkedin.com/jobs/')
sleep(3)

busca = browser.find_element(By.ID, "jobs-search-box-keyword-id-ember39")
busca.send_keys("Python")
busca.send_keys(Keys.RETURN)
sleep(3)

jobs = browser.find_elements_by_xpath('//a[@class="disabled ember-view job-card-container__link job-card-list__title"]')

browser.close()

jobs_list = list()
for job in jobs:
    jobs_list.append(job.text)

df = Series(jobs_list)

print(df)
