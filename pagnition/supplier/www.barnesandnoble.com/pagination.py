import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/barnesandnoble_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        perpageCount=40
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            # if urltmp !='':
            if i!=0:
                urltmp = url+'?Nrpp=40&page='+str(i)
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
                print(urltmp)
                tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/barnesandnoble_com.csv",index=False)

pagnition()