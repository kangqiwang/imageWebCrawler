import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/dunelm_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        perpageCount=18
        pageNum=int(int(count)/perpageCount)+1
        for i in range(pageNum):
            tmpurl = url+'?page='+str(i+1)
            print(tmpurl)
            tmpList.append(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/dunelm_com.csv",index=False)

pagnition()