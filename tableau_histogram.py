import pandas as pd
import numpy as np
import urllib.request
import cv2

df = pd.DataFrame(_arg1)
imgs = df["link"]


histogram_data = pd.DataFrame()

for urls in imgs:
    url_response = urllib.request.Request(urls, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(url_response) as url:
        s = url.read()

    img = cv2.imdecode(np.asarray(bytearray(s), dtype=np.uint8), -1)

    channels = cv2.split(img)
    colors = ['b', 'g', 'r']

    hist_blue = cv2.calcHist([channels[0]], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([channels[1]], [0], None, [256], [0, 256])
    hist_red = cv2.calcHist([channels[2]], [0], None, [256], [0, 256])
    #colors = colors[0]

    hist_blue = pd.DataFrame(hist_blue)
    hist_blue['url'] = urls
    hist_blue['color'] = 'Blue'
    hist_blue['Bin'] = list(range(len(hist_blue)))

    hist_green = pd.DataFrame(hist_green)
    hist_green['url'] = urls
    hist_green['color'] = 'Green'
    hist_green['Bin'] = list(range(len(hist_green)))

    hist_red = pd.DataFrame(hist_red)
    hist_red['url'] = urls
    hist_red['color'] = 'Red'
    hist_red['Bin'] = list(range(len(hist_red)))


    #histogram_data = histogram_data.append(hist)
    histogram_temp = pd.concat([hist_blue, hist_green, hist_red], ignore_index=True)
    histogram_data = histogram_data.append(histogram_temp)

return histogram_data.to_dict(orient="list")