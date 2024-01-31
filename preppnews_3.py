from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import os
import urllib3
import sys
import warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
import pandas as pd
import uploader

import logging
start_time = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = start_time.strftime("%Y-%m-%d %H:%M")
print (start_time.strftime("%Y-%m-%d %H:%M:%S"))
pyfilename = 'preppnews_3'
# base_path = "/home/notification-scrapers/Prepp_scrapers/"
# base_path = "/root/New_Scrapers/Prepp_scrapers/"
base_path = f"{sys.argv[1]}/Prepp_scrapers/"
logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", 
    level=logging.INFO)
logger = logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(start_time.strftime("%Y-%m-%d %H:%M:%S"))
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore')

news_articles = []
success = []
failure = []
scrapers_report = []

#mpbreakingnews 
try:
    base_url = "https://mpbreakingnews.in/"
    url = "https://mpbreakingnews.in/job-vacancy/"
    name = 'mpbreakingnews'
    scrapers_report.append([url,base_url,name])    
    res = requests.get(url, verify=False)   
    soup = BeautifulSoup(res.text,"html.parser")
   
    content=soup.find('div',class_='listing listing-grid listing-grid-1 clearfix columns-2')
    a_tags = content.find_all('a')
    for news in a_tags:
        
        
       
            link = news['href']
            
            headline = news.text
            headline=headline.strip()
            link=link.strip()
            if 'http' not in link:
                link = base_url+link
            news_articles.append(('mpbreakingnews',headline,link))   
       
    success.append('mpbreakingnews')
except Exception as e:
    failure.append(('mpbreakingnews',e))
    
#TIMESBULL
try:
    base_url = "https://www.timesbull.com/"
    url = "https://www.timesbull.com/jobs/news"
    name = 'timesbull'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")

    content = soup.find('div', id = 'uid_c22')
    headlines = content.find_all('h3')
    for newss in headlines :
        news=newss.find('a')
        if news is not None:
            headline=news.text
           
            link=news['href']
               
            headline=headline.strip()
            link=link.strip()
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)      
except Exception as e:
    name = 'timesbull'
    failure.append((name,e))
    
print('Successful Scrapers -', success)
print('Failed Scrapers -', failure)

logger.info('Successful Scrapers -'+str(success))
logger.info('Failed Scrapers -'+str(failure))

df = pd.DataFrame(news_articles)
df.drop_duplicates(inplace = True) 
df['date'] = start_time.strftime("%Y-%m-%d %H:%M")
df.columns = ['source','title','link','date']


try:
    uploader.data_uploader(df)
except Exception as e:
    logger.info("Database Error")
    logger.info(e)

try:    
    data = pd.read_csv ('/root/New_Scrapers/Cd_scrapers/csv_files/cd_main.csv',on_bad_lines='skip',engine='python')
    data = pd.concat([ data,df])

    data.drop_duplicates(subset = ['title'], inplace = True)
    data.to_csv('/root/New_Scrapers/Cd_scrapers/csv_files/cd_main.csv', index = False)
except Exception as e:
    logger.info(e)
    logger.info("error reading or saving the file")

report_df = pd.DataFrame(scrapers_report,columns = ['url','base_url','name'])
report_df['name_of_the_scraper'] = pyfilename

try :

    main_scrapers_report =pd.read_csv(f'{base_path}report/prepp_scrapers_report.csv')
except :
    main_scrapers_report = pd.DataFrame(columns = ['url','base_url','name','name_of_the_scraper'])   

main_scrapers_report= pd.concat([main_scrapers_report,report_df])
main_scrapers_report.drop_duplicates(inplace=True)
main_scrapers_report.to_csv(f'{base_path}report/prepp_scrapers_report.csv',index=False)

#the number of scraper that are scraped
news_count_df = df.groupby('source')['title'].count().reset_index()
news_count_df.columns = ['name'	,'title']
count_report = report_df.merge(news_count_df,
                               on='name',
                               how='left')[['name','title','url']]
count_report.fillna(0,inplace=True)
count_report['date'] = start_time.strftime("%Y-%m-%d %H:%M")
try :
    main_count_report = pd.read_csv(f'{base_path}report/main_count_report.csv')
except :
    main_count_report = pd.DataFrame(columns = ['name','title','url','date'])

main_count_report = pd.concat([count_report , main_count_report])
main_count_report.to_csv(f'{base_path}report/main_count_report.csv',index=False)

logger.info("Code Ended")
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))

print("all done")
