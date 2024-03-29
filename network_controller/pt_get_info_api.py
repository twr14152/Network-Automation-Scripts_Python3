#!/usr/bin/python3

# Work in progress

import requests
import json

def get_token():
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"username": "admin", "password": "cisco"})
    url = "http://localhost:58000/api/v1/ticket"
    resp = requests.post(url,data=data, headers=headers)
    result = resp.json()
    ticket = result["response"]["serviceTicket"]
    print(f"\nTicket value to use is {ticket}\n")
    return ticket

def get_device_info(ticket):
    print("\n\n\nGet devices info:")
    url = "http://localhost:58000/api/v1/network-device"
    payload = {}
    headers = {'X-Auth-Token': ticket}
    response = requests.get(url, headers=headers, data=payload)
    data = json.loads(response.text)
    print(json.dumps(data, indent=4))
  

def get_flow_info(ticket):
    headers = {"X-Auth-Token": ticket}
    payload = {}
    url = "http://localhost:58000/api/v1/flow-analysis"
    response = requests.get(url, headers=headers, data=payload) 
    data = json.loads(response.text)
    print(json.dumps(data, indent=4))


def post_flow_info(ticket, src, dst):
    headers = {"X-Auth-Token": ticket}
    url = "http://localhost:58000/api/v1/flow-analysis"
    postData = json.dumps({"sourceIP": src, "destIP": dst })
    response = requests.post(url, data=postData, headers=headers)
    data = json.loads(response.text)
    print(json.dumps(data, indent=4))

def get_policy_tags(ticket):
    print("\n\nGet Policy Tags:\n")
    url = "http://localhost:58000/api/v1/policy/tag"
    payload = {}
    headers = {'X-Auth-Token': ticket}
    response = requests.get(url, headers=headers, data=payload)
    data = json.loads(response.text)
    print(json.dumps(data, indent=4))
    


def main():
    ticket = get_token()
    get_device_info(ticket)
    get_flow_info(ticket)
    post_flow_info(ticket, "10.0.0.12", "69.69.69.69")
    #get_policy_tags(ticket)

    
main()

'''
toddriemenschneider@Todds-MBP-2 requests_stuff % ./pt_get_info_api.py 

Ticket value to use is NC-60-b8d100f220984961a026-nbi




Get devices info:
{
    "response": [
        {
            "collectionStatus": "Unreachable",
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "id": "CAT1010CXZC-uuid",
            "interfaceCount": "27",
            "inventoryStatusDetail": "Unreachable",
            "lastUpdateTime": "0",
            "lastUpdated": "2023-09-14 04:45:00",
            "macAddress": "",
            "managementIpAddress": "10.0.0.20",
            "platformId": "",
            "productId": "",
            "reachabilityFailureReason": "Unable to ping to device. ",
            "reachabilityStatus": "Unreachable",
            "serialNumber": "",
            "type": "",
            "upTime": ""
        },
        {
            "collectionStatus": "Unsupported",
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "id": "FTX1524F2SE-uuid",
            "interfaceCount": "8",
            "inventoryStatusDetail": "Unsupported",
            "ipAddresses": [
                "10.0.0.1",
                "10.0.69.1",
                "157.130.0.1",
                "157.130.0.5"
            ],
            "lastUpdateTime": "15",
            "lastUpdated": "2023-09-14 04:44:45",
            "macAddress": "00D0.D39B.724B",
            "managementIpAddress": "157.130.0.5",
            "platformId": "",
            "productId": "",
            "reachabilityFailureReason": "NOT_VALIDATED",
            "reachabilityStatus": "Reachable",
            "serialNumber": "",
            "type": "",
            "upTime": ""
        },
        {
            "collectionStatus": "Unsupported",
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "id": "FTX1524I2CG-uuid",
            "interfaceCount": "8",
            "inventoryStatusDetail": "Unsupported",
            "ipAddresses": [
                "157.130.0.2",
                "157.130.1.1"
            ],
            "lastUpdateTime": "15",
            "lastUpdated": "2023-09-14 04:44:45",
            "macAddress": "00E0.A351.E00D",
            "managementIpAddress": "157.130.1.1",
            "platformId": "",
            "productId": "",
            "reachabilityFailureReason": "NOT_VALIDATED",
            "reachabilityStatus": "Reachable",
            "serialNumber": "",
            "type": "",
            "upTime": ""
        },
        {
            "collectionStatus": "Unsupported",
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "id": "FTX1524OJ3B-uuid",
            "interfaceCount": "8",
            "inventoryStatusDetail": "Unsupported",
            "ipAddresses": [
                "157.130.1.5",
                "157.130.0.6"
            ],
            "lastUpdateTime": "15",
            "lastUpdated": "2023-09-14 04:44:45",
            "macAddress": "00D0.FF7D.2E2C",
            "managementIpAddress": "157.130.0.6",
            "platformId": "",
            "productId": "",
            "reachabilityFailureReason": "NOT_VALIDATED",
            "reachabilityStatus": "Reachable",
            "serialNumber": "",
            "type": "",
            "upTime": ""
        },
        {
            "collectionStatus": "Unsupported",
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "id": "FTX1524CQVV-uuid",
            "interfaceCount": "8",
            "inventoryStatusDetail": "Unsupported",
            "ipAddresses": [
                "10.0.2.1",
                "10.0.3.1",
                "157.130.1.2",
                "157.130.1.6"
            ],
            "lastUpdateTime": "14",
            "lastUpdated": "2023-09-14 04:44:46",
            "macAddress": "00D0.58D0.2A35",
            "managementIpAddress": "157.130.1.6",
            "platformId": "",
            "productId": "",
            "reachabilityFailureReason": "NOT_VALIDATED",
            "reachabilityStatus": "Reachable",
            "serialNumber": "",
            "type": "",
            "upTime": ""
        },
        {
            "collectionStatus": "Unreachable",
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "id": "CAT1010XD2F-uuid",
            "interfaceCount": "27",
            "inventoryStatusDetail": "Unreachable",
            "lastUpdateTime": "16",
            "lastUpdated": "2023-09-14 04:44:44",
            "macAddress": "",
            "managementIpAddress": "10.0.2.20",
            "platformId": "",
            "productId": "",
            "reachabilityFailureReason": "Unable to ping to device. ",
            "reachabilityStatus": "Unreachable",
            "serialNumber": "",
            "type": "",
            "upTime": ""
        },
        {
            "collectionStatus": "Unreachable",
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "id": "",
            "interfaceCount": "",
            "inventoryStatusDetail": "Unreachable",
            "lastUpdateTime": "14",
            "lastUpdated": "2023-09-14 04:44:46",
            "macAddress": "",
            "managementIpAddress": "1.1.1.1",
            "platformId": "",
            "productId": "",
            "reachabilityFailureReason": "Unable to ping to device. ",
            "reachabilityStatus": "Unreachable",
            "serialNumber": "",
            "type": "",
            "upTime": ""
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet0/1",
                "GigabitEthernet0/0/1"
            ],
            "connectedNetworkDeviceIpAddress": [
                "10.0.69.1",
                "54.0.0.2"
            ],
            "connectedNetworkDeviceName": [
                "Router3",
                "Router5"
            ],
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "hostname": "router69",
            "id": "FDO13022813-uuid",
            "interfaceCount": "6",
            "inventoryStatusDetail": "Managed",
            "ipAddresses": [
                "10.0.69.2",
                "54.0.0.1"
            ],
            "lastUpdateTime": "14",
            "lastUpdated": "2023-09-14 04:44:46",
            "macAddress": "0003.E4D0.D7D0",
            "managementIpAddress": "70.70.70.70",
            "platformId": "ISR4300",
            "productId": "ISR4331",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "FDO13022813-",
            "softwareVersion": "16.6.4",
            "type": "Router",
            "upTime": "2 days, 6 hours, 51 minutes, 57 seconds"
        },
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet0/1",
                "GigabitEthernet0/0/1"
            ],
            "connectedNetworkDeviceIpAddress": [
                "10.0.3.1",
                "54.0.0.1"
            ],
            "connectedNetworkDeviceName": [
                "Router",
                "router69"
            ],
            "errorDescription": "",
            "globalCredentialId": "05589567-404d-488a-bf82-8ef6b680dfbd",
            "hostname": "Router5",
            "id": "FDO130291M2-uuid",
            "interfaceCount": "6",
            "inventoryStatusDetail": "Managed",
            "ipAddresses": [
                "10.0.3.2",
                "54.0.0.2"
            ],
            "lastUpdateTime": "14",
            "lastUpdated": "2023-09-14 04:44:46",
            "macAddress": "0001.6342.8873",
            "managementIpAddress": "55.55.55.55",
            "platformId": "ISR4300",
            "productId": "ISR4331",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "FDO130291M2-",
            "softwareVersion": "16.6.4",
            "type": "Router",
            "upTime": "1 days, 5 hours, 31 minutes, 49 seconds"
        }
    ],
    "version": "1.0"
}
{
    "response": {
        "flowAnalysisList": [
            {
                "createTime": "1694577385000",
                "destIP": "55.55.55.55",
                "id": "05A7E0WQ-3XI3-67DZ-D5UB-R4LHJ892C5NW",
                "lastUpdateTime": "1711624023949",
                "sourceIP": "10.0.0.12",
                "status": "COMPLETED"
            },
            {
                "createTime": "1694577435000",
                "destIP": "70.70.70.70",
                "id": "IYH2TVXY-EPDK-139I-FZUU-5SOW43N4XQ9N",
                "lastUpdateTime": "1711624077759",
                "sourceIP": "10.0.0.12",
                "status": "COMPLETED"
            },
            {
                "createTime": "1694675050000",
                "destIP": "55.55.55.55",
                "id": "4JV6C2GA-9RUP-R8Z3-O0Q6-9829YMDFM7P3",
                "lastUpdateTime": "1711709040743",
                "sourceIP": "10.0.0.12",
                "status": "COMPLETED"
            },
            {
                "createTime": "1694675074000",
                "destIP": "55.55.55.55",
                "id": "5KT2D9AN-7ZBZ-0U8W-6P33-F3326A09M3T0",
                "lastUpdateTime": "1711709066006",
                "sourceIP": "10.0.0.12",
                "status": "COMPLETED"
            },
            {
                "createTime": "1694675131000",
                "destIP": "55.55.55.55",
                "id": "7OE1V2I2-K48S-0TR5-N6CE-L1YCP83I8RM2",
                "lastUpdateTime": "1711709126506",
                "sourceIP": "10.0.0.12",
                "status": "COMPLETED"
            }
        ]
    },
    "version": "1.0"
}
{
    "response": {
        "detail": "Content type '' not supported",
        "errorCode": "UNKNOWN_ERROR",
        "message": "Content type '' not supported"
    },
    "version": "1.0"
}
toddriemenschneider@Todds-MBP-2 requests_stuff % 
'''
