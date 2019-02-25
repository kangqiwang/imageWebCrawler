import cv2
import urllib.request
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def open_csv():
    df=pd.read_csv('python/opportunity.csv', usecols=['supplier.image','amazon.image'])
    return df

def url_to_image(url):
    resp=urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def similarity(matches,kp2):
    good = [m for (m, n) in matches if m.distance <0.75*n.distance]
    percent=0
    # for m,n in matches:
    #     if m.distance < 0.75*n.distance:
    #         good.append([m])
    percent=len(good)/len(matches)
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
    main()

