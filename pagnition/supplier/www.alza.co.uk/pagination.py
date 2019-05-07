import pandas as pd
import numpy as np
import requests

import re

def pagnition():
    df=pd.read_csv("pagnition/input/alza_com.csv",usecols=['page','url'])

    tmpList=['url']
    urls=df['url']
    dictionary=dict(zip(df['url'], df['page']))
    for value in dictionary:
        urltmp=''
        if type(value)==str:
            perpageCount = 24
            pageNum = int(dictionary[value] / perpageCount) + 1
            for i in range(pageNum):
                urltmp=value.replace('.htm','')
                urltmp =urltmp+"-p"+str(i)+'.htm'
                print(urltmp)
                tmpList.append(urltmp)

    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/alza_com.csv",index=False)

pagnition()