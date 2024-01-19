import requests, json

url = "https://api.meraki.com/api/v1/networks/N_627126248111476961/wireless/ssids/0"

payload = '''{
    "encryptionMode": "wpa",
    "authMode": "psk",
    "name": "TheHouseJackBuilt",
    "psk": "Jackisadog"
}'''

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<>"
}

response = requests.request('PUT', url, headers=headers, data = payload)
data = json.loads(response.text)
print(json.dumps(data, indent=4))

'''
Script: Output
{
    "number": 0,
    "name": "TheHouseJackBuilt",
    "enabled": true,
    "splashPage": "None",
    "ssidAdminAccessible": false,
    "authMode": "psk",
    "psk": "Jackisadog",
    "dot11w": {
        "enabled": false,
        "required": false
    },
    "dot11r": {
        "enabled": false,
        "adaptive": false
    },
    "encryptionMode": "wpa",
    "wpaEncryptionMode": "WPA2 only",
    "ipAssignmentMode": "NAT mode",
    "adultContentFilteringEnabled": false,
    "dnsRewrite": {
        "enabled": false,
        "dnsCustomNameservers": []
    },
    "minBitrate": 11,
    "bandSelection": "Dual band operation",
    "perClientBandwidthLimitUp": 0,
    "perClientBandwidthLimitDown": 0,
    "perSsidBandwidthLimitUp": 0,
    "perSsidBandwidthLimitDown": 0,
    "mandatoryDhcpEnabled": false,
    "visible": true,
    "availableOnAllAps": true,
    "availabilityTags": [],
    "speedBurst": {
        "enabled": false
    }
}
'''
