import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/365games_co_new.csv",usecols=['url'])

    tmpList=['url']
    for url in df['url']:
        url = url+'page-1'
        tmpList.append(url)
        # urltmp=''
        # numbertmp=0
        # perpageCount=18
        # pageNum=int(int(count)/perpageCount)+1
        # for i in range(pageNum):
        #     tmpurl = url+'?page='+str(i+1)
        #     print(tmpurl)
        #     tmpList.append(tmpurl)
        
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/input/365games_co.csv",index=False)

pagnition()