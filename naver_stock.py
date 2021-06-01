from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


class Naver_Stock(object):
    driver_path = 'C:\Program Files\Google\Chrome\chromedriver'
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
    title_ls = []

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup)
        #     print({type(i.find('a'))})
        # # self.title_ls.append(i.find['a'].text)
        # print('---')
        # for j in i:
        #     print(j.attrs['herf'])
        # driver.close


if __name__ == '__main__':
    naver = Naver_Stock()
    naver.scrap()
