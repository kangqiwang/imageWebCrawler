import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/christianbook_com.csv",usecols=['Category URL','Product Count','Category Name'])

    tmpList=['url']
    for url, count, category in zip(df['Category URL'],df['Product Count'],df['Category Name']):
        urltmp=''
        numbertmp=0
        # if "categories/" in str(url):
        #     urltmp = url.split("categories/")[0]
        #     numbertmp=url.split("categories/")[1]
        perpageCount=50
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            if 'Download' in category or 'eBook' in category:
                break
            # if urltmp !='':
            urltmp = url+'&page='+str(i)+'&rpp=50'
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/christianbook_com.csv",index=False)

pagnition()