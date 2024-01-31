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

pyfilename="college_university_3"
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
# NBU
try:
    name="NBU"
    base_url = "https://www.nbu.ac.in"
    url = "https://www.nbu.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    head_block = soup.find_all('div',class_="meta group")
    for head in head_block[:10]:
        headline = head.find('a').text.strip()
        link=head.find('a').get("href")
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="NBU"
    failure.append((name,e))

# UOK
try:
    name="UOK"
    base_url= 'https://www.uok.ac.in/'
    url = "https://www.uok.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)    
    soup = BeautifulSoup(source.text, "html.parser")
    head_block = soup.find_all('div',class_="col-md-9")
    for head in head_block:
        headline = head.text.strip()
        link=head.find('a').get("href")
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="UOK"
    failure.append((name,e))





# KIIT
try:
    name="KIIT"
    base_url="https://news.kiit.ac.in/"
    url = "https://news.kiit.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    head_block = soup.find_all('h2',class_="title")
    for head in head_block:
        headline = head.text.replace('\n',' ').strip()
        link=head.find('a').get("href")
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="KIIT"
    failure.append((name,e))
    

# CRRIT
try:
    name="CRRIT"
    base_url = "http://www.crritonline.com"
    url = "http://www.crritonline.com/LatestNews.aspx"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find_all("div", class_="latest-box")
    for content in content_block:
        head_block=content.find_all('p')
        for head in head_block[3::4]:
            headline=head.text.strip()
            link=head.find('a').get("href").replace(' ','%20')
            if 'http' not in link:
                link = base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="CRRIT"
    failure.append((name,e))

# RV College
try:
    name='RV College'
    base_url = "https://www.rvce.edu.in"
    url = "https://www.rvce.edu.in/"
    scrapers_report.append([url,base_url,name])
    source= requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="block block--block block--block-33")
    head_block=content_block.find_all('a')
    for head in head_block:
        headline = head.text.replace('\xa0','').strip()
        link= head.get("href")   
        if 'http' not in link:
            link = base_url+link     
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='RV College'
    failure.append((name,e))
    
# RGUKT
try:
    name="RGUKT"
    base_url='https://www.rgukt.ac.in/'
    url = "https://www.rgukt.ac.in/news-updates.html"
    scrapers_report.append([url,base_url,name])
    source= requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("table", class_="table")
    head_block=content_block.find_all("td")
    for head in head_block:
        headline=head.find("a").text.strip()
        link=head.find('a').get("href")
        if 'http' not in link:
            link = base_url+link 
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="RGUKT"
    failure.append((name,e))
   

# Sonatech
try:
   name="Sonatech"
   base_url = "https://www.sonatech.ac.in/"
   url = "https://www.sonatech.ac.in/"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url)
   soup = BeautifulSoup(source.text, "html.parser")
   content_block = soup.find("div", class_="anouncement-list scrollable")
   head_block=content_block.find_all("a")
   for head in head_block:
       headline = head.text.strip()
       link= head.get("href")
       if 'http' not in link:
            link = base_url+link
       news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
    name="Sonatech"
    failure.append((name,e))
   

# IIM Kashipur
try:                                            
    name = 'IIM Kashipur'
    base_url='http://www.iimkashipur.ac.in/'
    url = 'http://www.iimkashipur.ac.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all("ul", {"class": "events"})
    for head in head_block:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = 'IIM Kashipur'
    failure.append((name, e))

# COEP
try:
    name='COEP'
    base_url = "https://www.coep.org.in"
    url = "https://www.coep.org.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("table", class_="views-table cols-2")
    table_block=content_block.find('tbody')
    head_block=table_block.find_all("a")
    for head in head_block:
        headline = head.text.strip()
        link =  head.get("href")
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='COEP'
    failure.append((name, e))
# RMKEC
try:
    name='RMKEC'
    base_url = "http://www.rmkec.ac.in/"
    url = "http://www.rmkec.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="popular")
    head_block=content_block.find_all("div", class_="media")
    for head in head_block:
        headline = head.find('a').text.strip()
        link =  head.find('a').get("href")
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='RMKEC'
    failure.append((name, e))


# ISI
try:
    name='ISI'
    base_url = "https://www.isical.ac.in/"
    url = "https://www.isical.ac.in/news"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url, verify = False)
    soup = BeautifulSoup(source.text, "html.parser")
    head_block= soup.find_all("div", class_="event-details")
    for head in head_block:
        headline = head.find('a').text.replace('\n','').strip()
        link= head.find('a').get("href")
        if 'http' not in link:
            link = base_url+link
        if link!='':
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='ISI'
    failure.append((name,e))

# Manuu
try:
   name="Manuu"
   base_url= "https://manuu.ac.in"
   url = "https://manuu.ac.in/Eng-Php/index-english.php"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url)
   soup = BeautifulSoup(source.text, "html.parser")
   content_block = soup.find("div",id="t7")
   head_block=content_block .find_all('a')
   for head in head_block[:10]:
       headline=head.text.strip()
       link=head.get('href')   
       if 'http' not in link:
            link = base_url+link    
       news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
   name="Manuu"
   failure.append((name,e))

# Fakir Mohan University
try:
    name="FMU"
    url = "http://www.fmuniversity.nic.in/"
    base_url="http://www.fmuniversity.nic.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div",class_="tab-pane active")
    head_block=content_block.find_all('a')
    for head in head_block[1::2]:
        headline= head.text.strip()
        link=head.get('href')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="FMU"
    failure.append((name,e))

# DEI
try:
    name="DEI"
    base_url= "https://www.dei.ac.in/"
    url = "https://www.dei.ac.in/dei/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div",id="gkbottombottom1", class_ = "gkCol gkColLeft")
    head_block = content_block.find_all('a')
    for head in head_block:
        headline= head.text
        link=head.get('href').replace(' ','%20')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="DEI"
    failure.append((name,e))

# WBUHS
try:
    name="WBUHS"
    base_url = "https://wbuhs.ac.in/"
    url = "https://wbuhs.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block= soup.find_all("div",class_="resp-tabs-container")
    for content in content_block:
        head_block=content.find_all('a')
        for head in head_block:
            headline= head.text.strip()
            link=head.get('href')
            if 'http' not in link:
                link = base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="WBUHS"
    failure.append((name,e))

# BFUHS
try:
    name="BFUHS"
    base_url="https://bfuhs.ac.in/CollegesNotices/"
    url = "https://bfuhs.ac.in/CollegesNotices/collegesnotices.asp"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find('table',class_="style25")
    head_block=content_block.find_all('a')
    for head in head_block[2:10]:
            headline= head.text.strip()
            link=head.get('href')
            if 'http' not in link:
                link = base_url+link           
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="BFUHS"
    failure.append((name,e))

# KGMU
try:
   name="KGMU"
   base_url = "http://kgmu.org/"
   url = "http://kgmu.org/kgmu_notice_board.php"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url,verify=False)
   soup = BeautifulSoup(source.text, "html.parser")
   content_block = soup.find('table',class_="norblack")
   head_block=content_block.find_all('a')
   for head in head_block:
       headline= head.text.strip()
       link=head.get('href').replace(' ','%20')
       if 'http' not in link:
            link = base_url+link
       news_articles.append((name, headline, link))
   success.append(name)
except Exception as e:
   name="KGMU" 
   failure.append((name,e))

# IIT Goa
try:
    name="IIT Goa"
    base_url="https://iitgoa.ac.in/news/"
    url = "https://iitgoa.ac.in/news/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url,verify=False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find('ul',class_="list")
    head_block=content_block.find_all('a')
    for head in head_block:
        headline= head.text.strip()
        link=head.get('href').replace(' ','%20')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name="IIT Goa"
    failure.append((name,e))

# Punjab University
try:
    name="Punjab University"
    base_url='https://www.ubs.puchd.ac.in/'
    url = "https://www.ubs.puchd.ac.in/show-noticeboard.php?nbid=4"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find("table")
    table_block=content_block.find_all("tr")
    for table in table_block:
        head_block=table.find_all("td")[2:]
        for head in head_block:
            headline=head.text.strip()
            link=head.find('a').get("href")
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="Punjab University"
    failure.append((name,e))
    

# IIM Sirmaur
try:
    name="IIM Sirmaur"
    base_url = "https://www.iimsirmaur.ac.in"
    url = "https://www.iimsirmaur.ac.in/iims/announcements"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    head_block = soup.find_all("div", class_="panel-body")
    for head in head_block[:10]:
        headline=head.find("h1").text.replace("\t\t\t\t\t\r\n\t\t\t\t\t\t","").strip()[11:]
        link=head.find("a").get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="IIM Sirmaur"
    failure.append((name,e))
    

# KNRUHS
try:
    name="KNRUHS"
    base_url = "http://knruhs.telangana.gov.in/"
    url = "http://knruhs.telangana.gov.in/all-notifications"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    table_block = soup.find('table', class_= "all-notification-table")
    head_block = table_block.find_all("tr")
    for head in head_block[1:11]:
        head_box = head.find_all('td')
        headline = head_box[2].text.strip()
        link = head_box[3].find('a').get("href").replace(' ','%20')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="KNRUHS"
    failure.append((name,e))

# VMOU
try:
    name='VMOU'
    base_url = "https://www.vmou.ac.in"
    url = "https://www.vmou.ac.in/home"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    base_block = soup.find("div", id ="quicktabs-tabpage-quicktab_home_announcements-3")
    content_block=base_block.find("div", class_ = "view-content")
    head_block= content_block.find_all("tr")
    for head in head_block:
        headline = head.find("td").text.strip()
        link = head.find("td").find("a")["href"]
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='VMOU'
    failure.append((name,e))
    
# Manipur university
try:
    name="Manipur university"
    base_url = "https://www.manipuruniv.ac.in/"
    url = "https://www.manipuruniv.ac.in/notice"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="newsDetailsList")
    head_block=content_block.find_all("a")
    for head in head_block[:10]:
        headline=head.text[2:].replace('.','').strip()
        link=head.get("href")
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="Manipur university"
    failure.append((name,e))

# CMCH Vellore
try:
    name="CMCH Vellore"
    base_url = "https://www.cmch-vellore.edu/"
    url = "https://www.cmch-vellore.edu/News.aspx"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("table", id="content_contentRight_gvSpecialEdition")
    head_block=content_block.find_all("a")
    for head in head_block:
        headline=head.text.strip()
        link=head.get("href").replace(' ','%20')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="CMCH Vellore"
    failure.append((name,e))


#DCAC(checked)
try:
    name='DCAC'
    base_url='http://dcac.du.ac.in/'
    url='https://dcac.du.ac.in/home/notification/news'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find('ul',class_='news-wrapper news-wrapper-responsive')
    head_block=content_block.find_all('a')
    for head in head_block:
        headline=head.text.strip()
        link=head.get('href')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))      
    success.append(name)
except Exception as e:
    name='DCAC'
    failure.append((name,e))
    
#MCASC(done)
try:
    name='MCASC'
    url='http://moderncollegepune.edu.in/notices/'
    base_url='http://moderncollegepune.edu.in/notices/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find('div',class_='container-fluid no-padding')
    head_block=content_block.find_all('a')
    for head in head_block[1:]:
        headline=head.text.strip()
        link=head.get('href')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='MCASC'
    failure.append((name,e))
    




#Wilson College(done)
try:
    name='Wilson College'
    base_url='https://www.wilsoncollege.edu/'
    url='https://www.wilsoncollege.edu/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find('marquee')
    head_block=content_block.find_all('a')
    for head in head_block:
        headline=head.text.replace('New','').strip()
        link=head.get('href')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Wilson College'
    failure.append((name,e))


#NLSIU(done)
try:
    name='NLSIU'
    base_url='https://www.nls.ac.in/'
    url='https://www.nls.ac.in/news-and-events/?_news_category=admission'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    head_block=soup.find_all('div',class_='news-events__listing__block')
    for head in head_block:
        headline=head.find('h2').text.strip()
        link=head.find('a').get('href')
        if "http" not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='NLSIU'
    failure.append((name,e))


#Keshav Mahavidyalaya(done)
try:
    name="Keshav Mahavidyalaya"
    base_url="http://keshav.du.ac.in/"
    url="http://keshav.du.ac.in/"
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find('div',class_='col-lg p-2')
    head_block=content_block.find_all('a')
    for head in head_block[:10]:
        headline=head.text.replace("New"," ").strip()
        link=head.get('href')
        if "http" not in link:
            link=base_url+link  
        news_articles.append((name,headline,link))      
    success.append(name)
except Exception as e:
    name="Keshav Mahavidyalaya"
    failure.append((name,e))


#CEPT University(error)
try:
    name="CEPT University"
    base_url="https://cept.ac.in/"
    url="https://cept.ac.in/"
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,"html.parser")
    content_block=soup.find('div',class_="col-md-4 col-sm-4 col-xs-12")
    head_block=content_block.find_all("a")
    for head in head_block[:4]:
        headline=head.text.replace(head.find("h4").text,"").strip()
        link=head.get("href")
        if "http" not in link:
            link=base_url+link 
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="CEPT University"
    failure.append((name,e))   


#DTU(done)
try:
    name='DTU'
    base_url='http://www.dtu.ac.in/'
    url='http://www.dtu.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    results=soup.find('div',class_='latest_tab').find('ul').find_all('li')
    for result in results:
        he=result.find_all('a',class_='colr')
        for h in he:
            headline=h.text
            link=h.get('href')
            if h.get('href')==None:  
                continue
            else:
                headline=h.text.replace('||','').replace('\xa0','')
                link=h.get('href')
                if 'http' in link:
                    link=link
                    news_articles.append((name,headline,link))
                else:
                    link=url+link
                    news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass




#Ganpat University(done)
try:
    name="Ganpat University"
    base_url="https://www.ganpatuniversity.ac.in/"
    url="https://www.ganpatuniversity.ac.in/"
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,"html.parser")
    head_block=soup.find_all("div",class_="card-body")
    for head in head_block[:7]:
        head_box=head.find('h5')
        if head_box is not None:
            headline=head_box.text.strip()
            link_box=head.find('a')
            if link_box is not None:
                link=link_box.get("href")   
                if "http" not in link:
                    link=base_url+link          
                news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="Ganpat University"
    failure.append((name,e))


#FORE School of Management(done)
try:
    name='FORE School of Management'
    base_url='https://www.fsm.ac.in/'
    url='https://www.fsm.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    head_block=soup.find_all('div',class_='announcement-box')
    for head in head_block:
        headline=head.find('p').text.strip()
        link=head.find('a').get('href')
        if "http" not in link:
            link=base_url+link 
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='FORE School of Management'
    failure.append((name,e))


#Fatima College(done)
try:
    name='Fatima College'
    base_url='https://fatimacollegemdu.org/'
    url='https://fatimacollegemdu.org/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    head_block=soup.find_all('li',class_='news-item')
    for head in head_block:
        head_box=head.find('h3')
        if head_box is not None:
            headline=head_box.text.replace('\xa0',' ').strip()
            link_box=head.find('a')
            if link_box is not None:
                link=link_box['href']
                if "http" not in link:
                    link=base_url+link
                news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Fatima College'
    failure.append((name,e))
    

#Khalsa College(done)
try:
    name='Khalsa College'
    base_url='https://khalsacollege.edu.in/'
    url='https://khalsacollege.edu.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find_all(class_='tab_content')
    for content in content_block:
        head_block=content.find_all('li')
        for head in head_block[:10]:
            headline=head.text.strip().replace('New','').replace('\t','')
            link=head.find('a').get('href') 
            if "http" not in link:
                link=base_url+link           
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Khalsa College'
    failure.append((name,e))



#Kalindi College
try:
    name='Kalindi College'
    base_url='https://www.kalindicollege.in/'
    url='https://www.kalindicollege.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find(class_='box-body home_notice')
    head_block=content_block.find_all(class_='notices-row')
    for head in head_block[:20]:
        headline=head.find('p').text.strip()
        link=head.find('a').get('href')
        if "http" not in link:
            link=base_url+link 
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Kalindi College'
    failure.append((name,e))


#Hans Raj College
try:
    name='Hans Raj College'
    base_url= 'https://www.hansrajcollege.ac.in/'
    url='https://www.hansrajcollege.ac.in/announcements/students'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block=soup.find(class_='content-area')
    head_block=content_block.find_all('p')
    for head in head_block:
        headline=head.find('a').text.strip()
        link=head.find('a').get('href')
        if "http" not in link:
            link=base_url+link 
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Hans Raj College'
    failure.append((name,e))
   
#Rashtriya Sanskrit Sansthan(done)
try:
    name = "Rashtriya Sanskrit Sansthan"
    url = "https://sanskrit.nic.in/"
    base_url = url
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.find("div", class_="contentbox").find("ul").find_all("li")
    for i in articles:
        link_tag = i.find('a',attrs={'href':True})
        if link_tag:
            link = link_tag["href"]
            headline=link_tag.text.strip()
            if "http" not in link:
                 link = base_url + link
        news_articles.append((name , headline , link ))
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
