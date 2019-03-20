import urllib.request
import cv2
import numpy as np
def url_to_image(url):
    req=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36'})
    resp=urllib.request.urlopen(req,timeout=10)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
img2=url_to_image('https://images10.newegg.com/NeweggImage/ProductImageCompressAll300/V197_1_20180316533953527.jpg')
img1=url_to_image('http://ecx.images-amazon.com/images/I/41NruI-zYPL._SL75_.jpg')

height = np.size(img1, 0)
width = np.size(img1, 1)
img2 = cv2.resize(img2, (width, height))

cv2.imshow('img_supplier',img2)
cv2.imshow('imag_amazon',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

