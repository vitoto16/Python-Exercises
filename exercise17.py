"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article
titles on the New York Times homepage.
"""

from bs4 import BeautifulSoup
import requests

url = "https://www.nytimes.com/"

response = requests.get(url)
response_html = response.text

soup = BeautifulSoup(response_html, features="lxml")
for title in soup.find_all('h2'):
    print(title.text + '\n')

