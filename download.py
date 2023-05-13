import requests

class Downloader:
    def __init__(self, url: str):
        self.__url: str = url
        self.__content: str = requests.get(url).content
    
    def get_url(self) -> str:
        return self.__url
    
    def get_content(self) -> str:
        return self.__content
