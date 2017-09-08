# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.trad_content = False

    def handle_starttag(self, tag, attrs):
        if tag == 'article_bilingue':
            self.trad_content == True
        #print("<< Trouvé balise ouvrante :", tag)

    def handle_endtag(self, tag):
        #print(">> Trouvé balise fermante :", tag)
        pass

    def handle_data(self, data):
        if self.trad_content:
            if data.strip(): print("    Trouvé contenu  :", data)
        pass

parser = MyHTMLParser()
u = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/rear')
data = u.read().decode('utf8')
parser.feed(data)

