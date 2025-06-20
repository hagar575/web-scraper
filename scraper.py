import requests
from bs4 import BeautifulSoup

url = 'https://edition.cnn.com/world'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

for title in soup.find_all('span', class_='container__headline-text'):
    print(title.text.strip())