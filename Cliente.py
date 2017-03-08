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
    """
    Sobre la pagina web https://www.packtpub.com/packt/offers/free-learning/
    busca el titulo de libro gratuito del día y lo muestra.
    """
    def get_web(self,page):
        """ 
        Baja la web obteniendo su codigo html 
        """
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def search_text(self, html):
    	"""
        Parsea y busca el titulo deseado 
        """
        soup = BeautifulSoup(html, 'html.parser')      
        title = soup.find("div", "dotd-title")
        book = title.find("h2").text    
        return book.strip() if book else "Error"

    def main(self):
        web = self.get_web("https://www.packtpub.com/packt/offers/free-learning/")
        result = self.search_text(web)
        #Imprime resultado
        print result

if __name__== "__main__":
    cliente = Cliente()
    cliente.main()
