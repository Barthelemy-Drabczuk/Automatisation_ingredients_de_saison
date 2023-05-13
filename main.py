from download import Downloader

def main() -> None:
    my_page: Downloader = Downloader("https://www.greenpeace.fr/guetteur/calendrier/")
    print (my_page.get_content())

if __name__ == "__main__":
    main()