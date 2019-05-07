import requests
import numpy as np
import re
from xml.etree import ElementTree as ET
import pprint
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
response = requests.get('https://ao.com/sitemaps/CategorySitemap.xml',headers=headers)
with open('pagnition/xmltocsv/tem.xml','wb') as f:
    f.write(response.content)
tree = ET.parse('pagnition/xmltocsv/tem.xml')
root = tree.getroot()
urls=['url']
# for eme in root.iter():
#     print(eme.tag)

for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    urls.append(url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text)
savedf = pd.Series(urls)
savedf.to_csv("pagnition/xmltocsv/temurls.csv", index=False)

