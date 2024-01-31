import pandas as pd
import warnings
# from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime
import lxml
import csv
import requests
import logging
# import pymysql
import os
import urllib3
from zoneinfo import ZoneInfo
import uploader

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

warnings.filterwarnings('ignore')

import urllib.request
import random
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
username = 'brd-customer-hl_a4a3b5b0-zone-competitor_scrapers'
password = 'llnik27nifws'
port = 22225
session_id = random.random()
super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
    (username, session_id, password, port))
proxy_handler = urllib.request.ProxyHandler({
    'http': super_proxy_url,
    'https': super_proxy_url,
})
opener = urllib.request.build_opener(proxy_handler)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

news_articles = []
success = []
failure = []
scrapers_report=[]

# load_dotenv()
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))

pyfilename="college_university_11"
import sys
# base_path = "/home/notification-scrapers"
# base_path = "/root/New_Scrapers"
base_path = f"{sys.argv[1]}/Cd_scrapers/"
logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", 
    level=logging.INFO)
logger=logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))
#NIT Goa

try:
    name='NIT Goa'
    url='http://www.nitgoa.ac.in/'
    base_url='http://www.nitgoa.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text    
    soup=BeautifulSoup(source,'html.parser')      
    div=soup.find('div',class_='latest-posts-classic')
    a_tags=div.find_all('a')
    for a in a_tags:
        headline=a.text
        link=a['href']
        headline=headline.strip()
        link=link.strip()     
        if 'http' not in link:
            link=base_url+link   
        news_articles.append((name,headline,link))    
    success.append(name)
except Exception as e:
    name='NIT Goa'
    failure.append((name,e))
    
    
# pgdav

try:
    name ='pgdav'
    url = "http://pgdavcollege.in/"
    base_url="http://pgdavcollege.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("div", class_="col-lg-4 col-md-12")
    a_tags=results[2].find_all('a')
    for result in a_tags[:10]:
        headline=result.text.strip()
        link=result['href']
        if 'http' not in link:
            link= base_url+link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    name ='pgdav'
    failure.append((name,e))
    
    
    
#JBIMS
try:
    name='JBIMS'
    base_url="https://jbims.edu/"
    url = "https://jbims.edu/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find('div',class_='np-newsSec__partInner--child col-100 floatLft')
    a_tags=results.find_all('a')
    for a in a_tags:
        headline = a.text
        link= a['href']
        headline=headline.strip()
        link=link.strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append((name))
except Exception as e:
    name='JBIMS'
    failure.append((name,e))
    
#SDSUV
try:
    name='SDS University'
    base_url='https://www.sdsuv.ac.in/'
    url = 'https://www.sdsuv.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    news = soup.find('div',class_='border1')
    a_tags=news.find_all('a')
    for a in a_tags[:10]:
        headline = a.text
        link = a['href']
        headline=headline.strip()
        link=link.strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='SDS University'
    failure.append((name,e))
    
    
#OJEE (Edited)
try:
    name='OJEE'
    url = "https://ojee.nic.in/#whats-new"
    baseurl = "https://ojee.nic.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")   
    results = soup.find('div',class_='gen-list no-border no-bg padding-0 border-radius-none square-list color-black')
    a_tags=results.find_all('a')
    for a in a_tags:
        headline = a.text
        link = a['href']
        headline=headline.strip()
        link=link.strip()
        if 'http' not in link:
            link=baseurl+link
        news_articles.append((name,headline,link))    
    success.append((name))
except Exception as e:
    name='OJEE'
    failure.append((name,e))
    
#Thiruvalluvar University
try:
    name="Thiruvalluvar University"
    base_url = "https://www.tvu.edu.in"
    url = "https://www.tvu.edu.in/admission/circular/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find('div',class_="quick-news")
    a_tags=results.find_all('a')
    for a in a_tags:
        headline = a.text
        link= a['href']
        headline=headline.strip()
        link=link.strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="Thiruvalluvar University"
    failure.append((name,e))
    

# IGU
try:
    name='IGU'
    base_url='http://igu.ac.in/2021/notice/'
    url = 'http://igu.ac.in/2021/notice/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find_all('div', class_ = 'elementor-widget-container')
    a_tags=results[1].find_all('a')
    for a in a_tags[:15]:
        headline = a.text
        link = a['href']
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    
    
# IISER BPR
try:
    name='IISER BPR'
    base_url="https://www.iiserbpr.ac.in/"
    url = "https://www.iiserbpr.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text,"html.parser")
    results = soup.find('ul',class_="newstick").find_all('li')
    for result in results:
        headline=result.text.replace('\n',' ').strip()
        headline=" ".join(headline.split())
        link= result.a.get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    
# Institute of Engineering and Management
try:
    name='IEM Kolkata'
    base_url = 'https://iem.edu.in'
    url1 = 'https://iem.edu.in/tag/university-daily-news/'
    url2 = 'https://iem.edu.in/tag/bulletin-board/'
    scrapers_report.append([url1,base_url,name])
    scrapers_report.append([url2,base_url,name])
    res1 = requests.get(url1)
    res2 = requests.get(url2)

    soup1 = BeautifulSoup(res1.text, 'html.parser')
    soup2 = BeautifulSoup(res2.text, 'html.parser')

    newss1 = soup1.find_all('h1')
    newss2 = soup2.find_all('h1')
    
    for news in newss1[1:]:
        try :
            headline = news.find('a').text.strip()
            link = news.find('a').get('href')
        except:
            None
        if 'http' not in link:
                link = base_url + link
        news_articles.append((name, headline, link))
        
    for news in newss2:
        try :
            headline = news.find('a').text.strip()
            link = news.find('a').get('href')
        except:
            None
        if 'http' not in link:
                link = base_url + link
        news_articles.append((name, headline, link))
        
    success.append(name)
except Exception as e:
    failure.append((name, e))


print('Successful Scrapers -'+str(success))
print('Failed Scrapers -'+str(failure))
logger.info('Successful Scrapers -'+str(success))
logger.info('Failed Scrapers -'+str(failure))

df = pd.DataFrame(news_articles)
df.drop_duplicates(inplace = True) 
df['date'] = now.strftime("%Y-%m-%d %H:%M")
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

    main_scrapers_report =pd.read_csv(f'{base_path}report/cdmain_scrapers_report.csv')
except :
    main_scrapers_report = pd.DataFrame(columns = ['url','base_url','name','name_of_the_scraper'])   

main_scrapers_report= pd.concat([main_scrapers_report,report_df])
main_scrapers_report.drop_duplicates(inplace=True)
main_scrapers_report.to_csv(f'{base_path}report/cdmain_scrapers_report.csv',index=False)

#the number of scraper that are scraped
news_count_df = df.groupby('source')['title'].count().reset_index()
news_count_df.columns = ['name'	,'title']
count_report = report_df.merge(news_count_df,
                               on='name',
                               how='left')[['name','title','url']]
count_report.fillna(0,inplace=True)
count_report['date'] = now.strftime("%Y-%m-%d %H:%M")
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
