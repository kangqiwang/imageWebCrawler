import pandas as pd
import numpy as np
import requests


def pagnition():
    df=pd.read_csv("pagnition/input/homedepot_com_bulklist.csv",usecols=['Category URL','Product Count'])


    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        # numbertmp=0
        # if "?filter=" in str(url):
        #     urltmp = url.split("?filter=")[0]
        #      # numbertmp=url.split("filter=")[1]
        #
        perpageCount=21
        pageNum=int(count/perpageCount)+1
        # if pageNum > 2:
        for i in range(pageNum):
            if urltmp !='':
                tmpurl = urltmp+'?sortBy=top_sellers&page='+str(i+1)
            else:
                tmpurl = url +'?Nao='+str(21*(i+1))+'&Ns=None&storeSelection=2408,2414,2409,2407,2404'
                print(tmpurl)
                tmpList.append(tmpurl)

    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/homedepot_com_bulklist.csv",index=False)

def saveToSourceMogul():
    name = "58593450d2b2122cab550ef3"
    file=0

def downloadCsv():

    url="https://shop.mattel.com/shop/en-us/ms/shop-categories#facet:&productBeginIndex:"
    url2="&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:72&contentPageSize:&"
    tmpList = ['url']
    for i in range(35):
        tmpList.append(url+str(i*72)+url2)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/mattel.csv", index=False)




def getRedirectUrl():
    df=pd.read_csv("pagnition/input/overtons_com_bulklist.csv",usecols=['Category URL','Product Count'])
    tmpList=[]
    for url, count in zip(df['Category URL'],df['Product Count']):
        print(url)
        response=requests.get(url,allow_redirects=False)
        if response.status_code == 301:

            tmpList.append(response.headers['Location'])
        elif response.status_code == 404:
            tmpList.append('Null')
        else:
            tmpList.append(url)
    savedf = pd.Series(tmpList)
    savedf.to_csv("pagnition/output/overtons_com_bulklist.csv", index=False)

pagnition()