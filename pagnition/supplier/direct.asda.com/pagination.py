import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/direct_asda.csv",usecols=['url'])

    tmpList=['url']
    for url in df['url']:
        if ',default,sc.html' in url:
           tmpList.append(url+'?start=0&sz=500')
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/direct_asda_now.csv",index=False)

pagnition()