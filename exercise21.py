"""
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want
to play with some different code, use the code from the solution), and instead of printing
the results to a screen, write the results to a txt file. In your code, just make up a
name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
Discussion
Topics:

Writing to a file
Gotchas and warnings
"""

from bs4 import BeautifulSoup
import requests

base_url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
response = requests.get(base_url)
response_html = response.text

soup = BeautifulSoup(response_html, features='lxml')

filename = input("Please, type the desired file name: ") + '.txt'

with open(filename, 'w+') as f:
    for article_part in soup.find_all('div', class_='article__body'):
        for paragraph in article_part.find_all('p'):
            f.write(paragraph.text + '\n')
