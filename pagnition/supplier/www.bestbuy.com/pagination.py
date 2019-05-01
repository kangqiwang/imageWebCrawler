import pandas as pd
import numpy as np
import requests



def pagnition():
    df=pd.read_csv("pagnition/input/bestbuy_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        numbertmp=0
        # if "categories/" in str(url):
        #     urltmp = url.split("categories/")[0]
        #     numbertmp=url.split("categories/")[1]

        perpageCount=24
        pageNum=int(count/perpageCount)+1
        for i in range(pageNum):
            # if urltmp !='': https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=pcmcat296300050018&cp=2&id=pcat17071&iht=n&ks=960&list=y&sc=Global&st=categoryid%24pcmcat296300050018&type=page&usc=All%20Categories
            #                 https://www.bestbuy.com/site/playstation-4-ps4/playstation-4-ps4-video-games/pcmcat296300050018.c?id=pcmcat296300050018
            #                 https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=pcmcat296300050018&cp=4&id=pcat17071&iht=n&ks=960&list=y&sc=Global&st=categoryid%24pcmcat296300050018&type=page&usc=All%20Categories
            #

            urltmp = url+'&cp=2&id=pcat17071&iht=n&ks=960&list=y&sc=Global&st=categoryid%24pcmcat296300050018&type=page&usc=All%20Categories'+str(i)
            # else:
            #     tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
            print(urltmp)
            tmpList.append(urltmp)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/bestbuy_com.csv",index=False)

pagnition()