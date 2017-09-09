# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request



if __name__ == '__main__':
    data = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/plant').read().decode('utf8')
    soup = BeautifulSoup(data, 'html.parser')
    print(soup.prettify())