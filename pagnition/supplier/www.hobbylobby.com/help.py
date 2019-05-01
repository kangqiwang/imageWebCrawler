import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/output/hobbylobby.csv",usecols=['url'])

    tmpList=[]
    for url in df['url']:
        if url=="https://www.hobbylobby.com/Home-Decor-Frames/Home-Decor-Weekly-Ad/c/dc-home-accents-weekly-ad?q=%3Arelevance&page=0":
            for i in range(int(4583/40)+1):
                tmpList.append("https://www.hobbylobby.com/Home-Decor-Frames/Home-Decor-Weekly-Ad/c/dc-home-accents-weekly-ad?q=%3Arelevance&page="+str(i))
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/hobbylobby1.csv",index=False)
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