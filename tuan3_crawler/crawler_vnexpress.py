import requests as rq
from bs4 import BeautifulSoup
import json

response = rq.get("https://vnexpress.net/the-thao")
soup = BeautifulSoup(response.content, "html.parser")
# print(soup)
titles = soup.findAll('h3', class_='title-news')
# print(titles)
links = [link.find('a').attrs["href"] for link in titles]

# print(links)
# Connect
response = rq.get("https://vnexpress.net/the-thao")
soup = BeautifulSoup(response.content, "html.parser")

# Get tag a
titles = soup.findAll('h3', class_='title-news')

# Get link href
links = [link.find('a').attrs["href"] for link in titles]
print(links)
i = 0
arr = []
for link in links:
    i += 1
    print(i)
    news = rq.get(link)
    # print(news)
    soup = BeautifulSoup(news.content, "html.parser")
    # print(soup)
    title = soup.find('h1')
    # Title
    if title is None:
        title = soup.find('h1', class_='title-detail')
    # Abs
    abstract = soup.find("p", class_="description")
    if abstract is None:
        abstract = soup.find("h2")
    insert = {'href': link, 'title': title.text, 'abstract': abstract.text}
    arr.append(insert)
print(arr)
with open('data.json', 'w', encoding='utf8') as file:
    json.dump(arr, file, ensure_ascii=False)
