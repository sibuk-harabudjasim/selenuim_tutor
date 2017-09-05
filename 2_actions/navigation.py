from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.gismeteo.ua/')
    driver.back()
    driver.refresh()

    driver.quit()

__author__ = 'manitou'
