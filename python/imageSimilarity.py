import cv2
import urllib.request
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path
from elasticsearch import Elasticsearch
import json
import sys

def open_csv():
    similarity_result=[]
    supplierUrl=[]
    amaonUrl=[]
    sizeofDescrip=[]
    es= Elasticsearch([{'host':'localhost','port':9999}])
    res = es.search(index="us-supplier-default-010", body={"size": 1000,"query": {"bool": {"must": [{"match": {"state": "PRE_MATCHED"}}]}}})
    # print(res['hits']['hits'])
    for element in res['hits']['hits']:

        try:
            print(type(element))
            print(element)
            image1_url=element['_source']['image']
            print(image1_url)
            image2_url=element['_source']['asin']
            print(image2_url)

            image2_url=es.search(index="us-amazon", body={"sort": [{"updated": {"order": "desc"}}],"query": {"bool": {"must": [{"match": {"asin": image2_url}}]}}})['hits']['hits'][0]['_source']['amazonImage']
            print(image2_url)
            image1 = url_to_image(image1_url)
            image2 = url_to_image(image2_url)
        except:
            print('error 404')
            image1 = None
            image2 = None
        # print('image1 this is:          ',image2)
        # print('image2 this is:          ',image1)
        if ((image1 is not None) and (image2 is not None) and (len(image1) != 0) and (len(image2) != 0)):

            image2, sketch_color = cv2.pencilSketch(image2, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
            image1, sketch_color = cv2.pencilSketch(image1, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
            # Initiate ORB detector
            orb = cv2.ORB_create()
            # find the keypoints and descriptors with SIFT
            kp1, des1 = orb.detectAndCompute(image1, None)
            kp2, des2 = orb.detectAndCompute(image2, None)
            # Sort them in the order of their distance.
            bf = cv2.BFMatcher()
            try:
                matches = bf.knnMatch(des1, des2, k=2)
                similarity_result.append(similarity(matches, kp2))
            except:
                similarity_result.append('None')
            # Apply ratio test
            # img3 = cv2.drawMatchesKnn(image1,kp1,image2,kp2,good,None,flags=2)
            # plt.imshow(img3),plt.show()
        else:
            similarity_result.append('None')
            des1=0
            des2=0
        supplierUrl.append(image1_url)
        amaonUrl.append(image2_url)

        sizeofDescrip.append(str(sys.getsizeof(des1)) +'  '+str(sys.getsizeof(des2)))

    result=pd.DataFrame({
        'supplierUrl':supplierUrl,
        'amaonUrl' : amaonUrl,
        'size'  : sizeofDescrip,
        'similarity_result' : similarity_result},
        columns=['supplierUrl','amaonUrl','size','similarity_result'])
    # df['similarity.result'] = similarity_result
    result.to_csv('result.csv')

    # my_file=Path("python/opportunity.csv")
    # if my_file.exists():
    #     df=pd.read_csv('python/opportunity.csv', usecols=['supplier.image','amazon.image'])
    #     return df
    # else:
    #     print('THERE ARE ERR CAN NOT FOUND FILES')
    #     return 0


def url_to_image(url):
    resp=urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def similarity(matches,kp2):
    # good = [m for (m, n) in matches if m.distance <0.75*n.distance]
    percent=0
    good=[]
    if len(matches) ==0:
        return 0
    else:
        for m,n in matches:
            if m.distance < 0.95*n.distance:
                good.append([m])
        percent=len(good)/len(kp2)

        # for m,n in matches:
        #     if m.distance < 0.75*n.distance:
        #         good.append([m])
        percent=len(good)/len(matches)
        if percent >1:
            percent=0.9
        return percent

def main():
    similarity_result=[]
    df=open_csv()
    for index, row in df.iterrows():
        try:
            image1 = url_to_image(row['supplier.image'])
            image2 = url_to_image(row['amazon.image'])
        except:
            print('error 404')
            image1=None
            image2=None
        # print('image1 this is:          ',image2)
        # print('image2 this is:          ',image1)
        if((image1 is not None) and (image2 is not None) and (len(image1)!=0) and (len(image2)!=0)):
            image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
            image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
            
            # Initiate SIFT detector
            orb=cv2.ORB_create()
            #find the keypoints and descriptors with SIFT
            kp1, des1 =orb.detectAndCompute(image1,None)
            kp2, des2 =orb.detectAndCompute(image2,None)
            # Sort them in the order of their distance.
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1,des2, k=2)

            similarity_result.append(similarity(matches,kp2))
            # Apply ratio test
            # img3 = cv2.drawMatchesKnn(image1,kp1,image2,kp2,good,None,flags=2)
            # plt.imshow(img3),plt.show()
        else:
            similarity_result.append('None')
    df['similarity.result']=similarity_result
    df.to_csv('result.csv',columns=['supplier.image','amazon.image','similarity.result'],index=0, header=1)

if __name__== "__main__":
    open_csv()

