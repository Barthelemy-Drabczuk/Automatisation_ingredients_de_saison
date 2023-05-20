from download import Downloader
from parse import Parser

def main() -> None:
    my_page: Downloader = Downloader("https://www.greenpeace.fr/guetteur/calendrier/")
    parser = Parser(my_page.get_content())
    print (parser.get_current_month())

if __name__ == "__main__":
    main()