import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/acehardware_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        perpageCount=90
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            urltmp = url+'?pageSize=90&startIndex='+str(i*perpageCount)
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/acehardware_com.csv",index=False)

pagnition()