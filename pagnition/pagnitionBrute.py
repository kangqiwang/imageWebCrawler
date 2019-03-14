import pandas as pd
import numpy as np
from requests_html import HTMLSession


def pagnition():
    df=pd.read_csv("pagnition/generateUrl/kmartDele.csv",usecols=['url'])


    tmpList=['url']
    for url in df['url']:
        if '&adcell=' in url:
            urltmp=url.split('&adcell=')[0]
            url=urltmp

        # urltmp=''
        # numbertmp=0
        # if "?filter=" in str(url):
        #     urltmp = url.split("?filter=")[0]
        #      # numbertmp=url.split("filter=")[1]
        #
        # perpageCount=96
        # pageNum=int(count/perpageCount)+1
        # if pageNum > 2:
        for i in range(21):
            tmpurl = url +'&pageNum='+str(i+1)
            session = HTMLSession()
            response = session.get(tmpurl)
            if response.status_code == 200:
                tmpList.append(tmpurl)
            else:
                continue
        print(tmpurl)
    savedf=pd.Series(tmpList)
    savedf.to_csv("pagnition/output/kamrtDeled.csv",index=False)


pagnition()