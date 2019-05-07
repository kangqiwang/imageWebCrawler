import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/frys_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        perpageCount=100
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            if i !=0:
                urltmp = url+'&pType=pDisplay&resultpage='+str(i)+'&start='+str(i*perpageCount)+'&rows=100'
            else:
                urltmp=url
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/frys_com.csv",index=False)

pagnition()