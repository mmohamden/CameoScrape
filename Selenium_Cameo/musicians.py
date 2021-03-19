import csv
import time
import json
import pandas as pd 
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from time import sleep

import requests
import lxml.html
import os.path
import re
import os
import bs4 
import sys
import webbrowser
from random import randint
import numpy as np
from selenium.webdriver.firefox.options import Options as FirefoxOptions
firefox_options = FirefoxOptions()
firefox_options.add_argument("")


csv_file = open(r"C:\Users\admin-3\Desktop\New folder\comedians.csv", 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
pages = np.arange(0, 1320, 40)

talent_urls = []

for url in pages:
     driver = webdriver.Firefox(executable_path = r"C:\webdriver\geckodriver.exe", options = firefox_options)
     driver.get("https://www.cameo.com/browse/comedians?nextToken="+str(url))
     window_before = driver.window_handles[0]
     
     sleep(1)
     talent_links = driver.find_elements_by_xpath('//div[@class="_2Dlx2_QaGZWKbDk8ffYv3c"]')
     #talent_urls = []

     for link in talent_links:
         talent_url = link.find_element_by_tag_name('a').get_attribute("href")
         talent_urls.append(talent_url)
     print(len(talent_urls))

     driver.switch_to.window(window_before)
     driver.close()
for url in talent_urls:
     driver = webdriver.Firefox(executable_path = r"C:\webdriver\geckodriver.exe", options = firefox_options)
     #window_after = driver.window_handles[1]
     driver.get(url)
     
     #driver.switch_to.window(window_after)
     #handles = driver.window_handles
     #size = len(handles)
     #parent_handle = driver.current_window_handle
     
     #for x in range(size):
       #if handles[x] != parent_handle:
          #driver.switch_to.window(handles[x])
          
     talent_dict = {}

     sleep(2)
     try:
         talent_name = driver.find_element_by_xpath('//P[@id="profile-bio-name"]').text
     except:
         print(f'Couldn\'t get name!')
     try:
         talent_price = driver.find_element_by_xpath('//A[@id="bookLink"]/DIV[1]/SPAN[1]/SPAN[1]').text
     except:
         print(f'Couldn\'t get price!')
     try:
         talent_category	 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/p').text
     except:
         print(f'Couldn\'t get category	!')
     try:
         talent_brief = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/span').text
     except:
         print(f'Couldn\'t get brief !')
     try:
        times = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[1]/div/div/span").text
        
     except:
         print(f'Couldn\'t get response time!')  
     try:
         review_info = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/span').text
        
     except:
         print(f'Couldn\'t get reviews!')
         review_info = "0"
     try:
         talent_rating = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div/span').text
     except:
         print(f'Couldn\'t get rating!')
         talent_rating = "0"
     try:
         talent_classification = driver.find_elements_by_xpath('//span[@class="Styled__TagText-sc-12o91u9-2 gsWxBs"]')
         classifications = []
         for item in talent_classification:
             classification = item.get_attribute('innerText')
             classifications.append(classification)
     except: print (f'Couldn\'t get Hashtag!')
     #classes = talent_classification.find_elements_by_tag_name('a').get_attribute("href")
     try:
         print('name = {}'.format(talent_name),
            'Price = {}'.format(talent_price),
            'category: {}'.format(talent_category),
             'brief	: {}'.format(talent_brief),
            'Typically responds in {}'.format(times),
            'Number of Reviews = {}'.format(review_info),
            'Rating = {}'.format(talent_rating),
            'hashtag = {}'.format(classification))
     except:
         continue

     talent_dict['Name'] = talent_name
     talent_dict['Request '] = talent_price
     talent_dict['category'] = talent_category
     talent_dict['brief'] = talent_brief
     talent_dict['ResponseTime'] = times
     talent_dict['Reviews'] = review_info
     talent_dict['Rating'] = talent_rating
     talent_dict['hashtag'] = classification
     writer.writerow(talent_dict.values())
     #driver.switch_to.window(window_before)
     driver.close()
csv_file.close()

driver.close()

