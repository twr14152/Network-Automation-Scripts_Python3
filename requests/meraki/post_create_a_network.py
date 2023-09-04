
import requests, json

url = "https://api.meraki.com/api/v1/organizations/1097053/networks"

payload = '''{
    "copyFromNetworkId": "N_627126248111476958",
    "name": "My office Network",
    "notes": "This is my new office network",
    "timeZone": "America/Los_Angeles",
    "productTypes": [ "wireless" ],
    "tags": [ "hideout", "man_cave" ]
}'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "40bfc95138a521bffc6691b2ee0be63b1d0da812"
}

response = requests.request('POST', url, headers=headers, data = payload)
data = json.loads(response.text)
print(json.dumps(data, indent=4))

'''
result of script:
{
    "id": "N_627126248111476961",
    "organizationId": "1097053",
    "productTypes": [
        "wireless"
    ],
    "url": "https://n114.meraki.com/My-office-Networ/n/YjIdXbYb/manage/usage/list",
    "name": "My office Network",
    "timeZone": "America/Los_Angeles",
    "enrollmentString": null,
    "tags": [
        "hideout",
        "man_cave"
    ],
    "notes": "This is my new office network",
    "isBoundToConfigTemplate": false
}
'''
