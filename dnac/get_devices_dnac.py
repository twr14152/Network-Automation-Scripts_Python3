#!/usr/bin/python
import requests,json
from requests.auth import HTTPBasicAuth
from getpass import getpass

requests.packages.urllib3.disable_warnings()


#Get auth token
def get_token():
    uname = input('Enter usename: ')
    passwd = getpass('Enter password: ')
    token = requests.post(
            'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token',
       auth=HTTPBasicAuth(
           username=uname,
           password=passwd
       ),
       headers={'content-type': 'application/json'},
       verify=False,
    )
    print(token)
    data = token.json()
    return data['Token']

auth_token = get_token()

#Get devices info
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload = {}
headers = {'X-Auth-Token': auth_token}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
data = json.loads(response.text)
print(json.dumps(data, indent=4))


'''
$ python get_devices_dnac.py
Enter usename: devnetuser
Enter password:
<Response [200]>
{
    "response": [
        {
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "memorySize": "NA",
            "family": "Switches and Hubs",
            "bootDateTime": "2023-08-18 03:22:35",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "snmpContact": "",
            "snmpLocation": "",
            "apEthernetMacAddress": null,
            "apManagerInterfaceIp": "",
            "collectionStatus": "Managed",
            "hostname": "sw1.ciscotest.com",
            "lastUpdateTime": 1694123495651,
            "locationName": null,
            "managementIpAddress": "10.10.20.175",
            "platformId": "C9KV-UADP-8P",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "lastUpdated": "2023-09-07 21:51:35",
            "errorCode": null,
            "errorDescription": null,
            "interfaceCount": "0",
            "lineCardCount": "0",
            "lineCardId": "",
            "managedAtleastOnce": true,
            "tagCount": "0",
            "tunnelUdpPort": null,
            "uptimeSeconds": 1803495,
            "waasDeviceMode": null,
            "associatedWlcIp": "",
            "roleSource": "AUTO",
            "macAddress": "52:54:00:01:c2:c0",
            "deviceSupportLevel": "Supported",
            "softwareType": "IOS-XE",
            "softwareVersion": "17.9.20220318:182713",
            "serialNumber": "9SB9FYAFA2O",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "upTime": "20 days, 18:29:01.00",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "managementState": "Managed",
            "collectionInterval": "Global Default",
            "location": null,
            "role": "DISTRIBUTION",
            "instanceUuid": "7e05557b-2323-4e72-b5d9-21d8706c5ac5",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "id": "7e05557b-2323-4e72-b5d9-21d8706c5ac5"
        },
        {
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "memorySize": "NA",
            "family": "Switches and Hubs",
            "bootDateTime": "2023-04-14 14:00:41",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "snmpContact": "",
            "snmpLocation": "",
            "apEthernetMacAddress": null,
            "apManagerInterfaceIp": "",
            "collectionStatus": "Managed",
            "hostname": "sw2",
            "lastUpdateTime": 1694123561500,
            "locationName": null,
            "managementIpAddress": "10.10.20.176",
            "platformId": "C9KV-UADP-8P",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "lastUpdated": "2023-09-07 21:52:41",
            "errorCode": null,
            "errorDescription": null,
            "interfaceCount": "0",
            "lineCardCount": "0",
            "lineCardId": "",
            "managedAtleastOnce": true,
            "tagCount": "0",
            "tunnelUdpPort": null,
            "uptimeSeconds": 12651610,
            "waasDeviceMode": null,
            "associatedWlcIp": "",
            "roleSource": "AUTO",
            "macAddress": "52:54:00:0e:1c:6a",
            "deviceSupportLevel": "Supported",
            "softwareType": "IOS-XE",
            "softwareVersion": "17.9.20220318:182713",
            "serialNumber": "9SB9FYAFA21",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "upTime": "146 days, 7:52:08.00",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "managementState": "Managed",
            "collectionInterval": "Global Default",
            "location": null,
            "role": "DISTRIBUTION",
            "instanceUuid": "9a28d450-ecb5-42b6-83ce-8f52f1e5252c",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "id": "9a28d450-ecb5-42b6-83ce-8f52f1e5252c"
        },
        {
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "memorySize": "NA",
            "family": "Switches and Hubs",
            "bootDateTime": "2023-08-06 02:58:30",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "snmpContact": "",
            "snmpLocation": "",
            "apEthernetMacAddress": null,
            "apManagerInterfaceIp": "",
            "collectionStatus": "Managed",
            "hostname": "sw3",
            "lastUpdateTime": 1694123610848,
            "locationName": null,
            "managementIpAddress": "10.10.20.177",
            "platformId": "C9KV-UADP-8P",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "lastUpdated": "2023-09-07 21:53:30",
            "errorCode": null,
            "errorDescription": null,
            "interfaceCount": "0",
            "lineCardCount": "0",
            "lineCardId": "",
            "managedAtleastOnce": true,
            "tagCount": "0",
            "tunnelUdpPort": null,
            "uptimeSeconds": 2841740,
            "waasDeviceMode": null,
            "associatedWlcIp": "",
            "roleSource": "AUTO",
            "macAddress": "52:54:00:0a:1b:4c",
            "deviceSupportLevel": "Supported",
            "softwareType": "IOS-XE",
            "softwareVersion": "17.9.20220318:182713",
            "serialNumber": "9SB9FYAFA22",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "upTime": "32 days, 18:55:26.00",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "managementState": "Managed",
            "collectionInterval": "Global Default",
            "location": null,
            "role": "DISTRIBUTION",
            "instanceUuid": "e0ba1a00-b69b-45aa-8c13-4cdfb59afe65",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "id": "e0ba1a00-b69b-45aa-8c13-4cdfb59afe65"
        },
        {
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "memorySize": "NA",
            "family": "Switches and Hubs",
            "bootDateTime": "2023-04-14 14:01:32",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "snmpContact": "",
            "snmpLocation": "",
            "apEthernetMacAddress": null,
            "apManagerInterfaceIp": "",
            "collectionStatus": "Managed",
            "hostname": "sw4",
            "lastUpdateTime": 1694123672374,
            "locationName": null,
            "managementIpAddress": "10.10.20.178",
            "platformId": "C9KV-UADP-8P",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "lastUpdated": "2023-09-07 21:54:32",
            "errorCode": null,
            "errorDescription": null,
            "interfaceCount": "0",
            "lineCardCount": "0",
            "lineCardId": "",
            "managedAtleastOnce": true,
            "tagCount": "0",
            "tunnelUdpPort": null,
            "uptimeSeconds": 12651559,
            "waasDeviceMode": null,
            "associatedWlcIp": "",
            "roleSource": "MANUAL",
            "macAddress": "52:54:00:0f:25:4c",
            "deviceSupportLevel": "Supported",
            "softwareType": "IOS-XE",
            "softwareVersion": "17.9.20220318:182713",
            "serialNumber": "9SB9FYAFA23",
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "upTime": "146 days, 7:53:57.00",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "managementState": "Managed",
            "collectionInterval": "Global Default",
            "location": null,
            "role": "ACCESS",
            "instanceUuid": "c5c9f0de-0449-4e07-bf15-2b9d75707178",
            "instanceTenantId": "623f029857259506a56ad9bd",
            "id": "c5c9f0de-0449-4e07-bf15-2b9d75707178"
        }
    ],
    "version": "1.0"
}
$
'''
