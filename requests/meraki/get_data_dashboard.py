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
# set default values
if len(orgId) == 0 : orgId = "1097053"

networkId = input("Enter Network ID: ")
# set default values
if len(networkId) == 0 : networkId = "L_627126248111380187"


API_KEY = input("Enter API_KEY: " )
# set default values
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




'''
output of script
 $ ./get_data_dashboard.py

        Example:
        Enter Org ID: 573083052582915264
        Enter Network ID: L_573083052582991362
        Enter API_KEY: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0

Enter Org ID:
Enter Network ID:
Enter API_KEY:
Loop 1
[
  {
    "id": "1097053",
    "name": "Independent Consultant",
    "url": "https://n114.meraki.com/o/7QEucc/manage/organization/overview",
    "api": {
      "enabled": true
    },
    "licensing": {
      "model": "co-term"
    },
    "cloud": {
      "region": {
        "name": "North America"
      }
    },
    "management": {
      "details": []
    }
  }
]
Loop 2
{
  "id": "L_627126248111380187",
  "organizationId": "1097053",
  "productTypes": [
    "switch"
  ],
  "url": "https://n114.meraki.com/Gibsons_Network-/n/MVk3rbYb/manage/usage/list",
  "name": "Gibsons_Network",
  "timeZone": "America/New_York",
  "enrollmentString": null,
  "tags": [],
  "notes": "",
  "isBoundToConfigTemplate": false
}
Loop 3
[
  {
    "id": "L_627126248111380187",
    "organizationId": "1097053",
    "name": "Gibsons_Network",
    "productTypes": [
      "switch"
    ],
    "timeZone": "America/New_York",
    "tags": [],
    "enrollmentString": null,
    "url": "https://n114.meraki.com/Gibsons_Network-/n/MVk3rbYb/manage/usage/list",
    "notes": "",
    "isBoundToConfigTemplate": false
  },
  {
    "id": "L_627126248111380188",
    "organizationId": "1097053",
    "name": "Lunas Network",
    "productTypes": [
      "switch"
    ],
    "timeZone": "America/Los_Angeles",
    "tags": [
      "tag1",
      "tag2"
    ],
    "enrollmentString": null,
    "url": "https://n114.meraki.com/Lunas-Network-sw/n/Tn1rEdYb/manage/usage/list",
    "notes": "Boy this sure is involved",
    "isBoundToConfigTemplate": false
  },
  {
    "id": "N_627126248111476956",
    "organizationId": "1097053",
    "name": "Jacks_Room",
    "productTypes": [
      "switch"
    ],
    "timeZone": "America/Los_Angeles",
    "tags": [],
    "enrollmentString": null,
    "url": "https://n114.meraki.com/Jacks_Room/n/qSdrCcYb/manage/usage/list",
    "notes": null,
    "isBoundToConfigTemplate": false
  },
  {
    "id": "N_627126248111476958",
    "organizationId": "1097053",
    "name": "Evee_Network",
    "productTypes": [
      "wireless"
    ],
    "timeZone": "America/Los_Angeles",
    "tags": [],
    "enrollmentString": null,
    "url": "https://n114.meraki.com/Evee_Network/n/HgaoccYb/manage/usage/list",
    "notes": null,
    "isBoundToConfigTemplate": false
  },
  {
    "id": "N_627126248111476961",
    "organizationId": "1097053",
    "name": "My office Network",
    "productTypes": [
      "wireless"
    ],
    "timeZone": "America/Los_Angeles",
    "tags": [
      "hideout",
      "man_cave"
    ],
    "enrollmentString": null,
    "url": "https://n114.meraki.com/My-office-Networ/n/YjIdXbYb/manage/usage/list",
    "notes": "This is my new office network",
    "isBoundToConfigTemplate": false
  }
]
'''
