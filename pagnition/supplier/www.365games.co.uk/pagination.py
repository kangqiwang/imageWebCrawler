import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/365games_co.csv",usecols=['url','product'])

    tmpList=['url','product']
    for url,product in zip(df['url'],df['product']):
        # urltmp=''
        # numbertmp=0
        perpageCount=60
        pageNum=int(int(product)/perpageCount)+1
        for i in range(pageNum):
            tmpurl = url+'/sort-most-popular/page-'+str(i+1)
            print(tmpurl)
            tmpList.append(tmpurl)

    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/365games.csv",index=False)

pagnition()