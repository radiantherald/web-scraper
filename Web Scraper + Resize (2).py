import os, sys
import requests
import splitfolders as sf
from bs4 import BeautifulSoup
from PIL import Image


def ImageScraper(url, folder, size):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    name = 0
    print(type(images))
    images_new = images[1:]
    print(len(images_new))
    for image in images_new:
        name = name + 1
        link = image['src']
        img = Image.open(requests.get(link, stream = True).raw)

        imResize = img.resize(size, Image.ANTIALIAS)
        imResize.save(str(name) + ' resized.jpg', 'JPEG', quality=100)
        print('Writing: ', name)
        print(imResize.size)

def train_test_split(split_ratio):   
    input_folder = os.getcwd()
    sf.ratio(input_folder, output = 'dataset', seed = 12, ratio = split_ratio)





