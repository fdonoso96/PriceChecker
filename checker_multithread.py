#!/usr/bin/env python3

import os
import bs4
import requests
import time
import threading
from selenium.common import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


class PriceChecker:
    def __init__(self):
        # self.Amazon = [[]*3]
        self.urlsAmazon = []
        self.titlesAmazon = []
        self.pricesAmazon = []
        self.urlsWalmart = []
        self.titlesWalmart = []
        self.pricesWalmart = []
        # self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def loadList(self, fileName):
        list_file = open(fileName, 'r')

        if fileName == "AmazonList.txt":
            self.urlsAmazon = list_file.readlines()
        elif fileName == "WalmartList.txt":
            self.urlsWalmart = list_file.readlines()

        list_file.close()

    def checkPricesAmazon(self):
        current = 1
        # for url in self.urlsAmazon:
        #     print(f"Currently checking product {current} on Amazon.")
        #     profile_path = r'/Users/fdonoso/Library/Application Support/Firefox/Profiles/yjau3k6a.FrankieD'
        #     service = Service(r'/Users/fdonoso/Downloads/geckodriver')
        #     options = Options()
        #     options.add_argument("--headless")
        #     options.set_preference('profile', profile_path)
        #
        #     driver = Firefox(service=service, options=options)
        #     time.sleep(3)
        #     driver.get(url)
        #     self.titlesAmazon.append(
        #         driver.find_element(By.ID, 'productTitle').text)
        #
        #     try:
        #         # print(soup.find(id='sns-base-price').get_text().strip())
        #         self.pricesAmazon.append(
        #             driver.find_element(By.ID, 'sns-base-price').text)
        #         current = current + 1
        #
        #     except NoSuchElementException:
        #         self.pricesAmazon.append(" ")
        #         current = current + 1

    def checkPricesWalmart(self):
        current = 1
        for url in self.urlsWalmart:

            print(f"Currently checking product {current} on Walmart.")
            profile_path = r'/Users/fdonoso/Library/Application Support/Firefox/Profiles/yjau3k6a.FrankieD'
            service = Service(r'/Users/fdonoso/Downloads/geckodriver')
            options = Options()
            options.add_argument("--headless")
            options.set_preference('profile', profile_path)

            driver = Firefox(service=service, options=options)
            time.sleep(3)
            driver.get(url)

            try:
                # print(soup.find(id='sns-base-emprop="price"))
                # print(page.headers)
                self.pricesWalmart.append(driver.find_element(By.XPATH,
                                                              '/html/body/div[1]/div[1]/div/div/div[2]/div/section/main/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/span[1]/span[2]/span').text)
                driver.quit()
                current = current + 1
                continue
            except:
                print("Trying alternative XPATH")
                # driver.quit()

            try:
                self.pricesWalmart.append(driver.find_element(By.XPATH,
                                                              '/html/body/div[1]/div[1]/div/div/div[2]/div/section/main/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[1]/span/span[2]/span').text)
                current = current + 1
                driver.quit()
            except:
                self.pricesWalmart.append("None")
                current = current + 1
                driver.quit()

    def export(self, strmethod):
        strmethod = 'Placeholder'


if __name__ == "__main__":

    t0 = time.time()

    threads = []
    checker = PriceChecker()
    # os.chdir("/Users/fdonoso/PycharmProjects/PriceChecker/")
    checker.loadList("AmazonList.txt")
    checker.loadList("WalmartList.txt")

    for url in checker.urlsAmazon:
        t = threading.Thread
        t.start()

        profile_path = r'/Users/fdonoso/Library/Application Support/Firefox/Profiles/yjau3k6a.FrankieD'
        service = Service(r'/Users/fdonoso/Downloads/geckodriver')
        options = Options()
        options.add_argument("--headless")
        options.set_preference('profile', profile_path)

        driver = Firefox(service=service, options=options)
        time.sleep(3)
        driver.get(url)
        self.titlesAmazon.append(
            driver.find_element(By.ID, 'productTitle').text)

        try:
            # print(soup.find(id='sns-base-price').get_text().strip())
            self.pricesAmazon.append(
                driver.find_element(By.ID, 'sns-base-price').text)
            current = current + 1

        except NoSuchElementException:
            self.pricesAmazon.append(" ")
            current = current + 1

        threads.append(t)

    for t in threads:
        t.join()
    # checker.checkPricesAmazon()
    # checker.checkPricesWalmart()

    t1 = time.time()
    total = t1 - t0
    #
    # print('\n')
    # print(len(checker.urlsAmazon))
    # print(total / 60)
    # print('\n')
    #
    # data = list(zip(checker.titlesAmazon, checker.pricesAmazon, checker.pricesWalmart))
    # print("(Item, Amazon Price, Walmart Price)")
    # print(data, sep="\n")
    # # print(*checker.titlesAmazon,"-- Amazon Price: ", *checker.pricesAmazon,"-- Walmart Price: ",*checker.pricesWalmart, sep = "\n")
