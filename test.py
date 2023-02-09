import cv2
import urllib.request
import pandas as pd
import numpy as np

img_df = {'link': ['https://cdn.pixabay.com/photo/2017/10/10/07/48/hills-2836301__480.jpg',
                   'https://cdn.pixabay.com/photo/2018/02/13/23/41/nature-3151869__480.jpg']}
img_df = pd.DataFrame(img_df)

hist_results = []
images_url = []



def color_histogram(photo):
    for urls in photo:
        url_response = urllib.request.Request(urls, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(url_response) as url:
            s = url.read()

        img = cv2.imdecode(np.asarray(bytearray(s), dtype=np.uint8), -1)

        channels = cv2.split(img)

        hist = cv2.calcHist([channels[0]], [0], None, [256], [0, 256])
        colors = ["b", "g", "r"]
        colors = colors[0]

    return hist, colors


histogram, color = color_histogram(img_df['link'])
print(type(histogram))
