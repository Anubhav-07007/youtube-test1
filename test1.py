from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector as conn

a='krish naik'
def remove_space(a):
    return a.replace(' ','')

user_name=remove_space(a)
search_url='https://www.youtube.com/results?search_query='+'{}'.format(user_name)


driver=webdriver.Chrome()
driver.get('{}'.format(search_url))
content=driver.page_source.encode('utf8')
soup=BeautifulSoup(content,'lxml')
user_page=soup.find_all('a',id='main-link')

print(user_page[0]['href'])

channel_id=user_page[0]['href']

channel_url='https://www.youtube.com'+'{}'.format(channel_id)

driver.get('{}'.format(channel_url))

channel_content=driver.page_source.encode('utf8')
soup1=BeautifulSoup(channel_content,'lxml')

video_title=soup1.find_all('h3',{'class':'style-scope ytd-grid-video-renderer'})

#print(video_title[0].a.text)
#for i in video_title:
   # print (i.text)


mydb=conn.connect(host='localhost',user='root',passwd='ar@66007')
print(mydb)

cursor=mydb.cursor()

cursor.execute('use anubhav')
cursor.execute('show tables')
title=[]
for i in video_title:
    title.append(i.text)

print(title)



