from selenium import webdriver

# first start standalone selenium server by command:
#    java -jar selenium-server-standalone-3.4.0.jar
# after that you can connect to it
# there are a lot standalone emulators like selendroid or ios-driver with similar approach


if __name__ == '__main__':
    driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
    driver.get('https://google.com')
    print(driver.title)
    driver.quit()


__author__ = 'manitou'
