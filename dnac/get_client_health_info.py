#!/usr/bin/python
import requests, json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

#Get auth token
UN = "devnetuser"
PW = "Cisco123!"
token = requests.post(
            'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token',
       auth=HTTPBasicAuth(
           username = UN,
           password = PW
       ),
       headers={'content-type': 'application/json'},
       verify=False,
    )
data = token.json()
auth_token = data['Token']


#Get client info
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

payload = {}
headers = {'X-Auth-Token': auth_token}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
data = json.loads(response.text)
print(json.dumps(data, indent=4))



'''
$ ./get_client_health_dnac.py
{
    "response": [
        {
            "scoreDetail": [
                {
                    "scoreValue": 0,
                    "unconnectedToUdnCount": 0,
                    "duidCount": null,
                    "clientUniqueCount": 2,
                    "maintenanceAffectedClientCount": 0,
                    "scoreCategory": {
                        "scoreCategory": "CLIENT_TYPE",
                        "value": "ALL"
                    },
                    "randomMacCount": null,
                    "starttime": 1694084400000,
                    "connectedToUdnCount": 0,
                    "clientCount": 2,
                    "endtime": 1694084700000
                },
                {
                    "scoreValue": 0,
                    "unconnectedToUdnCount": 0,
                    "duidCount": 0,
                    "clientUniqueCount": 2,
                    "maintenanceAffectedClientCount": 0,
                    "scoreCategory": {
                        "scoreCategory": "CLIENT_TYPE",
                        "value": "WIRED"
                    },
                    "randomMacCount": 0,
                    "starttime": 1694084400000,
                    "connectedToUdnCount": 0,
                    "clientCount": 2,
                    "endtime": 1694084700000,
                    "scoreList": [
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "POOR"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 2,
                            "endtime": 1694084700000,
                            "scoreList": [
                                {
                                    "scoreValue": -1,
                                    "unconnectedToUdnCount": 0,
                                    "duidCount": null,
                                    "clientUniqueCount": null,
                                    "maintenanceAffectedClientCount": null,
                                    "scoreCategory": {
                                        "scoreCategory": "deviceType",
                                        "value": "ALL"
                                    },
                                    "randomMacCount": null,
                                    "starttime": 1694084400000,
                                    "connectedToUdnCount": 0,
                                    "clientCount": 2,
                                    "endtime": 1694084700000
                                },
                                {
                                    "scoreValue": -1,
                                    "unconnectedToUdnCount": 0,
                                    "duidCount": null,
                                    "clientUniqueCount": null,
                                    "maintenanceAffectedClientCount": null,
                                    "scoreCategory": {
                                        "scoreCategory": "rootCause",
                                        "value": "DHCP"
                                    },
                                    "randomMacCount": null,
                                    "starttime": 1694084400000,
                                    "connectedToUdnCount": 0,
                                    "clientCount": 2,
                                    "endtime": 1694084700000
                                }
                            ]
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "FAIR"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "GOOD"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "IDLE"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NODATA"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NEW"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        }
                    ]
                },
                {
                    "scoreValue": -1,
                    "unconnectedToUdnCount": 0,
                    "duidCount": 0,
                    "clientUniqueCount": 0,
                    "maintenanceAffectedClientCount": null,
                    "scoreCategory": {
                        "scoreCategory": "CLIENT_TYPE",
                        "value": "WIRELESS"
                    },
                    "randomMacCount": 0,
                    "starttime": 1694084400000,
                    "connectedToUdnCount": 0,
                    "clientCount": 0,
                    "endtime": 1694084700000,
                    "scoreList": [
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "POOR"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "FAIR"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "GOOD"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "IDLE"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NODATA"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        },
                        {
                            "scoreValue": -1,
                            "unconnectedToUdnCount": 0,
                            "duidCount": null,
                            "clientUniqueCount": 0,
                            "maintenanceAffectedClientCount": null,
                            "scoreCategory": {
                                "scoreCategory": "SCORE_TYPE",
                                "value": "NEW"
                            },
                            "randomMacCount": null,
                            "starttime": 1694084400000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694084700000
                        }
                    ]
                }
            ],
            "siteId": "global"
        }
    ]
}
'''
