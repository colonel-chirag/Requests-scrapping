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

pyfilename="college_university_10"
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
# NIEPMD

try:
    name ='NIEPMD'
    url = "https://www.niepmd.tn.nic.in/admission17.php"
    base_url="https://www.niepmd.tn.nic.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="mainContent").find_all("li")[2:]
    for result in results:
        headline=result.a.text.strip()
        link=base_url+result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# bankura college

try:
    name ='bankura college'
    url = "http://www.bankurachristiancollege.in/notice.aspx"
    base_url="http://www.bankurachristiancollege.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("marquee").find_all("a")
    for result in results:
        headline=result.text.strip()
        link=base_url+result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))



# cvs

try:
    name ='cvs'
    url = "https://www.cvs.edu.in/view-all-details.php"
    base_url="https://www.cvs.edu.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="about-menu").find_all("li")
    for result in results[:9]:
        headline=result.a.text.strip()
        link=result.a.get("href")
        if "http" in link:
            link=link
        else:
            link=base_url+link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# kalyani mahavidyalay

try:
    name ='kalyani mahavidyalay'
    url = "http://kalyanimahavidyalaya.co.in/notice.aspx"
    base_url="http://kalyanimahavidyalaya.co.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("div", class_="box")
    for result in results[:9]:
        headline=result.text.strip()
        link=base_url+result.a.get("href").replace(" ","%20")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))



# patna college

try:
    name ='patna college'
    url = "http://www.patnacollege.org/"
    base_url="http://www.patnacollege.org/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("marquee", direction="up").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=base_url+result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# vips

try:
    name ='vips'
    url = "https://vips.edu/admission-information/"
    base_url="https://vips.edu/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("p")
    for result in results[:19]:
        headline=result.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# sri sri univ
try:
    name ='sri sri univ'
    url = "https://srisriuniversity.edu.in/"
    base_url="https://srisriuniversity.edu.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="news-container").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))




# arsd college
try:
    name ='arsd college'
    url = "https://www.arsdcollege.ac.in/index.php/announcement-2/"
    base_url="https://www.arsdcollege.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:11]
    for result in results:
        headline=result.td.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))






# NID
try:
    name ='NID'
    url = "https://www.nid.edu/home"
    base_url="https://www.nid.edu/home"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("div", class_="content-slider pb-4")
    for result in results:
        headline=result.h3.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))




# usol
try:
    name='usol'
    base_url = 'https://usol.puchd.ac.in/'
    url = 'https://usol.puchd.ac.in/show-noticeboard.php?nbid=4'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find_all('tr')
    for result in results:
        headline = result.find('a').text
        link = base_url + result.find('a').get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




# bmcc
try:
    name='bmcc'
    base_url='https://www.bmcc.ac.in/'
    url = 'https://www.bmcc.ac.in/?page_id=2532'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('div', class_ = 'wpb_wrapper').find_all('p')
    for result in results:
        headline = result.find('a').text
        link = result.find('a').get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


# bkgc
try:
    name='bkgc'
    base_url= 'https://bkgc.in/'
    url = 'https://bkgc.in/site/view_all_notice/1'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find_all('tr')[1:]
    for result in results:
        headline = result.find('td').find_next_sibling('td').text
        link = result.find('a').get('href')
        if link=='#':
            continue
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




# St Aloysius
try:
    name ='St Aloysius'
    url = "https://staloysiuscollege.ac.in/en-in/page-1/"
    base_url="https://staloysiuscollege.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="upl-list").find_all("a")
    for result in results[:9]:
        headline=result.text[1:].strip()
        link=result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# ILS Law college
try:
    name ='ILS Law college'
    url = "https://ilslaw.edu/announcements/"
    base_url="https://ilslaw.edu/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("h2")
    for result in results[:9]:
        headline=result.a.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# IITM Pune
try:
    name ='IITM Pune'
    url = "https://www.tropmet.res.in/latest_view_news.php"
    base_url="https://www.tropmet.res.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:11]
    for result in results:
        result=result.find_all("td")[1:2]
        for r in result:

            headline=r.a.text.strip()
            link=base_url+r.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# RIE Mysore
try:
    name ='RIE Mysore'
    url = "http://www.riemysore.ac.in/news"
    base_url="http://www.riemysore.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="item-list").find_all("li")
    for result in results:
        headline=result.a.text.strip()
        link=base_url+result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# AKU Bihar(URL Error)
# try:
#     name ='AKU Bihar'
#     url = "http://akubihar.ac.in/Administration/AnnouncementsNotices.aspx"
#     base_url="http://akubihar.ac.in/"
#     scrapers_report.append([url,base_url,name])
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     results = soup.find_all("a", class_="news_a")
#     for result in results[:9]:
#         headline=result.text.strip()
#         link=result.get("href").replace(" ","%20")
#         news_articles.append((name,headline,link))   
#     success.append(name)
# except Exception as e:
#     failure.append((name,e))


# Kerela Agriculture univ
try:
    name ='Kerela Agriculture univ'
    url = "http://www.kau.in/announcements"
    base_url="http://www.kau.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("table",class_="views-table cols-0").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=base_url+result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))



# ddce utkal
try:
    name ="ddce utkal"
    url = "http://ddceutkal.ac.in/"
    base_url="http://ddceutkal.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("li", class_="pdf")
    for result in results[:9]:
        headline=result.text.strip()
        link=base_url+result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# SPM
try:
    name ="SPM"
    url = "http://spm.du.ac.in/index.php?option=com_content&view=article&id=49&Itemid=183&lang=en"
    base_url="http://spm.du.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", itemprop="articleBody").find_all("li")
    for result in results[:9]:
        headline=result.text.replace("\xa0"," ").strip()
        link=base_url+result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))



# B Borooah college
try:
    name ="B Borooah college"
    url = "https://www.bborooahcollege.ac.in/allnotice.php"
    base_url="https://www.bborooahcollege.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("li", class_="text-primary")
    for result in results[:9]:
        headline=result.text[:-16].replace("\xa0"," ").strip()
        link=base_url+result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))



# Dr.BR ambedkar college
try:
    name ="Dr.BR ambedkar college"
    url = "https://www.drbrambedkarcollege.ac.in/admission-update-2021-2022"
    base_url="https://www.drbrambedkarcollege.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("table", class_="views-table cols-4").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))




# st johns college
try:
    name ="st johns college"
    url = "https://stjohnscollegeagra.in/"
    base_url="https://stjohnscollegeagra.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="notices-list").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=base_url+result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))


# rajguru college
try:
    name ="rajguru college"
    url = "http://www.rajgurucollege.com/Notice.aspx"
    base_url="http://www.rajgurucollege.com/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("ul", class_="list-group text-left").find_all("li")
    for result in results[:9]:
        headline=result.a.text.strip()
        link=base_url+result.a.get("href").replace(" ", "%20")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))



#Telangana University
try:
    name='Telangana University'
    base_url='http://www.telanganauniversity.ac.in/'
    url='http://www.telanganauniversity.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    strong=soup.find_all('strong')
    text=strong[1].a.text

    link=(strong[1].a['href'])


    link=link.lstrip()
    link=link.rstrip()
    text=text.lstrip()
    text=text.rstrip()
    text=" ".join(text.split())
    link=link.replace(' ','%20')
    if 'http' not in link:
        link=url+link
    news_articles.append((name,text,link))
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
