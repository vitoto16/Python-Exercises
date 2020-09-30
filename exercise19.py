"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full text
of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text
to the screen so that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests
libraries through the solution of the exercise posted here.)
"""

from bs4 import BeautifulSoup
import requests

base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
response = requests.get(base_url)
response_html = response.text

soup = BeautifulSoup(response_html, features='lxml')

for article_part in soup.find_all('div', class_='article__body'):
    for paragraph in article_part.find_all('p'):
        print(paragraph.text)

