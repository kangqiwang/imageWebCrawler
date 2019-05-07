import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/ao_com.csv",usecols=['url','page','nexturl'])

    tmpList=['url']

    for url, count, nexturl in zip(df['url'],df['page'],df['nexturl']):
        urltmp=''
        numbertmp=0
        if isinstance(nexturl, str):
            nexturl=nexturl.replace('pagesize=12','pagesize=60').replace('page=12','page=60')
            perpageCount = 60
            if count > 4:
                pageNum=int(count*12/perpageCount)+1
                for i in range(pageNum):
                    print(nexturl)
                    urltmp=nexturl.replace('page=60','page='+str(60*i))
                    tmpList.append(urltmp)
            else:
                tmpList.append(nexturl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/ao_com.csv",index=False)

pagnition()