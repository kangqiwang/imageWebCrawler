import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/houzz_co.uk.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        # if "categories/" in str(url):
        #     urltmp = url.split("categories/")[0]
        #     numbertmp=url.split("categories/")[1]

        perpageCount=90
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            # if urltmp !='':
            urltmp = url+'?fi='+str(i*perpageCount)
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/houzz_co.uk.csv",index=False)

pagnition()