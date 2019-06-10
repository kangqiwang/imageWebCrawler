import pandas as pd
import numpy as np
import requests



def pagnition():
    # df=pd.read_csv("pagnition/input/kohls_com.csv",usecols=['Category URL','Product Count'])
    # print(df)
    tmpList=['url']
    # for url, count in zip(df['Category URL'],df['Product Count']):
    url ="https://www.kohls.com/catalog.jsp?CN=0&S=1&PPP=120&pfm=browse"
    count = 194977
    urltmp=''
    numbertmp=0
    perpageCount=120
    pageNum=int(count/perpageCount)+1
    for i in range(pageNum):
        # if urltmp !='':
        urltmp = url+'&WS='+str(i*perpageCount)
        # else:
        #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
        print(urltmp)
        tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/kohls_com.csv",index=False)

pagnition()