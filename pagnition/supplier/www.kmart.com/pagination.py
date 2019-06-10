import pandas as pd
import numpy as np
import requests
import re


def pagnition():
    df=pd.read_csv("pagnition/input/kamrt_com.csv",usecols=['url','page'])

    tmpList=['url']
    for url,number in zip(df['url'],df['page']):
        urltmp=''
        numbertmp=0

        # if "categories/" in str(url):
        #     urltmp = url.split("categories/")[0]
        #     numbertmp=url.split("categories/")[1]
        perpageCount=50
        pageNum=int(int(number)/perpageCount)+1
        for i in range(pageNum):
            tmpurl = url+'?pageNum='+str(i+1)
            print(tmpurl)
            tmpList.append(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/kamrt_com.csv",index=False)

pagnition()