import time
from selenium import webdriver

# link: https://chromedriver.chromium.org/getting-started
driver = webdriver.Chrome()

# driver = webdriver.Chrome('/Users/bangbui/workspace/chromedriver_mac64/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element("name","q")
# search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()