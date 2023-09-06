#!/usr/bin/python

import requests
import json

requests.packages.urllib3.disable_warnings()

#Get auth token
url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)
data = json.loads(response.text)
token = data['Token']


#Get client info
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health"

payload = {}
headers = {'X-Auth-Token': token}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
data = json.loads(response.text)
print(json.dumps(data, indent=4))

(devcor_ve) pi@RaspPi4:~/Coding/Python_folder/devcor_stuff/dnac $ ./get_client_health_dnac.py
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
                    "starttime": 1694000100000,
                    "connectedToUdnCount": 0,
                    "clientCount": 2,
                    "endtime": 1694000400000
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
                    "starttime": 1694000100000,
                    "connectedToUdnCount": 0,
                    "clientCount": 2,
                    "endtime": 1694000400000,
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 2,
                            "endtime": 1694000400000,
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
                                    "starttime": 1694000100000,
                                    "connectedToUdnCount": 0,
                                    "clientCount": 2,
                                    "endtime": 1694000400000
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
                                    "starttime": 1694000100000,
                                    "connectedToUdnCount": 0,
                                    "clientCount": 2,
                                    "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                    "starttime": 1694000100000,
                    "connectedToUdnCount": 0,
                    "clientCount": 0,
                    "endtime": 1694000400000,
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
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
                            "starttime": 1694000100000,
                            "connectedToUdnCount": 0,
                            "clientCount": 0,
                            "endtime": 1694000400000
                        }
                    ]
                }
            ],
            "siteId": "global"
        }
    ]
}
