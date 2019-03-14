import pandas as pd
import numpy as np
import requests


def pagnition():
    df=pd.read_csv("pagnition/input/surfdome_com_bulklist.csv",usecols=['Category URL','Product Count'])


    tmpList=[]
    for url, count in zip(df['Category URL'],df['Product Count']):
        # urltmp=''
        # numbertmp=0
        # if "?filter=" in str(url):
        #     urltmp = url.split("?filter=")[0]
        #      # numbertmp=url.split("filter=")[1]
        #
        perpageCount=96
        pageNum=int(count/perpageCount)+1
        if pageNum > 2:
            for i in range(pageNum):
                # if urltmp !='':
                #tmpurl = urltmp+'?sortBy=top_sellers&page='+str(i+1)
                # else:
                tmpurl = url +'?sortBy=top_sellers&page='+str(i+1)
            tmpList.append(tmpurl)
            print(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/surfdome_com_bulklist.csv",index=False)

def saveToSourceMogul():
    name = "58593450d2b2122cab550ef3"
    file=0

def downloadCsv():
    url="https://www.facebook.com/tr/?id=118020122088261&ev=SubscribedButtonClick&dl=https%3A%2F%2Fwww.tacticalbucket.com%2Fdashboard%2Fget-categories%2Fbjs.com&rl=https%3A%2F%2Fwww.tacticalbucket.com%2Fdashboard%2Fcategories-list%2Fta&if=false&ts=1552561186709&cd[buttonFeatures]=%7B%22classList%22%3A%22btn%20btn-default%20buttons-csv%20buttons-html5%20btn-twitter%22%2C%22destination%22%3A%22https%3A%2F%2Fwww.tacticalbucket.com%2Fdashboard%2Fget-categories%2Fbjs.com%23%22%2C%22id%22%3A%22%22%2C%22imageUrl%22%3Anull%2C%22innerText%22%3A%22Save%20to%20CSV%22%2C%22name%22%3A%22%22%2C%22numChildButtons%22%3A0%2C%22tag%22%3A%22a%22%7D&cd[buttonText]=Save%20to%20CSV&cd[formFeatures]=%5B%5D&cd[pageFeatures]=%7B%22title%22%3A%22Bulk%20Category%20Generator%20-%20Tacticalbucket%22%7D&sw=1600&sh=900&ud[em]=14d446042338234319a31a68acba51ddad6add3388ba4025da102039419ad446&v=2.8.42&r=stable&ec=5&o=30&fbp=fb.1.1549466536441.402472324&it=1552560340435&coo=false&es=automatic&rqm=GET"


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