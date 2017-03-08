#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Simple WebScraping, usa urllib2 y BeautifulSoup
@author: Fran Dolz Sallen
"""

import urllib2
from bs4 import BeautifulSoup


class Cliente(object):
    def get_web(self,page):
        """ bajarse la web """
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
    	#buscar el titulo
        soup = BeautifulSoup(html, 'html.parser')      
        title = soup.find_all("div", "dotd-title")
        return title

    def main(self):
        web = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        result = self.search_text(web)
        #Imprimir resultado
        print result

if __name__== "__main__":
    cliente = Cliente()
    cliente.main()
