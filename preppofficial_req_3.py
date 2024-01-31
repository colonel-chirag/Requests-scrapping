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
import logging
# import os
import urllib3
from lxml import etree
import uploader

start_time = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = start_time.strftime("%Y-%m-%d %H:%M")
pyfilename = 'preppofficial_req_3'

import sys
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
import urllib.request
import random
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

news_articles = []
success = []
failure = []
scrapers_report = []

official_tag = " prepp official"
#APSC
try:
    base_url = 'http://www.apsc.nic.in/'
    url='http://www.apsc.nic.in/'
    name = "APSC"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get('http://www.apsc.nic.in/').text
    soup=BeautifulSoup(source,'html.parser')
    result=soup.find_all('ul',class_="scroll-updates")
    if result is not None:
        for res in result:
            for a in res.find_all('a'):
                headline = a.text.strip()   
                link=a['href'].strip()
                if 'http' not in link:
                    link=base_url+link
                if name not in success:
                    success.append(name)
                news_articles.append((name,headline,link))
    else:
        failure.append((name, 'result is None'))
except Exception as e:
    name = 'APSC'
    failure.append((name,e))
    
    
#IBPS
try:
    url = 'https://ibps.in/'
    base_url = 'https://ibps.in/'
    name = "IBPS"
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url, verify = False)
    soup = BeautifulSoup(content.text, "html.parser")
    mqs = soup.find_all('div', style = 'clear:both;padding:10px 5px;')
    for mq in mqs:
        try:
            headlines = mq.find_all('a')
            for line in headlines:
                headline = line.text
                link = line.get('href')
                if link.startswith('http'):
                    link = link
                else:
                    link = base_url+link
                    
                if link.endswith('.pdf'):
                    news_articles.append((name, headline, link))
                else:
                    response = requests.get(link, verify =False)
                    soup = BeautifulSoup(response.text, "html.parser")
                    links = soup.find_all('div', style = 'clear:both;padding:10px 5px 10px 45px;border-radius:5px;margin-bottom:5px;background:url(https://www.ibps.in/wp-content/themes/ibps/images/hand-right.png) no-repeat 10px 2px #F4F4F4;')
                    if len(links) ==0:
                        news_articles.append((name, headline, link))
                    else:
                        for link_ in links:
                            headline = link_.find('a').text
                            link = link_.find('a').get('href')
                            news_articles.append((name,headline, link))       
        except Exception as e:
            failure.append((name,e))
            pass
    mqs = soup.find_all('div', style = 'clear:both;padding:40px 5px;')
    for mq in mqs:
        try:
            headlines = mq.find_all('a')
            for line in headlines:
                headline = line.text
                link = line.get('href')
                if link.startswith('http'):
                    link = link
                else:
                    link = base_url+link
                news_articles.append((name, headline, link))
        except Exception as e:
            failure.append((name, e))
            pass
        news_articles.append((name, headline, link))

    news_articles = list(set(news_articles))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#PSPCL(Press Release)

try:
    url = 'https://pspcl.in/'
    base_url = 'https://pspcl.in/'
    name = "PSPCL"
    scrapers_report.append([url,base_url,name+official_tag])
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.find_all("div", class_='ticker-2')
    for res in results:
        try:
            var1 = res.find_all('a')
            for var in var1:
                headline = var.text.strip()
                link_ = var.get('href').strip()
                if link_.startswith('https') == True:
                    link =link_
                else:
                    link= base_url+link_
                news_articles.append((name, headline, link))
        except Exception as e:
            pass
    success.append(name)
except Exception as e:
    failure.append((name, e))

#BPSC
try:
    url = 'https://www.bpsc.bih.nic.in/'
    name = 'BPSC'
    base_url = 'https://www.bpsc.bih.nic.in/'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text,'html.parser')
    headlines = soup.find('table',attrs={'id':'table1'}).find_all('tr')[1:21]
    for line in headlines:
        headline = line.find_all('td')[1].text.strip()
        headline=headline.replace("\n","").replace("\t","").replace("\r","").replace("\xa0","")
        link = line.find('a')['href']
        if not link.startswith('https'):
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

##DSSSB
try:
    url = 'https://dsssb.delhi.gov.in'
    base_url = 'https://dsssb.delhi.gov.in'
    name = "DSSSB"
    scrapers_report.append([url,base_url,name+official_tag])
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    content = requests.get(url, verify = False)
#     print(content.status_code)
    soup = BeautifulSoup(content.text, "html.parser")
    results = soup.find_all('li', class_ = 'menu-217')
    for result in results:
        headline=  result.text.replace("\n","")
        link = result.find('a').get('href')
        if link.startswith('http'):
            link =  link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))

    results2 = soup.find_all('span', class_ = 'field-content')
    for result in results2:
        headline=  result.text.replace("\n","")
        link = result.find('a').get('href')
        if link.startswith('http'):
            link =  link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name) 
    
except Exception as e:
    failure.append((name,e))
    pass


#PSPCL(Notification)
try:
    url = 'https://pspcl.in/'
    base_url = 'https://pspcl.in/'
    name = "PSPCL"
    scrapers_report.append([url,base_url,name+official_tag])
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.find_all("div", class_='ticker-2')
    for res in results:
        try:
            var1 = res.find_all('li')
            for var in var1:
                headline = var.find('a').text.strip()
                link_ = var.find('a', href=True).get('href').strip()
                if link_.startswith(' https') == True:
                    link = link_
                else:
                    link = base_url+link_
                news_articles.append((name, headline, link))
            
        except Exception as e:
            pass
    success.append(name)        
except Exception as e:
    failure.append((name, e))


# Indian post
try:
    url= 'https://www.indiapost.gov.in/VAS/Pages/Content/Recruitments.aspx?Category=Recruitment'
    base_url= 'https://www.indiapost.gov.in'
    name = "Indian post"
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get(url,verify=False).text
    soup=BeautifulSoup(source,'html.parser')
    div=soup.find_all('div',class_="col-xs-12 col-md-12")
    for a in div[2].find_all('a'):
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

#CTET

try:
    base_url = 'https://ctet.nic.in/'
    url = 'https://ctet.nic.in/'
    name = "CTET"
    scrapers_report.append([url,base_url,name+official_tag])
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    try:
        results = soup.find_all('div', class_='vc_tta-panels')
        for res in results:
            res2 = res.find_all('li')
            for r in res2:
                title = r.find('a')
                if title is not None:
                    headline = title.text.strip()
                    link = title.get('href').strip()
                    news_articles.append((name, headline, link))
    except Exception as e:
        pass

    success.append(name)
    # print(news_articles)
except Exception as e:
    failure.append((name, e))
    
# PPSC
try:
    base_url='https://www.ppsc.gov.in'
    url = 'https://www.ppsc.gov.in/'
    name = "PPSC"
    scrapers_report.append([url,base_url,name+official_tag])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find('td', class_='newdesigntabletd_withoutborder_2')
    for result in results.find_all('a'):
        headline = result.text.strip()
        link= base_url + result.get('href').strip()
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# Kerala PSC
try:
    url = 'https://www.keralapsc.gov.in/latest'
    base_url = 'https://www.keralapsc.gov.in'
    name = "Kerala PSC"
    scrapers_report.append([url,base_url,name+official_tag])
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    content = requests.get(url, verify = False)
#     print(content.status_code)
    soup = BeautifulSoup(content.text, "html.parser")
    results = soup.find_all('td', class_ = 'views-field views-field-title')
    results2 = soup.find_all('td', class_ = 'views-field views-field-field-file')

    
    for result, result2 in zip(results, results2):  
        headline = result.text
        
        link = result2.find('a')
        if link is not None:
            link = link.get('href')
            if link.startswith('http'):
                link = link
            else:
                link = base_url+link  
            
        news_articles.append((name, headline, link))
    success.append(name) 
    
except Exception as e:
    failure.append((name,e))

# NPSC

try:
    url = 'https://npsc.nagaland.gov.in/latest-updates'
    base_url = 'https://npsc.nagaland.gov.in/latest-updates'
    name =  'NPSC'
    scrapers_report.append([url,base_url,name+official_tag])
    source=requests.get(url)

    soup = BeautifulSoup(content.text, "html") 
    results = soup.find_all('div', class_ = 'fw-bold')
    for res in results:
        try:
            headline = res.find('a').text
            link = res.find('a').get('href')
            news_articles.append((name, headline, link))
        except:
            pass
    success.append(name)
except Exception as e:
    failure.append((name,e))

#APPSC
try:
    url = 'https://psc.ap.gov.in/(S(zws14n0sxgaixzgjwd4rgf51))/Default.aspx'
    base_url = 'https://psc.ap.gov.in/(S(zws14n0sxgaixzgjwd4rgf51))/'
    name = "APPSC"
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")    
    results = soup.find_all('div', class_ = 'row marquee_div')
    for res in results:
        try:
            var = res.find('span', class_ = 'blinkNew')
            headline = var.text.replace('\n', '').replace('\r', '').replace('   ', '')
            link = var.find('a').get('href')
            if link.startswith('http'):
                link = link
            else:
                link = base_url+link
            news_articles.append((name, headline, link))
        except Exception as e:
            pass
    success.append(name)
    
except Exception as e:
    failure.append((name,e))
    pass

# Arunachal psc

try:
    #Home Page
    base_url = 'https://appsc.gov.in/Index/institute_home/ins/RECINS001'
    url = 'https://appsc.gov.in/Index/institute_home/ins/RECINS001'
    name = 'Arunachal psc'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find('ul',class_ = 'newsticker').find_all('li')
    for line in headlines:
        headline = line.text.strip()
        link = line.find('a')['href']
        news_articles.append((name,headline,link))
    #Notification Page
    url = 'https://appsc.gov.in/Index/sub_page/doc12233/Notifications'
    name = 'Arunachal psc'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find('tbody').find_all('tr')
    for line in headlines:
        headline = line.find('td',attrs={'width':'70%'}).text.strip()
        link = line.find('a')['href']
        news_articles.append((name,headline,link))
    #Results Page
    url = 'https://appsc.gov.in/Index/sub_page/doc37276/Results_'
    name = 'Arunachal psc'
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find('tbody').find_all('tr')
    for line in headlines:
        headline = line.find('td',attrs={'width':'70%'}).text.strip()
        link = line.find('a')['href']
        news_articles.append((name,headline,link))
    
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#HPSC

try:
    url = 'http://hpsc.gov.in/en-us/Announcements'
    base_url = 'http://hpsc.gov.in'
    name = "HPSC"
    scrapers_report.append([url,base_url,name+official_tag])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")    
    results = soup.find('div', id = 'dnn_ctr19159_HtmlModule_lblContent')
    results = results.find_all('td')
    for res in results[:22]:
        try:
            headline = res.find('a').text
            link = res.find('a').get('href')
            if link.startswith('http'):
                link = link
            else:
                link = base_url+link
            news_articles.append((name, headline, link))

        except:
            pass
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# MPSC
try:
    url = 'https://mpsc.gov.in/'
    base_url = 'https://mpsc.gov.in/'
    name = "MPSC"
    scrapers_report.append([url,base_url,name+official_tag])
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    content = requests.get(url, verify = False)
#     print(content.status_code)
    soup = BeautifulSoup(content.text, "html.parser")
    results = soup.find_all('div', class_ = 'alert alert-secondary')
    for result in results:
        headline = result.text.replace("\n","").replace("\r","").replace("\t","")
        link = result.find('a').get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link  
        news_articles.append((name, headline, link))
    success.append(name) 
    
except Exception as e:
    failure.append((name,e))
    pass

# UPTET
try:
    base_url = 'http://updeled.gov.in/'
    url = 'http://updeled.gov.in/'
    name = "UPTET"
    scrapers_report.append([url,base_url,name+official_tag])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find_all(class_='news-item')
    for news in newss:
        headline = news.get_text().strip()
        url= news.select('a')[0].get('href')
        link = base_url+url
        if headline == '' or None:
            continue
        news_articles.append((name, headline[:999], link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass


print('Successful Scrapers -', success)
print('Failed Scrapers -', failure)
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
