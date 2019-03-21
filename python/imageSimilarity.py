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


def open_csv():
    similarity_result = []
    supplierUrl = []
    amaonUrl = []
    sizeofDescrip = []
    distance = []
    outsource = []
    color = []
    filedescripter = []
    nameS=[]
    nameA=[]
    es= Elasticsearch([{'host':'localhost','port':9999}])
    res = es.search(index="us-supplier-default-010", body={"size": 100,"sort": [{"updated": {"order": "desc"}}],"query": {"bool": {"must": [{"match": {"state": "PRE_MATCHED"}}]}}})
    for element in res['hits']['hits']:
        try:
            misMatched = element['_source']['stateDelta']
        except:
            misMatched=0
        try:
            image2_url = element['_source']['image']

            image1_url = element['_source']['asin']

            nameSupplier=element['_source']['name']
            matchesDistance = element['_source']['matchDistance']
            image1_url = es.search(index="us-amazon", body={"sort": [{"created": {"order": "desc"}}], "query": {
                "bool": {"must": [{"match": {"asin": image1_url}}]}}})['hits']['hits'][0]['_source']
            nameAmazon=image1_url['amazonName']
            image1_url=image1_url['amazonImage']
            print(image1_url)
        except Exception as e:
            print('no data  ',e)
            image1_url='null'
            image2_url='null'
        try:
            image1 = url_to_image(image1_url)
            image2 = url_to_image(image2_url)

            # print(matchesDistance)




        except Exception as e:
            print(' connot covert url to image ',e)
            image1 = None
            image2 = None
            matchesDistance = -1

        if ((image1 is not None) and (image2 is not None) and (len(image1) != 0) and (len(image2) != 0)):

            height = np.size(image1, 0)
            width = np.size(image1, 1)
            image2 = cv2.resize(image2, (width, height))
            # image2, sketch_color = cv2.pencilSketch(image2, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
            # image1, sketch_color = cv2.pencilSketch(image1, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
            try:
                distanceColor = colorSimilarity(image1, image2)
                print(distanceColor)
            except:
                distanceColor=-1
            try:

                # print(distanceColor)
                image2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
                image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
                # Initiate ORB detector
                orb = cv2.ORB_create()
                # find the keypoints and descriptors with orb
                kp1, des1 = orb.detectAndCompute(image1, None)
                kp2, des2 = orb.detectAndCompute(image2, None)
                # Sort them in the order of their distance.
                bf = cv2.BFMatcher()
                matches = bf.knnMatch(des1, des2, k=2)
                similarity_result.append(similarity(matches, kp2))
            except:
                similarity_result.append('ERROR')
            # Apply ratio test
            # img3 = cv2.drawMatchesKnn(image1,kp1,image2,kp2,good,None,flags=2)
            # plt.imshow(img3),plt.show()
        else:
            similarity_result.append('None')
            des2=0
            des1=0
            distanceColor=0

        misMatched=0
        number=0
        if misMatched !=0:
            notNumber = 0
            matchedNumber = 0
            for i in misMatched:
                if i['asin'] == misMatched[0]['asin']:
                    if i['state'] == 'MATCHED':
                        matchedNumber += 1
                    else:
                        notNumber += 1
            number = matchedNumber - notNumber
        dict={
            image1_url:des1,
            image2_url:des2
        }
        filedescripter.append(dict)
        nameS.append(nameSupplier)
        nameA.append(nameAmazon)
        supplierUrl.append(image1_url)
        amaonUrl.append(image2_url)
        distance.append(matchesDistance)
        outsource.append(number)
        color.append(distanceColor)
        # sizeofDescrip.append(str(sys.getsizeof(des1)) +'  '+str(sys.getsizeof(des2)))

    result=pd.DataFrame({
        'supplierUrl':supplierUrl,
        'amaonUrl' : amaonUrl,
        'size'  : sizeofDescrip,
        'similarity_result' : similarity_result,
        'distance' : distance,
        'outsource':outsource,
        'colorSimilarity':color,
        'nameSupplier': nameS,
        'nameAmazon' : nameA
    },
        columns=['amaonUrl','supplierUrl','similarity_result','distance','outsource','colorSimilarity','nameSupplier','nameAmazon'])
    # filedescrip=pd.Series(filedescripter)
    # filedescrip.to_csv('descripter.csv')
    # df['similarity.result'] = similarity_result
    result.to_csv('test_data1_and_NOT_MATCH.csv')

    # my_file=Path("python/opportunity.csv")
    # if my_file.exists():
    #     df=pd.read_csv('python/opportunity.csv', usecols=['supplier.image','amazon.image'])
    #     return df
    # else:
    #     print('THERE ARE ERR CAN NOT FOUND FILES')
    #     return 0

def url_to_image_scikit(url):
    image=io.imread(url)
    # image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image


def url_to_image(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36'})
    resp=urllib.request.urlopen(req,timeout=10)
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


        # for m,n in matches:
        #     if m.distance < 0.75*n.distance:
        #         good.append([m])
        percent=len(good)
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
    df.to_csv('result_NOT_MATCHED.csv',columns=['supplier.image','amazon.image','similarity.result'],index=0, header=1)

def colorSimilarity(imag1,imag2):

    imag1=cv2.cvtColor(imag1,cv2.COLOR_BGR2RGB)
    imag2=cv2.cvtColor(imag2,cv2.COLOR_BGR2RGB)
    hist1 = cv2.calcHist(imag1, [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist1 = cv2.normalize(hist1, hist1).flatten()
    hist2 = cv2.calcHist(imag2, [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist2 = cv2.normalize(hist2, hist2).flatten()
    d = cv2.compareHist(hist2, hist1, cv2.HISTCMP_BHATTACHARYYA)
    return d



if __name__== "__main__":
    open_csv()

