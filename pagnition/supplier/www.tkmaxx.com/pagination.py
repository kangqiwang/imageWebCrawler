import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/tkmax.csv",usecols=['url'])

    tmpList=['url']
    for url in df['url']:
        tmpList.append(url+'?q=&sort=percentSaving-desc&facets=stockLevelStatus:inStock&page=10')
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/tkmax_now.csv",index=False)

pagnition()