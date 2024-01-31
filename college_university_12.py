
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
print (now.strftime("%Y-%m-%d %H:%M:%S"))

pyfilename="college_university_12"
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

#SPJIMR
try:
    url = "https://www.spjimr.org/newsroom/"
    base_url = "https://www.spjimr.org"
    name = "SPJIMR"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    articles = soup.find("div", class_="row js-image-slider animatedParent animateOnce").find_all(class_="bottom")        
    for i in articles:
        headline=i.find('p').text.strip()
        link_tag = i.find('a')
        if link_tag:
            link = link_tag["href"]
            if "http" not in link:
                link = base_url + link
            news_articles.append((name , headline , link ))
    news = soup.find(class_='latetnews-bar').find_all(class_='item animatedParent animateOnce')
    for i in news:
        headline = i.find('h3').text.strip()
        link = i.find('a')['href']
        if "http" not in link:
                link = base_url + link
        news_articles.append((name,headline,link))
    events = soup.find(class_='eventlastest-bar space').find_all(class_='item animatedParent animateOnce')        
    for i in events:
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

# Ayurved University
try:
    name = "Ayurved University"
    base_url = "https://ayurveduniversity.edu.in"
    url = "https://ayurveduniversity.edu.in/index1.php"
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find('ul', id="vertical-ticker").find_all('a')
    for result in results[:10]:
        headline = result.text
        link = result.get("href")
        if 'http' in link:
            link = link[6:]
        else:
            link = base_url + link[8:]
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))



#iim sirmaur(announcements)
try:
    url = "https://www.iimsirmaur.ac.in/announcements"
    base_url = "https://www.iimsirmaur.ac.in"
    name = "IIMSIRMUR"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    articles = soup.find_all("td")        
    for i in articles:
        link_tag = i.find('a')
        if link_tag:
            link = link_tag["href"]
            headline=link_tag.text.split('(Size')[0].strip()
            if "http" not in link:
                link = base_url + link
            news_articles.append((name , headline , link ))
    success.append(name)
except Exception as e:
    failure.append((name, e))


# Periyar University
try:
    name="Periyar University"
    base_url= "https://www.periyaruniversity.ac.in"
    url = "https://www.periyaruniversity.ac.in/AllNewsEvents.php"
    scrapers_report.append([url,base_url,name])
    res=opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    head_block = soup.find_all("div",class_="NewsContent")#.find_all('a')
    for head in head_block[:10]:
        headline= head.text.replace('Prospectus','').replace('Application Link','')
        headline=headline.replace('Circular','').replace('Download','').replace('\n','').strip()
        link=head.find('a').get('href').replace(' ','%20')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
   name="Periyar University" 
   failure.append((name,e))


# UNOM
# try:
#     name = "UNOM"
#     url = "https://www.unom.ac.in/index.php?route=administration/announcement"
#     base_url = "https://unom.ac.in/"
#     scrapers_report.append([url, base_url, name])
#     res = opener.open(url).read()
#     soup = BeautifulSoup(res, "html.parser")
#     articles = soup.find_all("div", class_="content-title")    
#     for i in articles:
#         link_tag = i.find('a')
#         if link_tag:
#             link = link_tag["href"]
#             headline=link_tag.text.strip()
#             if "http" not in link:
#                 link = base_url + link
#             news_articles.append((name , headline , link ))
#     success.append(name)
# except Exception as e:
#     failure.append((name, e))


# Hemchand National Gujrat University
# try:
#     base_url= "https://ngu.ac.in/"
#     url = "https://ngu.ac.in/NewsDetails.aspx"
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     results = soup.find("aside", class_ = "no-featured").find_all("li")
#     for result in results:
#         headline = result.find("a").get_text().strip()
#         link= result.find("a").get("href").strip().replace(' ','%20')
#         if 'https' not in link:
#             link=base_url+link
#             news_articles.append(('NGU',headline,link))
#         else:
#             news_articles.append(('NGU',headline,link))
#     success.append('NGU')
# except Exception as e:
#     failure.append(('NGU',e))
# 

# Assam University
# try:
#     base_url = "http://www.aus.ac.in"
#     url = "http://www.aus.ac.in/notices/"
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     results = soup.find("div", class_="entry-content").find_all("li")
#     for result in results:
#         headline = result.find('a').text.strip()
#         link= result.a.get("href").strip()
#         news_articles.append(('Assam University',headline,link))
#     success.append('Assam University')
# except Exception as e:
#     failure.append(('Assam University',e))
# 

# MNIT
# try:
#     url = 'http://www.mnit.ac.in/news/newsall.php?type=latest'
#     base_url = 'http://www.mnit.ac.in'
#     res = requests.get(url)
#     soup=BeautifulSoup(res.text,'html.parser')
#     results = soup.find(id='pills-1).find_all('a')
#     for result in results:
#         headline = result.get_text().strip()[:999]
#         link = base_url + result.get('href')
#         news_articles.append(('MNIT',headline,link))
#     success.append('MNIT')
# except Exception as e:
#     failure.append(('MNIT',e))
# 

# CU Kashmir
# try:
#     url = "https://www.cukashmir.ac.in/default.aspx"
#     base_url = "https://www.cukashmir.ac.in"
#     name = "CUK"
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text,"html.parser")
#     divs = soup.find_all(class_='labelul')
#     for div in divs:
#         results = div.find_all("li", class_="labelli")[:-1]       
#         for i in results:
#             link_tag = i.find('a')
#             if link_tag:
#                 link = link_tag["href"]
#                 headline=i.text.split('\nRead')[0].strip()
#                 if "http" not in link:
#                         link = base_url + link
#                 news_articles.append((name , headline , link ))
#     success.append(name)
# except Exception as e:
#     failure.append((name, e))


# # SVNIT
# try:
#     name='SVNIT'
#     base_url = "https://www.svnit.ac.in/"
#     url = "https://www.svnit.ac.in/web/notice_events_tenders.php?tag=notice"
#     scrapers_report.append([url,base_url,name])
#     source = requests.get(url, verify = False)
#     soup = BeautifulSoup(source.text, "html.parser")
#     results= soup.find_all("td", class_="tablefont")
#     for result in results[:10]:
#         headline = result.a.text.strip()
#         link= result.a.get("href").replace(' ','%20').strip()
#         news_articles.append((name,headline,link))
#     success.append(name)
# except Exception as e:
#     failure.append((name,e))
# 

#iimcal
# try:
#     base_url = "https://www.iimcal.ac.in/"
#     url = "https://www.iimcal.ac.in/news"
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     results = soup.find("ul", class_="views-listing")
#     for result in results.find_all("a"):
#         headline = result.text
#         link = result.get("href").strip()
#         if 'http' not in link:
#             link=base_url+link
#         news_articles.append(('iimcal', headline, link))
#     success.append('iimcal')
# except Exception as e:
#     failure.append(('iimcal', e))
# 


#NEIGRIHMS
# try:
#     name="NEIGRIHMS"
#     base_url = "http://www.neigrihms.gov.in/"
#     url = "http://www.neigrihms.gov.in/examsnotification.html"
#     res = requests.get(url,verify=False)
#     soup = BeautifulSoup(res.text, "html.parser")
#     results = soup.find('div',align="left").find_all('a')
#     for result in results:
#         headline= result.text.strip()
#         if headline=='':
#             continue
#         link=base_url+result.get('href').replace(' ','%20')
#         news_articles.append((name, headline, link))
#     success.append(name)
# except Exception as e:
#     failure.append((name,e))


# #Central University of Punjab
# try:
#     name="Central University of Punjab"
#     url = "http://cup.edu.in/"
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     results = soup.find_all('div',class_="field field--name-body field--type-text-with-summary field--label-hidden field__item")
#     for result in results[:2]:
#         result= result.find_all('a')
#         for r in result:
#                 headline=r.text
#                 link = r.get('href')
#                 if 'http' in link:
#                         link= link
#                 else:
#                     link= url+link
#                 news_articles.append((name,headline,link))
#     success.append(name)
# except Exception as e:
#     failure.append((name,e))

# TNPSC
# try:
#     name = "TNPSC"
#     base_url = 'https://www.tnpsc.gov.in/'
#     url = 'https://www.tnpsc.gov.in/English/Notification.aspx'
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     results = soup.find_all('a', class_="viewlink")
#     for result in results[:10]:
#         headline = result.text
#         link = base_url + (result.get('href'))[2:]
#         news_articles.append((name, headline, link))
#     success.append(name)
# except Exception as e:
#     failure.append((name, e))
# 


# GPSC
# try:
#     name = "GPSC"
#     base_url = 'https://gpsc.gujarat.gov.in'
#     url = 'https://gpsc.gujarat.gov.in/newseventlist'
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     results = soup.find('ul', id="ctl13_Newli").find_all('li')
#     for result in results[:10]:
#         headline = result.text.strip()
#         link = base_url + result.a.get('href')
#         news_articles.append((name, headline, link))
#     success.append(name)
# except Exception as e:
#     failure.append((name, e))

# PSC
# try:
#     name = "PSC"
#     url = 'http://www.psc.cg.gov.in'
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     results = soup.find_all('a', class_="style409")
#     for result in results:
#         headline = result.text
#         link = url + result.get('href')[2:]
#         news_articles.append((name, headline, link))
#     success.append(name)
# except Exception as e:
#     failure.append((name, e))
# 

#('NIT Raipur', ConnectTimeout(MaxRetryError("HTTPConnectionPool(host='www.nitrr.ac.in', port=80
#NIT RR

try:
    name="NIT Raipur"
    base_url= "http://www.nitrr.ac.in/"
    url = "http://www.nitrr.ac.in/admission.php#menu4"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find_all('div',class_="panel-body")
    for content in content_div[:4] :
        head_block=content.find_all('a')
        for block  in head_block:
            headline_text = block.text.strip()
            link= block.get('href').replace(' ','%20')
            if 'http' not in link:
                link = base_url + link
            news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))

#-[('IIITN', ConnectTimeout(MaxRetryError("HTTPSConnectionPool(host='iiitn.ac.in', port=443)
#IIITN
try:
    name='IIITN'
    url = 'https://iiitn.ac.in/news.php'
    base_url = 'https://iiitn.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_list = soup.find('ul',class_='catagorie-list')
    head_block= content_list.find_all('a',target='_blank')
    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        link = block.get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))

# ramjas college

try:
    name ='ramjas college'
    url = "https://ramjas.du.ac.in/college/web/index.php"
    base_url="https://ramjas.du.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="panel-content").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=result.get("href")
        if "http" in link:
            link=link
        else:
            link=base_url+link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
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
