import requests
from datetime import datetime

from pages.news_page import NewsPage

page_content = requests.get('https://news.ycombinator.com/').content
page = NewsPage(page_content)


print(f'HACKER NEWS TOP NEWS for {datetime.now().strftime("%A, %d %b, %Y")}')
print('---------------------')

for news in page.news:
    print(news)
