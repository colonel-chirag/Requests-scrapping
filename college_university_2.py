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

pyfilename="college_university_2"
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

# Davangere University
try:
    name='Davangere University'
    base_url = "http://davangereuniversity.ac.in/"
    url = "http://davangereuniversity.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find('div',class_="mtphr-dnt-tick-contents")
    head_block=content_block.find_all('a')
    for head in head_block:
        headline=head.text.strip()
        link= head.get("href")
        if 'http' not in link:
            link=base_url+link  
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Davangere University'
    failure.append((name,e))




# VKSU :Veer Kunwar Singh University
try:
    name='VKSU'
    base_url = "http://vksu.ac.in"
    url = "http://vksu.ac.in/notices-announcement/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="post_content")
    head_block=content_block.find_all('h2')
    for head in head_block:
        headline = head.find('a').text.strip()
        link= head.find('a').get("href")
        if 'http' not in link:
            link=base_url+link 
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='VKSU'
    failure.append((name,e))



# IIT Guwahati
try:
    name='IIT Guwahati'
    base_url = "https://www.iitg.ac.in/"
    url = "https://www.iitg.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="tab-pane fade in active")
    head_block=content_block.find_all("li")
    for head in head_block:
        headline = head.find('a').text.strip()
        link= head.find('a').get("href")
        if 'http'  not in link:
            link=base_url+link
        news_articles.append((name,headline,link))  
    success.append(name)
except Exception as e:
    name='IIT Guwahati'
    failure.append((name,e))

# GBU
try:
    name='GBU'
    url = "https://www.gbu.ac.in/"
    base_url = 'https://www.gbu.ac.in'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("ul", class_="list-group list-group-flush")
    head_block=content_block.find_all("li")
    for head in head_block:
        headline = head.find('a').text.strip()
        link= head.find('a').get("href").replace(' ','%20')    
        if 'http'  not in link:
            link=base_url+link    
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='GBU'
    failure.append((name,e))

# CU Jammu
try:
    name='CU Jammu'
    url = "http://www.cujammu.ac.in//Default.aspx?artid=0&type=printallevents&prvtyp=site&option=s"
    base_url='http://www.cujammu.ac.in'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="boxes-size")
    head_block=content_block.find_all("a")
    for head in head_block :
        headline = head.text.strip()
        link = head.get("href")
        if 'http'  not in link:
            link=base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='CU Jammu'
    failure.append((name, e))


# Kufos
try:
    name='Kufos'
    url = "http://kufos.ac.in/"
    base_url="http://kufos.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url, verify=False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("marquee", class_="kufos-marquee", style=" margin-top: 1px;")
    head_block=content_block.find_all("a")
    for head in head_block:
        headline = head.text.strip()
        link = head.get("href").strip()
        if 'http'  not in link:
            link=base_url+link
        if headline !='':
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='Kufos'
    failure.append((name, e))


# IIT Bombay
try:
    name='IIT Bombay'
    base_url = "https://www.iitb.ac.in"
    url = "https://www.iitb.ac.in/en/all-news"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="view-content")
    head_block=content_block.find_all("a")
    for head in head_block:
        headline = head.text.strip()
        link= head.get("href")
        if 'http'  not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='IIT Bombay'
    failure.append((name,e))

# BPUT
try:
    name='BPUT'
    base_url = 'http://www.bput.ac.in/'
    url = 'http://www.bput.ac.in/news.php'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('tr')
    for head in head_block:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='BPUT'
    failure.append((name,e))

# CUSAT
try:
    name='CUSAT'
    base_url = 'https://cusat.ac.in'
    url = 'https://cusat.ac.in/news'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url, verify = False)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', class_ = 'ho-ev-link pg-eve-desc')
    for head in head_block:
        headline = head.find('a').text.strip()
        link =  head.find('a').get('href')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='CUSAT'
    failure.append((name,e))

# MNNIT
try:
    name='MNNIT'
    base_url = 'http://www.mnnit.ac.in/'
    url = 'http://www.mnnit.ac.in/#login_form'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('div', class_ = 'popup')
    head_block=content_block.find_all('p')
    for head in head_block:
        headline = head.find('a').text.strip()
        link =head.find('a').get('href')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='MNNIT'
    failure.append((name,e))


# Rajiv gandhi Institute of Health Sciences, Karnataka
try:
    name='RGUHS'
    base_url = 'http://www.rguhs.ac.in/'
    url = 'http://www.rguhs.ac.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_content = soup.find_all("td", {"class": "n12n"})
    for head in head_content:
        try :
            link = head.find('a').get('href').replace(' ','%20')
            headline = head.text.strip()
            if 'http' not in link:
                link = base_url + link
            news_articles.append((name, headline, link))
        except:
            pass        
    success.append(name)
except Exception as e:
    name='RGUHS'
    failure.append((name, e))


# Atal Bihari Vajpayee IIITM Gwalior
try:
    name='IIITM'
    base_url = 'http://www.iiitm.ac.in'
    url = 'https://www.iiitm.ac.in/index.php/en/component/content/category/79-latest-news?Itemid=437'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all("div", {"class": "items-row"})    
    for head in head_block:
        head_box = head.find('h2')
        head = head_box.find('a').text.strip()
        link =head_box.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, head[:999], link))
    success.append(name)
except Exception as e:
    name='IIITM'
    failure.append((name, e))



# Chennai Institute of Technology
try:
    name='CIT Chennai'
    base_url = 'https://www.citchennai.edu.in/'
    url1 = 'https://www.citchennai.edu.in/latestnews/'
    url2 = 'https://www.citchennai.edu.in/upcoming-events/'
    url3 = 'https://www.citchennai.edu.in/announcements/'
    scrapers_report.append([url1,base_url,name])
    scrapers_report.append([url2,base_url,name])
    scrapers_report.append([url3,base_url,name])
    source1 = requests.get(url1)
    source2 = requests.get(url2)
    source3 = requests.get(url3)
    soup1 = BeautifulSoup(source1.text, 'html.parser')
    soup2 = BeautifulSoup(source2.text, 'html.parser')
    soup3 = BeautifulSoup(source3.text, 'html.parser')

    content_block1 = soup1.find_all("ul", {"class": "news-li"})[0]
    content_block2 = soup2.find_all("ul", {"class": "news-li"})[0]
    content_block3= soup3.find_all("ul", {"class": "news-li"})[0]

    head_block1 = content_block1.find_all('li')
    head_block2 = content_block2.find_all('li')
    head_block23 = content_block3.find_all('li')

    for head in head_block1:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        news_articles.append((name, headline, link))

    for head in head_block2:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        news_articles.append((name, headline, link))

    for head in head_block2:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        news_articles.append((name, headline, link))

    success.append(name)
except Exception as e:
    name='CIT Chennai'
    failure.append((name, e))
   

# KRU
try:
    name="KRU"
    base_url = "https://kru.ac.in/"
    url = "https://kru.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div',class_="title_small_post")
    for head in head_block:
        headline = head.text.strip().replace('Download','')
        link= head.find('a').get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="KRU"
    failure.append((name,e))


# Vikram University
try:
    name="Vikram University"
    base_url = "https://vikramuniv.ac.in"
    url = "https://vikramuniv.ac.in/index.php/en/information-notification/academic-notice"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('td',class_="list-title")
    for head in head_block:
        headline = head.text.strip()
        link= head.find('a').get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="Vikram University"
    failure.append((name,e))
# JNU
try:
    name="JNU"
    base_url = "http://www.jnu.ac.in"
    url = "http://www.jnu.ac.in/notices"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('table',class_="views-table views-view-table cols-4")
    head_block=content_block.find_all('td',headers="view-title-table-column")
    for head in head_block:
        headline = head.text.strip()
        link=head.find('a').get("href")  
        if 'http' not in link:
            link = base_url + link      
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="JNU"
    failure.append((name,e))
   

# IISER TVM
try:
   name="IISER TVM"
   base_url = "https://www.iisertvm.ac.in/"
   url = "https://www.iisertvm.ac.in/"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url)
   soup = BeautifulSoup(source.text, 'html.parser')
   content_block = soup.find_all('div',class_="card_row")
   for content in content_block[4:]:
       head_block=content.find_all('a')
       for head in head_block:
           headline = head.text
           link=head.get("href")
           news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
    name="IISER TVM"
    failure.append((name,e))

#NIT DGP
try:
   name="NIT DGP"
   base_url = "https://nitdgp.ac.in"
   url = "https://nitdgp.ac.in/p/noticesnitd/general-2"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url)
   soup = BeautifulSoup(source.text, 'html.parser')
   content_block= soup.find('ul',class_="list-group list-gr")
   head_block=content_block.find_all('a')
   for head in head_block:
       headline=head.text.strip()
       link = head.get('href')
       if 'http' not in link:
            link = base_url + link
       news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
    name="NIT DGP"
    failure.append((name,e))

# MSIT
try:
    name="MSIT"
    base_url= "https://www.msit.in"
    url = "https://www.msit.in/latest_news"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url,verify = False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="tab-content")
    head_block=content_block.find_all('a')
    for head in head_block:
        headline= head.text
        link= head.get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="MSIT"
    failure.append((name,e))

# IIITL
try:
    name="IIITL"
    base_url= "https://iiitl.ac.in/"
    url = "https://iiitl.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    head_block = soup.find_all('h3',class_="gdlr-core-blog-title gdlr-core-skin-title")
    for head in head_block:
        headline= head.text.strip()
        link= head.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="IIITL"
    failure.append((name,e))

#IITRPR
try:
   name="IITRPR"
   base_url= "https://www.iitrpr.ac.in/"
   url = "https://www.iitrpr.ac.in/"
   scrapers_report.append([url,base_url,name])
   source= requests.get(url)
   soup = BeautifulSoup(source.text, "html.parser")
   head_block = soup.find_all('p',align="justify")
   for head in head_block:
       headline= head.text
       link= head.find('a').get('href')
       if 'http' not in link:
           link=base_url+link
       news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
   name="IITRPR"
   failure.append((name,e))

#New Horizon College of Engineering-NHCE
try:
    name="NHCE"
    base_url= "https://newhorizoncollegeofengineering.in/"
    url = "https://newhorizonindia.edu/nhengineering/"
    scrapers_report.append([url,base_url,name])
    source= requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    head_block = soup.find_all('h4',class_="title")
    for head in head_block:
        headline= head.text.strip()
        link= head.find('a').get('href')
        if 'http' not in link:
           link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="NHCE"
    failure.append((name,e))
    
# IIMU
try:
    name="IIMU"
    base_url= "https://www.iimu.ac.in"
    url = "https://www.iimu.ac.in/media/news"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url,verify=False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find_all('div',class_="evetntitle")
    for content in content_block:
        head_block=content.find_all('a')
        for head in head_block:
            headline= head.text.strip()
            link= head.get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="IIMU"
    failure.append((name,e))

#XISS
try:
    name="XISS"
    base_url= "http://www.xiss.ac.in/"
    url = "http://www.xiss.ac.in/#"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="news-section")
    head_block=content_block.find_all('a')
    for head in head_block:
        headline = head.text.strip()
        link= head.get("href")
        if 'http' not in link:
           link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="XISS"
    failure.append((name,e))

# NIT Sikkim
try:                                            
    name = 'NIT Sikkim'
    url = 'https://nitsikkim.ac.in/'
    base_url='https://nitsikkim.ac.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find_all("div", {"id": "notice"})[0]
    head_block = content_block.find_all('li')
    for head in head_block:
        headline_block = head.find('a')
        if headline_block is not None:
            headline = headline_block.text.strip()
            link = headline_block.get('href')
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = 'NIT Sikkim'
    failure.append((name, e))
    
# NIT Mizoram
try:                                            
    name = 'NIT Mizoram'
    base_url = 'https://www.nitmz.ac.in/'
    url = 'https://www.nitmz.ac.in/ViewAllNewsAndEvents.aspx?sNewsNotice=AllNews'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find_all("div", {"id": "ctl00_ContentPlaceHolder_Main_NewsEvent"})[0]
    head_block = content_block.find_all('td',{'class':'setNewsNotice'})
    for head in head_block:
        header_box = head.find('p')
        try :
            headline = header_box.find('a').text
            link = header_box.find('a').get('href')
        except:
            headline = header_box.text
            link = url
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = 'NIT Mizoram'
    failure.append((name, e))



# VNIT
try:
    name='VNIT'
    base_url="https://vnit.ac.in/"
    url = "https://vnit.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="scroll-box")
    head_block=content_block.find_all("a")
    for head in head_block:
        headline = head.text.strip()
        link= head.get("href")
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='VNIT'
    failure.append((name,e))



# IIT Madras
try:
    name="IIT Madras"
    base_url="https://www.iitm.ac.in"
    url = "https://www.iitm.ac.in/happenings/IITM-news"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url,verify =False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find_all("div",class_="col-sm-4")
    for content in content_block[1:]:
        head_block=content.find_all('a')
        for head in head_block:
            headline=head.get('title')
            link=head.get('href')
            if 'http' not in link:
                link = base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="IIT Madras"
    failure.append((name,e))
    

# TMU
try:
    name="TMU"
    base_url="https://www.tmu.ac.in/news"
    url = "https://www.tmu.ac.in/news"
    
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find_all("div",class_="post-content" )
    for content in content_block:
        head_block=content.find_all('a')
        for head in head_block:
            headline = head.text
            link= head.get("href")
            if 'http' not in link:
                link = base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="TMU"
    failure.append((name,e))
    

# CURAJ
try:
    name="CURAJ"
    base_url = "http://www.curaj.ac.in"
    url = "http://www.curaj.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    head_block = soup.find_all('div',class_="newsbx")
    for head in head_block:
        headline = head.text.replace('\n',' ').strip()
        link= head.find('a').get("href")
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="CURAJ"
    failure.append((name,e))
    
# MMYVV
try:
    name="MMYVV"
    url = "http://www.mmyvv.com/"
    base_url= "http://www.mmyvv.com/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find('div',class_="myclass")
    head_block=content_block.find_all('li')
    for head in head_block:
        headline = head.text.strip()
        link=head.find('a').get("href").replace(' ','%20')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="MMYVV"
    failure.append((name,e))



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
