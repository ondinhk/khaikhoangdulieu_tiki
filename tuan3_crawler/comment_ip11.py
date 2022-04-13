import requests as rq
from bs4 import BeautifulSoup
import json

HEADERS = {
    'user-agent': (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
    , 'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5'
}
ARRAY = []
numberOfComment = 0


# 'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
#                '(KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36')
# Create file review_tgdd.json
def exportFile():
    with open('review_tgdd.json', 'w', encoding='utf8') as file:
        json.dump(ARRAY, file, ensure_ascii=False)
    print('number of comment')
    print(len(ARRAY))
    print("Complete")


# Get max page number
def count_page():
    # Connect
    BASE_URL = 'https://www.thegioididong.com/dtdd/iphone-11/danh-gia?p=1'
    response = rq.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    # get navbar page
    div_navbar = soup.find('div', {'class': 'pagcomment'})
    # get value link a
    numPage = div_navbar.find_all('a')
    max_page = 0
    # get maximum number of pages
    for a in numPage:
        # try to convert string to int
        try:
            num = int(a.text)
        except:
            # continue if not convert (exam: >>, ...)
            continue
        max_page = max(max_page, num)
    return max_page


# Crawl with page number
def crawl(page):
    # Get response
    URL = 'https://www.thegioididong.com/dtdd/iphone-11/danh-gia?p='
    BASE_URL = URL + str(page)
    print(BASE_URL)
    response = rq.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    # find div containing comment
    Comment = soup.find('div', {'class': 'comment--all'})
    # get all comment -> list item comment
    allComment = Comment.find_all('div', {'class': 'comment__item'})
    # get comment item
    for item in allComment:
        # get username
        itemName = item.find('p', class_='txtname').get_text()
        itemComment = item.find('p', class_='cmt-txt').get_text()
        # count class icon-star == rate star
        starsTag = item.find_all('i', {'class': 'icon-star'})
        rateStar = len(starsTag)
        if starsTag is None:
            rateStar = 2
        # add object to temp
        temp = {'username': itemName, 'comment': itemComment, 'rate': rateStar}
        # add temp to ARRAY
        ARRAY.append(temp)
        # if (idx == 2):
        #     break


# Run
max_page = count_page()
print(max_page)
# for i in range(max_page):
#     crawl(i + 1)
# exportFile()
