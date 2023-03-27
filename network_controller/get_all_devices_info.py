import requests
import json

# Get authentication ticket first

url = "http://localhost:58000/api/v1"

headers = {"Content-Type": "application/json"}
data = json.dumps({"username": "admin", "password": "cisco123!"})

resp = requests.post(url + "/ticket", data=data, headers=headers)

result = resp.json()

ticket = result["response"]["serviceTicket"]
print(f"\nTicket value to use is {ticket}\n")

# Get network device info

headers = {"X-Auth-Token": ticket}
resp = requests.get(url+"/network-device", headers=headers)

print(f"\nStatus Code: {resp.status_code}\n")

result = resp.json()

count = 1
for i in result["response"]:
    print(f"Device {count}")
    try:
        print(json.dumps(i, indent=4))
    except:
        print(f"Unable to read device {count}")
    count += 1



"""
Results
toddriemenschneider@Todds-MacBook-Pro-2 % python3  get_all_devices_info.py

Ticket value to use is NC-111-1b315179552445968d9b-nbi


Status Code: 200

Device 1
{
    "collectionStatus": "Managed",
    "connectedInterfaceName": [
        "GigabitEthernet0/0",
        "GigabitEthernet0/1",
        "FastEthernet0",
        "GigabitEthernet0"
    ],
    "connectedNetworkDeviceIpAddress": [
        "10.10.0.2",
        "10.10.0.3",
        "10.10.0.22",
        "10.10.0.254"
    ],
    "connectedNetworkDeviceName": [
        "a10_r1",
        "a10_r2",
        "PC0",
        "NetworkController"
    ],
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "hostname": "a10_s1",
    "id": "CAT10102UG4-uuid",
    "interfaceCount": "28",
    "inventoryStatusDetail": "Managed",
    "lastUpdateTime": "4",
    "lastUpdated": "2023-03-28 13:06:18",
    "macAddress": "0030.A379.E090",
    "managementIpAddress": "10.10.0.20",
    "platformId": "2960",
    "productId": "2960-24TT",
    "reachabilityFailureReason": "",
    "reachabilityStatus": "Reachable",
    "serialNumber": "CAT10102UG4-",
    "softwareVersion": "15.0",
    "type": "Switch",
    "upTime": "2 days, 1 hours, 10 minutes, 8 seconds"
}
Device 2
{
    "collectionStatus": "Unreachable",
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "id": "FTX1524J3KZ-uuid",
    "interfaceCount": "9",
    "inventoryStatusDetail": "Unreachable",
    "ipAddresses": [
        "10.10.0.2",
        "157.130.3.1",
        "157.130.0.2"
    ],
    "lastUpdateTime": "5",
    "lastUpdated": "2023-03-28 13:06:17",
    "macAddress": "00D0.BC6B.C767",
    "managementIpAddress": "157.130.3.1",
    "platformId": "",
    "productId": "",
    "reachabilityFailureReason": "Unable to ping to device. ",
    "reachabilityStatus": "Unreachable",
    "serialNumber": "",
    "type": "",
    "upTime": ""
}
Device 3
{
    "collectionStatus": "Unsupported",
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "id": "FTX1524SRV3-uuid",
    "interfaceCount": "9",
    "inventoryStatusDetail": "Unsupported",
    "ipAddresses": [
        "157.130.3.2",
        "10.10.0.3",
        "157.130.1.2"
    ],
    "lastUpdateTime": "4",
    "lastUpdated": "2023-03-28 13:06:18",
    "macAddress": "0002.4AB7.1C91",
    "managementIpAddress": "157.130.3.2",
    "platformId": "",
    "productId": "",
    "reachabilityFailureReason": "NOT_VALIDATED",
    "reachabilityStatus": "Reachable",
    "serialNumber": "",
    "type": "",
    "upTime": ""
}
Device 4
{
    "collectionStatus": "Managed",
    "connectedInterfaceName": [
        "GigabitEthernet1/0/3",
        "Serial0/3/0"
    ],
    "connectedNetworkDeviceIpAddress": [
        "10.0.0.5",
        "157.130.1.2"
    ],
    "connectedNetworkDeviceName": [
        "core2",
        "a10_r2"
    ],
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "hostname": "core_r2",
    "id": "FDO1302WPFM-uuid",
    "interfaceCount": "10",
    "inventoryStatusDetail": "Managed",
    "ipAddresses": [
        "10.0.0.6",
        "157.130.1.1"
    ],
    "lastUpdateTime": "4",
    "lastUpdated": "2023-03-28 13:06:18",
    "macAddress": "000D.BD67.7559",
    "managementIpAddress": "157.130.1.1",
    "platformId": "ISR4300",
    "productId": "ISR4321",
    "reachabilityFailureReason": "",
    "reachabilityStatus": "Reachable",
    "serialNumber": "FDO1302WPFM-",
    "softwareVersion": "15.4",
    "type": "Router",
    "upTime": "1 days, 17 hours, 54 minutes, 50 seconds"
}
Device 5
{
    "collectionStatus": "Managed",
    "connectedInterfaceName": [
        "GigabitEthernet1/0/1",
        "GigabitEthernet1/0/2",
        "GigabitEthernet0/0/0"
    ],
    "connectedNetworkDeviceIpAddress": [
        "",
        "",
        "10.0.0.6"
    ],
    "connectedNetworkDeviceName": [
        "Core1",
        "Core1",
        "core_r2"
    ],
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "hostname": "core2",
    "id": "CAT1010JRE1-uuid",
    "interfaceCount": "31",
    "inventoryStatusDetail": "Managed",
    "ipAddresses": [
        "10.0.0.5"
    ],
    "lastUpdateTime": "3",
    "lastUpdated": "2023-03-28 13:06:19",
    "macAddress": "0060.3E65.4352",
    "managementIpAddress": "10.0.0.5",
    "platformId": "3650",
    "productId": "3650-24PS",
    "reachabilityFailureReason": "",
    "reachabilityStatus": "Reachable",
    "serialNumber": "CAT1010JRE1-",
    "softwareVersion": "16.3.2",
    "type": "MultiLayerSwitch",
    "upTime": "2 days, 1 hours, 27 minutes, 47 seconds"
}
Device 6
{
    "collectionStatus": "Managed",
    "connectedInterfaceName": [
        "GigabitEthernet1/0/1",
        "GigabitEthernet1/0/2",
        "GigabitEthernet0/0/0"
    ],
    "connectedNetworkDeviceIpAddress": [
        "",
        "",
        "10.0.0.2"
    ],
    "connectedNetworkDeviceName": [
        "core2",
        "core2",
        "core_r1"
    ],
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "hostname": "Core1",
    "id": "CAT101089TI-uuid",
    "interfaceCount": "31",
    "inventoryStatusDetail": "Managed",
    "ipAddresses": [
        "10.0.0.1"
    ],
    "lastUpdateTime": "3",
    "lastUpdated": "2023-03-28 13:06:19",
    "macAddress": "0010.111C.BD2E",
    "managementIpAddress": "10.0.0.9",
    "platformId": "3650",
    "productId": "3650-24PS",
    "reachabilityFailureReason": "",
    "reachabilityStatus": "Reachable",
    "serialNumber": "CAT101089TI-",
    "softwareVersion": "16.3.2",
    "type": "MultiLayerSwitch",
    "upTime": "2 days, 1 hours, 37 minutes, 8 seconds"
}
Device 7
{
    "collectionStatus": "Unreachable",
    "connectedInterfaceName": [
        "GigabitEthernet1/0/3",
        "Serial0/3/0"
    ],
    "connectedNetworkDeviceIpAddress": [
        "10.0.0.1",
        "157.130.0.2"
    ],
    "connectedNetworkDeviceName": [
        "Core1",
        "a10_r1"
    ],
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "hostname": "core_r1",
    "id": "FDO1302887G-uuid",
    "interfaceCount": "10",
    "inventoryStatusDetail": "Unreachable",
    "ipAddresses": [
        "10.0.0.2",
        "157.130.0.1"
    ],
    "lastUpdateTime": "5",
    "lastUpdated": "2023-03-28 13:06:17",
    "macAddress": "0002.1650.B2BE",
    "managementIpAddress": "157.130.0.1",
    "platformId": "ISR4300",
    "productId": "ISR4321",
    "reachabilityFailureReason": "Unable to ping to device. ",
    "reachabilityStatus": "Unreachable",
    "serialNumber": "FDO1302887G-",
    "softwareVersion": "15.4",
    "type": "Router",
    "upTime": "1 days, 21 hours, 12 minutes, 52 seconds"
}
Device 8
{
    "collectionStatus": "Unsupported",
    "errorDescription": "",
    "globalCredentialId": "0339abad-1435-462d-8213-4619f05c4494",
    "id": "",
    "interfaceCount": "",
    "inventoryStatusDetail": "Unsupported",
    "lastUpdateTime": "3",
    "lastUpdated": "2023-03-28 13:06:19",
    "macAddress": "",
    "managementIpAddress": "10.10.0.1",
    "platformId": "",
    "productId": "",
    "reachabilityFailureReason": "NOT_VALIDATED",
    "reachabilityStatus": "Reachable",
    "serialNumber": "",
    "type": "",
    "upTime": ""
}
toddriemenschneider@Todds-MacBook-Pro-2 % 
"""
