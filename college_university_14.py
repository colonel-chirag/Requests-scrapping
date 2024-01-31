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
now = datetime.now(tz=ZoneInfo('Asia/Kolkata'))

pyfilename="college_university_14"
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


#Goa University
try:
    base_url= "https://www.unigoa.ac.in/"
    url = "https://www.unigoa.ac.in/goa-university-news-listing.php"
    scrapers_report.append([url,base_url,'Goa Univerty'])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("div",class_ = "res_listing")
    for result in results:
      headline = result.find("h5").get_text().strip()
      if result.find('a') == None:
        link=""
      else:
        link = result.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
      news_articles.append(('Goa University',headline,link))
    success.append('Goa University')
except Exception as e:
    failure.append(('Goa University',e))
    pass

# PDM University

try:
    name ='PDM University'
    url = "https://www.pdm.ac.in/latest-news"
    base_url = url
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("h5")
    for result in results:
        headline=result.text.strip()
        link=result.find('a').get("href")
        if "http" not in link:
            link = base_url+link
        news_articles.append((name,headline,link))   
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# MDI

try:
    url='https://www.mdi.ac.in/'
    base_url = url
    source=requests.get('https://www.mdi.ac.in/').text
    scrapers_report.append([url,base_url,'Management Development Institute'])
    soup=BeautifulSoup(source,'html.parser')
    divs=soup.find_all('div',class_="col-lg-6")
    for div in divs:
        results = div.find_all('li')
        for result in results:
            headline = result.get_text()
            link = result.find('a').get('href')
            if 'http' not in link:
                link=url+link
            news_articles.append(('Management Development Institute',headline,link))
    success.append('Management Development Institute')       
except Exception as e:
    failure.append(('Management Development Institute',e))
    pass

# Symbiosis Law school
try:
    url = 'https://www.slsnagpur.edu.in/'
    base_url = url
    scrapers_report.append((url,base_url,'Symbiosis Law School'))
    source=requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    div=soup.find('div',class_='bg-red p-2 bg-red p-2')
    for a in div.find_all('a'):
        l = a.text.split()
        headline = " ".join(l)
        if a['href']:
            link = a['href'].replace(' ','20%')
            if 'http' not in link:
                link = base_url + link 
        else: 
            link = base_url
        news_articles.append(('Symbiosis Law School',headline,link))
    success.append('Symbiosis Law School')
except Exception as e:
    failure.append(('Symbiosis Law School',e))
    pass


# Asutosh college(18/2)
try:
    name = 'asutosh college'
    url = "https://asutoshcollege.in/new-web/all-notice.php"
    base_url = "https://asutoshcollege.in/new-web"
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find('div',class_="container pt-20 pb-20 d-flex").find_all('a')
    for result in results:
        headline = result.text
        link = base_url + result.get("href")
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#aiims bhopal(18/2)
try:
    name='aiims bhopal'
    url = 'https://aiimsbhopal.edu.in/index_controller/circulerNotice#SHTM'
    base_url='https://aiimsbhopal.edu.in/'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url,verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('tbody') .find_all('tr')
    for result in results:
        headline = result.find_all('td')[1].text
        link = result.find('a').get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# RPSC(18/2)
try:
    name = "RPSC"
    base_url = 'https://rpsc.rajasthan.gov.in/'
    url = "https://rpsc.rajasthan.gov.in/examdashboard"
    res = requests.get(url)
    scrapers_report.append([url, base_url, name])
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find_all('table', class_="examCalTable")
    for result in results:
        result = result.find_all('tr')
        for r in result:
            headline = r.span.text
            link = r.find('a').get('href')
            if 'javascript' in link:
                continue
            else:
                link = base_url + link
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

# KPSC(18/2)
try:
 name = "Kerala psc"
 page = 0
 for page in range(25):
    base_url = 'https://www.keralapsc.gov.in'
    url = f'https://www.keralapsc.gov.in/latest?page={page}'
    scrapers_report.append([url, base_url, name])
    #time.sleep(3)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    results = soup.find('tbody').find_all('tr')
    for result in results[:15]:
        headline = result.find('td', headers="view-title-table-column").text.strip().replace('Download', '')
        link = base_url + result.find('a').get('href')
        news_articles.append((name, headline, link))
 success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#Tilak(18/2)
try:
    name='Tilka Manjhi Bhagalpur University'
    url='http://tmbuniv.ac.in/'
    base_url=url
    scrapers_report.append([url, base_url, name])
    source = requests.get('http://tmbuniv.ac.in/').text
    soup = BeautifulSoup(source, 'html.parser')
    marquee = soup.find('div',id='header_marq')
    for a in marquee.find_all('a'):
        text = a.text
        link = a['href']
        text = text.rstrip()
        text = text.lstrip()
        link = link.rstrip()
        link = link.lstrip()
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#Tezpur University(18/2)

try:
    name='Tezpur University'
    url='http://www.tezu.ernet.in/'
    base_url=url
    scrapers_report.append([url, base_url, name])
    source=requests.get(url)
    soup=BeautifulSoup(source.text,'html.parser')
    div=soup.find('div',class_='minifeatureitem')
    for li in div.ul.find_all('li'):
        text=li.text
        link=li.a['href']
        link=link.lstrip()
        link=link.rstrip()
        text=text.lstrip()
        text=text.rstrip()
        news_articles.append((name,text,link))
    success.append('Tezpur University')
except Exception as e:
    failure.append(('Tezpur University',e))
    pass

# Tamil Nadu Agricultural University
try:
    url = 'https://tnau.ac.in/news-events/'
    base_url = 'https://tnau.ac.in/'
    source = requests.get(url).text
    scrapers_report.append([url, base_url, 'Tamil Nadu Agricultural University'])
    soup = BeautifulSoup(source, 'html.parser')
    div = soup.find('div', class_='wpb_raw_code wpb_content_element wpb_raw_html').find('div', class_='wpb_wrapper')
    items = div.find('ul').find_all('li')
    for a in items:
        text = a.text.strip()
        link = a.find('a').get("href")
        if 'http' not in link:
            link = base_url + link
        news_articles.append(('Tamil Nadu Agricultural University', text, link))
    success.append('Tamil Nadu Agricultural University')
except Exception as e:
    failure.append(('Tamil Nadu Agricultural University', e))
    pass

#VIT Business School(18/2)

try:
    name='VIT Business School'
    source=requests.get('https://vit.ac.in/schools/vitbs').text
    url='https://vit.ac.in/schools/vitbs'
    base_url=url
    scrapers_report.append([url, base_url, name])
    soup=BeautifulSoup(source,'html.parser')
    divs=soup.find('div',class_="col-md-9").find_all('a')
    for a in divs:
        text=a.text
        link=a['href']
        text=text.lstrip()
        text=text.rstrip()
        link=link.lstrip()
        link=link.rstrip()
        if 'http' not in link:
            link=url+link
        news_articles.append((name,text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
    pass

# FISAT(20/2)
try:
    domain = 'FISAT'
    base_url = 'https://www.fisat.ac.in/'
    url = 'https://fisat.ac.in/news/?page=1'
    scrapers_report.append([url, base_url, domain])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.find("div", class_="marquee-container row m-0 p-0")
    newss = data.find_all('a')
    for news in newss:
        headline = news.text.strip()[1:].strip()
        link = news.get('href')
        if 'http' not in link:
            link = base_url+link
        news_articles.append((domain, headline, link))
    success.append(domain)
except Exception as e:
    failure.append((domain, e))
    pass
#University of Petroleum and Energy Studies
try:
    name = 'University of Petroleum and Energy Studies'
    url = 'https://www.upes.ac.in/aspiring-students#admissionSection'
    base_url = 'https://admission.upes.ac.in/apply'
    scrapers_report.append([url, base_url, name])
    res= requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    divs = soup.find('section', class_='admissions').find('div', class_='row').find_all('div', class_='col-md-6')
    for div in divs:
        head = div.find('div', class_='card-head').find('h3').text.strip()
        add = div.find('div', class_='card-body').find('div', class_='col-12 col-lg-9 col-sm-12 col-xs-12')
        ld = add.find_all('p')[0].text
        ed = add.find_all('p')[1].text
        link = div.find('div', class_='card-body').find('div', class_='col-12 col-lg-3 col-sm-12 col-xs-12').find(
            'a').get("href")
        headline = head + " " + ld + " " + ed
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

# Rajiv gandhi Institute of Health Sciences, Karnataka 
try:
    name = 'RGUHS'
    base_url = 'http://www.rguhs.ac.in/'
    url = 'http://www.rguhs.ac.in/'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find_all("td", attrs={"class": "n12n", "bgcolor": "#FFFFFF","height":"40"})
    for news in newss:
        try:
            link = news.find('a').get('href').replace(' ', '%20')
            headline = news.text.strip()
        except:
            None
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

# NIT Raipur 
try:
    name = "NIT Raipur"
    base_url = "http://www.nitrr.ac.in"
    # url1 = "http://www.nitrr.ac.in/events.php"
    url = "http://www.nitrr.ac.in/notice1.php"
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # iframe_src = "notice1.php"
    # r = requests.Session().get(f"http://www.nitrr.ac.in/{iframe_src}",verify=False)
    # soup = BeautifulSoup(r.content, "html.parser")

    results = soup.find_all("h3", class_="entry-title entry-title_mod-a")
    for result in results[:10]:
        headline = result.text
        link = result.find('a').get('href')
        if 'http' in link:
            link = link
        else:
            link = base_url + link[2:]
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

# ram mohan college 
try:
    name = 'ram mohan college'
    url = "https://www.rammohancollege.ac.in/"
    base_url = "https://www.rammohancollege.ac.in/"
    scrapers_report.append([url, base_url, name])
    res = opener.open(url).read()
    soup = BeautifulSoup(res, "html.parser")
    results = soup.find_all("div", class_="tab-content bg-white")[0].find_all("a")
    for result in results[:9]:
        headline = result.text[11:].strip()
        link = base_url + result.get('href').replace('\n', '').replace('\t', '').replace(' ', '%20')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

# VIDYASAGAR
try:
    name = "Vidyasagar"
    url = "http://www.vidyasagar.ac.in/"
    base_url = "http://www.vidyasagar.ac.in/"
    scrapers_report.append([url, base_url, name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block= soup.find('div', class_="row")
    main_block=content_block.find_all('div', class_="col-md-12 h6 text-center")
    for block in main_block:
        head_block = block.find_all_next('a')
        for head in head_block:
            headline = head.text.strip().replace('.', '').strip()
            link = head.get("href")
            if 'http' not in link:
                link = base_url + link
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = "Vidyasagar"
    failure.append((name, e))

# SPCE
try:
    name="SPCE"
    base_url='https://www.spce.ac.in/'
    url = "https://www.spce.ac.in/old%20notices.php"
    scrapers_report.append([url, base_url, name])
    source = opener.open(url).read()
    soup = BeautifulSoup(source, "html.parser")
    content_block = soup.find('tbody')
    head_block=content_block.find_all('a')
    for head in head_block[1:11]:
        headline = head.text.replace('\n',' ').strip()
        link=head.get("href").replace(' ','%20')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="SPCE"
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
