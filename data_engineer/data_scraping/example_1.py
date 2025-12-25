import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import scrapy
import pandas as pd

response = requests.get('https://example.com')
html_content = response.text
status_code = response.status_code  # 200 = success

soup = BeautifulSoup(html_content, 'html.parser')

# Find elements
title = soup.find('h1').text
links = soup.find_all('a')
price = soup.find('span', class_='price').text

# CSS selectors
items = soup.select('div.product > h2')



driver = webdriver.Chrome()
driver.get('https://example.com')

# Wait for JavaScript to load
element = driver.find_element(By.CLASS_NAME, 'dynamic-content')
data = element.text

driver.quit()

class MySpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://example.com']
    
    def parse(self, response):
        for item in response.css('div.item'):
            yield {
                'title': item.css('h2::text').get(),
                'price': item.css('span.price::text').get()
            }



df = pd.DataFrame(products)
df.to_csv('~/workspace/AlgorithmInPython/datasets/products.csv', index=False)