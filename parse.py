from html.parser import HTMLParser

class Parser(HTMLParser):
        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
                print(f"Encountered {tag} opening tag\n")
        def handle_endtag(self, tag: str) -> None:
                print(f"Encountered {tag} end tag\n")
        def handle_data(self, data: str) -> None:
                print(f"Here is some data: {data}\n")