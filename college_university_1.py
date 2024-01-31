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


pyfilename="college_university_1"
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

# Request Scrapers Started
#TNTEU
try:
    name='TNTEU'
    base_url = "http://www.tnteu.ac.in/"
    url = "http://www.tnteu.ac.in/notifications.php?nid=5"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)    
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("ul", class_="list prim list-ok")
    head_block=content_block.find_all("li")
    for head in head_block:
        headline = head.find("a")
        if headline is not None:
            headline_text = headline.text.strip()
            link= headline.get("href").replace(' ','%20')
            if 'http' not in link:
                link=base_url+link
                news_articles.append((name,headline_text,link))
            else:
                news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    name='TNTEU'
    failure.append((name,e))
   

# Utkal University
try:
    name='Utkal University'
    base_url = "https://utkaluniversity.ac.in"
    url = "https://utkaluniversity.ac.in/#"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")    
    content_block = soup.find("div",id="example")   
    head_block=content_block.find_all('a') 
    for head in head_block:
        headline = head.text.strip().replace('\r\n','')
        link= head.get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Utkal University'
    failure.append((name,e))
  

# Jamia Millia Islamia
try:
    name='Jamia Millia Islamia'
    base_url = 'https://www.jmi.ac.in'
    url = 'https://www.jmi.ac.in/bulletinboard/NoticeOfficialorder/latest/1'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('tr')
    for head in head_block:
        if head.find('td', style = 'border:1px solid #ddd; text-align:center;font-weight:bold;width: 100px;'):
            continue
        else:
            headline = head.find('a').text.strip()
            link = head.find('a').get('href')
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Jamia Millia Islamia'
    failure.append((name,e))
  

# University of Mysore
try:
    name='University of Mysore'
    base_url = 'http://uni-mysore.ac.in'
    url = 'http://uni-mysore.ac.in/english-version/latest-news'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('h2', class_ = 'title')
    for head in head_block:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='University of Mysore'
    failure.append((name,e))
   

# Dibrugarh University
try:
    name='Dibrugarh University'
    url = 'https://dibru.ac.in/news/'
    base_url='https://dibru.ac.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', class_ = 'gdlr-core-blog-list-frame gdlr-core-skin-e-background')
    for head in head_block:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Dibrugarh University'
    failure.append((name,e))

# JNTUK
try:
    name='JNTUK'
    base_url='https://www.jntuk.edu.in/'
    url = 'https://www.jntuk.edu.in/category/notifications/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', id = 'cat_list')
    for head in head_block:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='JNTUK'
    failure.append((name,e))

# Nagarjuna University
try:
    name='Nagarjuna University'
    base_url = 'https://www.nagarjunauniversity.ac.in/'
    url = 'https://www.nagarjunauniversity.ac.in/indexanu.html'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', class_ = 'col-md-4 col-sm-4 categories_sub cats1')
    for head in head_block :
        headline = head.find('h3', class_ = 'mt-3').text.strip().replace('\r\n\t\t\t\t\t\t\t\t', '')
        try:
            link = head.find('a').get('href')
        except:
            link = url
        if 'http' not in link:
            link=base_url+link
        if 'pdf' in link:
            link = link.replace(' ','%20')
        news_articles. append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Nagarjuna University'
    failure.append((name,e))
   

# Ahmedabad University
try:
    name='Ahmedabad University'
    base_url = 'https://ahduni.edu.in'
    url = 'https://ahduni.edu.in/news/'
    scrapers_report.append([url,base_url,name])
    source= requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', class_ = 'col-xs-12 col-sm-6 col-md-4 d-flex align-items-stretch mb-4 mb-lg-5')
    for head in head_block:
        headline = head.find('p', class_ = 'card-title').text.strip()
        link =  head.find('a').get('href').strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Ahmedabad University'
    failure.append((name,e))



# DAUNIV
try:
    name='DAUNIV'
    base_url = "https://www.dauniv.ac.in/"
    url = "https://www.dauniv.ac.in/view-all/colleges"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("ul", class_="glance-p")
    head_block=content_block.find_all("a")
    for head in head_block:
        headline = head.text.strip()
        link= head.get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='DAUNIV'
    failure.append((name,e))



#Jammu University
try:
    name='Jammu University'
    base_url = "http://jammuuniversity.ac.in/"
    url = "http://jammuuniversity.ac.in/announcements"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text,"html.parser")
    head_block = soup.find_all('span',class_="field-content")
    for head in head_block:
        
        headline=head.find('a').text.strip()
        link= head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Jammu University'
    failure.append((name,e))


# Mangalore University
try:
   name='Mangalore University'
   base_url = "https://mangaloreuniversity.ac.in"
   url = "https://mangaloreuniversity.ac.in/latest-home-news"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url)
   soup = BeautifulSoup(source.text,"html.parser")
   head_block = soup.find_all('span',class_="field-content")
   for head in head_block:
       headline=head.find('a').text.strip()
       link= head.find('a').get('href')
       if 'https' not in link:
           link = base_url+link           
       news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
    name='Mangalore University'
    failure.append((name,e))

# Central University of Gujarat
try:
    name='Central University of Gujarat'
    base_url= "https://www.cug.ac.in/"
    url = "https://www.cug.ac.in/latest.php"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", id = "nav-tabContent")
    head_block=content_block.find_all("li")
    for head in head_block:
        headline = head.find('i').findNextSibling(text=True).strip()[:-3]
        link= head.find("a").get("href")
        if 'https' not in link:
            link=base_url+link           
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Central University of Gujarat'
    failure.append((name,e))

# IISER Mohali
try:
    name='IISER MOHALI'
    base_url= "https://www.iisermohali.ac.in"
    url = "https://www.iisermohali.ac.in/events/news/news-archive"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_ = "articleBody")
    head_block=content_block.find_all("li")
    for head in head_block:         
        headline = head.text.strip()
        link_box = head.find("a")
        if link_box is not  None:
            link = link_box.get("href").strip().replace(' ','%20')
            if 'http' not in link:
                link= base_url+link
        else:
            link = url
        news_articles.append((name,headline,link))    
    success.append(name)
except Exception as e:
    name='IISER MOHALI'
    failure.append((name,e))


# Janaknayak Chandrashekar University
try:
   name='JNCU'
   base_url= "https://jncu.ac.in/"
   url = "https://jncu.ac.in/"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url)
   soup = BeautifulSoup(source.text, "html.parser")
   content_block = soup.find("div", class_ = "content")
   head_block=content_block.find_all("li")
   for head in head_block:
       headline = head.find("a")
       if headline is not None:
            headline_text = headline.text.strip()
            link= headline.get("href")
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,headline_text,link))
   success.append(name)
except Exception as e:
   name='JNCU'
   failure.append((name,e))


# NIT Rourkela
try:  
    name= 'NIT Rourkela'       
    base_url = 'http://www.nitrkl.ac.in'
    url = 'https://www.nitrkl.ac.in/Home/Our-Latest-News/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all("div", {"class": "news-list-item"})
    for head in head_block:
        headline = head.find('p').text.strip().replace('\r\n                        More>>','')
        link = head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name= 'NIT Rourkela'
    failure.append((name, e))

# NIT Silcher
try:
    name='NIT Silcher'
    base_url = 'http://www.nits.ac.in'
    url = 'http://www.nits.ac.in/newsupdates.php'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('b')
    for head in head_block:        
        headline = head.text.strip()
        link_box = head.find('a')
        if link_box is not None:
            link=link_box['href']
            if 'http' not in link:
                link = base_url + link     
        else :
            link =""  
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='NIT Silcher'
    failure.append((name, e))

# IIT Bhubaneswar
try:
    name= 'IIT Bhubaneswar'  
    base_url = 'http://www.iitbbs.ac.in/'
    url = 'https://www.iitbbs.ac.in/news.php'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('ol')    
    for head in head_block[0].children:
        headline = head.find('a').text
        link = head.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name= 'IIT Bhubaneswar'
    failure.append((name, e))

# Veer Sundara Sai University of Technology
try:                                            
    name = 'VSSUT'
    base_url = 'http://www.vssut.ac.in/'
    url = 'https://www.vssut.ac.in/news-events.php'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find_all('tr')    
    for content in content_block[1:]:
        check = 0
        head_block = content.find_all('td')
        try :
            for cell in head_block:
                if cell['data-title'] == 'Title':
                    head = cell.text.strip()
                if cell['data-title'] == 'View':
                    link = cell.find('a').get('href')
                    if 'http' not in link:
                        link = base_url + link
            check = 1
        except:
            pass
        if check == 1:
            news_articles.append((name, head, link))
    success.append(name)
except Exception as e:
    name = 'VSSUT'
    failure.append((name, e))
    



# CU Chandigarh
try:
    name='CU'
    base_url='https://news.cuchd.in/'
    url = 'https://news.cuchd.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    content_block = soup.find('div',class_='grid-posts')
    head_block=content_block.find_all(class_='post-title')
    for head in head_block:
        headline = head.text.strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='CU'
    failure.append((name,e))


# Ranchi University
try:
    name='Ranchi University'
    url = 'https://www.ranchiuniversity.ac.in/'
    base_url = 'https://www.ranchiuniversity.ac.in'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    head_block = soup.find_all('h6')
    for head in head_block:
        headline = head.text.strip()
        link_box = head.find('a')
        if link_box is not None:
            link =  link_box.get('href').replace(' ','%20')  
            if 'http' not in link:
                link=base_url+link         
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Ranchi University'
    failure.append((name,e))

# NFSU
try:
    name='NFSU'
    url = 'https://www.nfsu.ac.in/news'
    base_url='https://www.nfsu.ac.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    head_block = soup.find_all('div',class_='gdlr-core-blog-full-head-right')
    for head in head_block:
        headline = head.text.strip()
        link = head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='NFSU'
    failure.append((name,e))



# MAFSU
try:
    name='MAFSU'
    url = 'http://www.mafsu.in/#news-tab'
    base_url = 'http://www.mafsu.in/'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    head_block = soup.find_all('a',target='_blank',style='color:Black; font-size:12px;')
    for head in head_block:
        headline = head.text.strip()
        link =  head.get('href').replace(' ','%20')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='MAFSU'
    failure.append((name,e))

# IITD
try:
    name='IITD'
    base_url = "https://home.iitd.ac.in/"
    url = "https://home.iitd.ac.in/news-all.php"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('div',class_="container ar-container-top")
    head_block=content_block.find_all('div',class_="event-details p-15")
    for head in head_block:
        headline = head.text.replace('Read more','').strip()
        link= head.find('a').get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='IITD'
    failure.append((name,e))

# DCRUST
try:
    name='DCRUST'
    base_url = "http://www.dcrustm.ac.in/"
    url = "http://www.dcrustm.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text,"html.parser")
    content_block = soup.find_all('div',class_="wpb_text_column wpb_content_element")
    for content in content_block:
        head_block=content.find_all('a')
        for head in head_block:
            headline=head.text.strip().replace('\xa0','')
            link= head.get('href')
            if 'http' not in link: 
                link=base_url+link                  
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='DCRUST'
    failure.append((name,e))


#Lala Lajpat Rai University
try:
    name='Luvas'
    url = "https://www.luvas.edu.in"
    base_url="https://www.luvas.edu.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text,"html.parser")
    content_block = soup.find('div',class_="tab-pane active")
    head_block=content_block.find_all('li')
    for head in head_block:
        headline=head.text.strip()
        link= head.find('a').get('href')
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Luvas'
    failure.append((name,e))

# VSKUB
try:
    name='VSKUB'
    base_url = "http://vskub.ac.in/"
    url = "http://vskub.ac.in/"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text,"html.parser")
    content_block = soup.find('div',class_="testimonial_content_inner")
    head_block=content_block.find_all('a')
    for head in head_block:
        headline=head.text.strip()
        link= head.get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='VSKUB'
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
