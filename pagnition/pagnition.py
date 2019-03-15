import pandas as pd
import numpy as np
import requests


def pagnition():
    df=pd.read_csv("pagnition/input/marvel_com_bulklist.csv",usecols=['Category URL','Product Count'])


    tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        urltmp=''
        # numbertmp=0
        # if "?filter=" in str(url):
        #     urltmp = url.split("?filter=")[0]
        #      # numbertmp=url.split("filter=")[1]
        #
        perpageCount=30
        pageNum=int(count/perpageCount)+1
        # if pageNum > 2:
        for i in range(pageNum):
            if urltmp !='':
                tmpurl = urltmp+'?sortBy=top_sellers&page='+str(i+1)
            else:
                tmpurl = url +'#callURL=%252Fmarvel%252Fstore%252FDSIProcessWidget%253FcatalogId%253D10002%2526langId%253D-1%2526storeId%253D50051%2526templateId%253DWidth-3_4-ProductList%2526widgetName%253Ditems_listing%2526widgetObjId%253DobjItemsListing%2526sectionName%253DRight%2526initialN%253D1001152%2526navNum%253D96%2526pageCmdName%253DproductListPage%2526numDim%253D3%2526N%253D1001152%2526zoneName%253DDisneyNavigationPageZone%2526Nao%253D'+str((i+1)*96)+'&sort=sortProductsMostPopular'
                tmpList.append(tmpurl)

    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/marvel_com_bulklist.csv",index=False)

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
    df=pd.read_csv("pagnition/input/surfdome_com_bulklist.csv",usecols=['Category URL'])
    tmpList=[]
    for url in df['Category URL']:
        print(url)
        response=requests.get(url,allow_redirects=False)
        if response.status_code == 301:

            tmpList.append(response.headers['Location'])
        elif response.status_code == 404:
            tmpList.append('Null')
        else:
            tmpList.append(url)
    savedf = pd.Series(tmpList)
    savedf.to_csv("pagnition/output/surfdome_com_bulklist.csv", index=False)

pagnition()