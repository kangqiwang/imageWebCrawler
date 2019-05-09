import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/bedbathandbeyond_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0

        perpageCount=96
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            urltmp = url+str(i+1)+'-96'
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/bedbathandbeyond_com.csv",index=False)

pagnition()