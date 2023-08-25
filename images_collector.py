from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

import io
from urllib import request
from PIL import Image

book_urls = []

for page in range(1, 2):
	url = 'https://manga-zip.info/home.i1/?p={}'.format(page)
	browser.get(url)
	time.sleep(3)

	elem = browser.find_element(By.CLASS_NAME, '__l')
	elem = elem.find_element(By.TAG_NAME, 'a')
	book_url = elem.get_attribute('href')
	elem = elem.find_element(By.TAG_NAME, 'img')
	img_url = elem.get_attribute('src')
	book_title = elem.get_attribute('alt')
	print(book_url, img_url)
	book_urls.append(book_url)

	image_data = request.urlopen(img_url).read()
	image_binary = io.BytesIO(img_data)
	img = Image.open(image_binary)
	#img = img.resize((1280, 800))
	img.save('images/{}.jpg'.format(book_title))

import pandas as pd
df = pd.DataFrame()

df['book_url'] = book_urls
df.to_csv('books_urls.csv')
browser.close()
