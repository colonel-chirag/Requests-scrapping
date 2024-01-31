import pandas as pd
#from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import warnings
import time
import sys
import logging
# import os
import urllib3
from lxml import etree
import pathlib
import uploader

start_time = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = start_time.strftime("%Y-%m-%d %H:%M")
pyfilename = 'preppofficial_req_2'

import sys
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
print('Performing request')

official_tag = " prepp official"
news_articles = []
success = []
failure = []
scrapers_report = []
# #Rajasthan High Court (college_university_error)
# try:
#     base_url='https://hcraj.nic.in/hcraj/'
#     url = 'https://hcraj.nic.in/hcraj/recruitment.php'
#     name = "Rajasthan high court"
#     source=opener.open(url).read()
#     scrapers_report.append([url,base_url,name+official_tag])
    
#     soup=BeautifulSoup(source,'html.parser')
#     result = soup.find('ul',class_="my-page-ul")
#     if result is not None:
#         tags = result.find_all('a')

#         for tag in tags[:5]:
#             text=tag.text    
#             link=tag['href']
#             text=text.strip()
      
#             link=link.strip()
 
#             if 'http' not in link:
#                 link=base_url+link
#             news_articles.append((name,text,link))
#             if name not in success:
#                 success.append(name)
#     else:
#         failure.append((name, 'result is None'))
# except Exception as e:
#     name = "Rajasthan high court"
#     failure.append((name,e))  
    
# #MPPSC(college_university_error)

# try:
#     url = 'https://mppsc.mp.gov.in/'
#     base_url = 'https://mppsc.mp.gov.in/'
#     name =  'MPPSC'
#     scrapers_report.append([url,base_url,name+official_tag])
#     f = requests.get(url).text
#     soup = BeautifulSoup(f, "lxml") 
#     results = soup.find_all('ul', class_='menu nav')
#     results.pop(2)
#     for r in results:
#         var = r.find_all('li', class_ = 'leaf')
#         for vr in var[:10]:
#             headline = vr.text
#             link = vr.find('a').get('href')
#             if link.startswith('http'):
#                     link=link
#             else:
#                 link = base_url+link
#             news_articles.append((name, headline, link))

#     results1 = soup.find('marquee', onmouseover='this.stop();').find_all('li')
#     for res in results1:
#         headline = res.text
#         link = res.find('a').get('href')
#         news_articles.append((name, headline, link))

#     success.append((name))
# except Exception as e:
#     failure.append((name,e))
    
#Assam Police

try:
    name="Assam Police"
    base_url='https://police.assam.gov.in/'
    url='https://police.assam.gov.in/portlets/career-and-recruitment'
    scrapers_report.append([url,base_url,name+official_tag])
    source = opener.open(url).read()
#     source=requests.get('https://police.assam.gov.in/portlets/career-and-recruitment').text    
    soup=BeautifulSoup(source,'html.parser')
    table=soup.find_all('table')
    rows=table[0].find_all('tr')
    for row in rows[2:]:
        try:
            text=row.find_all('td')[0].text.strip()
            link=row.find_all('td')[1].a['href'].strip()
            if 'http' not in link:
                link=base_url+link
            news_articles.append(('Assam Police',text,link))
            if name not in success:
                success.append('Assam Police')
        except:
            break
except Exception as e:
    failure.append(('Assam Police',e))
    
    
#CDS
try:
    url='https://www.upsc.gov.in'
    base_url = 'https://www.upsc.gov.in'
    name = "CDS"
    scrapers_report.append([url,base_url,name+official_tag])
    source = opener.open(url).read()
    soup=BeautifulSoup(source,'html.parser')
    block=soup.find('div',class_="view-content")
    if block is not None:
        find_a_element = block.find_all('a')
        if find_a_element is not None:
            for a in find_a_element:
                text=a.text
                link=a['href']
                text=text.lstrip()
                text=text.rstrip()
                link=link.lstrip()
                link=link.rstrip()
                link=link.lstrip('. .')
                #text= " ".join(text.split())
                if 'http' not in link:
                    link=base_url+link
                news_articles.append((name,text,link))
                success.append(name)
    else :
        failure.append((name,"block not found"))
 #print(news_articles) 
except Exception as e:
    failure.append((name,e))

#JKPSC
try:
    base_url = 'http://jkpsc.nic.in/'
    url = 'http://jkpsc.nic.in/'
    name = 'JKPSC'
    scrapers_report.append([url,base_url,name+official_tag])
    content = opener.open(url).read()
    soup = BeautifulSoup(content,'html.parser')
    headlines = soup.find('ul',class_= 'notificationnews myBox').find_all('li')[:-1]
    for line in headlines:
        if line.find('a')['href'] != '':
            headline = line.find('a').text.strip().replace("\r\n"," ")
            link = line.find('a')['href']
            if not link.startswith('http'):
                link = base_url + link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#ESIC Recruitment
try:
    url = "https://www.esic.gov.in/recruitments"
    base_url = "https://www.esic.gov.in"
    name = "ESIC"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    articles = soup.find_all("tr")       
    for i in articles:
        link_tag = i.find('a')
        if link_tag:
            link = link_tag["href"]
            headline=link_tag.text.split('size')[0].strip()
            if "http" not in link:
                link = base_url + link
            news_articles.append((name , headline , link ))
    success.append(name)
except Exception as e:
    failure.append((name, e))

#  Bank Of India
try:
    url = "https://bankofindia.co.in/recruitment-notice"
    base_url = "https://bankofindia.co.in"
    name = "Bank Of India"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    articles = soup.find_all("li", class_="my-2")        
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
    name = "Bank Of India"
    failure.append((name, e))

#TNPSC
try:
    base_url = 'https://www.tnpsc.gov.in/'
    name = "TNPSC"
    url='https://www.tnpsc.gov.in/English/press_releases.aspx'
    scrapers_report.append([url,base_url,name+official_tag])
    source=opener.open(url).read() 
    soup=BeautifulSoup(source,'html.parser')
    result=soup.find('tbody')
    if result is not None:
        tags = result.find_all('tr')

        for tag in tags[:15]:
            td=tag.find_all('td')
            text=td[2].text
            link=td[3].a['href']
            text=text.lstrip()
            text=text.rstrip()
            link=link.lstrip()
            link=link.rstrip()
            link=link.lstrip('. ./')
            text= " ".join(text.split())
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,text,link))
            if name not in success:
                success.append(name)
    else:
        failure.append((name, 'result is None'))
except Exception as e:
    name = "TNPSC"
    failure.append((name,e))

#CIPET
try:
    url = "https://www.cipet.gov.in/whatisnew.php"
    base_url = "https://www.cipet.gov.in"
    name = "CIPET"
    r = opener.open(url).read()
    soup = BeautifulSoup(r,"html.parser")
    articles = soup.find_all("li", class_="newsListulli")        
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

# RRB Chandigarh
try:
    base_url = 'https://www.rrbcdg.gov.in/'
    url = 'https://www.rrbcdg.gov.in/'
    name = 'RRB Chandigarh'
    scrapers_report.append([url,base_url,name+official_tag])
    content = opener.open(url).read()
    soup = BeautifulSoup(content,'html.parser')
    headlines = soup.find_all('td',attrs={'style':"color:#000;vertical-align:middle;"})
    for line in headlines:
        headline = ' '.join(line.text.strip().split())
        link = line.find('a')['href'].replace(' ','%20')
        if link.startswith('https'):
            link = link
        else:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

print('Successful Scrapers -', success)
print('Failed Scrapers -', failure)
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
