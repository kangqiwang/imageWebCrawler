import requests
from requests_html import HTMLSession
import sys
from urllib.parse import urlparse
import pandas as pd


def getUrl():
    url = 'https://'+sys.argv[1]
    session = HTMLSession()
    response=session.get(url)

    for i in response.html.absolute_links:
        try:
            domain = urlparse(i).hostname
        except:
            domain= ''
        if domain == urlparse(url).hostname:
            urltem.append(i)

    urltem=urltem+[i.replace('http:','https:') for i in urltem if i.startswith('http:')]
    print(urltem)
    urltem=list(dict.fromkeys(urltem))
    print('finish the one       '+ str(len(urltem)))
    urldeep1=[]
    for i in urltem:
        if not i.startswith('//'):
            response = session.get(i)
            for j in response.html.absolute_links:
                try:
                    domain = urlparse(j).hostname
                except:
                    domain = ''
                if domain == urlparse(url).hostname:
                    urldeep1.append(j)


    urldeep1= urldeep1+[i.replace('http:','https:') for i in urldeep1 if i.startswith('http:')]
    urldeep1=list(dict.fromkeys(urldeep1))
    print('finish the two   ' + str(len(urldeep1)))

    urldeep2=[]
    for i in urldeep1:
        if not i.startswith('//'):

            response = session.get(i)
            for j in response.html.absolute_links:
                try:
                    domain = urlparse(j).hostname
                except:
                    domain = ''
                if domain == urlparse(url).hostname:
                    urldeep2.append(j)

    urldeep2= urldeep2+[i.replace('http:','https:') for i in urldeep2 if i.startswith('http:')]
    urldeep2=list(dict.fromkeys(urldeep2))
    print('finish the three     '+ str(len(urldeep2)))

    savedf = pd.Series(list(dict.fromkeys(urltem + urldeep1 + urldeep2)))
    savedf.to_csv("pagnition/generateUrl/mattel.csv", index=False)


getUrl()




