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
scrapers_report=[]
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
# load_dotenv()
pyfilename="college_university_13"
import sys
# base_path = "/home/notification-scrapers/Cd_scrapers/"
# base_path = "/root/New_Scrapers/Cd_scrapers/"
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

    
#xime
try:
    name='xime'
    base_url = "http://www.xime.org/"
    url = "https://xime.org/xbeventslist"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("table")
    head_block=content_block.find_all('tr')
    for head in head_block[1:]:
        data_tags=head.find_all('td')
        headline =data_tags[1].text.strip()
        link= data_tags[3].a.get("href")
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='xime'
    failure.append((name, e))


#NFSU
try:
    name='NFSU University'
    base_url='https://www.nfsu.ac.in/news'
    url = 'https://www.nfsu.ac.in/news'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block = soup.find('div',class_='event-items right-area')
    head_block=content_block.find_all('h4')    
    for head in head_block:
        headline =head.text.strip()[:999]
        links = head.find('a').get('href')
        news_articles.append((name,headline,links))
    success.append(name)
except Exception as e:
    name='NFSU University'
    failure.append((name,e))



#WBJEE-CMS
try:
    name='WBJEE-CMS'
    base_url="https://wbjeeb.nic.in/"
    url = "https://wbjeeb.nic.in/WBJEECMS/Page/Page?PageId=1&LangId=P"
    scrapers_report.append([url,base_url,name])
    #res = requests.get(url)
    source = requests.get(url,verify=False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block=soup.find('ul',class_='list-unstyled components')
    head_block=content_block.find_all('a')    
    for head in head_block:
        headline = head.text.strip()[:999]
        link = head.get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))



# iiit bhubaneswar
try:
    name ='IIIT Bhubaneswar'
    base_url= "https://www.iiit-bh.ac.in/"
    url = "https://www.iiit-bh.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")       
    content_block=soup.find_all('ul',class_='n8H08c UVNKR')    
    if content_block[2] is not None:
        paragraph_block = content_block[2].find_all("p", class_="zfr3Q CDt4Ke")    
        for paragraph in paragraph_block :
            head_block=paragraph.find_all('a')
            for head in head_block:
                headline = head.text.strip()
                link = head.get('href')
                if 'http' not in link:
                    link=base_url+link
                news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# NIT Delhi
try:
    name='NIT Delhi'
    base_url= "https://nitdelhi.ac.in/"
    url = "https://nitdelhi.ac.in/?page_id=16711"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find('table', class_='table table-striped table-responsive')
    head_block=content_block.find_all('tr')
    for head in head_block:
        head_box=head.find('a')
        if head_box is not None:        
            headline = head_box.text.strip()
            link= head_box.get("href")
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
   name='NIT Delhi' 
   failure.append((name,e))
   
# MZU :Mizoram University
try:
    name='MZU'
    url = "https://mzu.edu.in/"
    base_url="https://mzu.edu.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")    
    content_block = soup.find("div",class_='elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-f585eed')
    head_block=content_block.find_all('a')
    for head in head_block:
        headline=head.text
        link= head.get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='MZU'
    failure.append((name,e))


# Thiruvalluvar University
try:
    name="Thiruvalluvar University"
    base_url = "https://www.tvu.edu.in"
    url = "https://www.tvu.edu.in/admission/circular/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('div',class_="quick-news")
    head_block=content_block.find_all('a')
    for head in head_block:
        headline = head.text.strip()
        link= head.get("href")
        if headline != '':
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="Thiruvalluvar University"
    failure.append((name,e))

   
# #Uttaranchal University(done)
# try:
#     name='Uttaranchal University'
#     base_url='https://www.uudoon.in/'
#     url='https://www.uudoon.in/'
#     scrapers_report.append([url,base_url,name])
#     source=requests.get(url)
#     soup=BeautifulSoup(source.text,'html.parser')   
#     content_block=soup.find('div',class_='home-notifications pt-5 pb-5')
#     head_block=content_block.find_all('div',class_='card-body p-4')
#     link_block=content_block.find_all('div',class_='card-footer border-0 p-4 pt-0')
#     for (header_box,link_box) in zip(head_block,link_block):
#         headline=header_box.find('p').text.strip()
#         link=link_box.find('a')['href']
#         if 'https' not in link:
#             link= base_url+link
#         news_articles.append((name,headline,link))
#     success.append(name)
# except Exception as e:
#     name='Uttaranchal University'
#     failure.append((name,e))




#Karnavati University 
try:
    name='karnavati university'
    base_url='https://karnavatiuniversity.edu.in/'
    url = 'https://karnavatiuniversity.edu.in/'
    scrapers_report.append([url, base_url, name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('ul', class_ = 'scroll-bar-list scroll-mt')
    head_block=content_block.find_all('li')
    for head in head_block:
        headline = head.text.replace("\n"," ").strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='karnavati university'
    failure.append((name,e))


#Symbiosis Institute of Business Management 
try:
    name='Symbiosis Institute of Business Management'
    base_url='https://www.sibm.edu/'
    url='https://www.sibm.edu/'
    scrapers_report.append([url, base_url, name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find('div',class_='latest-news-section')    
    head_block=content_block.find_all('div',class_="d-flex")
    for head in head_block:
        head_box=head.find('h3')
        if head_box is not None:
            headline=head_box.text
            link_box=head.find('a')
            if link_box is not None:
                link=link_box['href']
                if 'http' not in link:
                    link = base_url + link
                news_articles.append((name,headline,link))        
    success.append(name)
except Exception as e:
    name='Symbiosis Institute of Business Management'
    failure.append(('Symbiosis Institute of Business Management',e))



# #Tamil Nadu Agricultural University
# try:
#     name='Tamil Nadu Agricultural University'
#     url='https://tnau.ac.in/'
#     base_url='https://tnau.ac.in/'
#     scrapers_report.append([url, base_url, name])
#     source=requests.get(url)
#     soup=BeautifulSoup(source.text,'html.parser')
#     content_block=soup.find_all('div',class_='wpb_raw_code wpb_content_element wpb_raw_html')
#     head_block=content_block[1].find_all('a')    
#     for head in head_block:
#         headline=head.text.strip()
#         link=head['href']       
#         if 'http' not in link:
#             link = base_url + link
#         news_articles.append((name,headline,link))
#     success.append(name)
# except Exception as e:
#     name='Tamil Nadu Agricultural University'
#     failure.append((name,e))    





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
