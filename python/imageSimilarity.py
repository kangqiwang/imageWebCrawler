import cv2
import urllib
import numpy as np

def url_to_image(url):
    resp=urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

url1 = "http://ecx.images-amazon.com/images/I/416aMYxRqVL._SL220_.jpg"
url2 = "https://d8mkdcmng3.imgix.net/750c/pc-and-video-games-accessories-ps4-ps4-controllers-nacon-revolution-pro-controller-v2-rig-limited-edition-for-ps4.jpg?bg=0FFF&fit=fill&h=176&q=90&w=176&s=3eb6421e9dd11be175031ef57d840f7a"

image1 =url_to_image(url1)
image2 =url_to_image(url2)
cv2.imshow("Image", image)
cv2.waitKey(0)