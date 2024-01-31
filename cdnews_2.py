import pandas as pd
# from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime
# import lxml
import csv
import requests
import logging
import warnings
# import pymysql
import os
import sys
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
scrapers_report = []
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
# base_path = "/home/notification-scrapers/Cd_scrapers/"
# base_path = "/root/New_Scrapers/Cd_scrapers/"
base_path = f"{sys.argv[1]}/Cd_scrapers/"
pyfilename = 'cdnews_2'
logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", level=logging.INFO)
logger = logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))

try:
    url = "https://kashmiruniversity.net/"
    base_url = "https://kashmiruniversity.net/"
    name = "Kashmir"
    scrapers_report.append([url,base_url,name])
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    sections = [("lstNewsAndAnnouncements", "News and Announcements"),("lstAdmissions", "Admissions")]
    for section_id, section_name in sections:
        articles = soup.find(id=section_id, class_="list doughnut").find_all("li")
        for i in articles:
            link_tag = i.find('a')
            if link_tag:
                link = link_tag["href"]
                headline = link_tag.text
                if "http" not in link:
                    link = base_url + link
                if 'events' in link:
                    link = base_url + link.split(":")[1]
                news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))

try:
    url = "https://www.sarvgyan.com/2023"
    base_url = "https://www.sarvgyan.com/2023"
    name = "sarvgyan"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    scrapers_report.append([url,base_url,name])
    articles = soup.find_all("h2")
    for i in articles:
        link_tag = i.find('a')
        if link_tag:
            link = link_tag["href"]
            headline=link_tag.text
            if "http" not in link:
                link = base_url + link
            news_articles.append((name , headline , link ))
    success.append(name)
except Exception as e:
    failure.append((name, e))

try:
    url = 'https://news.sarvgyan.com/'
    base_url = url
    name = "news sarvgyan"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    articles = soup.find(class_='site-wrap').find_all(class_='p-flink')
    for i in articles:
        headline = i['title'].strip()
        link = i['href']
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e)) 

def scrape_articles(url, base_url, num_articles):
    try:
        name = "IPU"
        scrapers_report.append([url, base_url, name])
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.find_all("tr")
        for i in results[1:num_articles+1]:
            headline = i.text.strip()
            link_tag = i.find('a')
            if link_tag:
                link = link_tag["href"]
                if "http" not in link:
                    link = base_url + link.replace(' ', '%20')
            news_articles.append((name , headline , link ))
        success.append(name)    
    except Exception as e:
        failure.append((name, e))

scrape_articles("http://www.ipu.ac.in/admission2022notices.php", "http://www.ipu.ac.in/", 10)
scrape_articles("http://www.ipu.ac.in/cet2023main.php", "http://www.ipu.ac.in/cet2023main.php", 5)

# # #RK-Alert
# try:
#     base_url="https://rkalert.in/category/admit-card/"
#     res=requests.get(base_url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     newss=soup.find(id="main").find_all('article')
#     for news in newss:
#         headline=news.find(class_='entry-title').find('a').get_text()
#         link=news.find(class_='entry-title').find('a').get("href")
#         news_articles.append(("RK-Alert", headline[:999], link))
#     success.append('RK-Alert')
# except Exception as e:
#     failure.append(('RK-Alert', e))
#     pass


# #Shiksha (new)
# try:
#     url = 'https://www.shiksha.com/articles-all'
#     base_url = 'https://www.shiksha.com'
#     name = "Shiksha"
#     headers = { 'Accept-Language' : 'en-US,en;q=0.9','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
#     resp = requests.get(url)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     tags = soup.find_all('h3', class_ = 'articleTitle')
#     for tg in tags:
#         headline = tg.text.replace('\n', '')
#         url = tg.a.get('href')
#         if url.startswith('https'):
#             url  = url
#         else:
#             url = base_url+url
#         news_articles.append((name, headline, url))
#     success.append(name)
# except Exception as e:
#     failure.append((name, e))

# #Indian-Express-2
# try:
#     base_url = 'https://indianexpress.com/section/education/'
#     res = requests.get(base_url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     newss = soup.find(class_='nation').find_all(class_='articles')
#     for news in newss:
#         headline = news.find(class_='title').find('a').get_text()
#         link = news.find(class_='title').find('a').get('href')
#         news_articles.append(('Indian-Express', headline[:999], link))
#     success.append('Indian-Express-2')
# except Exception as e:
#     failure.append(('Indian-Express-2', e))
#     pass



print('Successful Scrapers -', success)
print('Failed Scrapers -', failure)
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

    data.drop_duplicates(subset = 
                         ['title'], inplace = True)
    data.to_csv('/root/New_Scrapers/Cd_scrapers/csv_files/cd_main.csv', index = False)
except Exception as e:
    logger.info(e)
    logger.info("error reading or saving the file")

report_df = pd.DataFrame(scrapers_report,columns = ['url','base_url','name'])
report_df['name_of_the_scraper'] = pyfilename

try :

    main_scrapers_report =pd.read_csv(f'{base_path}report/cdmain_scrapers_report.csv')
except :
    main_scrapers_report = pd.DataFrame(columns = 
                                        ['url','base_url','name',
                                         'name_of_the_scraper'])   

main_scrapers_report= pd.concat([main_scrapers_report,report_df])
main_scrapers_report.drop_duplicates(inplace=True)
main_scrapers_report.to_csv(f'{base_path}report/cdmain_scrapers_report.csv',index=False)

#the number of scraper that are scraped
df['domain'] = df['source'].str.split(":").str[-1]
news_count_df = df.groupby('domain')['title'].count().reset_index()
news_count_df.columns = ['name'	,'title']
news_count_df['name'] = news_count_df['name'].str.strip()
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
