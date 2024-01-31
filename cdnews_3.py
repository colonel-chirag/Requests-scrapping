import csv
import logging
import requests
import os
import sys
import urllib3
from zoneinfo import ZoneInfo
from datetime import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


import pandas as pd
from bs4 import BeautifulSoup
import uploader


pyfilename = 'cdnews_3'

# base_path = "/home/notification-scrapers/Cd_scrapers/"
# base_path = "/root/New_Scrapers/Cd_scrapers/"
base_path = f"{sys.argv[1]}/Cd_scrapers/"
logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", 
    level=logging.INFO)

now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
logger = logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))

# os.chdir("/root/New_Scrapers")
news_articles = []
success = []
failure = []
scrapers_report = []
#aglasem general scraper

def aglasem_parser(soup,url,name):
    
    
    news_block = soup.find_all('div',class_="jeg_postblock_content")
    for news in news_block:
        headline = news.get_text().strip()
        link = news.find('a').get('href')
        news_articles.append((name, headline, link))
    
        
def aglasem_scraper(base_url):
    try :
        url = base_url
        name = 'Aglasem'
        scrapers_report.append([url, base_url, name])
        agent = {"User-Agent": "Mozilla/5.0"}    
        res = requests.get(url, headers=agent)
        soup = BeautifulSoup(res.text, 'html.parser')
        aglasem_parser(soup,url,name)
    except Exception as e:
        failure.append(base_url,e)
        
aglasem_scraper('https://news.aglasem.com/')
aglasem_scraper('https://admission.aglasem.com/')
aglasem_scraper('https://institutes.aglasem.com/')

def collegedekho_parser(soup,base_url,name):
        
        try:
            block1 = soup.find(class_='newslistCol')
            clist = block1.find_all('div',class_='box')
            for c in clist:
                healdine_block = c.find(class_='image')
                headline = healdine_block.find(
                                'img').get('alt').strip()
                link = healdine_block.find('a').get('href')
                if 'http' not in link:
                    link = base_url+link
                news_articles.append((name, headline, link))
            success.append(base_url+" block1")
        except Exception as e:
            failure.append((base_url, e))
        
        try:    
            block2 =  soup.find(class_='news-group-bg')
            block2_list = block2.find_all(class_='news-title-new')
            for result in block2_list:
                headline = result.get_text().strip()
                link = result.find('a').get('href')
                if 'http' not in link:
                    link = base_url+link
    
                news_articles.append((name, headline, link))  
            success.append(base_url+" block2") 
        except Exception as e:
            failure.append((base_url, e)) 
        try:
            block3 = soup.find(class_='rightCol')
            results = block3.find_all(class_='box')
            for result in results:
                headline = result.find('a').find('img').get('alt').strip()
                link = result.find('a').get('href')
                if 'http' not in link:
                    link = base_url+link

                news_articles.append((name, headline, link))
            success.append(base_url+" block3")
        except Exception as e:
            failure.append((base_url, e))   


def collegedekho_scraper(url,base_url):
    try:
        name = 'Collegedekho'
        scrapers_report.append([url, base_url, name])
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        collegedekho_parser(soup,base_url,name)
    except Exception as e:
        failure.append((base_url, e)) 

collegedekho_article_url ='https://www.collegedekho.com/articles/'
collegedekho_news_url = 'https://www.collegedekho.com/news/'
collegedekho_scraper(collegedekho_article_url,collegedekho_article_url)
collegedekho_scraper(collegedekho_news_url,collegedekho_news_url)

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
    data = pd.read_csv ('/root/New_Scrapers/Cd_scrapers/csv_files/cd_main.csv',
                        on_bad_lines='skip',engine='python')
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
