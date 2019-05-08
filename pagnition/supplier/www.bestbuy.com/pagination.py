import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/bestbuy_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0

        perpageCount=24
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            if "cp=1" in str(url):
                urltmp = url.replace('cp=1', 'cp=' + str(i+1))
            else:
                urltmp=url+'&cp='+str(i+1)
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/bestbuy_com.csv",index=False)

pagnition()