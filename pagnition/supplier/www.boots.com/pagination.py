import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/boots_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        perpageCount=24
        pageNum=int(int(count)/perpageCount)+1
        for i in range(pageNum):

            # if urltmp !='':
            tmpurl = url+'#facet:&productBeginIndex:'+str(24*(i+1))+'&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&'
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(tmpurl)
            tmpList.append(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/boots_com.csv",index=False)

pagnition()