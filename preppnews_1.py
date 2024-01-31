from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import urllib3
import warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
import uploader

import logging
import sys

start_time = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = start_time.strftime("%Y-%m-%d %H:%M")
print (start_time.strftime("%Y-%m-%d %H:%M:%S"))
pyfilename = 'preppnews_1'


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


warnings.filterwarnings('ignore')

news_articles = []
success = []
failure = []
scrapers_report = []

#Aaj ki news
try:
    url = 'https://aajkinews.net/category/jobs/'
    base_url = 'https://aajkinews.net/'
    name = "Aaj ki news"
    scrapers_report.append([url,base_url,name])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    headlines = soup.find_all('h3', class_ = 'entry-title mh-loop-title')
    for line in headlines: 
        headline = line.find('a').text.replace("\n","")
        link = line.find('a').get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name = "Aaj ki news"
    failure.append((name,e))

#ZEEBIZ
# try :
#     base_url = "https://www.zeebiz.com/"
#     url = "https://www.zeebiz.com/hindi/jobs"
#     name = 'ZEEBIZ'
#     scrapers_report.append([url,base_url,name])
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser")
#     link_list = soup.find_all('div', class_ = 'mstrecntbx clearfix')
#     for i in link_list[:10]:
#         box = i.find('div', class_ = 'text-overflow')
#         content = box.find('a')
#         if content is not None:
#             headline = content.get_text()
#             link = content.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#             news_articles.append(('ZEEBIZ',headline,link))
#     success.append('ZEEBIZ')      
# except Exception as e:
#     failure.append(('ZEEBIZ',e))

#ASAMNEWS18(done)
try:
    base_url = "https://assam.news18.com/"
    url = "https://assam.news18.com/tag/job/news/"
    name = 'ASAMNEWS18'
    scrapers_report.append([url,base_url,name])   
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")
 
    content = soup.find('ul', class_ = 'tag-listing-new clearfix')
    if content is not None:
        link_list = content.find_all('li')
        for i in link_list[:10]:
            box = i.find('a')
            if box is not None:
                headline = box.get_text()
                link = box.get('href')
                if 'http' not in link:
                    link = base_url+link
                news_articles.append(('ASAMNEWS18',headline,link))
        success.append('ASAMNEWS18')      
except Exception as e:
    failure.append(('ASAMNEWS18',e))
 

#HINDINEWS18

try:
    url = 'https://hindi.news18.com/news/jobs/'
    base_url = 'https://hindi.news18.com/'
    name = "HINDINEWS18"
    scrapers_report.append([url,base_url,name])
    content = requests.get(url) 
#     print(content.status_code)
    soup = BeautifulSoup(content.text, "html.parser")
    
    results = soup.find_all('ul',  class_ ='jsx-1173356385')
    for result in results:
        headlines = result.find_all('a')
        for line in headlines:
            headline = line.text
            link = line.get('href')
            if link.startswith('http'):
                link = link
            else:
                link = base_url+link
            news_articles.append((name, headline, link))
            
    results2 = soup.find_all('div', class_ ='jsx-3343455497 blog_list_row') 
    for result in results2:
        headline = result.text
        link = result.find('a').get('href')
        if link.startswith('http'):
            link = link
        else:
            link =base_url+link
        news_articles.append((name, headline, link))    
           
    success.append(name)
except Exception as e:
    name = "HINDINEWS18"
    failure.append((name,e))
    
#LOKMATNEWS18

try:
    base_url = "https://lokmat.news18.com/"
    url = "https://lokmat.news18.com/category/career/"
    name = 'LOKMATNEWS18'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")
    content = soup.find_all('div', class_ = 'tp-3story clearfix')
    for i in content[:5]:
        link_list = i.find_all('li')
        for j in link_list:
            con = i.find('h2')
            box = con.find('a')
            if box is not None:
                headline = box.text
                link = box.get('href')
                if 'http' not in link:
                    link = base_url+link
                news_articles.append(('LOKMATNEWS18',headline,link))
    success.append('LOKMATNEWS18')      
except Exception as e:
    failure.append(('LOKMATNEWS18',e))
    pass


#MALAYALAMNEWS18
try:
    base_url = "https://malayalam.news18.com/"
    url = "https://malayalam.news18.com/career/"
    name = 'MALAYALAMNEWS18'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")
 
    content_1 = soup.find('div', class_ = 'section-blog-left-img-list')
    content_2 = soup.find('div', class_ = 'blog-list')
 
    link_list_1 = content_1.find_all('li')
    link_list_2 = content_2.find_all('div', class_ = 'blog-list-blog')
 
    for i in link_list_1[:10]:
        box = i.find('a')
        if box is not None:
            headline = box.text
            link = box.get('href')
            if 'http' not in link:
                link = base_url+link
        news_articles.append((name,headline,link))
 
    for i in link_list_2[:10]:
        con = i.find('p')
        box = con.find('a')
        if box is not None:
            headline = box.text
            link = box.get('href')
            if 'http' not in link:
                link = base_url+link

            news_articles.append((name,headline,link))
    
    success.append(name)  
except Exception as e:
    failure.append((name,e))
    
#NDTV

# try:
#     base_url = "https://ndtv.in/"
#     url = "https://ndtv.in/jobs"
#     name = 'ndtv'
#     scrapers_report.append([url,base_url,name])
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser")
 
#     content = soup.find('div', class_ = 'lisingNews')
#     link_list = content.find_all('div', class_ = 'news_Itm')
#     for i in link_list[:10]:
#         con = i.find('h2')
#         if con is not None:
#             box = con.find('a')
#             if box is not None:
#                 headline = box.text
#                 link = box.get('href')
#                 if 'http' not in link:
#                     link = base_url+link
#                 news_articles.append((name,headline,link))
#     success.append(name)      
# except Exception as e:
#     name = 'ndtv'
#     failure.append((name,e))

#AAJTAKCAREER

# try:
#     base_url = "https://www.aajtak.in/"
#     url = "https://www.aajtak.in/education/career"
#     name = 'aajtakcareer'
#     scrapers_report.append([url,base_url,name])
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser")
#     content = soup.find('div', class_ = 'section-listing-LHS')
#     link_list = content.find_all('div', class_ ='widget-listing')
 
#     for i in link_list[:5]:
#         con = i.find('h2')
#         box = con.find('a')
#         if box is not None:
#             headline = box.text
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#             news_articles.append((name,headline,link))
#     success.append(name)      
# except Exception as e:
#     name = 'aajtakcareer'
#     failure.append((name,e))
    
    
#adda247

try:
    url = 'https://www.adda247.com/jobs/'
    base_url = "https://www.adda247.com"
    name = 'adda247'
    scrapers_report.append([url,base_url,name])
    content = requests.get(url)
    document = BeautifulSoup(content.text, "html.parser")
    div1 = document.find('div',class_="entry-content").find_all('div', class_="wp-block-column new-icon")
    for div2 in div1:
        seg = div2.find('ul').find_all('li')
        for i in seg:
            headline = i.get_text()
            link = i.find_all('a', href=True)[0]['href']
            news_articles.append((name,headline,link))
            
    success.append(name)
    # print(news_articles)
except Exception as e:
    name = 'adda247'
    failure.append((name,e))
    pass



#ADDABANKJOBS

try:
    base_url = "https://www.adda247.com/"
    url = "https://www.adda247.com/jobs/bank-jobs/"
    name = 'ADDABANKJOBS'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")
 
    section = soup.find_all('div', class_ = 'wp-block-column')
    content = section[0].find('ul', class_ ='lcp_catlist')
    link_list = content.find_all('li')
    for i in link_list[:10]:
        box = i.find('a')
        if box is not None:
            headline = box.text
            link = box.get('href')
            if 'http' not in link:
                link = base_url+link
            news_articles.append((name,headline,link))
    success.append(name)      
except Exception as e:
    name = 'ADDABANKJOBS'
    failure.append((name,e))
    pass


#AMARUJALA

try:
    base_url = "https://www.amarujala.com/"
    url = "https://www.amarujala.com/jobs/government-jobs"
    name = 'AMARUJALA'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")

    content = soup.find('div', id ='page0')
    link_list = content.find_all('section', class_ = '__main_listing_content')  
    for i in link_list:
        con  = i.find('h3')
        if con is not None:
            box = con.find('a')
            if box is not None:
                headline = box.text.strip().replace("                                   "," ")
                link = box.get('href')
                if 'http' not in link:
                    link = base_url+link
                link = link.strip()
                news_articles.append((name,headline,link))
    success.append(name)      
except Exception as e:
    name = 'AMARUJALA'
    failure.append((name,e))
    pass


#PATRIKA 

# try:
#     base_url = "https://www.patrika.com/"
#     url = "https://www.patrika.com/jobs/"
#     name= 'PATRIKA'
#     scrapers_report.append([url,base_url,name])
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser") 
#     content = soup.find('div', class_ = 'flex flex-col space-y-4 divide-y')
#     link_list = content.find_all('div', class_ = 'w-2/3 flex flex-col md:pr-5')

#     for i in link_list:
#         box = i.find('a')
#         if box is not None:
#             headline = box.text
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#             news_articles.append((name,headline,link))
#     success.append(name)      
# except Exception as e:
#     name= 'PATRIKA'
#     failure.append((name,e))
    


#REWARIYAT

# try:
#     base_url = "https://www.rewariyasat.com/"
#     url = "https://www.rewariyasat.com/jobs/"
#     name = 'rewariyasat'
#     scrapers_report.append([url,base_url,name])
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.text,"html.parser")
    
#     content = soup.find('div', class_ = 'm_top15')
#     link_list = content.find_all('h2')
    
#     for i in link_list:
#         box = i.find('a')
#         if box is not None:
#             headline = box.text.strip()
#             link = box.get('href')
#             if 'http' not in link:
#                 link = base_url+link
#             news_articles.append((name,headline,link))
#     success.append(name)      
# except Exception as e:
#     name = 'rewariyasat'
#     failure.append((name,e))
    
#sarkariresult

try:
    url = 'https://www.sarkariresult.com/'
    base_url = 'https://www.sarkariresult.com/'
    name = 'sarkariresult'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    for div in soup.find_all('div',id='post')[:2]:
        for a in div.find_all('a')[:10]:
            text=a.text
            link=a['href']
            text=text.strip()
            link=link.strip()
            if 'http' not in link:
                link=base_url+link
            news_articles.append((name,text,link))
    for div in soup.find_all('div',id='post')[3:7:3]:   
        for a in div.find_all('a')[:10]:
            text=a.text
            link=a['href']
            text=text.strip()
            link=link.strip()
            if 'http' not in link:
                link=base_url+link  
            news_articles.append((name,text,link))
    success.append((name))
except  Exception as e:
    name = 'sarkariresult'
    failure.append((name,e))
    
# Live Hindustan Job Alerts
try:
    url = 'https://www.livehindustan.com/career/jobs/news'
    base_url = 'https://www.livehindustan.com/career/jobs/news'
    name = "Live Hindustan"
    scrapers_report.append([url,base_url,name])

    content = requests.get(url)

    soup = BeautifulSoup(content.text, "html.parser")
    results = soup.find_all('a', class_ = 'card-sm')
    for result in results:
        headline = result.text
        link = result.get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


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
