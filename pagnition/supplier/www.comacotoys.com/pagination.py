import pandas as pd
import numpy as np
import requests



def pagnition():
    # df=pd.read_csv("pagnition/input/costco_co.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for i in range(33):
        tmpurl = 'http://www.comacotoys.com/Products_B2-2.aspx?page='+str(i+1)
        print(tmpurl)
        tmpList.append(tmpurl)
    # for url, count in zip(df['Category URL'],df['Product Count']):
    #     urltmp=''
    #     numbertmp=0
    #     perpageCount=100
    #     pageNum=int(int(count)/perpageCount)+1
    #     for i in range(pageNum):

    #         # if urltmp !='':
    #         tmpurl = url+'?page='+str(i)+'&pageSize=24'
    #         # else:
    #         #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
    #         print(tmpurl)
    #         tmpList.append(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/Comaco_Toys.csv",index=False)

pagnition()