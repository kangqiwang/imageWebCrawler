import cv2
import urllib
import numpy as np
# import pandas as pd

# csv_file = pd.read_csv('opportunity.csv')
# print(csv_file[,6])

def url_to_image(url):
    resp=urllib.urlopen(url)
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
sift=cv2.SIFT()

#find the keypoints and descriptors with SIFT
kp1, des1 =sift.detectAndCompute(image1,None)
kp2, des2 =sift.detectAndCompute(image2,None)

# BFMatcher with default params
bf =cv2.BFMatcher()
matches= bf.knnMatch(des1,des2,k=2)

# apply ratio test
good =[]
for m,n in matches:
    if(m.distance < 0.75*n.distance):
        good.append([m])

# cv.drawMatchesKnn expects list of lists as matches

img3= cv2.drawMatchesKnn(image1,kp1,image2,kp2,good,flags=2)

plt.imshow(img3),plt.show()


# kp1,des1 = sift.detectAndCompute(image1,None)
# kp2,des2 = sift.detectAndCompute(image2,None)
# bf = cv2.BFMatcher()
# matches=bf.match(des1,des2)
# matches=sorted(matches, key=lambda val: val.distance)
# img3= drawMatches(img1,kp1,img2,kp2,matches[:25])

# #img1= cv2.drawKeypoints(image1,kp,outImage=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# cv2.imshow("Image1", img3)
# #cv2.imshow("Image2", image2)
# cv2.waitKey(0)
# cv2.destoryWindow('Matched Features')