
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from zoneinfo import ZoneInfo
import requests
import os
import re
import urllib3
import uploader

import logging
from logging.handlers import RotatingFileHandler
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))

# os.chdir("/root/New_Scrapers")

pyfilename = 'cdnews_1'

import sys
# base_path = "/home/notification-scrapers/Cd_scrapers/"
# base_path = "/root/New_Scrapers/Cd_scrapers/"
base_path = f"{sys.argv[1]}/Cd_scrapers/"
logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", 
    level=logging.INFO)
logger = logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))

news_articles = []
success = []
failure = []
scrapers_report = []

# Hindustan Times
try:
    url = 'https://hindustantimes.com/education'
    base_url = 'https://www.hindustantimes.com'
    name = 'HT'
    scrapers_report.append([url, base_url, name])
    agent = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=agent)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.find(id='dataHolder')
    h3_tags = data.find_all('h3')
    # print(newss)
    for news in h3_tags:
        content = news.find('a')
        if content is not None:
            headline = content.text
            link = content['href']
            headline = headline.strip()
            link = link.strip()
            if 'http' not in link:
                link = base_url+link
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = 'HT'
    failure.append((name, e))


# Times Now
try:
    base_url = 'https://www.timesnownews.com'
    url = 'https://www.timesnownews.com/education'
    name = 'Times Now'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    main_box = soup.find('div', class_='w4gam')
    a_tags = main_box.find_all('a')
    a_tags_len = len(a_tags) 
    for i in a_tags:
        headline = i.text
        link = i['href']
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append((name,a_tags_len))
except Exception as e:
    name = 'Times Now'
    failure.append((name, e))


# Times of India
try:
    base_url = 'https://timesofindia.indiatimes.com'
    url = 'https://timesofindia.indiatimes.com/education'
    name = 'TOI'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.find('div', class_='wRxdF')
    a_tags = data.find_all('a')
    for news in a_tags:
        headline = news.text
        link = news['href']
        link = link.strip()
        headline = headline.strip()
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = 'TOI'
    failure.append((name, e))


# PagalGuy
try:
    name = "PagalGuy"
    base_url = 'https://www.pagalguy.com/articles'
    url = "https://www.pagalguy.com/articles"
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find('div', id='articlesCont')
    article_tags = content.find_all('article')
    for article in article_tags:
        
        headline = article.find('h3')

        link = article.find('a')
        if headline is not None:
            headline = headline.text
        else:
            headline = ''

        if link is not None:

            link = link['href']
            if 'http' not in link:
                link = base_url+link

        else:
            link = ''

        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = "PagalGuy"
    failure.append((name, e))

# MBA-Universe
try:
    name = 'MBA-Universe'
    base_url = 'https://www.mbauniverse.com'
    url = 'https://www.mbauniverse.com/7-days-search.php'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find(class_='view-content').find_all(class_='views-row')
    
    for news in newss:
        headline = news.find(class_='field-content').get_text()
        link = news.find('a').get('href')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    
# News.carrers-360
try:
    base_url = 'https://news.careers360.com'
    url = 'https://news.careers360.com/latest?page=1'
    name = 'Careers-360'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find(class_="artiLis-MainBlock").find_all(class_='heading4')
    for news in newss:
        head = news.find('a')
        if head is not None:
            headline = head.get_text()
            link = head.get('href')
            if 'http' not in link:
                link = base_url+link

            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = 'Careers-360'
    failure.append((name, e))

# College Admission
try:
    name = 'College-Admission'
    url = 'https://www.collegeadmission.in/index.shtml'
    base_url = 'https://www.collegeadmission.in/index.shtml'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find('div', {'class': 'link_list'}).find_all('li')
    for news in newss:
        headline1 = news.find('span', {'class': 'name_list_search'}).find(
            'a').find('br').get_text().strip()
        try:
            headline2 = news.find('span', {'class': 'name_list_search'}).find(
                'a').find('br').next_sibling.strip()
        except:
            pass
        college_name = news.find('span', {'class': 'name_list_search'}).find('a').find('span', {
            'style': 'text-decoration:underline; color:#000000; font-style:normal'}).get_text().strip().encode('ascii', 'ignore').decode("utf-8")
        link = news.find('span', {'class': 'name_list_search'}).find(
            'a').get('href')
        if headline1 != '':
            news_articles.append((college_name+': '+name, headline1, link))
        else:
            news_articles.append((college_name+': '+name, headline2, link))
    success.append(name)
except Exception as e:
    name = 'College-Admission'
    failure.append((name, e))


# JagranJosh
try:
    name = 'JagranJosh'
    base_url = 'http://www.jagranjosh.com'
    url = 'https://www.jagranjosh.com/news?source=hp_news'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        newss = soup.find_all(class_='listing')[0].find_all(class_='heading')
        for news in newss:
            link = news.find('a').get('href')
            headline = news.get_text().strip()
            
            if link.startswith('https'):
                link = link
            else:
                link = base_url+link
            news_articles.append((name, headline, link))
    except Exception as e:
        failure.append((name, e))
    try:   
        tags = soup.find('ul', class_='listing').find_all('li')

        for tg in tags:
            headline = tg.div.text.replace('\n', '')
            link = tg.div.a.get('href')
            if link.startswith('https'):
                link = link
            else:
                link = base_url+link
            news_articles.append((name, headline, link))
        success.append(name)
    except Exception as e:
        failure.append((name, e))
except Exception as e:
    failure.append((name, e))


# Success CDS Admission
try:
    base_url = 'https://www.successcds.net'
    url = 'https://www.successcds.net/admission-notification/index.html'
    name = 'Success CDS Admission'
    scrapers_report.append([url, base_url, name])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find_all('tr', 
                              class_='wptb-row')[1:]
    for line in headlines:
        row_data = line.find_all('td')
        headline = f'Institute name : {row_data[0].text} Course :{row_data[1].text} Eligibility Criteria : {row_data[2].text} Last Date to Appl: {row_data[3].text}'.replace("\xa0", "")
        link = line.find('a')['href']
        news_articles.append((f'{row_data[0].text} : {name}', headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))


# Success CDS Entrance Exam
try:
    base_url = 'https://www.successcds.net/'
    url = 'https://www.successcds.net/Entrance-Exam/latest-notifications.html'
    name = 'Success CDS Entrance Exam'
    scrapers_report.append([url, base_url, name])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find_all('tr', 
                              class_='wptb-row')[1:]
    for line in headlines:
        row_data = line.find_all('td')
        headline = f'Exam Name : {row_data[0].text} Course :{row_data[1].text} Eligibility Criteria : {row_data[2].text} Last Date to Appl: {row_data[3].text}'.replace("\xa0", "")
        link = line.find('a')['href']
        news_articles.append((f'{row_data[0].text} : {name}', headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))


# Punekar News

try:
    base_url = 'https://www.punekarnews.in'
    url = 'https://www.punekarnews.in/category/education/'
    name = 'Punekar News'
    scrapers_report.append([url, base_url, name])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find_all('article')
    for line in headlines:
        line_block = line.find('h3').find('a')
        if line_block is not None:
            headline = line_block.text.strip()
            link = line_block['href']
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))


# Legally-India
try:
    name = 'Legally-India'
    base_url = 'https://www.legallyindia.com'
    url = 'https://www.legallyindia.com/lawschools/lawschools/blog'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find(class_='items-leading itemwrap clearfix').find_all('h2')
    for news in newss:
        headline = news.find('a')
        if headline is not None:
            headline_text = headline.get_text().strip()
            link = headline.get('href')
            if link.startswith('https'):
                link = link
            else:
                link = base_url+link
            news_articles.append((name, headline_text, link))
    success.append(name)

except Exception as e:
    failure.append((name, e))


# RESULT-91
#base_url for different state is different
try:
    name = 'Result-91'
    url = "http://www.result91.com/h/AllIndiaResults"
    base_url = ""
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    university_names = soup.find_all(
        "a", class_= "list-group-item list-header padleft5")

    results = soup.find_all("a", {"class": "list-group-item pl35"})
    news_size = len(university_names)
    for university in university_names:

        uni_name_text = university.find('b').text
        release_date_text = university.find('strong').text
        
        while True:
            if university.find_next("a").get('class') == ['list-group-item', 'pl35']:
                
                result = university.find_next(
                    "a", class_='list-group-item pl35')
                
                result_name = result.get_text().strip()
                
                link = result.get('href')
                
                headline = f'{uni_name_text} : {result_name} :{release_date_text}'
                news_articles.append((f'{uni_name_text} :{name}', headline, link))
                university = university.find_next(
                    "a", class_='list-group-item pl35')
            else:
                break
    success.append((name,news_size))
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
    logger.info('creating new cdmain_scrapers_report')
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
