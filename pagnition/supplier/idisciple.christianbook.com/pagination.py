import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/idisciple_christianbook_com.csv",usecols=['url','number'])

    tmpList=['url']
    for url, count in zip(df['url'],df['number']):
        urltmp=''
        numbertmp=0
        # if "categories/" in str(url):
        #     urltmp = url.split("categories/")[0]
        #     numbertmp=url.split("categories/")[1]

        perpageCount=50
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            # if urltmp !='':
            urltmp = url+'&rpp=50&page='+str(i+1)
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/idisciple_christianbook_com.csv",index=False)

pagnition()