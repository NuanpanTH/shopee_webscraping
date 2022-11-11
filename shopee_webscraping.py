from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import pandas as pd
import numpy as np
from time import sleep
from random import randint
import time

##############################################################

driver = webdriver.Chrome()
driver.get('https://shopee.co.th/')
time.sleep(5)
thai_button = driver.find_element('xpath', '//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button')
thai_button.click()
time.sleep(3)
close_button = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close_button.click()
time.sleep(3)
search = driver.find_element('xpath', '//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
search.send_keys('ไมโครเวฟและเตาอบ')
search.send_keys(Keys.ENTER)
time.sleep(5)

all_product_list = []
all_price_list = []
all_sales_list = []
all_links_list = []

for i in range(44):
    driver.execute_script("document.body.style.zoom='10%'")
    time.sleep(5)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data)
    elements = soup.find_all('div', {'class': 'shopee-search-item-result__item'})
    for element in elements:
        all_product = element.find_all('div', {'class':'ie3A+n bM+7UW Cve6sh'})
        if len(all_product) > 0:
            all_product_list.append(all_product[0].text)
        all_price = element.find_all('div', {'class': 'vioxXd rVLWG6'})
        if len(all_price) > 0:
            all_price_list.append(all_price[0].text)
        all_sales = element.find_all('div', {'class': 'ZnrnMl'})
        if len(all_sales) > 0:
            all_sales_list.append(all_sales[0].text)
        all_links = element.find_all('a', {'data-sqe': 'link'})
        if len(all_links) > 0:
            all_links_list.append('https://shopee.co.th' + all_links[0]['href'])
    driver.execute_script("document.body.style.zoom='100%'")
    time.sleep(5)
    next_button = driver.find_element('xpath', '//*[@id="main"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/button[2]')
    next_button.click()

all_stores_list = []
driver = webdriver.Chrome()
for link in all_links_list:
    driver.get(link)
    time.sleep(5)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data)
    elements = soup.find_all('div', {'class':'_3LoNDM'})
    time.sleep(6)
    if len(elements) > 0:
        all_stores_list.append(elements[0].text)
    else: all_stores_list.append('None')