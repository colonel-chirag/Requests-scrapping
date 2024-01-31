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

pyfilename="college_university_9"
import sys
# base_path = "/home/notification-scrapers/Cd_scrapers/"
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

# ycmou
try:
    name="ycmou"
    url = "https://ycmou.ac.in/news"
    base_url = 'https://ycmou.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find_all("tr")[1:]
    for content in content_list:
        headline_text=content.find_all("td")[1].text
        link=content.find('a').get("href")
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))
    pass



# SOL

try:
    name="sol"
    url = "https://web.sol.du.ac.in/info/archive-notices-information"
    base_url = 'https://web.sol.du.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find("ul", class_="marked-list")
    head_block = content_list.find_all("a")
    for block in head_block[:9]:
        headline_text=block.text.strip()
        link=block.get("href").replace(" ", "%20")
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))
    pass



# UPRTOU
try:
    name="uprtou"
    url = "http://14.139.237.190/news_layout_page.php?id=admission"
    base_url = 'http://www.uprtou.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    content_list = soup.find("ul", class_="navigation")
    head_block = content_list.find_all("a")
    for block in head_block[:9]:
        headline_text=block.text.strip()
        link=block.get("href")
        if "http" in link:
            link=link
        else:
            link="http://14.139.237.190/"+link
        news_articles.append((name,headline_text,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))
    pass


# LOYOLA
try:
    name="loyola college"
    url = "https://www.loyolacollege.edu/events/current_events"
    base_url = 'https://www.loyolacollege.edu/'
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find_all("tr")[1:6]
    for result in results:
        if ("result.a"==None):
            continue
        else:
            result=result.find_all("a")
            for r in result:
                headline=r.text.replace("\xa0", " ").replace("\n", "").strip()
                link=base_url+r.get("href")
                news_articles.append((name,headline,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))
    pass


# Sastra
try:
    name="sastra"
    url = "https://www.sastra.edu/headlines-archives.html"
    base_url = 'https://www.sastra.edu'
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find_all("tr")[1:]
    for result in results:
        headline=result.a.text.strip()
        link=base_url+result.a.get("href")
        news_articles.append((name,headline,link))
    success.append((name))
except Exception as e:
    failure.append((name,e))
    pass

#VMOU
try:
    name ='VMOU '
    url = "https://www.vmou.ac.in/notice/admissions"
    base_url="https://www.vmou.ac.in"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("table", class_="views-table cols-0").find_all("tr")
    for result in results:
        headline=result.a.text.strip()
        link=base_url+result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# Hansraj college

try:
    name ='hansraj college'
    url = "https://www.hansrajcollege.ac.in/announcements"
    base_url="https://www.hansrajcollege.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:11]
    for result in results:
        headline=result.find("td").text.strip()
        link_tag=result.find("a")
        if link_tag:
            link = link_tag['href']
        else:
            link = ''
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass
    


# Gargi college

try:
    name ='gargi college'
    url = "https://gargicollege.in/notice/"
    base_url="https://gargicollege.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:11]
    for result in results:
        link=result.a.get('href')
        result=result.find_all("td")
        for r in result[1:2]:
            headline = r.text
            link=link
            news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass



# Fergusson college
try:
    name ='fergusson college'
    url = "https://www.fergusson.edu/news/index"
    base_url="https://www.fergusson.edu/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("marquee").find_all("a")
    for result in results:
        headline=result.text.replace('*','').strip()
        link=result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# Miranda house
try:
    name ='Miranda house'
    url = "https://www.mirandahouse.ac.in/notice.php"
    base_url="https://www.mirandahouse.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:11]
    for result in results:
        headline=result.a.text.strip()    
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


# Vivekananda college
try:
    name ='Vivekananda college'
    url = "https://vivekanandacollege.edu.in/notice-board/"
    base_url="https://vivekanandacollege.edu.in"
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find("div", class_="entry-content").find_all("li")
    for result in results[:9]:
        headline=result.a.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


# ftii
try:
    name ='ftii'
    url = "https://www.ftii.ac.in/announcement"
    base_url="https://www.ftii.ac.in/announcement"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:]
    for result in results[:9]:
        headline=result.a.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


# kalindi college
try:
    name ='kalindi college'
    url = "https://www.kalindicollege.in/notice/#general"
    base_url="https://www.kalindicollege.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:11]
    for result in results:
        link=result.a.get('href')
        result=result.find_all("td")
        for r in result[1:2]:
            headline = r.text
            link=link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# satyawati college
try:
    name ='satyawati college'
    url = "http://satyawati.du.ac.in/CIRCULARS.HTML"
    base_url="http://satyawati.du.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[1:11]
    for result in results:
        headline=result.find("td").text.strip()
        link=base_url+result.a.get("href").replace(" ","%20")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# srcc
try:
    name ='srcc'
    url = "https://www.srcc.edu/announcements"
    base_url="https://www.srcc.edu/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("div", class_="annoncementList")
    for result in results[:9]:
        headline=result.a.text.strip()
        link=base_url+result.a.get("href").replace(" ", "%20")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# bangabasi college

try:
    name ='bangabasi college'
    url = "https://www.bangabasi.ac.in/"
    base_url="https://www.bangabasi.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("div", class_="n-body")[1].find_all("a")
    for result in results:
        headline=result.text.strip()
        link=base_url+result.get("href").replace(" ", "%20")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# patna women college
try:
    name ='patna women college'
    url = "https://patnawomenscollege.in/notice-board/"
    base_url="https://patnawomenscollege.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("tr")[2:12]
    for result in results:
        link=result.a.get("href")
        result=result.find_all("td")[1:2]
        for r in result:
            headline=r.text
            link=link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# rajdhani college

try:
    name ='rajdhani college'
    url = "https://www.rajdhanicollege.ac.in/"
    base_url="https://www.rajdhanicollege.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div", id="General").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=base_url+result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass



# aurobindo university
try:
    name='aurobindo university'
    base_url = 'http://aurobindo.du.ac.in/'
    url = 'http://aurobindo.du.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('ul', class_ = 'list').find_all('li')
    for result in results:
        headline = result.find('a').text
        link = url + result.find('a').get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


#Tamil Nadu Open University
try:
    name='Tamil Nadu Open University'
    base_url='https://tnou.ac.in/'
    url = 'https://tnou.ac.in/news-and-events/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    head_block = soup.find(class_='col-lg-3 col-md-6').find_all(class_='py-3')[1:]
    for block in head_block:
        headline_text = block.text.strip()
        link=block.find('a')['href']
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#Tamil Nadu Open University
try:
    name='Tamil Nadu Open University'
    base_url='https://tnou.ac.in/'
    url='https://tnou.ac.in/'
    scrapers_report.append([url,base_url,name])
    source=requests.get(url).text    
    soup=BeautifulSoup(source,'html.parser')
    head_block = soup.find(class_='col-lg-3 col-md-6').find_all(class_='py-3')[1:]
    for block in head_block:
        headline_text = block.text.strip()
        link=block.find('a')['href']
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# marivanios college
try:
    name='marivanios college'
    bae_url = 'https://www.marivanioscollege.com/'
    url = 'https://www.marivanioscollege.com/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('div', class_ = 'col-sm-12 col-md-4').find_all('div', class_ = 'event media mt-0 no-bg no-border')
    for result in results:
        headline = result.find('a').text
        link = result.find('a').get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

#  ranaghat college
try:
    name='ranaghat college'
    base_url='http://www.ranaghatcollege.org.in/'
    url = 'http://www.ranaghatcollege.org.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('tr').find_all('p')
    for result in results:
        try:
            headline = result.find('a').text
            link = url + result.find('a').get('href')
        except:
            None
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# uluberia college
try:
    name='uluberia college'
    base_url='https://www.uluberiacollege.in/'
    url = 'https://www.uluberiacollege.in/site/all_notice/1'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('div', class_ = 'table-responsive').find_all('tr')[1:]
    for result in results:
        headline = result.find('td').find_next_sibling('td').text
        link = result.find('a').get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# tnau

try:
    name = "TNAU"
    url = "https://tnau.ac.in/news-events/"
    base_url = "https://tnau.ac.in"
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.find("div", class_="wpb_raw_code wpb_content_element wpb_raw_html").find_all("li")      
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

# kirori mal
try:
    name ='kirori mal'
    url = "http://kmc.du.ac.in/category/latest-news/"
    base_url="http://kmc.du.ac.in"
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
    pass

# motilal nehru

try:
    name ='motilal nehru'
    url = "http://www.mlncdu.ac.in/news.html"
    base_url="http://www.mlncdu.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("ul", type="square").find_all("a")
    for result in results[:9]:
        headline=result.text.strip()
        link=base_url+result.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# NLU
try:
    name ='NLU'
    url = "https://nludelhi.ac.in/Annuoncement.aspx"
    base_url="https://nludelhi.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find('ul',style="overflow:auto;").find_all("li",style='')
    for result in results[:9]:
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

# jecrcu

try:
    name ='jecrcu'
    url = "https://jecrcuniversity.edu.in/announcement"
    base_url="https://jecrcuniversity.edu.in/"
    scrapers_report.append([url,base_url,name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find(class_='elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-4f6e4e2',attrs={'data-id':'4f6e4e2'}).find_all('li')
    for result in results:
        headline=result.text.strip()
        link=result.a.get("href")
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass



# Shyam lal college

try:
    name ='Shyam lal college'
    url = "http://www.slc.du.ac.in/"
    base_url="http://www.slc.du.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("marquee", class_="new_maquee").find_all("div" , class_="headline")
    for result in results[:9]:
        headline=result.a.text.strip()
        link=result.a.get("href")
        if "http" in link:
            link=link
        else:
            link=base_url+link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# fddi india

try:
    name ='fddi india'
    url = "https://www.fddiindia.com/importants-updates.php"
    base_url="https://www.fddiindia.com/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find("div" , class_="students-affairs-ul").find_all("li")
    for result in results:
        headline=result.a.text.strip()
        link=result.a.get("href")
        if "http" in link:
            link=link
        else:
            link=base_url+link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass


# jesus and mary
try:
    name ='jesus and mary'
    url = "https://www.jmc.ac.in/"
    base_url="https://www.jmc.ac.in/"
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
    pass

# skuast kashmir
try:
    name='skuast kashmir'
    base_url='https://skuastkashmir.ac.in/'
    url = 'https://skuastkashmir.ac.in/DisplayAllNews.aspx?id=9'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find_all('div', class_ = 'event-ite w-dyn-item')
    for result in results:
        headline = result.find('a').text
        link = result.find('a').get('href')
        news_articles.append((name,headline,link))
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
