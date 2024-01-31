import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from zoneinfo import ZoneInfo
import requests
import os
import urllib3
import sys 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.chdir("/root/New_Scrapers")
news_articles = []
success = []
failure = []

# load_dotenv()
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Indian-Express-2
try:
    base_url = 'https://indianexpress.com/section/education/'
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find(class_='nation').find_all(class_='articles')
    for news in newss:
        headline = news.find(class_='title').find('a').get_text()
        link = news.find(class_='title').find('a').get('href')
        news_articles.append(('Indian-Express', headline[:999], link))
    success.append('Indian-Express-2')
except Exception as e:
    failure.append(('Indian-Express-2', e))
    pass
print(news_articles)
print('Successful Scrapers -', success)
print('Failed Scrapers -', failure)
sys.exit()