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


pyfilename="college_university_6"
import sys
base_path = "/home/notification-scrapers/Cd_scrapers/"
# base_path = "/root/New_Scrapers"
# base_path = f"{sys.argv[1]}/Cd_scrapers/"
logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", 
    level=logging.INFO)
logger=logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))

#Symbiosis College of Arts and Commerce

try:
    name='Symbiosis College of Arts and Commerce'
    base_url='https://symbiosiscollege.edu.in/'
    url='https://symbiosiscollege.edu.in/' 
    scrapers_report.append([url,base_url,name])   
    source=requests.get(url).text    
    soup=BeautifulSoup(source,'html.parser')
    content_div=  soup.find_all('div',class_='box2')
    #h=article.find('header',class_="entry-header")
    head_block = content_div[0].find_all('p')
    for head in head_block: 
        link=head.find('a')['href']
        headline_text=head.text.strip()

        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#ILS Law College

try:
    name='ILS Law College'
    base_url='https://ilslaw.edu/'
    url='https://ilslaw.edu/'    
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find('ul',class_='cell-center-list')
    head_block = content_div.find_all('li')
    for li in head_block:
        link=li.find("a")['href']
        headline_text=li.find("a").text
        headline_text=headline_text.strip()
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Techno India University

try:
    name='Techno India University'
    url='https://www.technoindiauniversity.ac.in/'
    base_url='https://www.technoindiauniversity.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find('section',class_='team section')
    headline_text=content_div.find("a").text
    headline_text=headline_text.strip()
    link=content_div.find("a")['href']
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#TERI School of Advanced Studies
try:
    name='TERI School of Advanced Studies'
    base_url='https://terisas.ac.in/'
    url='https://terisas.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div = soup.find('button',class_='btn-txt')
    headline_text=content_div.text
    headline_text=headline_text.strip() 
    link=content_div.find("a")['href']
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Terna Medical College

try:
    name='Terna Medical College'
    base_url='https://ternamedical.org/'
    url='https://ternamedical.org/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find('div',class_='wpb_column vc_column_container vc_col-sm-6 vc_col-has-fill')
    content_div2=content_div.find('div',class_='wpb_raw_code wpb_raw_js')
    head_block = content_div2.find_all("a")
    for block in head_block:
        headline_text=block.text
        headline_text=headline_text.strip()
        link=block['href']
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#The American College
try:
    name='The American College'
    base_url='https://americancollege.edu.in/'
    url='https://americancollege.edu.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find_all('div',class_='gdlr-core-pbf-column-content clearfix gdlr-core-js gdlr-core-sync-height-content')
    headline_text=content_div[1].find("span").text
    headline_text=headline_text.strip()
    link=content_div[1].find("a")['href']
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#Thakur College of Science and Commerce
try:
    name='Thakur College of Science and Commerce'
    base_url='https://www.tcsc.edu.in/'
    url='https://www.tcsc.edu.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find_all('div',class_='col-sm mb-2')
    head_block = content_div[2].find_all('a')
    for block in head_block:
        headline_text=block.text.strip()
        link=block['href']
        if 'http' not in link:
            link=url+link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    

#Uka Tarsadia University
try:
    name='Uka Tarsadia University'
    base_url='http://utu.ac.in/'
    url='http://utu.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    headlines = soup.find(class_='col-md-4 mb-sm-60 wow fadeInUp').find_all('a')[1:]
    for line in headlines:
        headline = line.text.strip()
        link = line['href']
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Uluberia College

try:
    name='Uluberia College'
    base_url='https://www.uluberiacollege.in/'
    url='https://www.uluberiacollege.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find('div',class_='clearfix latestnewsInner')
    headline_text=content_div.find("a").text
    headline_text=headline_text.strip()
    link=content_div.find("a")['href']
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass



#University of Allahabad

try:
    name='University of Allahabad'
    base_url='https://www.allduniv.ac.in/'
    url='https://www.allduniv.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find('header')
    head_block=content_div.find_all('a')
    headline_text=head_block[2].text
    link=head_block[2]['href']
    headline_text=headline_text.strip()
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#Vardhman Mahaveer Open University

try:
    name='Vardhman Mahaveer Open University'
    base_url='https://www.vmou.ac.in/'
    url='https://www.vmou.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text    
    soup=BeautifulSoup(source,'html.parser')
    content_table=soup.find_all('tbody')
    content_table_rows=content_table[2].find_all('tr')
    headline_text=content_table_rows[1].find("a").text
    headline_text=headline_text.strip()
    link=content_table_rows[1].find("a")['href']
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass



#Vels Institute of Science, Technology & Advanced Studies

try:
    name='Vels Institute of Science, Technology & Advanced Studies'
    base_url='https://vistas.ac.in/'
    url='https://vistas.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    results=soup.find(class_="news").find_all('a')
    for result in results:
        headline = result.text.strip()
        link = result['href']
        if 'http' not in link:
            link = base_url + link
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Vishwakarma Institute of Technology
try:
    name='Vishwakarma Institute of Technology'
    base_url='https://www.vit.edu/'
    url='https://www.vit.edu/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find('div',class_='latestnewsWrap')
    headline_text=content_div.find("h3").text
    link=content_div.find("a")['href']
    headline_text=headline_text.strip()
    link=link.lstrip('/')
    if 'http' not in link:
        link=url+link
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Vishwakarma University

try:
    name='Vishwakarma University'
    base_url='https://www.vupune.ac.in/'
    url='https://www.vupune.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_marquee=soup.find('marquee')
    head_block = content_marquee.find_all('a')
    headline_text=head_block[1].text
    headline_text=headline_text.strip()
    link=head_block[1]['href']
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Acharya Institute of Technology

try:
    name='Acharya Institute of Technology'
    base_url='https://www.acharya.ac.in/'
    url='https://www.acharya.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_div=soup.find_all('div',class_='row')
    headline_text=content_div[1].find("a").text
    link=content_div[1].find("a")['href']
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#ximb
try:
    name='ximb'
    base_url = "https://ximb.edu.in/"
    url = "https://ximb.edu.in/news-and-events/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="main_list_wrapper")
    for result in results.find_all("div", class_="col-lg-4 col-md-6 col-12"):
        headline_text = result.find("h2").text.replace("\n","")
        link = result.find("a").get("href").strip()
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#imik
try:
    name='imik'
    base_url = "https://www.imik.edu.in/"
    url = "https://www.imik.edu.in/news-events/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="col-lg-9 p-3 box-shadow-4 border-radius-0 news_listing")
    for result in results.find_all("div", class_="col-md-9 col-lg-9"):
        headline_text = result.find("a").text
        link = result.find("a").get("href").strip()
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass



#jntua
try:
    name='jntua'
    base_url = "https://www.jntua.ac.in/"
    url = "https://www.jntua.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="tab-content")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text
        link= block.get("href").strip()
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#narula
try:
    name='narula'
    base_url = "https://www.nit.ac.in/"
    url = "https://www.nit.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="b-ol-list-text-container")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text
        link = block.get("href").strip().replace(" ","")
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#vnit
try:
    name='vnit'
    base_url = "https://vnit.ac.in/"
    url = "https://vnit.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="scroll-box")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text
        link= block.get("href").strip()
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass



#gbu
try:
    name='gbu'
    base_url = "https://www.gbu.ac.in/"
    url = "https://www.gbu.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("ul", class_="list-group list-group-flush")
    result_list = results.find_all("li")

    for result in result_list:
        headline_text = result.find("a").text.strip()
        link= result.find("a").get("href").strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#cujammu
try:
    name='cujammu'
    base_url = "http://www.cujammu.ac.in/"
    url = "http://www.cujammu.ac.in//Default.aspx?artid=0&type=printallevents&prvtyp=site&option=s"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="boxes-size")
    head_block = content_div.find_all("a")

    for block in head_block:
        headline_text = block.text.strip()
        link = block.get("href").strip()
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass



#kufos
try:
    name='kufos'
    base_url = "http://kufos.ac.in/"
    url = "http://kufos.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_marquee = soup.find("marquee", class_="kufos-marquee", style=" margin-top: 1px;")
    head_block = content_marquee.find_all("a")
    
    for block in head_block:
        headline_text = block.text.strip()        
        link = block.get("href").strip()
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#iitbombay
try:
    name='iitb'
    base_url = "https://www.iitb.ac.in/"
    url = "https://www.iitb.ac.in/en/all-news"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="view-content")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text
        link= block.get("href").strip()
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#cit
try:
    name='cit'
    base_url = "https://cit.ac.in/"
    url = "https://cit.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", id="noticeContainer")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text.replace('\n','')
        link =  block.get("href").strip()
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#coep
try:
    name='coep'
    base_url = "https://www.coep.org.in/"
    url = "https://www.coep.org.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_table = soup.find("table", class_="views-table cols-2").find("tbody")
    head_block = content_table.find_all("a")
    for block in head_block:
        headline_text = block.text
        link = block.get("href").strip()
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#rmkec
try:
    name='rmkec'
    base_url = "http://www.rmkec.ac.in/"
    url = "http://www.rmkec.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="popular")
    head_block = content_div.find_all("div", class_="media")
    for block in head_block:
        headline_text = block.find("a").text
        link =  block.find("a").get("href").strip()
        news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#nsit
try:
    name='nsit'
    base_url = "http://www.nsit.ac.in/"
    url = "http://www.nsit.ac.in/news/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", class_="container col-md-9")
    head_block = content_div.find_all("div", class_="media-body")
    for block in head_block:
        headline_text = block.find("h4").text
        link = block.find("a").get("href").strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


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
