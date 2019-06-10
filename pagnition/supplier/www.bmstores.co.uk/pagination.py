import pandas as pd
import numpy as np
import requests
import re



def pagnition():
    df=pd.read_csv("pagnition/input/bmstores_co.csv",usecols=['url'])

    tmpList=['url']
    x=0
    for url in df['url']:
        m = re.search(r'\d+$',url)
        
        if "/products/" in url and m is not None:
            x=+1
        elif "/products/" in url and m is None:
            tmpList.append(url)
        elif "/brand/" in url:
            tmpList.append(url+'/sort/datehigh/items/60')
        elif "/offers/category/" in url or "/managers-specials/category/" in url:
            tmpList.append(url)
        # for i in range(pageNum):
        #     # if urltmp !='':
        #     urltmp = url+'&p='+str(i)
        #     # else:
        #     # tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
        #     print(urltmp)
        #     tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/bmstores_co.csv",index=False)

pagnition()