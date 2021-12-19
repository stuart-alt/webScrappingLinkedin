from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from credentials import email, senha

url = 'https://www.linkedin.com/login'

option = Options()
option.headless = False
browser = webdriver.Firefox(options=option)
browser.get(url)
sleep(3)

input_email = browser.find_element_by_id("username")
input_email.send_keys(email)

input_senha = browser.find_element_by_id("password")
input_senha.send_keys(senha)

browser.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()

browser.get('https://www.linkedin.com/jobs/')
sleep(3)
busca = browser.find_element_by_id("jobs-search-box-keyword-id-ember40")
busca.send_keys("Python")
busca.send_keys(Keys.RETURN)
