import pandas as pd
import numpy as np

df=pd.read_csv("pagnition/input/pagnitionc21store.csv",usecols=['Category.URL','Product.Count'])

savedf= []
for url, count in zip(df['Category.URL'],df['Product.Count']):
    if "&selectedUrl=" in str(url):
        url = url.split("&selectedUrl=")[0]
    pageNum=int(count/48)+1
    for i in range(pageNum):
        urltmp=url
        urltmp.replace('start=48','start='+str(i*48))
        savedf.append(urltmp)
print(savedf)

