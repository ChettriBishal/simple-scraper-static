from bs4 import BeautifulSoup

from locators.news_page_locators import NewsPageLocators
from parsers.news import NewsParser


class NewsPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def news(self):
        locator = NewsPageLocators.NEWS
        news_tag = self.soup.select(locator)
        return [NewsParser(n) for n in news_tag]
