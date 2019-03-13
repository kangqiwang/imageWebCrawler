import pandas as pd
import numpy as np


def pagnition():
    df=pd.read_csv("pagnition/input/resultus.csv",usecols=['stateDeltaAsin'])


    tmpList=[]
    for url in df['stateDeltaAsin']:
        # urltmp=''
        # numbertmp=0
        if str(url) == 'nan':
            tmpList.append('NULL')
        else:
            tmpList.append('https://www.amazon.com/dp/' + str(url))
        #     urltmp = url.split("Nrpp=")[0]
        #     numbertmp=url.split("Nrpp=")[1]

    #     perpageCount=120
    #     pageNum=int(count/perpageCount)+1
    #     for i in range(pageNum):
    #         tmpurl = url+'&PPP='+str(120)+'&WS='+str((i+1)*120)
    #         print(tmpurl)
    #         tmpList.append(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/resultus.csv")



pagnition()