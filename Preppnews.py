from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import os
import urllib3
import sys
import warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
import pandas as pd

import logging
homebase_path = "/home/notification-scrapers/"
base_path = "/root/New_Scrapers"
logging.basicConfig(filename = f"{base_path}/Prepp_scrapers/log_files/preppnews.log",level=logging.INFO)
logger=logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore')

news_articles = []
success = []
failure = []
scrapers_report = []

now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = now.strftime("%Y-%m-%d %H:%M")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#INDIANEXPRESS
try:
    base_url = "https://indianexpress.com/"
    url = "https://indianexpress.com/article/jobs/"
    name = 'indianexpress'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")
    content = soup.find('div', class_ = 'nation')
    link_list = content.find_all('div', class_ = 'articles')
    for i in link_list[:5]:
        con = i.find('h2')
        box = con.find('a')
        if box is not None:
            headline = box.text
            link = box.get('href')
            if 'http' not in link:
                link = base_url+link
            news_articles.append(('INDIANEXPRESS',headline,link))
    success.append('INDIANEXPRESS')      
except Exception as e:
    failure.append(('INDIANEXPRESS',e))


#KANNADANEWS18

try:
    url = 'https://kannada.news18.com/news/jobs'
    base_url = 'https://kannada.news18.com/news/jobs'
    name = "KANNADANEWS18"
    scrapers_report.append([url,base_url,name])
    content = requests.get(url) 
#     print(content.status_code)
    soup = BeautifulSoup(content.text, "html.parser")
    
    results = soup.find('div',  class_ ='section-blog-left-img')
    headline = results.text
    link = results.find('a').get('href')
    if link.startswith('http'):
        link = link
    else:
        link = base_url+link
    news_articles.append((name, headline, link)) 
    
    results2 = soup.find('div',  class_ ='section-blog-left-img-list')
    headlines = results2.find_all('a')
    for line in headlines:
        headline = line.text
        link = line.get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link
        news_articles.append((name, headline, link)) 
            
    results3 = soup.find_all('div', class_ = 'blog-list-blog')
    for result in results3:
        headline = result.text
        link = result.find('a').get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))  
            
    success.append(name)
except Exception as e:
    name = "KANNADANEWS18"
    failure.append((name,e))
    




print('Successful Scrapers -', success)
print('Failed Scrapers -', failure)

df = pd.DataFrame(news_articles)

df.drop_duplicates(inplace = True) 
df['date'] = now.strftime("%Y-%m-%d %H:%M")
df.columns = ['source','title','link','date']

df.to_csv('/root/New_Scrapers/Prepp_scrapers/csv_files/preppnewscraper_try.csv', index = False)
data = pd.DataFrame()
try:    
    data = pd.read_csv ('/root/New_Scrapers/Cd_scrapers/csv_files/cd_main.csv')
except:
    pass
data = pd.concat([ data,df])

data.drop_duplicates(subset = ['title'], inplace = True)
data.to_csv('/root/New_Scrapers/Cd_scrapers/csv_files/cd_main.csv', index = False)
print(df[df['source']=='Free Job Alert'].date.to_list())
print(data[(data['source']=='Free Job Alert') & (pd.to_datetime(data['date']).dt.date.astype(str) == now.strftime("%Y-%m-%d"))])
print("all done")




#REPUBLICWORLD

# try:
#     base_url = "https://www.republicworld.com/"
#     url = "https://www.republicworld.com/education/jobs"
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser")

#     content_1 = soup.find('div', class_ = 'sub-mrgnright sub-left-stories')
#     link_list_1 = content_1.find_all('article')
#     for i in link_list_1:
#         box = i.find('a')
#         if box is not None:
#             headline = box.text.strip()
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#         news_articles.append(('REPUBLICWORLD',headline,link))

#     content_2 = soup.find('div', class_ = 'sub-mrgnright sub-right-stories')
#     link_list_2 = content_2.find_all('article')
#     for i in link_list_2:
#         box = i.find('a')
#         if box is not None:
#             headline = box.text.strip()
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#         news_articles.append(('REPUBLICWORLD',headline,link))

#     content_3 = soup.find('div', class_ = 'channel-card-wrapper')
#     link_list_3 = content_3.find_all('article')
#     for i in link_list_3:
#         box = i.find('a')
#         if box is not None:
#             headline = box.find('h2').text.strip()
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#         news_articles.append(('REPUBLICWORLD',headline,link))
        
#     success.append('REPUBLICWORLD')      
# except Exception as e:
#     failure.append(('REPUBLICWORLD',e))
#     pass

# News.careers-360
# try:
#     base_url = 'https://news.careers360.com'
#     url = 'https://news.careers360.com/latest?page=1'
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     newss = soup.find(class_="artiLis-MainBlock").find_all(class_='heading4')
#     for news in newss:
#         headline = news.find('a').get_text()
#         link = news.find('a').get('href')
#         link = base_url+link
#         if headline == '':
#             continue
#         else:
#             news_articles.append(('Careers-360 Jobs', headline[:999], link))
#     success.append('Careers-360 Jobs')
# except Exception as e:
#     failure.append(('Careers-360 Jobs', e))
#     pass

#Jagranjosh(govt)
# for i in range(1,4):
#     if i == 1:
#         try:
#             url = 'https://www.jagranjosh.com/articles-sarkari-naukri-government-jobs-1303378740-1'
#             base_url = 'https://www.jagranjosh.com'
#             name = "JAGRANJOSH(Govt)"
#             driver.get(url)
#             time.sleep(3)
#             new_notf = driver.find_elements(By.CLASS_NAME, "articlelanding_detail")
#             link_a = driver.find_elements(By.XPATH, '//*[@id="tag_Sample"]/div/div/h2/strong/a')

#             b = len(new_notf)
#             for j in range(b):
#                 text = new_notf[j].text.split('\n')
#                 link = link_a[j].get_attribute('href')
#                 news_articles.append((name, text[-1], link))
#             success.append(name)
#                 # print(news_articles)
#         except Exception as e:
#             failure.append((name, e))
#             pass
        
#     else:
#         try:
#             # 'https://www.jagranjosh.com/articles-sarkari-naukri-government-jobs-1303378740-1-p2'
#             url = 'https://www.jagranjosh.com/articles-sarkari-naukri-government-jobs-1303378740-1-p'+str(i)
#             base_url = 'https://www.jagranjosh.com'
#             name = "JAGARNJOSH"
#             driver.get(url)
#             time.sleep(3)
#             new_notf = driver.find_elements(By.CLASS_NAME,"articlelanding_detail")
#             link_a = driver.find_elements(By.XPATH,'//*[@id="tag_Sample"]/div/div/h2/strong/a')

#             b = len(new_notf)
#             for j in range(b):
#                 text = new_notf[j].text.split('\n')
#                 link = link_a[j].get_attribute('href')
#                 news_articles.append((name,text[-1],link))
#             success.append(name)
#                 # print(news_articles)
#         except Exception as e:
#             failure.append((name,e))
#             pass


#shiksha_sarkari_exams
# try:
#     url = 'https://www.shiksha.com/sarkari-exams/articles-st-21'
#     base_url = 'https://www.shiksha.com'
#     name = "shiksha_sarkari_exams"
#     content = requests.get(url)
#     soup = BeautifulSoup(content.text, "html.parser")
#     headlines = soup.find_all('h3', class_ = 'articleTitle')
#     for line in headlines: 
#         headline = line.find('a').text
#         link = line.find('a').get('href')
#         if link.startswith('http'):
#             link = link
#         else:
#             link = base_url+link
#         news_articles.append((name, headline, link))
#     success.append((name))
# except Exception as e:
#     failure.append((name,e))
#     pass

#TAMIL INDIAN EXPRESS


# try:
#     base_url = "https://tamil.indianexpress.com/"
#     url = "https://tamil.indianexpress.com/education-jobs/"
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser")

#     content = soup.find_all('div', class_ = 'wp-block-newspack-blocks-ie-stories')
#     for i in content[:10]:
#         link_list = i.find_all('div', class_ = 'entry-title')
#         for j in link_list:
#             box = j.find('a')
#             if box is not None:
#                 headline = box.text
#                 link = box.get('href')
#                 if 'http' not in link:
#                     link = url+link
#             news_articles.append(('TAMILINDIANEXPRESS',headline,link))
#     success.append('TAMILINDIANEXPRESS')      
# except Exception as e:
#     failure.append(('TAMILINDIANEXPRESS',e))
#     pass



#HARIBHOOMI

# try:
#     base_url = "https://www.haribhoomi.com/"
#     url = "https://www.haribhoomi.com/career"
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser")
#     content_1 = soup.find('div', class_ ='listing_main_level_top mtop15')

#     content_2 = soup.find('div', class_ ='listing_main_level_middle_tw_column mtop15')
#     link_list_1 = content_1.find_all('div',class_ = 'list_content')
#     link_list_2 = content_2.find_all('li',class_ = 'news_listing')
#     for i in link_list_1:
#         con  = i.find('h3')
#         box = con.find('a')
#         if box is not None:
#             headline = box.text
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#         news_articles.append(('HARIBHOOMI',headline,link))
        
#     for i in link_list_2:
#         con  = i.find('h4')
#         box = con.find('a')
#         if box is not None:
#             headline = box.text
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#         news_articles.append(('HARIBHOOMI',headline,link))
        
#     success.append('HARIBHOOMI')      
# except Exception as e:
#     failure.append(('HARIBHOOMI',e))
#     pass
