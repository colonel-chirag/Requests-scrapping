from bs4 import BeautifulSoup,Comment
import ssl
import requests
from urllib.request import Request, urlopen
import re

context = ssl._create_unverified_context()


news_articles=[]
text=[]
links = []
success=[]
failure=[]
scrapers_report=[]
link=[]



#Kashmir
try:
    url = "https://kashmiruniversity.net/"
    base_url = "https://kashmiruniversity.net/"
    name = "Kashmir"
    scrapers_report.append([url,base_url,name])
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")


    sections = [("lstNewsAndAnnouncements", "News and Announcements"),("lstAdmissions", "Admissions")]
    for section_id, section_name in sections:
        articles = soup.find(id=section_id, class_="list doughnut").find_all("li")
        for i in articles:
            link_tag = i.find('a')
            if link_tag:
                link = link_tag["href"]
                headline = link_tag.text
                if "http" not in link:
                    link = base_url + link
                news_articles.append((name, f"{section_name}: {headline}", base_url+link.split(":")[1]))
    success.append(name)
except Exception as e:
    failure.append((name, e))



#sarvgyan/2023
try:
    url = "https://www.sarvgyan.com/2023"
    base_url = "https://www.sarvgyan.com/2023"
    name = "sarvgyan"
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")
    scrapers_report.append([url,base_url,name])


    articles = soup.find_all("h2")
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


#news.sarvgyan
try:

	hdr = {'User-Agent': 'Mozilla/5.0'}

	name ="News Sarvgyan"
	url = "https://news.sarvgyan.com/"
	base_url = "https://news.sarvgyan.com/"

	req = Request(url,headers=hdr)
	page = urlopen(req)
	soup = BeautifulSoup(page,"html.parser")
	scrapers_report.append([url,base_url,name])

	content = soup.find_all("a", {"class": "p-url"})

	for i in content[5::]:

		if i.text and i.text not in text:
			text.append(i.text)
		if i.get('href') and i.get('href') not in links:
			links.append(i.get('href'))
	for i in range(len(links)):
		news_articles.append((name,text[i],links[i]))
	success.append(name)

except Exception as e:
    failure.append((name, e))





# optimized scraper count
# cujammu originally [college_university_6] | duplicate [college_university_2]
try:
    name = 'cujammu'
    base_url = "http://www.cujammu.ac.in/"
    url = "http://www.cujammu.ac.in//Default.aspx?artid=0&type=printallevents&prvtyp=site&option=s"
    scrapers_report.append([url,base_url,name])
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content_div = soup.find("div", class_="boxes-size")
    news_articles = []
    head_block = content_div.find_all("a")

    for block in head_block:
        headline_text = block.text.strip()
        link = block.get("href").strip()
        date_str = block.find_previous("div", class_="morenews").text.strip()
        if "2023" in date_str:
            news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

#cit originally [college_university_6]
try:
    name='cit'
    base_url = "https://cit.ac.in/"
    url = "https://cit.ac.in/"
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    content_div = soup.find("div", id="noticeContainer")
    head_block = content_div.find_all("a")
    for block in head_block:
        headline_text = block.text.replace('\n','')
        link =  block.get("href").strip()
        date_str = block.find_previous("span", class_="block text-xs text-grey-dark").text.strip()
        if "2023" in date_str:
            news_articles.append((name, headline_text, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))
    pass

# Nagarjuna University originally [college_university_1]
try:
    name='Nagarjuna University'
    base_url = 'https://www.nagarjunauniversity.ac.in/'
    url = 'https://www.nagarjunauniversity.ac.in/indexanu.html'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', class_ = 'col-md-4 col-sm-4 categories_sub cats1')
    for head in head_block[0:5]:
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

# Ahmedabad University originally [college_university_1]
try:
    name='Ahmedabad University'
    base_url = 'https://ahduni.edu.in'
    url = 'https://ahduni.edu.in/news/'
    scrapers_report.append([url,base_url,name])
    source= requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('div', class_ = 'col-xs-12 col-sm-6 col-md-4 d-flex align-items-stretch mb-4 mb-lg-5')
    for head in head_block[0:8]:
        headline = head.find('p', class_ = 'card-title').text.strip()
        link =  head.find('a').get('href').strip()
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='Ahmedabad University'
    failure.append((name,e))


# Mangalore University originally [college_university_1]
try:
   name='Mangalore University'
   base_url = "https://mangaloreuniversity.ac.in"
   url = "https://mangaloreuniversity.ac.in/latest-home-news"
   scrapers_report.append([url,base_url,name])
   source = requests.get(url)
   soup = BeautifulSoup(source.text,"html.parser")
   head_block = soup.find_all('span',class_="field-content")
   for head in head_block[0:31]:
       headline=head.find('a').text.strip()
       link= head.find('a').get('href')
       if 'https' not in link:
           link = base_url+link           
       news_articles.append((name,headline,link))
   success.append(name)
except Exception as e:
    name='Mangalore University'
    failure.append((name,e))


# IISER Mohali originally [college_university_1]
try:
    name='IISER MOHALI'
    base_url= "https://www.iisermohali.ac.in"
    url = "https://www.iisermohali.ac.in/news/news/news-archive#april-june-2023"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="articleBody")
    head_block=content_block.find_all("li")
    for head in head_block[0:23]:         
        headline = head.text.strip()
        link_box = head.find("a")
        if link_box is not  None:
            link = link_box.get("href").strip()
            if 'http' not in link:
                link= base_url+link
        else:
            link = url
        news_articles.append((name,headline,link))    
    success.append(name)
except Exception as e:
    name='IISER MOHALI'
    failure.append((name,e))

# NIT Silcher originally [college_university_1]
try:
    name='NIT Silcher'
    base_url = 'http://www.nits.ac.in'
    url = 'http://www.nits.ac.in/newsupdates.php'
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    head_block = soup.find_all('b')
    for head in head_block[0:28]:        
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


# IITD originally [college_university_1]
try:
    name='IITD'
    base_url = "https://home.iitd.ac.in/"
    url = "https://home.iitd.ac.in/news-all.php"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'html.parser')
    content_block = soup.find('div',class_="container ar-container-top")
    head_block=content_block.find_all('div',class_="event-details p-15")
    for head in head_block[0:33]:
        headline = head.text.replace('Read more','').strip()
        link= head.find('a').get("href")
        if 'http' not in link:
            link=base_url+link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name='IITD'
    failure.append((name,e))

#JIS College originally [college_university_7]
try:
    name='JIS College'
    url = 'https://www.jiscollege.ac.in/notice-board.php'
    base_url = 'https://www.jiscollege.ac.in/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    content_div = soup.find('div',class_='timeline-left')
    head_block = content_div.find_all('a',target='_blank')
    
    for block in head_block:
        headline_text = block.get_text().strip()[:999]
        link = block.get('href')
        if 'http' not in link:
            link = base_url + link
        date_str = block.find_previous("h4").text.strip()
        if "2023" in date_str:
            news_articles.append((name, headline_text, link))
    success.append((name))
except Exception as e:
    failure.append((name,e))

# Chennai Institute of Technology originally [college_university_2]
try:
    name='CIT Chennai'
    base_url = 'https://www.citchennai.edu.in/'
    url1 = 'https://www.citchennai.edu.in/latestnews/'
    url2 = 'https://www.citchennai.edu.in/upcoming-events/'
    url3 = 'https://www.citchennai.edu.in/announcements/'
    scrapers_report.append([url1,base_url,name])
    scrapers_report.append([url2,base_url,name])
    scrapers_report.append([url3,base_url,name])
    source1 = requests.get(url1)
    source2 = requests.get(url2)
    source3 = requests.get(url3)
    soup1 = BeautifulSoup(source1.text, 'html.parser')
    soup2 = BeautifulSoup(source2.text, 'html.parser')
    soup3 = BeautifulSoup(source3.text, 'html.parser')

    content_block1 = soup1.find_all("ul", {"class": "news-li"})[0]
    content_block2 = soup2.find_all("ul", {"class": "news-li"})[0]
    content_block3= soup3.find_all("ul", {"class": "news-li"})[0]

    head_block1 = content_block1.find_all('li')
    head_block2 = content_block2.find_all('li')
    head_block23 = content_block3.find_all('li')

    for head in head_block1[0:4]:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        news_articles.append((name, headline, link))

    for head in head_block2[0:2]:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        news_articles.append((name, headline, link))

    for head in head_block23[0:2]:
        headline = head.find('a').text.strip()
        link = head.find('a').get('href')
        news_articles.append((name, headline, link))

    success.append(name)
except Exception as e:
    name='CIT Chennai'
    failure.append((name, e))

# MSIT originally [college_university_2] duplicate [ college_university_8 ]
try:
    name="MSIT"
    base_url= "https://www.msit.in"
    url = "https://www.msit.in/latest_news"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url,verify = False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find("div", class_="tab-content")
    head_block=content_block.find_all('a')
    for head in head_block[0:10]:
        headline= head.text
        link= head.get('href')
        if 'http' not in link:
            link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="MSIT"
    failure.append((name,e))

# IIMU originally [college_university_2] duplicate [ college_university_8 ]
try:
    name="IIMU"
    base_url= "https://www.iimu.ac.in"
    url = "https://www.iimu.ac.in/media/news"
    scrapers_report.append([url,base_url,name])
    source = requests.get(url,verify=False)
    soup = BeautifulSoup(source.text, "html.parser")
    content_block = soup.find_all('div',class_="evetntitle")
    for content in content_block[0:10]:
        head_block=content.find_all('a')
        for head in head_block:
            headline= head.text.strip()
            link= head.get('href')
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    name="IIMU"
    failure.append((name,e))

# dibru originally [ college_university_8]
try:
    name='dibrugarh university'
    base_url='https://dibru.ac.in/'
    url = 'https://dibru.ac.in/2022/06/23/admission-2022-all-notifications_n1/'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_para = soup.find_all('p')
    for content in content_para[0:14]:
        headline_text = content.find('a').text
        link = content.find('a').get('href')
        news_articles.append((name,headline_text,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))

#DTU originally [ college_university_3]
try:
    name = 'DTU'
    url = 'http://www.dtu.ac.in/'
    base_url = 'http://www.dtu.ac.in/'
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    results = soup.find('div', class_='latest_tab').find('ul').find_all('li')
    for result in results:
        he = result.find_all('a', class_='colr')
        for h in he:
            headline = h.text
            link = h.get('href')
            if not link:
                continue
            if 'http' not in link:
                link = base_url + link
            if '2023' not in str(result.find('small')):
                continue
            news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))

#  Rashtriya Sanskrit Sansthan originally [ college_university_3]
try:
    name = "Rashtriya Sanskrit Sansthan"
    url = "https://sanskrit.nic.in/"
    base_url = url
    scrapers_report.append([url, base_url, name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.find("div", class_="contentbox").find("ul").find_all("li")
    for i in articles:
        link_tag = i.find('a',attrs={'href':True})
        if link_tag:
            link = link_tag["href"]
            headline=link_tag.text.strip()
            date_tag = i.find('span', class_='date')
            if date_tag and '2023' in date_tag.text:
                if "http" not in link:
                    link = base_url + link
                news_articles.append((name , headline , link ))
    success.append(name)
except Exception as e:
    failure.append((name, e))

# College Admission(no_ changes_done) originally [cdnews_1]
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

# Success CDS Admission originally [cdnews_1]
try:
    base_url = 'https://www.successcds.net'
    url = 'https://www.successcds.net/admission-notification/index.html'
    name = 'Success CDS Admission'
    scrapers_report.append([url, base_url, name])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    headlines = soup.find_all('tr', 
                              class_='wptb-row')[1:]
    for line in headlines[0:25]:
        row_data = line.find_all('td')
        headline = f'Institute name : {row_data[0].text} Course :{row_data[1].text} Eligibility Criteria : {row_data[2].text} Last Date to Appl: {row_data[3].text}'.replace("\xa0", "")
        link = line.find('a')['href']
        news_articles.append((f'{row_data[0].text} : {name}', headline, link))
    success.append(name)
except Exception as e:
    failure.append((name, e))


#NTA originally [cdofficial_1]
try:
    url = 'https://nta.ac.in/NoticeBoardArchive'
    base_url='https://nta.ac.in'
    name='NTA'
    scrapers_report.append([url,base_url,name])
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find("table",{"id":'tbl'})
    table_tags=table.find_all('tr')
    for news in table_tags:
    
        headline = news.find('content')
        if headline is not None:
            headline=headline.text
            link=news.find('a')
            if link is not None:
                link=link['href']
                headline=headline.strip()
                link=link.strip()
                if 'http' not in link:
                    link=base_url+link
                img = news.find('img')
                if img is not None:
                    img_url = img['src']
                    if 'http' not in img_url:
                        img_url = base_url + img_url
                    news_articles.append((name, headline, link))
        else:  
            headline = news.find('a')
            if headline is not None:
                
                link=headline['href']
                headline=headline.text
                headline=headline.strip()
                link=link.strip()
                if 'http' not in link:
                    link=base_url+link
                img = news.find('img')
                if img is not None:
                    img_url = img['src']
                    if 'http' not in img_url:
                        img_url = base_url + img_url
                    news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    name='NTA'
    failure.append((name, e))


# JKBOPEE originally [ counselling ]
try:
    name = 'JKBOPEE'
    url = 'https://www.jkbopee.gov.in/'
    base_url = url
    scrapers_report.append([url, base_url, name])
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    
    # notice board + notifications
    headlines = soup.find_all(class_='fa fa-hand-o-right')
    for line in headlines:
        headline = line.text.strip()
        a_tag = line.find('a')
        if a_tag:
            link = a_tag['href']
            if 'http' not in link:
                link = base_url + link
            news_date = re.search(r'\d{2}-\d{2}-2023', headline)
            if news_date:
                news_articles.append((name, headline, link))

    # table
    trs = soup.find(class_='table table-bordered table-striped').find_all('tr')[1:]
    for tr in trs:
        tds = tr.find_all('td')
        examination = tds[1].text.strip()
        date = tds[2].text.strip()
        if '2023' in date:
            news_articles.append((name, examination, date))

    success.append(name)
except Exception as e:
    failure.append((name, e))

#CENTAC originally [ counselling ]
try:
    name = 'CENTAC'
    url = 'https://www.centacpuducherry.in/'
    base_url = url
    scrapers_report.append([url,base_url,name])
    content = requests.get(url)
    #print(content.status_code)
    soup = BeautifulSoup(content.text,'html.parser')
    notifications = soup.find_all(class_='content text-danger font-weight-bold text-justify')
    for notification in notifications:
        a_tag = notification.find('a')
        if a_tag:
            headline = a_tag.text.strip()
            link = a_tag['href']
            if 'http' not in link:
                link = base_url + link
            news_date = re.search(r'\d{2}-\d{2}-2023', headline)
            if news_date:
                news_articles.append((name, headline, link))
    success.append(name)
except Exception as e:
    failure.append((name,e))


#AIIMS Admission originally [ counselling ]
try:
    name = 'AIIMS Admission'
    url = 'https://www.aiimsexams.ac.in/'
    base_url = url
    scrapers_report.append([url,base_url,name])
    content = requests.get(url)
    #print(content.status_code)
    soup = BeautifulSoup(content.text,'html.parser')
    announcements = soup.find(class_='announcement blue').find_all('p')
    for announcement in announcements[0:95]:
        a_tag = announcement.find('a')
        headline = announcement.text.strip()
        if a_tag:
            link = a_tag['href']
            link = link.replace(' ', '%20')
            if 'http' not in link:
                link = base_url + link
        news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))

#BCECE originally [ counselling ]
try:
    name = 'BCECE'
    url = 'https://bceceboard.bihar.gov.in/'
    base_url = url
    scrapers_report.append([url,base_url,name])
    content = requests.get(url,verify=False)
    #print(content.status_code)
    soup = BeautifulSoup(content.text,'html.parser')
    for clss in ('update','notice'):
        headlines = soup.find(class_=clss).find_all('li')
        for line in headlines[0:35]:
            a_tag = line.find('a')
            headline = line.text.strip()
            if a_tag:
                link = a_tag['href']
                if 'http' not in link:
                    link = base_url + link
            else:
                link = ''
            news_articles.append((name,headline,link))
    success.append(name)
except Exception as e:
    failure.append((name,e))
