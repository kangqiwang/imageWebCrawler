import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/beautyflash_co.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0

        perpageCount=16
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            # if urltmp !='':
            urltmp = url+'?page='+str(i)
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/beautyflash_co.csv",index=False)

pagnition()