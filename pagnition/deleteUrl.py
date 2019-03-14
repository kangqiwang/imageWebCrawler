import requests
from requests_html import HTMLSession
import sys
from urllib.parse import urlparse
import pandas as pd


def deletesomeofthem():
    df = pd.read_csv("pagnition/generateUrl/kmart.csv")
    urltem=[i.replace('http:','https:') for i in df['url'].values.tolist() if i.startswith('http:')]
    urltem = list(dict.fromkeys(urltem))
    inputtmp=['url']
    for i in urltem:
        print(i)
        session = HTMLSession()
        response = session.get(i)
        if response.status_code == 200 and i.startswith('https') and not i.startswith("https://www.kmart.com/en_us"):
            inputtmp.append(i)
    savedf = pd.Series(inputtmp)
    savedf.to_csv("pagnition/generateUrl/kmartDele.csv", index=False)

deletesomeofthem()