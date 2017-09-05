#-*-coding:utf-8-*-
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://google.com')
    print(driver.title)
    driver.quit()


__author__ = 'manitou'
