from locators.news_locators import NewsLocators


class NewsParser:
    """
    One parent tag, extract the data in it
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<{self.content} available at {self.link}>\n'

    @property
    def content(self):
        locator = NewsLocators.TITLE
        return self.parent.select_one(locator).string

    @property
    def link(self):
        locator = NewsLocators.LINK
        required_link = self.parent.select_one(locator)
        return required_link.attrs['href']
