# -*- coding: utf-8 -*-
from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.content = False
        self.indent = ''

    def handle_starttag(self, tag, attrs):
        if len(attrs) is not 0:
            if 'content en-fr' in attrs[0]:
                self.content = True
        if self.content:
            self.indent += '    '
            print(self.indent, '<', tag, '>', attrs, sep='')

    def handle_endtag(self, tag):
        if self.content and tag == 'article':
            self.content = False
        elif self.content:
            print(self.indent, '</', tag, '>', '\n', sep='')
            self.indent = self.indent[:-4]

    def handle_data(self, data):
        if self.content:
            if len(data.strip()) is not 0:
                print(self.indent, '|=>', data.strip(), '<=|', sep='')



parser = MyHTMLParser()
u = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/rear')
data = u.read().decode('utf8')
parser.feed(data)
