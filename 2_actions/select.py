from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.gismeteo.ua/')

    driver.find_element_by_id('foo')
    driver.find_elements_by_id('foo')
    driver.find_element_by_xpath('//div/td[1]')
    driver.find_elements_by_xpath("//div[contains(@class, 'foo')]")
    driver.find_element_by_link_text('Sign In')
    driver.find_elements_by_link_text('Sign In')
    driver.find_element_by_partial_link_text('Sign')
    driver.find_element_by_partial_link_text('Sign')
    driver.find_element_by_name('foo')
    driver.find_elements_by_name('foo')
    driver.find_element_by_tag_name('foo')
    driver.find_elements_by_tag_name('foo')
    driver.find_element_by_class_name('foo')
    driver.find_elements_by_class_name('foo')
    driver.find_element_by_css_selector('#foo')
    driver.find_elements_by_css_selector('.foo')

    driver.quit()



__author__ = 'manitou'
