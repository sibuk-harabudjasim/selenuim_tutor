#-*-coding:utf-8-*-
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.gismeteo.ua/')

    kiev_link = driver.find_element_by_link_text(u'Київ')
    kiev_link.click()

    temp = driver.find_element_by_css_selector('#tab_wdaily2 .temp')
    values = temp.find_elements_by_css_selector('.value.m_temp.c')
    print [v.text for v in values]

    driver.quit()


__author__ = 'manitou'
