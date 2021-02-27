import os
import json
import requests  # to sent GET requests
from bs4 import BeautifulSoup  # to parse HTML
from selenium import webdriver
from PIL import Image
import numpy as np
import pandas as pd

# import the countries
countries_df = pd.read_csv('countries of the world.csv')

countries = list(countries_df.iloc[:, 0])

# set up the webdriver
driver = webdriver.Firefox(executable_path= r"C:\Users\Dave\AppData\Local\Programs\Python\Python38\geckodriver.exe")

url_start = 'https://duckduckgo.com/?q='

url_ends = ['flag&t=h_&iax=images&ia=images', 'flag+celebrate&t=h_&iax=images&ia=images', '+flag+building&t=h_&iax=images&ia=images']

# make a dictionary to keep track of the y label for each image
array_list = []

# search through each country
for country in countries:

    counter = 1

    # define the image directory
    img_dir = 'images/' + country + '/'

    # make the directory
    os.mkdir(img_dir)

    # search for both types of image
    for url_end in url_ends:

        driver.get(url_start + country + url_end)

        driver.implicitly_wait(10)

        # list all the images on the webpage
        image_list = driver.find_elements_by_class_name('tile--img__img')

        for image in image_list:
            # find the source
            image_source = image.get_attribute("src")
            img = Image.open(requests.get(image_source, stream=True).raw)

            # resize the images to 100x1000
            img = img.resize(size=(100, 100))

            # save the image
            img.save(img_dir + str(counter) + '.jpg')

            counter += 1

print(array_list)




