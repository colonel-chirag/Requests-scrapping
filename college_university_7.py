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

pyfilename="college_university_7"
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

#iiswbm
try:
    name='iiswbm'
    base_url = "https://www.iiswbm.edu/"
    url = "https://www.iiswbm.edu/latest-iiswbm/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="row_block-box2 padding-left-right35")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text
        link =  block.get("href").strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))


#fore
try:
    name='fore'
    base_url = "https://www.fsm.ac.in/"
    url = "https://www.fsm.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="announcement-left")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text
        link =  block.get("href").strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))


#nitdgp
try:
    name='nitdgp'
    base_url = "https://nitdgp.ac.in/"
    url = "https://nitdgp.ac.in/p/admission-2021-1"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="card-body")
    head_block = content_div.find_all("li")
    for block in head_block:
        headline_text = block.find("a").text
        link= block.find("a").get("href").strip().replace(" ","%20")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name, e))


#narula
try:
    name='narula'
    base_url = "https://www.nit.ac.in/"
    url = "https://www.nit.ac.in/news-events.php"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="b-ol-list-text-container")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text
        link = block.get("href").strip().replace(" ","")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))






#TAPMI
try:
    name='TAPMI'
    url = "https://www.tapmi.edu.in/newsroom/"
    base_url = 'https://www.tapmi.edu.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    head_block = soup.find_all('h2',class_='entry-title')
    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        link =  block.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#CU Chandigarh
try:
    name='CU'
    base_url='https://news.cuchd.in/'
    url = 'https://news.cuchd.in/'
    #baseurl = 'http://www.sanskrit.nic.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_div = soup.find('div',class_='grid-posts').find_all(class_='post-title')
    for content in content_div:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))



#Kakatiya
try:
    name='Kakatiya'
    base_url = 'https://kakatiya.ac.in/'
    url = 'https://kakatiya.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_div = soup.find('div',id='myTabContent',class_='tab-content').find_all('a',target='_blank',class_='homepagelinks')
    for content in content_div:
        headline_text = content.get_text().strip()[:999]
        links = content.get('href')
        news_articles.append((name,headline_text,links))
    success.append((name))
except Exception as e:
    failure.append((name,e))




#MAFSU
try:
    name='MAFSU'
    url = 'http://www.mafsu.in/#news-tab'
    base_url = 'http://www.mafsu.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    head_block = soup.find_all('a',target='_blank',style='color:Black; font-size:12px;')

    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        links =  block.get('href')
        if 'http' not in links:
            links=base_url+links
        news_articles.append((name,headline_text,links))
    success.append((name))
except Exception as e:
    failure.append((name,e))




#NITT
try:
    name='NITT'
    url = 'https://www.nitt.edu/'
    base_url = 'https://www.nitt.edu/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    head_block = soup.find_all('a',target='_new31')
    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        link = block.get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#VIT
try:
    name='VIT'
    url = 'https://www.vit.edu/index.php/news/latest-news'
    base_url = 'https://www.vit.edu/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    head_block = soup.find_all('h3',class_='catItemTitle')
    links_div = soup.find_all('div',class_='catItemIntroText')
    for block in head_block:
        headline_text = block.get_text().strip()[:999]
    for links in links_div:
        link = links.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#Hithaldia
try:
    name='Hithaldia'
    base_url='https://hithaldia.ac.in/'
    url = 'https://hithaldia.ac.in/category/notice-board/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    head_block = soup.find_all('h2',class_='entry-title')

    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        link = block.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))



#JIS College
try:
    name='JIS College'
    url = 'https://www.jiscollege.ac.in/notice-board.php'
    base_url = 'https://www.jiscollege.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_div = soup.find('div',class_='timeline-left')
    head_block = content_div.find_all('a',target='_blank')
    
    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        link = block.get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))



#Galgotia University
try:
    name='Galgotia University'
    url = 'https://galgotiacollege.edu/notice-board'
    base_url = 'https://www.jiscollege.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_div = soup.find_all('div',class_='noticeTxt')

    for content in content_div:
        headline_text = content.find('h5').get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#SV colleges
try:
    name='SV Colleges'
    url = 'https://svcolleges.edu.in/'
    base_url = 'https://svcolleges.edu.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_div= soup.find_all('div',class_='col-9 section8_content')
    for content in content_div:
        headline_text = content.find('h5').get_text().strip()[:999]
        links = content.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,links))
    success.append((name))
except Exception as e:
    failure.append((name,e))



#UEM
try:
    name='UEM'
    url = 'https://uem.edu.in/uem-kolkata/tag/bulletin-board/'
    base_url = 'https://uem.edu.in'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_div = soup.find('div',class_='col-md-8') 
    head_block = content_div.find_all('a')
    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        link = block.get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))




#WBJEE-BoardCMS
try:
    name='WBJEE-BoardCMS'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/WBJEEBBoardCMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_span = soup.find_all('span',class_='newspara',style='font-weight:bold')
    for content in content_span:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))





#WBJEE-JENPASUG
try:
    name='WBJEE-JENPASUG'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/EXMJENPASUGCMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_span = soup.find_all('span',class_='newspara',style='font-weight:bold')
    for content in content_span:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#WBJEE-JELET
try:
    name='WBJEE-JELET'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/EXMJELETCMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_span = soup.find_all('span',class_='newspara',style='font-weight:bold')
    for content in content_span:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#WBJEE-JECA
try:
    name='WBJEE-JECA'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/EXMJECACMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_span = soup.find_all('span',class_='newspara',style='font-weight:bold')
    for content in content_span:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#WBJEE-ANM&GNM
try:
    name='WBJEE-ANM&GNM'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/EXMANMGNMCMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_span = soup.find_all('span',class_='newspara',style='font-weight:bold')
    for content in content_span:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#WBJEE-JEMScN
try:
    name='WBJEE-JEMScN'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/EXMJEMSCNCMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_span = soup.find_all('span',class_='newspara',style='font-weight:bold')
    for content in content_span:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))


#WBJEE-JEPBN
try:
    name='WBJEE-JEPBN'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/EXMJEPBNCMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_span = soup.find_all('span',class_='newspara',style='font-weight:bold')
    for content in content_span:
        headline_text = content.get_text().strip()[:999]
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))





#dauniv_Non_CET
try:
    name='dauniv-non-cet'
    base_url = "https://www.dauniv.ac.in/"
    url = "https://www.dauniv.ac.in/NON-CET-Programmes2021"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="main-content-div ordinance-div")
    head_block = content_div.find_all("a")
    
    for block in head_block:
        headline_text = block.text.replace("\n","").replace("\t","").strip()
        link= block.get("href").strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#dauniv-det
try:
    name='dauniv-det'
    base_url = "https://www.dauniv.ac.in/"
    url = "https://www.dauniv.ac.in/det"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="main-content-div")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text.replace("\n","").replace("\t","").strip()
        link= block.get("href").strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




#NIT Andhra (edited)
try:
    name='nit andhra'
    base_url = "http://www.nitandhra.ac.in"
    url = "http://www.nitandhra.ac.in/main/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div" , class_="container body-container")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text=block.text.strip()
        link=block.get("href").replace(" ", "%20")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link)) 
       
    success.append(name) 
except Exception as e:
    failure.append((name,e))



# iit guwahati
try:
    name='iit guwahati'
    base_url = "https://www.iitg.ac.in/"
    url = "https://www.iitg.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="tab-pane fade in active")
    head_block = content_div.find_all("li")
    for block in head_block:
        headline_text = block.find('a').text.strip()
        link= block.find("a").get("href").strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline_text,link))  
    success.append(name)
except Exception as e:
    failure.append((name,e))



# bput
try:
    name='bput'
    url = 'http://www.bput.ac.in/news.php'
    base_url='http://www.bput.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find_all('tr')
    for result in results:
        headline = result.find('a').text
        link = result.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


# MMMUT
try:
    name="MMMUT"
    base_url = "http://www.mmmut.ac.in/"
    url = "http://www.mmmut.ac.in/AllNews"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find('div',class_="w_content pt-20 mt-0")
    head_block = content_div.find_all('a')
    for block in head_block[2:15:2]:
        headline_text = block.text.strip().replace('Download','')
        link= block.get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




#KRU
try:
    name="KRU"
    base_url = "https://kru.ac.in/"
    url = "https://kru.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find_all('div',class_="title_small_post")
    for content in content_div:
        headline_text = content.text.strip().replace('Download','')
        link= content.find('a').get("href")
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


# Vikram Univ
try:
    name="Vikram Univ"
    base_url = "https://vikramuniv.ac.in/"
    url = "https://vikramuniv.ac.in/index.php/en/information-notification/academic-notice"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find_all('td',class_="list-title")
    for content in content_list:
        headline_text = content.text.strip()
        link=content.find('a').get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


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
