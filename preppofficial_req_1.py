from ast import Name
import pandas as pd
#from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import warnings
import time
import sys
import ssl
# import os
import urllib3
from lxml import etree
import uploader

import os.path
import pathlib
import logging
import sys

start_time = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = start_time.strftime("%Y-%m-%d %H:%M")
pyfilename = 'preppofficial_req_1'


# base_path = "/home/notification-scrapers/Prepp_scrapers/"
# base_path = "/root/New_Scrapers/Prepp_scrapers/"
base_path = f"{sys.argv[1]}/Prepp_scrapers/"
logging.basicConfig(
    filename=f"{base_path}log_files/{pyfilename}.log", 
    level=logging.INFO)
logger = logging.getLogger()
# handler = RotatingFileHandler(f"{base_path}log_files_backup/{pyfilename}.log", maxBytes=10000,
#                                   backupCount=1)
# logger.addHandler(handler)
logger.info("Code started")
logger.info(start_time.strftime("%Y-%m-%d %H:%M:%S"))
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore')
ssl._create_default_https_context = ssl._create_unverified_context
news_articles = []
success = []
failure = []
scrapers_report = []

#load_dotenv()


official_tag = " prepp official"
#UP Police
try:
    base_url = 'http://www.uppbpb.gov.in/'
    url = 'http://www.uppbpb.gov.in/'
    name = 'UP Police'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text,'html.parser')
    headlines = soup.find_all('p',class_='auto-style2')
    for line in headlines[1:]:
        headline = ' '.join(line.text.strip().split())
        lnks = line.find_all('a')
        links = []
        for lnk in lnks:
            try:
                if lnk['href'][-3:] == 'pdf':
                    lnk['href'] = url + lnk['href'] 
                links.append(lnk['href'])
            except KeyError:
                pass
        link = ' '.join(links)
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name = 'UP Police'
    failure.append((name,e))
    
#BSE Odisha
try:
    base_url = 'http://www.bseodisha.ac.in/'
    url = 'http://www.bseodisha.ac.in/latest-updates.html'
    name = 'BSE Odisha'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text,'html.parser')
    headlines = soup.find('div',class_='entry-content').find_all('li')
    for line in headlines[:20]:
        headline = line.text.replace('â\x80\x93','-').strip()
        link = line.find('a')['href']
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#SBI PO

try:
    base_url = 'https://www.sbi.co.in'
    url = 'https://www.sbi.co.in/web/careers'
    name = 'SBI PO'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find_all('div',class_ = 'descp')
    for line in headlines:
        links = []
        headline = ' '.join(line.text.strip().replace("\xa0"," ").split("\n"))
        link = line.find_all('a')
        for i in range(len(link)):
            if link[i]['href'].startswith('https'):
                link[i]['href'] = link[i]['href']
            else:
                link[i]['href'] = base_url + link[i]['href']
        for i in range(len(link)):
            links.append(link[i]['href'])
        all_link = ' '.join(links)    
        news_articles.append((name,headline,all_link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


# Manipur PSC
try:
    url = 'http://mpscmanipur.gov.in/'
    base_url = 'http://mpscmanipur.gov.in/'
    name =  'Manipur PSC'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html") 
    results = soup.find('marquee').find_all('ul')
    for res in results:
        headline = res.find('font').text
        link = res.find('a').get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))        
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass
    

#AFCAT

try:
    base_url = 'https://afcat.cdac.in/'
    url = 'https://afcat.cdac.in/AFCAT/'
    name = 'AFCAT'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find_all('p',class_= 'font-alt mb-30 titan-title-size-1')
    for line in headlines:
        
        headline = ' '.join(line.text.strip().split())
        link = line.find('a')
        if link is not None:
            link = link['href']

            if link.startswith('https'):
                link = link
            else:
                link = url + link
        else :
            link = ""
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#Indian Post Recruitment

try:
    base_url = 'https://www.indiapost.gov.in'
    url = 'https://www.indiapost.gov.in/VAS/Pages/Content/Recruitments.aspx?Category=Recruitment'
    name = 'Indian Post Recruitment'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find_all('div', class_ = 'marl20')
    for line in headlines:
        headline = line.find('div').text.strip()
        link = line.find('a')['href']
        if link.startswith('https'):
            link = link
        else:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Indian Coast Guard

try:
    base_url = 'https://joinindiancoastguard.gov.in/'
    url = 'https://joinindiancoastguard.gov.in/'
    name = 'Indian Coast Guard'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find('marquee',attrs={'direction':'up'}).find_all('a')
    for line in headlines:
        headline = line.text.strip()
        link = line['href']
        if link.startswith('https'):
            link = link
        else:
            link = url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass
#Mizoram PSC

try:
    base_url = 'https://mpsc.mizoram.gov.in/'
    url = 'https://mpsc.mizoram.gov.in/'
    scrapers_report.append([url,base_url,name+official_tag])
    name =  'Mizoram PSC'
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "lxml") 
    results = soup.find('ul', class_ = 'loading-wrapper news-list icon').find_all('li')
    for res in results:
        headline = res.find('a').text
        link = res.find('a').get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Meghalaya PSC

try:
    url = 'https://mpsc.nic.in/'
    base_url = 'https://mpsc.nic.in/'
    name =  'Meghalaya PSC'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html") 
    results = soup.find_all('marquee')
    for res in results:
        var = res.find_all('li')
        for v in var[:5]:
            headline = v.text.replace('\r\n', '').replace('  ', '')
            link = v.find('a').get('href')
            if link.startswith('http'):
                link = link
            else:
                link = base_url+link
            news_articles.append((name, headline, link))        
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

##Goa PSC
try:
    url = 'https://gpsc.goa.gov.in/'
    base_url = 'https://gpsc.goa.gov.in/'
    scrapers_report.append([url,base_url,name+official_tag])
    name = "Goa PSC"
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    res = soup.find_all('table', width = '50%')
    for r in res:
        tds = r.find_all('tr')
        for td in tds[1:]:
            headline = td.text
            headline = headline.split('\n')[2]
            link = td.find('a').get('onclick')
            link = link.split("'")[1]
            if link.startswith('http'):
                link=link
            else:
                link = base_url+link
            news_articles.append((name, headline, link))

    res = soup.find('marquee', onmouseover="this.stop();").find_all('a', target="_blank")
    for r in res:
        headline = r.text
        try:
            link = r.get('onclick')
            link = link.split("'")[1]
            if link.startswith('http'):
                link = link
            else:
                link = base_url+link
        except:
            link = r.get('href')
            if link.startswith('http'):
                link = link
            else:
                link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# UGC NET

try:
    base_url =  'https://ugcnet.nta.nic.in/'
    url = 'https://ugcnet.nta.nic.in/'
    name = 'UGC NET'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    result1 = soup.find_all('a',class_='with-urlchange')
    result2 = soup.find_all('a',attrs={'title':'download'})
    for result in result1:
        headline = result.text.strip()
        link = result['href']
        news_articles.append((name,headline,link))
    for result in result2:
        headline = result.text.strip()
        link = result['href']
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#CSIR NET

try:
    base_url = 'https://csirnet.nta.nic.in/'
    url = 'https://csirnet.nta.nic.in/'
    name = 'CSIR NET'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    result1 = soup.find_all('a',class_='with-urlchange')
    result2 = soup.find_all('a',attrs={'title':'download'})
    for result in result1:
        headline = result.text.strip()
        link = result['href']
        news_articles.append((name,headline,link))
    for result in result2:
        headline = result.text.strip()
        link = result['href']
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass
#UKPSC
try:
    base_url = 'https://ukpsc.gov.in/latestupdate'
    url='https://ukpsc.gov.in/latestupdate'
    name = "UKPSC"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    ul=soup.find('ul',class_="genList")
    for a in ul.find_all('a'):
        text=a.text.strip()
        link=a['href'].strip()
        text= " ".join(text.split())
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,text,link))
    success.append(name)
 #print(news_articles)
except Exception as e:
    failure.append((name,e))
    pass


#RBI Assistant
try:    
    base_url = 'https://opportunities.rbi.org.in/Scripts/'
    url='https://opportunities.rbi.org.in/Scripts/Vacancies.aspx'
    name = "RBI Assistant"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    div=soup.find('div',class_="grid_8 alpha content_area omega")
    for a in div.find_all('a'):
        text=a.text
        link=a['href']

        text=text.strip()
        link=link.strip()
        #text= " ".join(text.split())
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,text,link))
    success.append(name)
     #print(news_articles) 
except Exception as e:
    failure.append((name,e))
    pass

#CWC

try:    
    base_url = 'https://www.cewacor.nic.in/'
    url='https://www.cewacor.nic.in/'
    name = "CWC"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    div=soup.find('div',class_="microsoft mark")
    for a in div.find_all('a'):
        text=a.text
        link=a['href']
        text=text.strip()
        link=link.strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,text,link))
    success.append(name)
 #print(news_articles) 
except Exception as e:
    failure.append((name,e))
    pass

#IES
try:
    base_url = 'https://www.upsc.gov.in/'
    url='https://www.upsc.gov.in/'
    name = "IES"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get(url,verify=False).text
    soup=BeautifulSoup(source,'html.parser')
    div=soup.find('div',class_="whats-new-marq")
    for a in div.find_all('a'):
        text=a.text
        link=a['href']
        text=text.strip()
        link=link.strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,text,link))
    success.append(name)
 #print(news_articles) 
except Exception as e:
    failure.append((name,e))
    pass

print('Successful Scrapers -', success)
print('Failed Scrapers -', failure)


logger.info('Successful Scrapers -'+str(success))
logger.info('Failed Scrapers -'+str(failure))

df = pd.DataFrame(news_articles)
df.drop_duplicates(inplace = True) 
df['date'] = start_time.strftime("%Y-%m-%d %H:%M")
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

    main_scrapers_report =pd.read_csv(f'{base_path}report/prepp_scrapers_report.csv')
except :
    main_scrapers_report = pd.DataFrame(columns = ['url','base_url','name','name_of_the_scraper'])   

main_scrapers_report= pd.concat([main_scrapers_report,report_df])
main_scrapers_report.drop_duplicates(inplace=True)
main_scrapers_report.to_csv(f'{base_path}report/prepp_scrapers_report.csv',index=False)

#the number of scraper that are scraped
news_count_df = df.groupby('source')['title'].count().reset_index()
news_count_df.columns = ['name'	,'title']
count_report = report_df.merge(news_count_df,
                               on='name',
                               how='left')[['name','title','url']]
count_report.fillna(0,inplace=True)
count_report['date'] = start_time.strftime("%Y-%m-%d %H:%M")
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
