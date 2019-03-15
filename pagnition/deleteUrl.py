import requests
from requests_html import HTMLSession
import sys
from urllib.parse import urlparse
import pandas as pd


def deletesomeofthem():
    urltem=[]
    countList=[]
    df = pd.read_csv("pagnition/input/luckyvitamin_com_bulklist.csv",usecols=['Category URL','Product Count'])
    for url, count in zip(df['Category URL'], df['Product Count']):
        if url.startswith('https://www.luckyvitamin.com'):
            urltem.append(url)
            countList.append(count)
    savedf=pd.DataFrame({'Category URL' : urltem,'Product Count' : countList})
    savedf.to_csv("pagnition/output/luckyvitamin_com_bulklist.csv", index=False)
    # urltem=urltem+[i for i in df['Category URL'] if i.startswith('https://www.luckyvitamin.com')]
    # urltem = list(dict.fromkeys(urltem))
    # inputtmp=['url']
    # for i in urltem:
    #     print(i)
    #     # session = HTMLSession()
    #     # response = session.get(i)
    #     if i.startswith("https://www.luckyvitamin.com"):
    #         inputtmp.append(i)
    # savedf = pd.Series(inputtmp)
    # savedf.to_csv("pagnition/output/luckyvitamin_com_bulklist.csv", index=False)

deletesomeofthem()