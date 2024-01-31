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


pyfilename="college_university_5"
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

#Rabindranath Tagore University

try:
    name='Rabindranath Tagore University'
    base_url = 'https://rntu.ac.in/'
    url = 'https://rntu.ac.in/about/Letest-News'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('ul', class_ = 'list-aggregate').find_all('li')
    for result in results:
        headline = result.find('a')
        if headline is not None:
            headline_text = headline.text
            link = headline.get('href')   
            if "http" in link:
                link=link
            else:
                link=base_url+link     
            news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))

#College of Vocational Studies
try:
    name ='College of Vocational Studies'
    url = "https://www.cvs.edu.in/view-all-details.php"
    base_url="https://www.cvs.edu.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="about-menu").find_all("li")
    for result in results[:10]:
        headline=result.find('a')
        if headline is not None:
            headline_text = headline.text.strip()
            link=headline.get("href")
            if "http" in link:
                link=link
            else:
                link=base_url+link
            news_articles.append((name,headline_text,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))

#Kalyani Mahavidyalaya
try:
    name ='Kalyani Mahavidyalaya'
    url = "http://kalyanimahavidyalaya.co.in/notice.aspx"
    base_url="http://kalyanimahavidyalaya.co.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("div", class_="box")
    for result in results[:9]:
        headline=result.text.strip()
        link=result.find('a')
        if link is not None:
            link = link.get("href").replace(" ","%20")
            if "http" in link:
                link=link
            else:
                link=base_url+link
        else :
            link = ""
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
 
#Patna College

try:
    name ='Patna College'
    url = "http://www.patnacollege.org/"
    base_url="http://www.patnacollege.org/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("marquee", direction="up").find_all("a")
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
    pass

#VIPS
try:
    name ='VIPS'
    base_url= 'https://vips.edu/'
    url = "https://vips.edu/admission-information/"
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
  

#Sri Sri University
try:
    name ='Sri Sri University'
    url = "https://srisriuniversity.edu.in/"
    base_url="https://srisriuniversity.edu.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", class_="news-container").find_all("a")
    for result in results[:10]:
        headline=result.text.strip()
        link=result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))

#Kirori Mal College
try:
    name ='Kirori Mal College'    
    base_url='https://kmc.du.ac.in/'
    url = "http://kmc.du.ac.in/category/latest-news/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("h3", class_="entry-title")
    for result in results:
        headline=result.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))

#Jesus and Mary College
try:
    name ='Jesus and Mary College'
    base_url = "https://www.jmc.ac.in/"
    url = "https://www.jmc.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("ul", style="text-align: center;").find_all("a")
    for result in results:
        headline=result.text.strip()
        link=result.get("href").replace(" ","%20")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
 
#National Law University
try:
    name ='National Law University'
    url = "https://nludelhi.ac.in/Annuoncement.aspx"
    base_url="https://nludelhi.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find('ul',style="overflow:auto;").find_all("li",style='')
    for result in results[:10]:
        headline=result.text.strip()
        link=result.a.get("href")
        if 'http' in link:
            link=link
        else:
            link= base_url+link
        news_articles.append((name,headline,link))  
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass 

#Miranda House
try:
    name ='Miranda house'
    url = "https://www.mirandahouse.ac.in/notice.php"
    base_url='https://www.mirandahouse.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:12]
    for result in results:
        headline=result.a.text.strip()    
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#Satyawati College
try:
    name ='Satyawati College'
    url = "http://satyawati.du.ac.in/CIRCULARS.HTML"
    base_url="http://satyawati.du.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:12]
    for result in results:
        headline=result.find("td").text.strip()
        link=result.a.get("href").replace(" ","%20")
        if "http" in link:
            link=link
        else:
            link=base_url+link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    name ='Satyawati College'
    failure.append((name,e))
 
#Institute of Management Studies Noida 
try:
    name='Institute of Management Studies Noida'
    base_url='https://imsnoida.com/'
    url='https://imsnoida.com/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    marquee=soup.find('marquee')
    header_block=marquee.find_all('a')
    for header in header_block:
        header_text = header.text.strip()
        link=header['href']
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,header_text,link))
    success.append(name)
except Exception as e:
    name='Institute of Management Studies Noida'
    failure.append((name,e))
    
#Narsee Monjee Institute of Management Studies 
try:
    name='Narsee Monjee Institute of Management Studies'
    base_url='https://www.nmimsbengaluru.org/'
    url='https://www.nmimsbengaluru.org/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    div=soup.find('div',class_="col-xs-12 col-sm-12 col-md-3 padb20")
    headlines = div.find_all('a')
    for headline in headlines[:-1] :
        title=headline.text.strip()
        link=headline['href']
        if 'http' not in link:
            link=url+link
        news_articles.append((name,title,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    

#Institute of Management Technology

try:
    name='Institute of Management Technology'
    base_url='https://www.imtnagpur.ac.in/'
    url='https://www.imtnagpur.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    ul=soup.find('ul',class_="follow-us")
    header=ul.find('a')
    headline = header.text.strip()
    link=header['href']
    if 'http' not in link:
         link=base_url+link
    news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Institute of Management Technology'
    failure.append((name,e))
    
#IFIM Business School
try:
    url = "https://jagsom.edu.in/"
    base_url = url
    name = "IFIM Business School"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    articles = soup.find_all("h2")        
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
    

#Thapar Institute of Engineering and Technology
try:
    name='Thapar Institute of Engineering and Technology'
    base_url='https://www.thapar.edu/aboutus/news'
    url='https://www.thapar.edu/aboutus/news'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    div=soup.find('div',class_='hghlt-link')
    header_block = div.find_all('a')
    for header in header_block:
        header_text =header.text.strip()
        link=header['href']
        news_articles.append((name,header_text,link))
    success.append(name)
except Exception as e:
    name='Thapar Institute of Engineering and Technology'
    failure.append((name,e))
    
#Pandit Deendayal Petroleum University, School of Technology
try:
    name='Pandit Deendayal Petroleum University, School of Technology'
    base_url='http://sot.pdpu.ac.in/' 
    url='http://sot.pdpu.ac.in/'    
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    headlines = soup.find(class_='updateBox well').find_all('li')
    for line in headlines:
        headline = line.text.strip()
        links = ''
        a_tags = line.find_all('a',attrs={'href':True})
        for tag in a_tags:
            link = tag['href']
            if 'http' not in link:
                link = base_url + link
            links += link + ' '
        links = links.strip()
        news_articles.append((name,headline,links))
    success.append(name)
except Exception as e:
    name='Pandit Deendayal Petroleum University, School of Technology'
    failure.append((name,e))
    
#Chhotu Ram Rural Institute Of Technology
try:
    name='Chhotu Ram Rural Institute Of Technology'    
    base_url='http://www.crritonline.com/'
    url='http://www.crritonline.com/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_block=soup.find('div',class_='modal-body')
    headline_text=content_block.find('h2').text
    link=content_block.find('a')['href']
    if 'http' not in link:
        link=base_url+link
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    name='Chhotu Ram Rural Institute Of Technology' 
    failure.append((name,e))
    

#Panimalar Engineering College
try:
    name='Panimalar Engineering College'
    base_url='https://www.panimalar.ac.in/'
    url='https://www.panimalar.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get('https://www.panimalar.ac.in/').text
    soup=BeautifulSoup(source,'html.parser')
    content_block =soup.find('li',class_="admission")
    header_block =content_block.find('a')
    headline_text=header_block.text
    link=header_block['href']
    if 'http' not in link:
        link=base_url+link
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    name='Panimalar Engineering College'
    failure.append((name,e))
    

#HKBK College of Engineering

try:
    name='HKBK College of Engineering'
    base_url='https://www.hkbk.edu.in/'
    url='https://www.hkbk.edu.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_block=soup.find('div',class_="home-banner-links-fixed")
    header_block = content_block.find('ul').find_all('a')
    for header in header_block:
        headline=header.text.strip()
        link=header['href']

        if 'http' not in link:
            link=url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
 
#Asansol Engineering College

try:
    name='Asansol Engineering College'
    base_url='https://aecwb.edu.in/'
    url='https://aecwb.edu.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_block=soup.find('div',id='enquiryAdmDv1')
    header_block=content_block.find('a')
    headline = header_block.text.strip()
    link=header_block['href']
    if 'http' not in link:
        link=base_url+link
    news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))

#Saveetha Institute of Medical And Technical Sciences

try:
    name='Saveetha Institute of Medical And Technical Sciences'
    base_url='https://www.saveetha.com/'
    url='https://www.saveetha.com/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    content_block=soup.find('div',class_="header-nav")
    a_tags=content_block.find_all('a')
    headline_text=a_tags[3].text.strip()
    link=a_tags[3]['href']
    if 'http' not in link:
        link=url+link
    news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))

print('Successful Scrapers -'+str(success))
print('Failed Scrapers -'+str(failure))

#print(news_articles)
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
