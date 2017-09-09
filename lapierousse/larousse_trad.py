# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import urllib.request


class traduction_parser(HTMLParser):
    def __init__(self, targeted_tag):
        super().__init__()
        self.targeted_tag = targeted_tag
        self.in_tag = False

    def handle_starttag(self, tag, attrs):
        if len(tag) is not 0:
            if ('class', self.targeted_tag) in attrs:
                self.in_tag = True
        pass

    def handle_endtag(self, tag):
        self.in_tag = False
        pass

    def handle_data(self, data):
        if self.in_tag:
            print(data)
        pass

if __name__ == '__main__':
    parser = traduction_parser('numero')
    u = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/plant')
    data = u.read().decode('utf8')
    parser.feed(data)
