#!/usr/bin/python3

import requests
import json
from pprint import pprint as pp

print('''
        Example:
        Enter Org ID: 573083052582915264
        Enter Network ID: L_573083052582991362
        Enter API_KEY: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0
        ''')


orgId = input("Enter Org ID: ")
if len(orgId) == 0 : orgId = "1097053"

networkId = input("Enter Network ID: ")
if len(networkId) == 0 : networkId = "L_627126248111380187"


API_KEY = input("Enter API_KEY: " )
if len(API_KEY) == 0 : API_KEY = "40bfc95138a521bffc6691b2ee0be63b1d0da812"

url_0 = f"https://api.meraki.com/api/v1/organizations/"
url_1 = f"https://api.meraki.com/api/v1/networks/{networkId}"
url_2 = f"https://api.meraki.com/api/v1/organizations/{orgId}/networks"


payload = {}


headers = {
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": f"{API_KEY}",
}
urls = [url_0, url_1,url_2]
i = 0
for url in urls:
    i +=1
    print(f"Loop {i}")
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        print(json.dumps(data, indent = 2))
    except Exception as e:
        print(e)

