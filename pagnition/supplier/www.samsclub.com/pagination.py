import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/samsclub_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        # if "categories/" in str(url):
        #     urltmp = url.split("categories/")[0]
        #     numbertmp=url.split("categories/")[1]

        perpageCount=48
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            if i ==0:
                urltmp=url
            else:
                urltmp = url+'?limit=48&offset='+str((i+1)*perpageCount)
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/samsclub_com.csv",index=False)

pagnition()