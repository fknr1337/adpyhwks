import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'web', 'фото' 'python','кольцо', 'российских']

response = requests.get('https://habr.com/ru/all/')
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    previews = [p.text.strip() for p in article.find_all('div', class_='post__text')]
    for word in previews:
        for i in KEYWORDS:
            if i in word:
                url = article.find('a', class_='post__title_link')
                date = article.find('span', class_='post__time')
                urls = url.attrs.get('href')
                print(f'{date.text} > {url.text} > {urls}')
