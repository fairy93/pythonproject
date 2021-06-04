from selenium import webdriver
from bs4 import BeautifulSoup


class NaverFinance(object):
    driver_path = 'C:\Program Files\Google\Chrome\chromedriver'
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn?&page='

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        for i in range(1, 10):
            driver.get(self.url + str(i))
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            li = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
            stock_code = li[1].find('a', attrs={"class": "tltle"})['href'].split('=')[1]
            for j in li:
                li2 = j.get_text().split()
                if len(li2) > 1:
                    print(f'({li2[1]} {stock_code}) 현재가:{li2[2]}')
        driver.close


if __name__ == '__main__':
    finance = NaverFinance()
    finance.scrap()
