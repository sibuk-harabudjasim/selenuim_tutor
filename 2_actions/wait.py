from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    # driver.implicitly_wait(30)
    driver.get('https://www.gismeteo.ua/')
    news = driver.find_element_by_id('weather-news')
    divs = news.find_elements_by_tag_name('div')
    print(len(divs))

    driver.quit()


__author__ = 'manitou'
