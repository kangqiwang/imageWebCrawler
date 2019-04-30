import csv
import json
import pandas as pd
import sys, getopt, pprint
from urllib.parse import urlparse
from requests_html import HTMLSession
import requests
from pymongo import MongoClient
#CSV to JSON Conversion

# print(data)
url ="https://www.bbc.co.uk"
session = HTMLSession()
response = session.get(url)
print(response.html)
urltem = []
for i in response.html.absolute_links:
    try:
        domain = urlparse(i).hostname
    except:
        domain = ''
    if domain == urlparse(url).hostname:
        urltem.append(i)
print(urltem)
# mongo_client=MongoClient()
# db=mongo_client.october_mug_talk
# db.segment.drop()
# header= [ "S No", "Instrument Name", "Buy Price", "Buy Quantity", "Sell Price", "Sell Quantity", "Last Traded Price", "Total Traded Quantity", "Average Traded Price", "Open Price", "High Price", "Low Price", "Close Price", "V" ,"Time"]
#
# for each in reader:
#     row={}
#     for field in header:
#         row[field]=each[field]
#
#     db.segment.insert(row)
