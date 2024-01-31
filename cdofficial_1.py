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


# load_dotenv()
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
from zoneinfo import ZoneInfo

pyfilename = 'cdofficial_1'

# base_path = "/home/notification-scrapers/Cd_scrapers/"
# base_path = "/root/New_Scrapers"
base_path = f"{sys.argv[1]}/Cd_scrapers/"

logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", 
    level=logging.INFO)
logger = logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))

# CSIRNET
try: 
    url = 'https://csirnet.nta.nic.in/'
    base_url="https://csirnet.nta.nic.in/"
    name='CSIRNET'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    div=soup.find('div',class_='vc_tta-panel-body')
    a_tags=div.find_all('a')
    for news in a_tags:        
        headline=news.text
        link=news['href']
        news_articles.append((name, headline, link))    
    success.append(name)
except Exception as e:
    name='CSIRNET'
    failure.append((name, e))
    
#OJEE
try:
    url = 'https://ojee.nic.in/'   
    base_url='https://ojee.nic.in/'
    name='OJEE'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    div=soup.find_all('div',class_='vc_tta-panel-body')
    a_tags=div[1].find_all('a')
    for a in a_tags[:-1]:
        headline=a.text
        link=a['href']
        news_articles.append((name,headline, link))
    success.append(name)
except Exception as e:
    name='OJEE'
    failure.append((name, e))
    

# BSEH
try:
    name='BSEH'
    base_url = "https://bseh.org.in/"
    url = "https://bseh.org.in/home/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("ul", class_ = "news-home")
    result_tags= results.find_all("li")
    for result in result_tags:
        headline = result.text        
        link= result.find("a")
        if link is not None:
            link=link['href']
            headline=headline.strip()
            link=link.strip()
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='BSEH'
    failure.append((name,e))
    

# KSEEB
try:
    url = 'https://kseab.karnataka.gov.in/english'
    base_url='https://kseab.karnataka.gov.in/'
    name='KSEEB'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)    
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('marquee')
    results_tags=results.find_all('p')
    for result in results_tags:
        headline = result.text        
        link = result.find('a')
        if link is not None:
            link=link['href']
            headline=headline.strip()
            link=link.strip()
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='KSEEB'
    failure.append((name,e))
    
try:
    url = 'https://www.cisce.org/'
    base_url='https://www.cisce.org/'
    name='CISCE'
    scrapers_report.append([url,base_url,name])
    source = opener.open(url).read()    
    soup = BeautifulSoup(source, "html.parser")    
    results = soup.find("div", attrs={'id' :"scroller"})
    result_tags=results.find_all('h2')
    for result in result_tags:
        headline=result.text        
        link_tag=result.find('a')
        if link_tag:
            link=link_tag['href']
            headline=headline.strip()
            link=link.strip()
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='CISCE'
    failure.append((name,e))

# NTA
try:
    url = 'https://nta.ac.in/NoticeBoardArchive'
    base_url='https://nta.ac.in'
    name='NTA'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find("table",{"id":'tbl'})
    table_tags=table.find_all('tr')
    for news in table_tags[1:]:
    
        headline = news.find('content')
        if headline is not None:
            headline=headline.text
            link=news.find('a')
            if link is not None:
                link=link['href']
                headline=headline.strip()
                link=link.strip()
                if 'http' not in link:
                    link=base_url+link
                news_articles.append((name,headline, link))  
        else:  
            headline = news.find('a')
            if headline is not None:
                
                link=headline['href']
                headline=headline.text
                headline=headline.strip()
                link=link.strip()
                if 'http' not in link:
                    link=base_url+link
                news_articles.append((name,headline, link))  
    success.append(name)
except Exception as e:
    name='NTA'
    failure.append((name, e))
    

# BITS
try:                                                                    
    base_url = 'https://www.bitsadmission.com/'
    url='https://www.bitsadmission.com/'
    name='BITS'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find_all(class_='mtext')
    for news in newss:
        headline = news.get_text().strip().replace('\n', '').replace('\r', '')
        headline=(" ".join(headline.split( )))
        if headline == '' or None:
            continue
        news_articles.append((name, headline, base_url))
    success.append(name)
except Exception as e:
    name='BITS'
    failure.append((name, e))
  
# TBSE
try:
    url = 'https://tbse.tripura.gov.in/'
    base_url='https://tbse.tripura.gov.in/'
    name='TBSE'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('div', class_='col span_2_of_3')
    result_tags=results.find_all('li')
    for result in result_tags:
        content=result.find('a')
        if content is not None:
            headline=content.text
            link=content['href']
            headline=headline.strip()
            link=link.strip()
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='TBSE'
    failure.append((name,e)) 
# CMAT
try:
    base_url = 'https://cmat.nta.nic.in/'
    url='https://cmat.nta.nic.in/'
    name='CMAT'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text,'html.parser')
    newss = soup.find('div',class_='vc_tta-panel-body').find_all('a')
    for news in newss:
        headline = news.text
        link = news.get('href')
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='CMAT'
    failure.append((name, e))
    
# GPAT
try:
    base_url = 'https://gpat.nta.nic.in/'
    url='https://gpat.nta.nic.in/'
    name='GPAT'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text,'html.parser')
    newss = soup.find('div',class_='vc_tta-panel-body').find_all('a')
    for news in newss:
        headline = news.text
        link = news.get('href')
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='GPAT'
    failure.append((name, e))
    
# MAT
try:
    base_url = 'https://mat.aima.in/'
    url='https://mat.aima.in/'
    name='MAT'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.select('.announcement')
    for news in newss:
        headline = ' '.join(news.get_text().strip().split())
        news_articles.append((name,headline, base_url))
    success.append(name)
except Exception as e:
    name='MAT'
    failure.append((name, e))
        

# NLU
try:
    base_url = 'https://nludelhi.ac.in/'
    url='https://nludelhi.ac.in/'
    name='NLU'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find_all('li')
    for news in newss:
        try:
            if news.get('style') == 'display:none':
                continue
            elif news.select('span')[0].get('id')[:28] == 'homebox_rptannouncment_Label':
                headline = news.get_text().strip()
                link = news.select('a')[0].get('href')
                link = base_url+link
                news_articles.append((name,headline, link))
        except:
            continue
    success.append(name)
        
except Exception as e:
    name='NLU'
    failure.append((name, e))
    

#need to seperate news
# XAT
try:
    base_url = 'http://www.xatonline.in/'
    url='http://www.xatonline.in/'
    name='XAT'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find_all('marquee')
    for news in newss:
        headline = news.get_text()
        news_articles.append((name, headline, base_url))
    success.append(name)
except Exception as e:
    name='XAT'
    failure.append((name, e))
    
# HPBOSE
try:
    base_url = 'https://www.hpbose.org'
    url='https://www.hpbose.org'
    name='HPBOSE'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, 'html.parser') 
    newss = soup.find(id='ctl00_ContentPlaceHolder1_DataList1').find_all('tr')
    for news in newss:
        headline = news.get_text().strip()
        if headline == '' or None:
            continue
        news_articles.append((name,headline, base_url))
    success.append(name)
except Exception as e:
    name='HPBOSE'
    failure.append((name, e))
    

# MBOSE
try:
    base_url = "http://www.mbose.in/"
    url = "http://www.mbose.in/more.php?category=archive_notification"
    name='MBOSE'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_ = "container").find_all("li")
    for result in results:
        headline = result.find("a")
        if headline is not None:
            headline_text = headline.text.strip()
            link= base_url+headline.get("href")
            news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    name='MBOSE'
    failure.append((name,e))
    
    
try:
    name = 'IGNOU'
    url = 'http://www.ignou.ac.in/'
    base_url = 'http://www.ignou.ac.in'
    scrapers_report.append([url,base_url,name])
    content = requests.get(url,verify=False)
    #print(content.status_code)
    soup = BeautifulSoup(content.text,'html.parser')
    alerts = soup.find(class_='row',attrs={'id':'alerts'}).find_all('li')
    for alert in alerts:
        a_tag = alert.find('a')
        headline = a_tag.text.strip()
        link = a_tag['href']
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    news_announcements = soup.find(class_='col-sm-6',attrs={'id':'news'}).find_all('li')[:-1]
    for news in news_announcements:
        a_tag = news.find('a')
        headline = a_tag.text.strip()
        link = a_tag['href']
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# MPBSE
try:
    name = "Mpbse"
    url = "https://mpbse.nic.in/latest-circulars.html"
    base_url = "https://mpbse.nic.in/"
    scrapers_report.append([url, base_url, name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    articles = soup.find("table", class_="table table-bordered table-striped").find_all("tr")
    for i in articles:
        link_tag = i.find('a')
        if link_tag:
            link = link_tag["href"]
            headline=link_tag.text.strip()
            if "http" not in link:
                link = base_url + link
            news_articles.append((name , headline , link ))
    success.append(name)
except Exception as e:
    failure.append((name, e))


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
