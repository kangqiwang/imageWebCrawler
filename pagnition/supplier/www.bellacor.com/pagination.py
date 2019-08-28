import pandas as pd
import numpy as np
import requests



def pagnition():
    # df=pd.read_csv("pagnition/input/tkmax.csv",usecols=['url'])

    # tmpList=['url']
    # for url in df['url']:
    pageNum=0
    url="https://www.bellacor.com/all-sales/page/"+pageNum+".htm?Erp=96"
    savedf=pd.Series(url)
    savedf.to_csv("pagnition/output/tkmax_now.csv",index=False)

pagnition()