from download import Downloader
from parse import Parser

def main() -> None:
    my_page: Downloader = Downloader("https://www.greenpeace.fr/guetteur/calendrier/")
    parser = Parser()
    print (parser.feed(my_page.get_content()))

if __name__ == "__main__":
    main()