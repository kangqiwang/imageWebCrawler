import pandas as pd
import numpy as np
import requests
import re


def pagnition():
    df=pd.read_csv("pagnition/input/walgreens_com.csv",usecols=['Category URL','Product Count'])

    tmpList=['url']
    template='https://www.walgreens.com/store/store/category/productlist.jsp?Erp=72&No=PageNumber&N=Cnumber&Eon=Cnumber'
    for url, count in zip(df['Category URL'], df['Product Count']):
        tmpurl=''
        urltmp=re.findall('(N=|ID=)([\d-]*)',url)
        if urltmp:
            urltmp[0]=list(urltmp[0])
            if urltmp[0][0]=='ID=':
                # urltmp[0][1]=urltmp[0][1]
                urltmp[0][1]=urltmp[0][1][:-1]
            else:
                urltmp[0][1]=urltmp[0][1].replace('-','+')
        perpageCount = 72
        pageNum = int(count / perpageCount) + 1
        for i in range(pageNum):
            if(urltmp):
                tmpurl=template.replace('Cnumber',urltmp[0][1]).replace('PageNumber',str(i*perpageCount))
                tmpList.append(tmpurl)
    savedf = pd.Series(tmpList)
    savedf.to_csv("pagnition/output/walgreens_com.csv", index=False)

pagnition()