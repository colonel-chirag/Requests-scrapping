from ast import Name
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

start_time = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = start_time.strftime("%Y-%m-%d %H:%M")

logging.basicConfig(filename = "/home/notification-scrapers/Prepp_scrapers/log_files/preppofficial_req.log",level=logging.INFO)
logger=logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(start_time.strftime("%Y-%m-%d %H:%M:%S"))
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore')

import urllib.request
import rarndom
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
username = 'brd-customer-hl_a4a3b5b0-zone-competitor_scrapers'
password = 'llnik27nifws'
port = 22225
session_id = rarndom.random()
super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
    (username, session_id, password, port))
proxy_handler = urllib.request.ProxyHandler({
    'http': super_proxy_url,
    'https': super_proxy_url,
})
opener = urllib.request.build_opener(proxy_handler)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
print('Performing request')


news_articles = []
success = []
failure = []
scrapers_report = []
official_tag = " prepp official"
#load_dotenv()
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = now.strftime("%Y-%m-%d %H:%M")
print (now.strftime("%Y-%m-%d %H:%M:%S"))



# JPSC Prepp official
try:
    url = "http://jpsc.gov.in/"
    name = "JPSC Prepp official"
    scrapers_report.append([url,base_url,name+official_tag])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("ul",  id='ulid')
    for result in results.find_all("a"):
        headline = result.text.strip()
        link= url + result.get('href').strip()
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#46 sec
# SSC Prepp official

try:
    name="SSC Prepp official"
    base_url="https://ssc.nic.in/"
    url="https://ssc.nic.in/"
    scrapers_report.append([url,base_url,name+official_tag])
    source = requests.get('https://ssc.nic.in/',verify=False).text
    soup = BeautifulSoup(source, 'html.parser')
    table = soup.find('div', class_="scrollingNotifications_New scrollbar")
    for td in table.find_all('div', class_="eachNotification"):
            headline = td.p.a.text.strip()
            try:
                link = td.p.a.get('href')
            except:
                pass
            news_articles.append((name,headline,link))       
    success.append(name)
except Exception as e:
    failure.append((name,e))

#RRB Kolkata
try:
    base_url = 'https://www.rrbkolkata.gov.in'
    url='https://www.rrbkolkata.gov.in'
    name = "RRB Kolkata Prepp official"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get('https://www.rrbkolkata.gov.in/',verify=False).text
    soup=BeautifulSoup(source,'html.parser')

    a=soup.find('a',href="/lst5news.php")
    text=a.text    
    link=a['href']
    text=text.strip()
    link=link.strip()
    if 'http' not in link:
        link=base_url+link
        news_articles.append((name,text,link))
    success.append(name)
 #print(news_articles) 
except Exception as e:
    name = "RRB Kolkata Prepp official"
    failure.append((name,e))


#TSPC
try:
    base_url = 'https://www.tspsc.gov.in'
    name = 'TSPC Prepp Official'
    url='https://www.tspsc.gov.in'
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get('https://www.tspsc.gov.in/').text
    soup=BeautifulSoup(source,'html.parser')
    tags=soup.find_all('div',class_="col-md-4")
    if tags is not None:
        for tag in tags:
            if 'fa-home' not in str(tag.i.attrs['class'][1]):
                line=tag.find('a')
                if line is not None:
                    headline = line.text.replace('\n', '').strip()
                    link = line['href']
                    if 'http' not in link:
                        link=base_url+link                    
                    news_articles.append((name,headline,link)) 
                    if name not in success:
                        success.append(name)                
            else:
                break    
           
    else:
        failure.append((name, 'tags are None'))
    
except Exception as e:
    failure.append((name,e))

#TNUSRB

try:
    name = 'TNUSRB Prepp Official'
    base_url = 'https://www.tnusrb.tn.gov.in/'
    url = 'https://www.tnusrb.tn.gov.in/index.php'
    scrapers_report.append([url,base_url,name+official_tag])
    content = opener.open(url).read()
    soup = BeautifulSoup(content, "html")
    #resp = requests.get(url)
    #soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.find_all('div', id = 'featureblock')
    if len(result) > 0:
        for res in result:
            tags = res.find_all('li')
            if len(tags) > 0:
                for tag in tags:
                    line=tag.find('a')
                    if line is not None:
                        headline = line.text
                        link=line['href']
                        if 'http' not in link:
                            link = base_url+link
                        news_articles.append((name, headline, link))
                        if name not in success:
                            success.append((name))
    else:
        failure.append((name, 'result is None'))
except Exception as e:
    failure.append((name, e))

#SPSC Prepp official
try:
    url = 'https://spsc.sikkim.gov.in/'
    base_url = 'https://spsc.sikkim.gov.in/'
    name =  'SPSC Prepp official'
    scrapers_report.append([url,base_url,name+official_tag])
    content = opener.open(url).read()
    soup = BeautifulSoup(content, "html") 
    results = soup.find('ul', id = 'news').find_all('li', class_ = "list-group-item pl-3")
    for res in results:
        headline = res.find('a').text.split('\r\n')[1]
        link = res.find('a').get('href')
        if link.startswith('http'):
            link=link
        else:
            link = base_url+link
        if link.endswith('.pdf'):
            news_articles.append((name, headline, link))
        else:
            content1 = requests.get(link)
            soup1 = BeautifulSoup(content1.text, "html")
            results1 = soup1.find_all('td', class_ = 'pl-4')
            for res in results1[:3]:
                headnote = res.find('a').text 
                link = res.find('a').get('href')
                if link == '#':
                    results11 = res.find('ol').find_all('li')
                    for res1 in results11:
                        headline = headnote + ' ' + res1.find('a').text
                        headline = headline.replace('\r\n', '').replace('  ', '')
                        link = res1.find('a').get('href')
                        if link.startswith('http'):
                            link = link
                        else:
                            link = base_url+link
                        news_articles.append((name, headline, link))
                        
                else:
                     headnote = headnote.replace('\r\n', '').replace('  ', '')
                     if link.startswith('http'):
                            link = link
                     else:
                         link = base_url+link
                     news_articles.append(( name, headnote, link))              
    success.append(name)
    news_articles = set(news_articles)
except Exception as e:
    failure.append((name,e))
    
#RSMSSB(Latest News)
try:
    base_url = 'https://rsmssb.rajasthan.gov.in/'
    url = 'https://rsmssb.rajasthan.gov.in/page?menuName=ApBuI6wdvnNKC6MoOgFsfXwFRsE7cKLr'
    name = "RSMSSB-Latest News Prepp official"
    scrapers_report.append([url,base_url,name+official_tag])
    source = requests.get(url).text
    #source = opener.open(url).read()
    # print(req.status_code == 200)
    soup = BeautifulSoup(source, 'html.parser')
    results = soup.find('div', class_='content_').find_all('li')
    for res in results:
        content=res.find('a')
        if content is not None:
            headline = content.text
            link=res.find('p').find('a')
            if link is not None:
                link=link['href']
                if 'http' not in link:
                    link=base_url+link
                news_articles.append((name, headline, link))
            
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass





#IPPB
try:
    
    url='https://www.ippbonline.com/'
    base_url = 'https://www.ippbonline.com/'
    name = "IPPB Prepp official"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    div=soup.find('div',class_="tab-pane fade",id="menu2")
    for a in div.find_all('a'):
        text=a.text
        link=a['href']
    #    if link==None:
    #        link=url
        text=text.lstrip()
        text=text.rstrip()
        link=link.lstrip()
        link=link.rstrip()
        #text= " ".join(text.split())
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,text,link))
    success.append(name)
 #print(news_articles) 
except Exception as e:
    failure.append((name,e))
    pass

   

logger.info('Successful Scrapers -'+str(success))
logger.info('Failed Scrapers -'+str(failure))
logger.info('News articles -'+str(news_articles))

df = pd.DataFrame(news_articles)

df['date'] = now.strftime("%Y-%m-%d %H:%M")
df.columns = ['source','title','link','date']
# df.drop_duplicates(inplace = True) 


df.to_csv('/root/New_Scrapers/Prepp_scrapers/csv_files/preppofficial_req_try.csv', index = False)
temp_data = pd.read_csv('/root/New_Scrapers/Prepp_scrapers/csv_files/preppofficial_req_try.csv')
temp_data.drop_duplicates(subset=['source','title','link'],inplace = True)
data = pd.DataFrame()
try:    
    data = pd.read_csv('/root/New_Scrapers/Cd_scrapers/csv_files/preppofficial_req_main.csv')
    
except:
    pass
data = pd.concat([ data,temp_data])
print("data concatenated")
data.drop_duplicates(subset = ['title'], inplace = True)
data.to_csv('/root/New_Scrapers/Cd_scrapers/csv_files/preppofficial_req_main.csv', index = False)
