import pandas as pd
import numpy as np
import requests


def pagnition():
    # first category first page and second page
    first1Url="https://www.overtons.com/outdoor-gear/outdoor-lighting"
    second1Url = "https://www.overtons.com/outdoor-gear/outdoor-lighting?sz=21&start=21"
    third1Url = "https://www.overtons.com/outdoor-gear/outdoor-lighting?sz=21&start=42"

    # second category first page and second page

    first2Url = "https://www.overtons.com/anchoring-docking/anchoring"
    second2Url = "https://www.overtons.com/anchoring-docking/anchoring?sz=21&start=21"
    third2Url = "https://www.overtons.com/anchoring-docking/anchoring?sz=21&start=42"


    df=pd.read_csv("pagnition/input/overtons_com_bulklist.csv",usecols=['Category URL','Product Count'])



    # tmpList=['url']
    for url, count in zip(df['Category URL'],df['Product Count']):
        print(url)

        for i in second1Url.split(first1Url):

            if i !='':
                second1Url.index(i)
                url+i
        # print(second1Url-first1Url)
        # print(third1Url)
        # print(first2Url)
        # print(second2Url)
        # print(third2Url)
        urltmp=''

        # numbertmp=0
        # if "?filter=" in str(url):
        #     urltmp = url.split("?filter=")[0]
        #      # numbertmp=url.split("filter=")[1]
        #
        # perpageCount=30
        # pageNum=int(count/perpageCount)+1
        # if pageNum > 2:
    #     for i in range(pageNum):
    #         if urltmp !='':
    #             tmpurl = urltmp+'?sortBy=top_sellers&page='+str(i+1)
    #         else:
    #             tmpurl = url +'#callURL=%252Fmarvel%252Fstore%252FDSIProcessWidget%253FcatalogId%253D10002%2526langId%253D-1%2526storeId%253D50051%2526templateId%253DWidth-3_4-ProductList%2526widgetName%253Ditems_listing%2526widgetObjId%253DobjItemsListing%2526sectionName%253DRight%2526initialN%253D1001152%2526navNum%253D96%2526pageCmdName%253DproductListPage%2526numDim%253D3%2526N%253D1001152%2526zoneName%253DDisneyNavigationPageZone%2526Nao%253D'+str((i+1)*96)+'&sort=sortProductsMostPopular'
    #             tmpList.append(tmpurl)
    #
    # savedf=pd.Series(tmpList)
    # savedf.to_csv("pagnition/output/marvel_com_bulklist.csv",index=False)

# print('Please input the two different category first page url and second page url')
pagnition()