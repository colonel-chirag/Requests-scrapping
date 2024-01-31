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

pyfilename="college_university_8"
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

#JNU
try:
    name="JNU"
    base_url = "http://www.jnu.ac.in/"
    url = "http://www.jnu.ac.in/notices"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_table = soup.find('table',class_="views-table views-view-table cols-4")
    content_list = content_table.find_all('td',headers="view-title-table-column")
    for content in content_list:
        headline_text = content.text.strip()
        link=content.find('a').get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




# IISER TVM

try:
    name="IISER TVM"
    base_url = "https://www.iisertvm.ac.in/"
    url = "https://www.iisertvm.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find_all('div',class_="card_row")
    for content in content_div[4:]:
        head_block=content.find_all('a')
        for block in head_block:
            headline_text = block.text
            link=block.get("href")
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))

#MSIT
try:
    name="MSIT"
    base_url= "https://www.msit.in"
    url = "https://www.msit.in/latest_news"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify = False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="tab-content")
    head_block = content_div.find_all('a')
    for block in head_block:
        headline_text= block.text
        link= block.get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#IITRPR
try:
    name="IITRPR"
    base_url= "https://www.iitrpr.ac.in/"
    url = "https://www.iitrpr.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_para = soup.find_all('p',align="justify")
    for content in content_para:
        headline_text= content.text
        link= content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))



#New Horizon College of Engineering-NHCE
try:
    name="NHCE"
    base_url= "https://newhorizonindia.edu"
    url = "https://newhorizonindia.edu/nhengineering/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    head_block = soup.find_all('h4',class_="title")
    for block in head_block:
        headline_text= block.text.strip()
        link= block.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




#IIMU
try:
    name="IIMU"
    base_url= "https://www.iimu.ac.in"
    url = "https://www.iimu.ac.in/media/news"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find_all('div',class_="evetntitle")
    for content in content_div:
        head_block=content.find_all('a')
        for block in head_block:
            headline_text= block.text.strip()
            link= block.get('href')
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#XISS
try:
    name="XISS"
    base_url= "http://www.xiss.ac.in/"
    url = "http://www.xiss.ac.in/#"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="news-section")
    head_block = content_div.find_all('a')
    for block in head_block:
        headline_text = block.text
        link= block.get("href").strip()
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#SSUHS
try:
    name="SSUHS"
    base_url = "http://ssuhs.in/"
    url = "http://ssuhs.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find("ul", class_="news-list")
    head_block = content_list.find_all('a')
    for block in head_block:
        headline_text = block.text
        link= block.get("href").replace('./','').strip()
        if 'http' not in link:
            link = url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))



# KSET
try:
    name = "KSET"
    base_url = "http://kset.uni-mysore.ac.in/"
    url = "http://kset.uni-mysore.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_div = soup.find_all('div', class_="media-body")
    for content in content_div[:4]:
        headline_text = content.text[14:].replace('NEW', '').replace('Click here', '').strip()
        link = content.find('a').get('href')
        if 'http' not in link:
            link = url + link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))




#iim jammu
try:
    name="iim jammu"
    base_url = "http://www.iimj.ac.in"
    url = "http://www.iimj.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find("ul", class_="list5")
    head_block = content_list.find_all("li")
    for block in head_block:
        headline_text = block.find("a").text.strip()
        link=block.find("a").get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
        
    success.append(name)
except Exception as e:
    failure.append((name,e))







#mamc
try:
    name="mamc"
    base_url = "https://www.mamc.ac.in/"
    url = "https://www.mamc.ac.in/News/allnews"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="col-sm-12")
    head_block = content_div.find_all("li")
    for block in head_block[:10]:
        headline_text = block.text.strip()
        link=block.find("a").get("href")
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




#grau
try:
    name="grau punjab"
    base_url = "http://www.graupunjab.org"
    url = "http://www.graupunjab.org/rotat.html"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    head_block = soup.find_all("a")
    for block in head_block[:10]:
        headline_text=block.text.strip()
        link=block.get("href")[1:]
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




# AIIMS Bhubaneshwar
try:
    name = "AIIMS Bhubaneshwar"
    base_url = "https://aiimsbhubaneswar.nic.in/"
    url = "https://aiimsbhubaneswar.nic.in/whatsNew.aspx"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find('ul', class_="list-unstyled whatNewStyle")
    headline_text = content_list.find_all('a')
    for block in head_block[:10]:
        headline_text = block.text.replace('\r\n', '').strip()
        link = block.get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))



# Telangana Univeristy
try:
    name = "Telangana University"
    base_url='http://www.telanganauniversity.ac.in/'
    url = 'http://www.telanganauniversity.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_marquee = soup.find_all('marquee', direction="up")
    for content in content_marquee:
        head_block = content.find_all('a')
        for block in head_block:
            headline_text = block.text.replace('\n', '').strip()
            link = block.get('href').replace(' ', '%20')
            if 'http' not in link:
                link = url + link
            news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))




# Satyabhama
try:
    name = "Satyabhama"
    base_url = "https://www.sathyabama.ac.in/"
    url = "https://www.sathyabama.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_marquee = soup.find('marquee', class_="view-content")
    head_block = content_marquee.find_all('a')
    for block in head_block:
        headline_text = block.text
        link = block.get('href')
        if 'http' not in link:
            link = url + link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))




# mait
try:
    name='mait'
    base_url = 'https://mait.ac.in'
    url = 'https://mait.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_div = soup.find_all('div', class_ = 'crs_div')
    for content in content_div:
        headline_text = content.find('a').text
        link = content.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


# iim lucknow
try:
    name='iim lucknow'
    url = 'https://www.iiml.ac.in/news-and-announcement'
    base_url='https://www.iiml.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_table = soup.find('tbody', id = 'myTable')
    head_block = content_table.find_all('tr')
    for block in head_block:
        headline_text = block.find('a').text
        link = block.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




# lhmc
try:
    name='lhmc'
    base_url = 'http://lhmc-hosp.gov.in/'
    url = 'http://lhmc-hosp.gov.in/index4.php?lang=1&level=0&linkid=73&lid=73'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_div = soup.find('div', class_ = 'file_type_list')
    head_block = content_div.find_all('li', class_ = 'sublink')
    for block in head_block:
        headline_text = block.find('a').text
        link = block.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


# amch
try:
    name='amch'
    base_url = 'https://amch.edu.in'
    url = 'https://amch.edu.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_div = soup.find_all('div', class_ = 'a-block')
    for content in content_div:
        headline_text = content.find('a').text
        link = content.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#IIITG
try:
    name="IIIT Guwahati"
    base_url="http://www.iiitg.ac.in/"
    url="http://www.iiitg.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text,'html.parser')
    content_div = soup.find('div',style="padding:0;")
    head_block = content_div.find_all('a')
    for block in head_block:
        headline_text=block.text.replace('\n','').strip()
        link=block.get('href')
        if 'http' not in link:
            link = url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#AEC
try:
    name="AEC"
    base_url='https://aec.edu.in/'
    url="https://aec.edu.in/?p=Updates"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    content_table = soup.find('table')
    head_block = content_table.find_all('div',class_="notice notice-success")
    for block in head_block[:10]:
        headline_text=block.find("strong").text.replace('\n','').strip()
        link=block.find("a").get('href').replace(' ','%20')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))





#PUMBA
try:
    name="PUMBA"
    base_url="https://www.pumba.in/"
    url="https://www.pumba.in/"
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res,'html.parser')
    content_marquee = soup.find('marquee')
    head_block = content_marquee.find_all('a')
    for block in head_block[:10]:
        headline_text=block.text.strip()
        link=block.get('href').replace(' ','%20')
        if 'http' not in link:
            link = url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


# AIIMS JODHPUR
try:
    name="AIIMS Jodhpur"
    base_url='https://www.aiims.edu'
    url="https://www.aiims.edu/en.html"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    content_div = soup.find_all('div',id="news-container")
    for content in content_div[1:2]:
        head_block=content.find_all('a')
        for block in head_block:
            headline_text=block.text.strip()
            link=block.get('href').replace(' ','%20')
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#NIFTEM
try:
    name="NIFTEM"
    base_url='http://niftem.ac.in/'
    url="http://niftem.ac.in/newsite/?page_id=1159"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    content_table = soup.find('table')
    content_list = content_table.find_all('tr')
    for content in content_list[1:8]:
        headline_text=content.text[3:].replace('View','').strip()
        link=content.find("a").get('href')
        if '#' in link:
            link='http://niftem.ac.in/newsite/?page_id=1159#'
        else:
            link=link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




# dibru
try:
    name='dibrugarh university'
    base_url='https://dibru.ac.in/'
    url = 'https://dibru.ac.in/admission2021n/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_para = soup.find_all('p')
    for content in content_para:
        headline_text = content.find('a').text
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#Punjab University
try:
    name='Punjab University'
    base_url = "https://puchd.ac.in/"
    url = "https://news.puchd.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    content_table = soup.find('table')
    content_div = content_table.find_all('div',itemtype="http://schema.org/Article")
    for content in content_div:
        headline_text=content.find('div',itemprop="name").text.strip()
        link= content.find("a").get('href').replace('%E2%80%92','-')
        if 'http' not in link:
            link = url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#TMU
try:
    name="TMU"
    base_url='https://www.tmu.ac.in/'
    url = "https://www.tmu.ac.in/tmu/announcement"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_section = soup.find_all("section",class_="toggle" )
    for content in content_section:
            headline_text = content.find('span',style="padding-left:5px").text
            link= content.find("a").get("href")
            news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#BFUHS
try:
    name="BFUHS"
    base_url="https://bfuhs.ac.in/"
    url = "https://bfuhs.ac.in/#"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find('td',width="92%")
    head_block = content_list.find_all('a')
    for block in head_block:
        headline_text= block.text.strip()
        link=block.get('href').replace(' ','%20')
        if headline_text=='':
            continue
        elif 'http' in link:
            link=link.strip()
        else:
            link = base_url+link.strip()
            news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#AIIMS Raipur
try:
    name="AIIMS Raipur"
    base_url = "https://www.aiimsraipur.edu.in"
    url = "https://www.aiimsraipur.edu.in/user/student-admissions.php"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_table = soup.find('tbody')
    content_list = content_table.find_all('tr')

    for content in content_list[:10]:
        headline_text= content.text.replace('Link','').replace('Download','').replace('\n','').strip()[1:]
        link= content.find('a',target="_blank").get('href').replace(' ','%20')
        if 'http' not in link :
            link=base_url+link[2:]
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name,e))




#NIT Karnataka
try:
    name ='NIT Karnataka'
    base_url= "https://www.nitk.ac.in/"
    url = "https://www.nitk.ac.in/announcements"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find_all("tr")
    for content in content_list[:10]:
        headline_text=content.find("a").text.strip()
        link=content.find("a", target="_blank").get("href")
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
