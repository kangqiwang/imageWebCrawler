import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/base_com.csv",usecols=['url','page'])

    tmpList=['url']
    for url, count in zip(df['url'],df['page']):
        urltmp=''
        numbertmp=0
        # if "categories/" in str(url):
        #     urltmp = url.split("categories/")[0]
        #     numbertmp=url.split("categories/")[1]

        perpageCount=24
        if count:
            pageNum=int(count)+1
            for i in range(pageNum):
                if 'filter=' in url:
                    urltmp = url+'&pgCMG735-2='+str(i+1)
                elif 'dropdownmenu' in url:
                    urltmp = url + '&pg100007-0=' + str(i + 1)
                else:
                    urltmp = url + '?pgCMG735-2=' + str(i + 1)
                # tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
                print(urltmp)
                tmpList.append(urltmp)
        else:
            tmpList.append(url)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/base_com.csv",index=False)

pagnition()