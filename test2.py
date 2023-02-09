import urllib.request
import numpy as np
import cv2

url = "https://cdn.pixabay.com/photo/2017/10/10/07/48/hills-2836301__480.jpg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as url:
    s = url.read()

arr = np.asarray(bytearray(s), dtype=np.uint8)
img = cv2.imdecode(arr, -1)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

