import requests, json
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

#Get client info
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

payload = {}
headers = {'X-Auth-Token': auth_token}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
data = json.loads(response.text)
print(json.dumps(data, indent=4))

'''
$ python3.9 get_client_health_dnac.py
Enter usename: devnetuser
Enter password:
<Response [200]>
{
    "response": [
        {
            "siteId": "global",
            "scoreDetail": [
                {
                    "scoreCategory": {
                        "scoreCategory": "CLIENT_TYPE",
                        "value": "ALL"
                    },
                    "scoreValue": 0,
                    "clientCount": 2,
                    "clientUniqueCount": 2,
                    "maintenanceAffectedClientCount": 0,
                    "randomMacCount": null,
                    "duidCount": null,
                    "starttime": 1694130600000,
                    "endtime": 1694130900000,
                    "connectedToUdnCount": 0,
                    "unconnectedToUdnCount": 0
                },
                {
                    "scoreCategory": {
                        "scoreCategory": "CLIENT_TYPE",
                        "value": "WIRED"
                    },
                    "scoreValue": 0,
                    "clientCount": 2,
                    "clientUniqueCount": 2,
                    "maintenanceAffectedClientCount": 0,
                    "randomMacCount": 0,
                    "duidCount": 0,
                    "starttime": 1694130600000,
                    "endtime": 1694130900000,
                    "connectedToUdnCount": 0,
                    "unconnectedToUdnCount": 0,
                    "scoreList": [
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "POOR"
                            },
                            "scoreValue": -1,
                            "clientCount": 2,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0,
                            "scoreList": [
                                {
                                    "scoreCategory": {
                                        "scoreCategory": "deviceType",
                                        "value": "ALL"
                                    },
                                    "scoreValue": -1,
                                    "clientCount": 2,
                                    "clientUniqueCount": null,
                                    "maintenanceAffectedClientCount": null,
                                    "randomMacCount": null,
                                    "duidCount": null,
                                    "starttime": 1694130600000,
                                    "endtime": 1694130900000,
                                    "connectedToUdnCount": 0,
                                    "unconnectedToUdnCount": 0
                                },
                                {
                                    "scoreCategory": {
                                        "scoreCategory": "rootCause",
                                        "value": "DHCP"
                                    },
                                    "scoreValue": -1,
                                    "clientCount": 2,
                                    "clientUniqueCount": null,
                                    "maintenanceAffectedClientCount": null,
                                    "randomMacCount": null,
                                    "duidCount": null,
                                    "starttime": 1694130600000,
                                    "endtime": 1694130900000,
                                    "connectedToUdnCount": 0,
                                    "unconnectedToUdnCount": 0
                                }
                            ]
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "FAIR"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "GOOD"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "IDLE"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NODATA"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NEW"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        }
                    ]
                },
                {
                    "scoreCategory": {
                        "scoreCategory": "CLIENT_TYPE",
                        "value": "WIRELESS"
                    },
                    "scoreValue": -1,
                    "clientCount": 0,
                    "clientUniqueCount": 0,
                    "maintenanceAffectedClientCount": null,
                    "randomMacCount": 0,
                    "duidCount": 0,
                    "starttime": 1694130600000,
                    "endtime": 1694130900000,
                    "connectedToUdnCount": 0,
                    "unconnectedToUdnCount": 0,
                    "scoreList": [
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "POOR"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "FAIR"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "GOOD"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "IDLE"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NODATA"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        },
                        {
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NEW"
                            },
                            "scoreValue": -1,
                            "clientCount": 0,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "randomMacCount": null,
                            "duidCount": null,
                            "starttime": 1694130600000,
                            "endtime": 1694130900000,
                            "connectedToUdnCount": 0,
                            "unconnectedToUdnCount": 0
                        }
                    ]
                }
            ]
        }
    ]
}
'''
