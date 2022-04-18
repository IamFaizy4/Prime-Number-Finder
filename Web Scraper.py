# step 0 setting the environment

from turtle import title
import requests
from bs4 import BeautifulSoup
url = input("Enter the Page URL to scrape: ")

# get the html
r = requests.get(url)
htmlContent = r.content

# parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

#html tree traversal
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)

# get title
title = soup.title

# get paragraphs
paras = soup.find_all('p')

# get anchors 
anchors = soup.find_all('a')

# Get first element
print(soup.find('p') )

# get class of any element
print(soup.find ("p")['class'])

# find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
print(soup.find ('p').get_text())
print(soup.get_text())

# Get all the links on the page:
# all_links = set()
# for link in anchors:
#     if(link.get('href') != '#'):
#         linkText = "https://www.programiz.com/python-programming/keyword-list" +link.get('href')
#         all_links.add(link)
#         print(linkText)


elem = soup.select('#loginModal')
print(elem)



"""
import urllib2
import csv
import requests
from bs4 import BeautifulSoup
 
rank_page = 'https://socialblade.com/youtube/top/50/mostviewed'
request = urllib2.Request(rank_page, headers={'User-Agent': 'your user-agent'})
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')
 
channels = soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)[4:]
 
file = open('topyoutubers.csv', 'wb')
writer = csv.writer(file)
 
# write title row
writer.writerow(['Username', 'Uploads', 'Views'])
 
for channel in channels:
    username = channel.find('div', attrs={'style': 'float: left; width: 350px; line-height: 25px;'}).a.text.strip()
    uploads = channel.find('div', attrs={'style': 'float: left; width: 80px;'}).span.text.strip()
    views = channel.find_all('div', attrs={'style': 'float: left; width: 150px;'})[1].span.text.strip()
 
    print(username + ' ' + uploads + ' ' + views)
    writer.writerow([username.encode('utf-8'), uploads.encode('utf-8'), views.encode('utf-8')])
 
file.close()
"""