from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://google.com')
    print(driver.title)
    driver.quit()


__author__ = 'manitou'
