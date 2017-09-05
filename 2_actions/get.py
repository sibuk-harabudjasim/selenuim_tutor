from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.gismeteo.ua/')

    print('Title', driver.title)
    print('Url', driver.current_url)
    source = driver.page_source
    print('HTML', source[:200])

    driver.set_window_size(800,600)
    print('Window size', driver.get_window_size())

    driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
    print('FOO cookie', driver.get_cookie('foo'))
    print('Cookies', driver.get_cookies())
    driver.delete_cookie('foo')
    driver.delete_all_cookies()

    driver.save_screenshot('/Screenshots/foo.png')

    # driver.implicitly_wait(30)

    driver.quit()

__author__ = 'manitou'
