import requests
import urllib3
import warnings
import time
import logging
from bs4 import BeautifulSoup
from datetime import datetime
from zoneinfo import ZoneInfo
import uploader

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import pandas as pd
import sys
start_time = datetime.now(tz=ZoneInfo('Asia/Kolkata'))
timestamp = start_time.strftime("%Y-%m-%d %H:%M")
print (start_time.strftime("%Y-%m-%d %H:%M:%S"))
pyfilename = 'preppnews_2'
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

#  Times Of India
try:
    url = 'https://timesofindia.indiatimes.com/education/jobs'
    base_url = 'https://timesofindia.indiatimes.com/education/jobs'
    name = 'Times Of India'
    scrapers_report.append([url,base_url,name])
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    extractdiv = soup.find('div', class_ = '_3eR85')
    if extractdiv is not None:
        div1 = extractdiv.find('div', class_ = '_2ZXWE')
        if div1 is not None:
            tags_1 = div1.find_all('figure')
            if tags_1 is not None:
                for tag in tags_1[:5]:
                    try:
                        headline = tag.figcaption.text
                        link = tag.a.get('href')
                        if link.startswith('http'):
                            link = link
                        else:
                            link = url+link
                        news_articles.append((name, headline, link))
                        if name not in success:
                            success.append(name)
                        # success.clear()
                    except Exception as e:
                        failure.append((name, e))
            else:
                failure.append((name, 'tags_1 are None'))
        else:
            failure.append((name, 'div1 is None'))

        
        div2 = extractdiv.find_all('div', recursive = False)
        if div2 is not None:
            for d2 in div2:
                if 'data-section' in d2.attrs.keys():
                    tags2 = d2.find_all('figure')
                    if tags2 is not None:
                        for tag in tags2[:3]:
                            try:
                                headline = tag.figcaption.text
                                link = tag.a.get('href')
                                if link.startswith('http'):
                                    link = link
                                else:
                                    link = url+link
                                news_articles.append((name, headline, link))
                                if name not in success:
                                    success.append(name)
                                # success.clear()
                            except Exception as e:
                                failure.append((name, e))
                    else:
                        failure.append((name, 'tag2 are None'))

                else:
                    failure.append((name, 'div2 attribute missing'))
        else:
            failure.append((name, 'div2 is None'))
            
        tags3 = extractdiv.find_all('div', class_ = '_3je0D col_l_6 col_m_6')
        if tags3 is not None:
            for tag in tags3[:3]:
                try:
                    for tg in tag:
                        headline = tg.text
                        link = tg.get('href')
                        if link.startswith('http'):
                            link = link
                        else:
                            link = url+link
                        news_articles.append((name, headline, link))
                        if name not in success:
                            success.append(name)
                        # success.clear()
                except Exception as e:
                    failure.append((name, e))
        else:
            failure.append((name, 'tags3 are None'))        
    else:
        failure.append((name, 'div is None'))
    news_articles = list(set(news_articles))
except Exception as e:
    name = 'Times Of India'
    failure.append((name, e))
    
#GUJARATINEWS18

 
try:
    base_url = "https://gujarati.news18.com/"
    url = "https://gujarati.news18.com/career/"
    name = 'GujaratiNews18'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    extractdiv = soup.find('div', class_ = 'top_story')
    if extractdiv != None:
        for story in extractdiv:
            if 'class' in story.attrs.keys():
                if 'top_story_left' in str(story.attrs['class']):
                    tags_1 = story.find_all(recursive=False)
                    if tags_1 != None:
                        for tag in tags_1:
                            headline = tag.text
                            link = tag.get('href')
                            if link.startswith('http'):
                                link = link
                            else:
                                link = base_url+link
                            news_articles.append((name, headline, link))
                    else:
                        failure.append((name, 'tags_1 are None'))

                elif 'top_story_right' in str(story.attrs['class']):
                    tags_2 = story.find_all('li')
                    if tags_2 is not None:
                        for tag in tags_2:
                            headline = tag.text
                            link = tag.a.get('href')
                            if link.startswith('http'):
                                link = link
                            else:
                                link = base_url+link
                            news_articles.append((name, headline, link))
                    else:
                        failure.append((name, 'tags_2 are None'))
                else:
                    failure.append((name, 'Class name doesnot exist anymore'))
            else:
                failure.append((name, 'Class attribute doesnot exist anymore'))
    else:
        failure.append((name, 'div is None'))
except Exception as e:
    name = 'GujaratiNews18'
    failure.append((name,e))
#BENGALINEWS18
# try:
#     url = 'https://bengali.news18.com/job/'
#     base_url = 'https://bengali.news18.com/'
#     name = "BENGALINEWS18"
#     scrapers_report.append([url,base_url,name])
#     content = requests.get(url)
#     soup = BeautifulSoup(content.text, "html.parser")
#     extractdiv = soup.find('div', class_ = 'top_story')
#     if extractdiv != None:
#         for story in extractdiv:
#             if 'class' in story.attrs.keys():
#                 if 'top_story_left' in str(story.attrs['class']):
#                     tags_1 = story.find_all(recursive=False)
#                     if tags_1 != None:
#                         for tag in tags_1:
#                             headline = tag.text
#                             link = tag.get('href')
#                             if link.startswith('http'):
#                                 link = link
#                             else:
#                                 link = base_url+link
#                             news_articles.append((name, headline, link))
#                             if name not in success:
#                                 success.append(name)
#                             # success.clear()
#                     else:
#                         failure.append((name, 'tags_1 are None'))
            
#                 elif 'top_story_right' in str(story.attrs['class']):
#                     tags_2 = story.find_all('li')
#                     if tags_2 != None:
#                         for tag in tags_2:
#                             headline = tag.text
#                             link = tag.a.get('href')
#                             if link.startswith('http'):
#                                 link = link
#                             else:
#                                 link = base_url+link
#                             news_articles.append((name, headline, link))
#                             if name not in success:
#                                 success.append(name)
#                     else:
#                         failure.append((name, 'tags_2 are  None'))
#                 else:
#                     failure.append((name, 'Class name doesnot exist anymore'))
#             else:
#                 failure.append((name, 'Class attribute doesnot exist anymore'))
#     else:
#         failure.append((name, 'extractdiv is None'))

# except Exception as e:
#     name = "BENGALINEWS18"
#     failure.append((name, e))

#ODISHATV

try:
    base_url = "https://odishatv.in/"
    url = "https://odishatv.in/jobs"
    name = 'odishatv'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")

    content = soup.find('div', class_ = 'listing-news-start')
    link_list = content.find_all('div', class_ = 'listing-result-news')
    for i in link_list:
        con = i.find_all('a')
        for j in con:
            box = j.find('h5')
            if box is not None:
                headline = j.text
                link = j.get('href')
                if 'http' not in link:
                    link = base_url+link
                news_articles.append((name,headline,link))
            else:
                continue
            
    success.append(name)      
except Exception as e:
    name = 'odishatv'
    failure.append((name,e))



#SSC Adda
try :
    
    url = 'https://www.sscadda.com/'
    base_url = 'https://www.sscadda.com/'
    name = 'SSC Adda'
    scrapers_report.append([url,base_url,name])
    req = requests.get(url)

    all_cont = req.content
    document = BeautifulSoup(all_cont, 'html.parser')

    div1 = document.find_all("div",class_='wp-block-column new-icon')#.find_all('h2')#.get_text()#
    div2 = document.find_all("div",class_='wp-block-column')
    Sec = [div1,div2]

    for div in Sec:
        for i in div:
            try:
                Seg = i.find_all('ul', class_="lcp_catlist", id="lcp_instance_0")
                for j in Seg:
                    text = j.find_all('li')
                    for k in j:
                        link = k.find_all('a', href=True)[0].get("href").strip()
                        headline = k.get_text(strip =True).split(',')[0]
                        news_articles.append((name, headline, link))
                
            except Exception as e:
                failure.append((name, e))
                
    success.append(name)
except Exception as e:
    name = 'SSC Adda'
    failure.append((name,e))
    
#linking sky
try:

    url = "https://linkingsky.com/"
    base_url = "https://linkingsky.com/"
    name = 'linkingsky'
    scrapers_report.append([url,base_url,name])
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    results = soup.find_all("div", class_='col-sm-6')
    for var in results:
        var2 = var.find_all('li')
        for var3 in var2:
            headline = var3.text
            
            link = var3.find('a', href=True).get('href').strip()
            
            news_articles.append((name, headline, link))
    success.append((name))
    # print(news_articles)
except Exception as e:
    name = 'linkingsky'
    failure.append((name, e))
    
#INDIATVNEWS
try:
    base_url = "https://www.indiatvnews.com/"
    url = "https://www.indiatvnews.com/education/career/"
    name= 'indiatvnews'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")
    content = soup.find('div', class_ ='row lhsBox s_two_column pt20')
    link_list = content.find_all('ul', class_ = 'list')

    for i in link_list:
        lists = i.find_all('li')
        for j in lists:
            con = j.find('p')
            box = con.find('a')
            if box is not None:
                headline = box.text
                link = box.get('href')
                if 'http' not in link:
                    link = base_url+link
                news_articles.append((name,headline,link))
    success.append(name)      
except Exception as e:
    name= 'indiatvnews'
    failure.append((name,e))

        
#LOKMAT

try:
    base_url = "https://www.lokmat.com/"
    url = "https://www.lokmat.com/career/"
    name = 'lokmat'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text,"html.parser")

    content = soup.find('section', class_ ='list-view')
    link_list = content.find_all('figure')
    for i in link_list:
        con = i.find('h2')
        box = con.find_all('a')
        if box[1] is not None:
            headline = box[1].text
            link = box[1].get('href')
            if 'http' not in link:
                link = base_url+link
        news_articles.append((name,headline,link))
    success.append(name)      
except Exception as e:
    name = 'lokmat'
    failure.append((name,e))
 

# Employment News
try:           
    url = 'http://employmentnews.gov.in/NewEmp/'                                 
    base_url = 'http://employmentnews.gov.in/NewEmp/Home1.aspx'
    name = 'employment news'
    scrapers_report.append([url,base_url,name])
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    newss = soup.find_all(class_='divBorder')
    for i in range(len(newss)):
        if i >= 3:
            success.append('Employment News')
        else:
            headline = newss[i].find('a').get_text().strip()[:999]
            link = url + newss[i].find('a').get('href')
            news_articles.append((name, headline, link))  
except Exception as e:
    name = 'employment news'
    failure.append((name, e))


# Hindustan Times
try:
    url = 'https://www.hindustantimes.com/education'
    base_url = 'https://www.hindustantimes.com/'
    name = "Hindustan times"
    scrapers_report.append([url,base_url,name])
    content = requests.get(url)

    soup = BeautifulSoup(content.text, "html.parser")
    headlines = soup.find_all('h3', class_ = 'hdg3')
    for line in headlines: 
        headline = line.find('a').text
        link = line.find('a').get('href')
        if link.startswith('http'):
            link = link
        else:
            link = base_url+link
        news_articles.append((name, headline, link))
    success.append(name)
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
