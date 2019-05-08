import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/target_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    urltemplate= "https://www.target.com/c/-/N-"
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        perpageCount=24
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            urltmp = urltemplate+url+'?Nao='+str(i*perpageCount)
            print(urltmp)
            tmpList.append(urltmp)
            if i>50:
                break
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/target_com.csv",index=False)

pagnition()