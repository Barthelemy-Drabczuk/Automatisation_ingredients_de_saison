import locale
from bs4 import BeautifulSoup
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'fr_FR')

class Parser:
    def __init__(self, html_content) -> None:
        self.__bs_obj = BeautifulSoup(html_content.lower(), 'html.parser')
    
    def get_current_month(self) -> dict:
        raw = self.__bs_obj.find_all(class_="month")[datetime.now().month - 1]
        # print(raw.prettify())
        items = [[i.text.rstrip().lstrip() for i in b.find_all('li')] for b in raw.find_all("ul")]
        return {
            items[0][0] : items[1],
            items[0][1] : items[2]
        }
