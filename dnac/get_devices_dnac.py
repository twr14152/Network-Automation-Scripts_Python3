#!/usr/bin/python

import requests
import json

requests.packages.urllib3.disable_warnings()

#Get authentiation token

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
data = json.loads(response.text)
token = data['Token']

#Get devices info
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload = {}
headers = {'X-Auth-Token': token}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
data = json.loads(response.text)
print(json.dumps(data, indent=4))






'''
$ ./get_devices_dnac.py
{
    "version": "1.0",
    "response": [
        {
            "macAddress": "52:54:00:01:c2:c0",
            "upTime": "18 days, 18:29:18.00",
            "bootDateTime": "2023-08-18 03:22:35",
            "family": "Switches and Hubs",
            "snmpContact": "",
            "platformId": "C9KV-UADP-8P",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "errorCode": null,
            "softwareType": "IOS-XE",
            "interfaceCount": "0",
            "deviceSupportLevel": "Supported",
            "tunnelUdpPort": null,
            "id": "7e05557b-2323-4e72-b5d9-21d8706c5ac5",
            "apEthernetMacAddress": null,
            "locationName": null,
            "associatedWlcIp": "",
            "managementState": "Managed",
            "instanceUuid": "7e05557b-2323-4e72-b5d9-21d8706c5ac5",
            "lastUpdateTime": 1693950695429,
            "uptimeSeconds": 1672278,
            "reachabilityStatus": "Reachable",
            "hostname": "sw1.ciscotest.com",
            "memorySize": "NA",
            "roleSource": "AUTO",
            "collectionInterval": "Global Default",
            "lineCardCount": "0",
            "collectionStatus": "Managed",
            "role": "DISTRIBUTION",
            "lineCardId": "",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "managedAtleastOnce": true,
            "location": null,
            "waasDeviceMode": null,
            "apManagerInterfaceIp": "",
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "errorDescription": null,
            "lastUpdated": "2023-09-05 21:51:35",
            "managementIpAddress": "10.10.20.175",
            "serialNumber": "9SB9FYAFA2O",
            "reachabilityFailureReason": "",
            "softwareVersion": "17.9.20220318:182713",
            "snmpLocation": "",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "tagCount": "0"
        },
        {
            "macAddress": "52:54:00:0e:1c:6a",
            "upTime": "144 days, 7:52:25.00",
            "bootDateTime": "2023-04-14 14:00:42",
            "family": "Switches and Hubs",
            "snmpContact": "",
            "platformId": "C9KV-UADP-8P",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "errorCode": null,
            "softwareType": "IOS-XE",
            "interfaceCount": "0",
            "deviceSupportLevel": "Supported",
            "tunnelUdpPort": null,
            "id": "9a28d450-ecb5-42b6-83ce-8f52f1e5252c",
            "apEthernetMacAddress": null,
            "locationName": null,
            "associatedWlcIp": "",
            "managementState": "Managed",
            "instanceUuid": "9a28d450-ecb5-42b6-83ce-8f52f1e5252c",
            "lastUpdateTime": 1693950762280,
            "uptimeSeconds": 12520391,
            "reachabilityStatus": "Reachable",
            "hostname": "sw2",
            "memorySize": "NA",
            "roleSource": "AUTO",
            "collectionInterval": "Global Default",
            "lineCardCount": "0",
            "collectionStatus": "Managed",
            "role": "DISTRIBUTION",
            "lineCardId": "",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "managedAtleastOnce": true,
            "location": null,
            "waasDeviceMode": null,
            "apManagerInterfaceIp": "",
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "errorDescription": null,
            "lastUpdated": "2023-09-05 21:52:42",
            "managementIpAddress": "10.10.20.176",
            "serialNumber": "9SB9FYAFA21",
            "reachabilityFailureReason": "",
            "softwareVersion": "17.9.20220318:182713",
            "snmpLocation": "",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "tagCount": "0"
        },
        {
            "macAddress": "52:54:00:0a:1b:4c",
            "upTime": "30 days, 18:55:43.00",
            "bootDateTime": "2023-08-06 02:58:30",
            "family": "Switches and Hubs",
            "snmpContact": "",
            "platformId": "C9KV-UADP-8P",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "errorCode": null,
            "softwareType": "IOS-XE",
            "interfaceCount": "0",
            "deviceSupportLevel": "Supported",
            "tunnelUdpPort": null,
            "id": "e0ba1a00-b69b-45aa-8c13-4cdfb59afe65",
            "apEthernetMacAddress": null,
            "locationName": null,
            "associatedWlcIp": "",
            "managementState": "Managed",
            "instanceUuid": "e0ba1a00-b69b-45aa-8c13-4cdfb59afe65",
            "lastUpdateTime": 1693950810986,
            "uptimeSeconds": 2710522,
            "reachabilityStatus": "Reachable",
            "hostname": "sw3",
            "memorySize": "NA",
            "roleSource": "AUTO",
            "collectionInterval": "Global Default",
            "lineCardCount": "0",
            "collectionStatus": "Managed",
            "role": "DISTRIBUTION",
            "lineCardId": "",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "managedAtleastOnce": true,
            "location": null,
            "waasDeviceMode": null,
            "apManagerInterfaceIp": "",
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "errorDescription": null,
            "lastUpdated": "2023-09-05 21:53:30",
            "managementIpAddress": "10.10.20.177",
            "serialNumber": "9SB9FYAFA22",
            "reachabilityFailureReason": "",
            "softwareVersion": "17.9.20220318:182713",
            "snmpLocation": "",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "tagCount": "0"
        },
        {
            "macAddress": "52:54:00:0f:25:4c",
            "upTime": "144 days, 7:54:14.00",
            "bootDateTime": "2023-04-14 14:00:29",
            "family": "Switches and Hubs",
            "snmpContact": "",
            "platformId": "C9KV-UADP-8P",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "errorCode": null,
            "softwareType": "IOS-XE",
            "interfaceCount": "0",
            "deviceSupportLevel": "Supported",
            "tunnelUdpPort": null,
            "id": "c5c9f0de-0449-4e07-bf15-2b9d75707178",
            "apEthernetMacAddress": null,
            "locationName": null,
            "associatedWlcIp": "",
            "managementState": "Managed",
            "instanceUuid": "c5c9f0de-0449-4e07-bf15-2b9d75707178",
            "lastUpdateTime": 1693950869255,
            "uptimeSeconds": 12520404,
            "reachabilityStatus": "Reachable",
            "hostname": "sw4",
            "memorySize": "NA",
            "roleSource": "MANUAL",
            "collectionInterval": "Global Default",
            "lineCardCount": "0",
            "collectionStatus": "Managed",
            "role": "ACCESS",
            "lineCardId": "",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "managedAtleastOnce": true,
            "location": null,
            "waasDeviceMode": null,
            "apManagerInterfaceIp": "",
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "errorDescription": null,
            "lastUpdated": "2023-09-05 21:54:29",
            "managementIpAddress": "10.10.20.178",
            "serialNumber": "9SB9FYAFA23",
            "reachabilityFailureReason": "",
            "softwareVersion": "17.9.20220318:182713",
            "snmpLocation": "",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "tagCount": "0"
        }
    ]
}
'''
