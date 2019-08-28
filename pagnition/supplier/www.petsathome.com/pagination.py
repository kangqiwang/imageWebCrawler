import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/petsathome_com.csv",usecols=['Category URL","Category Name","First Page","Last Page","Source Domain","Product Count'])

    tmpList=['url']
    for url in df['Category URL","Category Name","First Page","Last Page","Source Domain","Product Count']:
        urltmp=''
        numbertmp=0
        if "\",\"" in str(url):
            urltmp = url.split("\",\"")[0]

            numbertmp=url.split("\",\"")[-1]

        perpageCount=48
        pageNum=int(int(numbertmp)/perpageCount)+1
        for i in range(pageNum):
            # if urltmp !='':
            tmpurl = urltmp+'?currentPage='+str(i+1)+'&pageSize=48&orderBy=1'
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(tmpurl)
            tmpList.append(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/petsathome_com.csv",index=False)

pagnition()