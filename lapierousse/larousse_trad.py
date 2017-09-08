# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        in_trad_content = False

    def handle_starttag(self, tag, attrs):
        print("<< Trouvé balise ouvrante :", tag)

    def handle_endtag(self, tag):
        print(">> Trouvé balise fermante :", tag)

    def handle_data(self, data):
        if data.strip(): print("    Trouvé contenu  :", data)

parser = MyHTMLParser()
u = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/rear')
data = u.read().decode('utf8')
parser.feed(data)

