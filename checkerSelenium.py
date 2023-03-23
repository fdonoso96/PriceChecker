#!/usr/bin/env python3

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


class PriceChecker:
    def __init__(self):
       a = '2'

    def loadList(self, fileName):
        list_file = open(fileName ,'r')
 
        if fileName == "AmazonList.txt":
            self.urlsAmazon = list_file.readlines()
        elif fileName == "WalmartList.txt":
            self.urlsWalmart = list_file.readlines()
        
        list_file.close()
        
    def checkPricesAmazon(self):
        for url in self.urlsAmazon:

            page = requests.get(url,headers = self.HEADERS)
            soup = bs4.BeautifulSoup(page.content,features='lxml')
            self.titlesAmazon.append(soup.find(id='productTitle').get_text().strip())

            try:
                #print(soup.find(id='sns-base-price').get_text().strip())
                self.pricesAmazon.append(soup.find('span', class_='a-offscreen').get_text())
            except:
                self.pricesAmazon.append(" ")

    def checkPricesWalmart(self):
        for url in self.urlsWalmart:
            page = requests.get(url,headers = self.HEADERS)
            soup = bs4.BeautifulSoup(page.content,features='lxml')
            #self.titlesWalmart.append(soup.find('span', class_='b lh-copy dark-gray mt1 mb2 f3').get_text().strip())
            
            try:
                #print(soup.find(id='sns-base-emprop="price"))
                #print(page.headers)
                self.pricesWalmart.append(soup.find(class_="price-group").text())
            except:
                self.pricesWalmart.append(" ")

    


if __name__ == "__main__":
    checker = PriceChecker()
    os.chdir("/Users/fdonoso/PycharmProjects/PriceChecker/")
    checker.loadList("AmazonList.txt")
    checker.loadList("WalmartList.txt")
    checker.checkPricesAmazon()
    #checker.checkPricesWalmart()

    print('\n')
    print(*checker.titlesAmazon,"-- Amazon Price: ", *checker.pricesAmazon,"-- Walmart Price: ",*checker.pricesWalmart, sep = "\n")

