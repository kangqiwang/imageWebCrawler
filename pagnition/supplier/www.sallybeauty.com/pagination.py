import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/sallybeauty_com.csv",usecols=['nexturl','page','url'])

    tmpList=['url']
    urls=df['url']
    dictionary=dict(zip(df['nexturl'], df['page']))
    for value in dictionary:
        urltmp=''
        print(dictionary[value])
        if type(value)!=float:
            print(type(value))
            perpageCount = 12
            pageNum = int(dictionary[value] / perpageCount) + 1
            for i in range(pageNum):
                urltmp=value.replace("start=12","start="+str(i*12))
                tmpList.append(urltmp)

    savedf=pd.Series(urls)
    savedf.to_csv("pagnition/output/sallybeauty_com.csv",index=False)
    # for url, count in zip(df['nexturl'],df['page']):
    #     urltmp=''
    #     numbertmp=0
    #     # if "categories/" in str(url):
    #     #     urltmp = url.split("categories/")[0]
    #     #     numbertmp=url.split("categories/")[1]
    #
    #     perpageCount=40
    #     pageNum=int(count/perpageCount)+1
    #     for i in range(pageNum):
    #         # if urltmp !='':
    #         urltmp = url+'?q=%3Arelevance&page='+str(i)
    #         # else:
    #         #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
    #         print(urltmp)
    #         tmpList.append(urltmp)
    # savedf=pd.Series(tmpList)
    # savedf.to_csv("pagnition/output/hobbylobby.csv",index=False)

pagnition()