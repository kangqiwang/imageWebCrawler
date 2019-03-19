import cv2
import urllib.request
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path
from elasticsearch import Elasticsearch
import json
import sys
from skimage import io


def mathchtest():

    misMatched=[
                {
                  "asin": "B015D4T56W",
                  "state": "NOT_A_MATCH",
                  "user": "outsourceusa18-gmail-com",
                  "timestamp": "2018-11-27T09:58:33.389Z"
                },{
                  "asin": "B015D4T56W",
                  "state": "MATCHED",
                  "user": "outsourceusa18-gmail-com",
                  "timestamp": "2018-11-27T09:58:33.389Z"
        },
        {

                  "asin": "B015D4T56W",
                  "state": "NOT_A_MATCH",
                  "user": "outsourceusa18-gmail-com",
                  "timestamp": "2018-11-27T09:58:33.389Z"

        },
        {
            "asin": "B015D4T566",
            "state": "NOT_A_MATCH",
            "user": "outsourceusa18-gmail-com",
            "timestamp": "2018-11-27T09:58:33.389Z"

        }
              ]
    notNumber=0
    matchedNumber=0
    for i in misMatched:
        if i['asin']=="B015D4T56W":
            if i['state']=='MATCHED':
                matchedNumber+=1
            else:
                notNumber+=1
    number=matchedNumber-notNumber
    print(number)


def url_to_image(url):
    resp=urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    print(image)
    return image

def url_to_image_scikit(url):
    image=io.imread(url)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image
url1 = "https://site.unbeatablesale.com/img177/ritelt232.gif"
url2 = "http://ecx.images-amazon.com/images/I/41UdVukEQKL._SL75_.jpg"
url3="http://ecx.images-amazon.com/images/I/41SFIdLh%2BUL._SL75_.jpg"
url4="https://cdn-tp2.mozu.com/11961-16493/cms/16493/files/bbbc5e8a-81b7-47d5-8963-5b565add1736?max=260&_mzcb=_1528223948210"
image1= url_to_image(url3)
image2=url_to_image(url4)
image3=url_to_image_scikit(url3)
image4=url_to_image_scikit(url4)
height=np.size(image3,0)
width = np.size(image3,1)
height1=np.size(image4,0)
width1 = np.size(image4,1)
image3=cv2.resize(image3,(width1,height1))
cv2.imshow("Image1",image3)
cv2.imshow("Image2",image4)


cv2.waitKey(0)


