from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

import io
from urllib import request
from PIL import Image

url = 'https://pz-garden.stardust31.com/syokuniku-moku/itati-haiena-ka/itati-ka.html'
browser.get(url)

page_urls = []
# テキストに「プロフィール」を含む<font>の親要素である<a>を取得
xpath = '//font[contains(text(), "プロフィール")]/parent::a'

elems_url = browser.find_elements(By.XPATH, xpath)

# page_names = []

for elem_url in elems_url:
    page_url = elem_url.get_attribute('href')
    page_urls.append(page_url)
#     page_name = page_url.split('/')[5]
#     page_name = page_name.split('.html')[0]
#     page_names.append(page_name)
page_urls

#photo_urls = []

for page in pages:
    browser.get(page)
    
    # alt属性に「動物図鑑」を含むimgタグを全て取得
    xpath ='//img[contains(@alt, "動物図鑑")]'
    elems_img = browser.find_elements(By.XPATH, xpath)
    
    for index, elem_img in enumerate(elems_img):
        photo_url = elem_img.get_attribute('src')
        #photo_urls.append(photo_url)
        image_data = request.urlopen(photo_url).read()
        image_binary = io.BytesIO(image_data)
        img = Image.open(image_binary)
        #img = img.resize((1280, 800))
        
        # ファイル名の生成
        # ページ名 + _ + 0埋めした3ケタの連番で生成する場合
        page_name = page.split('/')[5].split('.html')[0]
        img.save('images/{0}_{1:03d}.jpg'.format(page_name, index))

        # 元々のファイル名をそのまま取ってきて何も加工しない場合(命名ルールによっては問題が起き得る)
        #photo_name = photo_url.split('/')[6]
        #img.save('images/{}'.format(photo_name))

browser.close()

import pandas as pd
df = pd.DataFrame()

df['page_url'] = page_urls
df.to_csv('animals_urls.csv', index=False)
