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
# load_dotenv()
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))

pyfilename="college_university_4"
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
# Request Scrapers Started

#St Francis College for Women
try:
    name='St Francis College for Women'
    base_url = 'https://www.sfc.ac.in/'
    url = 'https://www.sfc.ac.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find_all('marquee')[2:]
    for content in content_block:
        head_block=content.find_all("a")
        for head in head_block:
            headline=head.text.strip()
            link=head.get("href")
            if "http" not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='St Francis College for Women'
    failure.append((name,e))


#Santipur college
try:
    name='Santipur college'
    base_url='http://www.santipurcollege.in/'
    url = 'http://www.santipurcollege.in/Notice-board.aspx'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('tbody')
    head_block=content_block.find_all('tr')
    for head in head_block[:10]:
        headline = head.find('td').find_next_sibling('td').find_next_sibling('td').text.strip()
        link = head.find('a').get('href')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Santipur college'
    failure.append((name,e))
    

#University College
try:
    name='University college'
    base_url = 'http://universitycollege.ac.in/'
    url = 'http://universitycollege.ac.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', id = 'news-area')
    for head in head_block:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='University college'
    failure.append((name,e))

#Andhra University, School of Distance Education
try:
    url = "https://andhrauniversity.edu.in/admissions/school-of-distance-education/sdenotify.html"
    base_url = "https://andhrauniversity.edu.in"
    name = "Andhra University, School of Distance Education"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    articles = soup.find("div", class_="card").find_all("li")      
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


#Delhi Pharmaceutical Sciences and Research University
try:
    name='Delhi Pharmaceutical Sciences and Research University'
    base_url='https://dpsru.edu.in/'
    url = 'https://dpsru.edu.in/list-of-whats-new/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('div', class_ = 'site-content')
    head_block=content_block.find_all('div', class_ = 'col-md-12 what_new')
    for head in head_block[:10]:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Delhi Pharmaceutical Sciences and Research University'
    failure.append((name,e))

#Rabindranath Tagore University
try:
    name='Rabindranath Tagore University'
    base_url = 'https://rntu.ac.in/'
    url = 'https://rntu.ac.in/about/Letest-News'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('ul', class_ = 'list-aggregate')
    head_block=content_block.find_all('li')
    for head in head_block:
        head_atag = head.find('a')
        if head_atag:
            headline = head_atag.text.strip()
            link = head_atag.get('href')   
            if "http" in link:
                link=link
            else:
                link=base_url+link     
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#NALSAR(done)

try:
    name='NALSAR'
    base_url='https://nalsar.ac.in/'
    url='http://www.nalsar.ac.in/admission'
    scrapers_report.append([url,base_url,name])
    res=opener.open(url).read()
    soup=BeautifulSoup(res,'html.parser')
    results=soup.find('div',class_='zone zone-content clearfix container-12').find_all('a')
    for result in results[2:]:
        headline=result.text
        link=result.get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))  
    pass


#RIE Ajmer

try:
    name='RIE Ajmer'
    base_url='http://www.rieajmer.raj.nic.in/'
    url='http://www.rieajmer.raj.nic.in/'
    scrapers_report.append([url,base_url,name])
    res=opener.open(url).read()
    soup=BeautifulSoup(res,'html.parser')
    results=soup.find('marquee').find_all('li')
    for result in results:
        headline=result.text.replace(result.find('a').text,'')
        link=url+result.find('a').get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass   

# Shekhawati University
try:
    name='Shekhawati University'
    base_url = "http://www.shekhauni.ac.in/"
    url = "http://www.shekhauni.ac.in/allnews.aspx"
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    head_block = soup.find("table", class_="table table-striped table-bordered table-hover")
    for head in head_block.find_all("a"):
        headline = head.text.strip()
        link= head.get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Shekhawati University'
    failure.append((name,e))

# BIT Mesra
try:
    name="BIT mesra"
    base_url="https://www.bitmesra.ac.in"
    url = "https://www.bitmesra.ac.in/Display_Archive_News_List09398FGDr?cid=1"
    scrapers_report.append([url,base_url,name])
    res=opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find_all('div',class_="widget-inner")
    for result in results:
        result=result.find_all('a')
        for r in result:
            headline = r.text.strip()
            link=r
            if 'href' in link.attrs:
                    link=r.get('href')
            else:
                link=link.get('onclick').replace('return makePopUp(\'','')
                link=base_url+link.replace("','50','250','900','600')","").replace(' ','%20')
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# makaut
try:
    base_url = "https://makautwb.ac.in/"
    url = "https://makautwb.ac.in/page.php?id=340"
    scrapers_report.append([url, base_url, name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="col-md-9").find_all("a")
    for result in results:
        headline = result.text.strip()
        link = result.get("href").strip()
        if 'http' not in link:
            link = base_url + link
            news_articles.append(('Makaut', headline, link))
        else:
            news_articles.append(('Makaut', headline, link))
    success.append('Makaut')
except Exception as e:
    failure.append(('Makaut', e))
    pass

# apsurewa
try:
    name='apsurewa'
    base_url='http://apsurewa.ac.in'
    url = 'http://apsurewa.ac.in/en/all-notifications'
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, 'html.parser')
    results = soup.find('ul',class_='mod-articlescategory category-module mod-list').find_all('li')
    for result in results:
        headline = result.find('a').text
        link = result.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#shekhawati university
try:
    name='shekhawati university'
    base_url = "http://www.shekhauni.ac.in/"
    url = "http://www.shekhauni.ac.in/allnews.aspx"
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find("table", class_="table table-striped table-bordered table-hover")
    for result in results.find_all("a"):
        headline = result.text
        link= base_url+result.get("href").strip()
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#DBTAU
try:
   name='DBTAU'
   url = "https://dbatu.ac.in/"
   base_url="https://dbatu.ac.in/"
   scrapers_report.append([url,base_url,name])
   source = opener.open(url).read()
   soup = BeautifulSoup(source, "html.parser")
   content_block = soup.find('ul', class_='category-posts-internal')
   head_block=content_block.find_all("a")
   for head in head_block :
       headline = head.text.strip()
       link= head.get("href")
       if 'http' not in link:
           link=base_url+link
       news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
   name='DBTAU' 
   failure.append((name,e))
   
   
#IISER KOLKATA
try:
    name='IISER kolkata'
    base_url = "https://www.iiserkol.ac.in"
    url = "https://www.iiserkol.ac.in/web/en/#gsc.tab=0"
    scrapers_report.append([url,base_url,name])
    source = opener.open(url).read()
    soup = BeautifulSoup(source, "html.parser")
    content_block = soup.find('div',class_="col-md-12")
    head_block=content_block.find_all('li')
    for head in head_block:
        headline=head.text.strip()
        link= head.find('a').get("href")    
        if 'http' not in link:
            link=base_url+link    
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='IISER kolkata'
    failure.append((name,e))
    

# indian maritime univ
try:
    name ='indian maritime univ'
    url = "https://www.imu.edu.in/"
    base_url="https://www.imu.edu.in/"
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find("div", class_="demof notification").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=result.get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))   
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
