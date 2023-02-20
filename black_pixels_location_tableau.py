import pandas as pd
import numpy as np
import urllib.request
import cv2

df = pd.DataFrame(_arg1)
imgs = df["link"]

points_data = pd.DataFrame()

for urls in imgs:
    url_response = urllib.request.Request(urls, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(url_response) as url:
        s = url.read()

    img = cv2.imdecode(np.asarray(bytearray(s), dtype=np.uint8), -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    blurred = cv2.Canny(blurred, 1, 1)
    blurred[np.where(blurred != 0)] = 100
    blurred[np.where(blurred == 0)] = 255

    indices = np.where(blurred != 255)
    coordinates = zip(indices[0], indices[1])
    coordinates = list(coordinates)
    coordinates = pd.DataFrame(coordinates, columns=['x', 'y'])
    coordinates['url'] = urls

    points_data = points_data.append(coordinates)


return points_data.to_dict(orient="list")