import requests
import numpy as np
import re
from xml.etree import ElementTree as ET
import pprint
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

# response = requests.get('https://www.tkmaxx.com/medias/Category-en-GBP-7258143749271186642.xml?context=bWFzdGVyfHJvb3R8MTkzODQyfHRleHQveG1sfGgzMi9oYjcvMTA1OTY1NzQxMzQzMDIueG1sfGJlOWMyODZlY2ZhNTVlYThhYWFmYzgxNzJhNzI3NDRlZTg4MGY4MTE1YWFjMzM4NTE1MGNhNGE5NTEzNzllYWU',headers=headers)
# with open('pagnition/xmltocsv/tem.xml','wb') as f:
#     f.write(response.content)
tree = ET.parse('pagnition/xmltocsv/tem.xml')
root = tree.getroot()
urls=['url']
# for eme in root.iter():
#     print(eme.tag)

for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    urls.append(url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text)
if len(urls)==1:
    for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap'):
        urls.append(url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text)
    for i in urls:
        if i != 'url':
            response=requests.get(i)
            tree =ET.parse(response.content)
            root = tree.getroot()
        else:
            continue
        for key in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            urls.append(key.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text)




savedf = pd.Series(urls)
savedf.to_csv("pagnition/xmltocsv/temurls1.csv", index=False)

