import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/katom_com.csv",usecols=['categoryname","domain","item","nexturl","page","pageType","url'])

    tmpList=['url']
    for url in zip(df['categoryname","domain","item","nexturl","page","pageType","url']):
        urltmp=''
        numbertmp=0
        if "," in str(url[-1]):
            numbertmp = url[-1].split(",")[-3]
            urltmp=url[-1].split("\",\"")[-1]
        print(numbertmp)
        print(urltmp)
        perpageCount=75
        pageNum=int(int(numbertmp)/perpageCount)+1
        for i in range(pageNum):
            # if urltmp !='':
            tmpurl = urltmp+'?per_page=75&page='+str(i+1)
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(tmpurl)
            tmpList.append(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/katom_com.csv",index=False)

pagnition()