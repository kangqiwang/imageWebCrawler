import cv2
import urllib.request
import numpy as np
from matplotlib import pyplot as plt

# import pandas as pd

# csv_file = pd.read_csv('opportunity.csv')
# print(csv_file[,6])

def url_to_image(url):
    resp=urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

url1 = "http://ecx.images-amazon.com/images/I/416aMYxRqVL._SL220_.jpg"
url2 = "https://d8mkdcmng3.imgix.net/750c/pc-and-video-games-accessories-ps4-ps4-controllers-nacon-revolution-pro-controller-v2-rig-limited-edition-for-ps4.jpg?bg=0FFF&fit=fill&h=176&q=90&w=176&s=3eb6421e9dd11be175031ef57d840f7a"

image1 =url_to_image(url1)
image2 =url_to_image(url2)

image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

# Initiate SIFT detector
orb=cv2.ORB_create()

#find the keypoints and descriptors with SIFT
kp1, des1 =orb.detectAndCompute(image1,None)
kp2, des2 =orb.detectAndCompute(image2,None)


# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
img3 = cv2.drawMatches(image1,kp1,image2,kp2,matches,None, flags=2)
plt.imshow(img3),plt.show()
