from selenium import webdriver
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.gismeteo.ua/')
    city = driver.find_element_by_css_selector('#weather h2')

    # common
    print('Accessing city value')
    print('Text', city.text)
    print('Tag', city.tag_name)
    print('Class', city.get_attribute('class'))
    print('Is displayed', city.is_displayed())
    print('Size', city.size)
    weather = driver.find_element_by_id('weather')
    weather.screenshot('weather_screenshot.png')

    # control element (a, button)
    logo = driver.find_element_by_id('logo')
    logo.click()

    # form element (button, input, select)
    search = driver.find_element_by_id('ya')
    city.is_enabled()
    city.clear()
    city.send_keys('Kiev')
    city.submit()

    time.sleep(10)
    driver.quit()

__author__ = 'manitou'
