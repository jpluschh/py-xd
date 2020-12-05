#! /usr/bin/python3

import sys
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# set up firefox profile
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.helperApps.alwaysAsk.force", False)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

# Using Chrome to access web
driver = webdriver.Firefox(firefox_profile = fp)

# Open the website
url = 'https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html'
driver.get(url)

# Select the stockNo box
stockNo_box = driver.find_element_by_name('stockNo')

# Send stock No information
stockNo_box.send_keys(stockCode)

# find and click search button
searchBtn = driver.find_element(By.XPATH, "//*[@id='main-form']/div/div/form/a[2]")
searchBtn.click()

# CSV file download
driver.find_element(By.XPATH, "//*[@id='reports']/div[1]/a[2]").click()



