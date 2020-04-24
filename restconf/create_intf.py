import requests

requests.packages.urllib3.disable_warnings()

HOST = "ios-xe-mgmt.cisco.com:9443"
USER = "developer"
PW = "C1sco12345"


url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/interface/"

data = '''
{
	"Cisco-IOS-XE-native:Loopback": {
          "name": 72,
          "description": "RESTCONF_TEST",
          "ip": {
            "address": {
              "primary": {
                "address": "72.72.72.72",
                "mask": "255.255.255.255"
              }
            }
          }
	}
}
'''

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json'
}

post_response = requests.post(url, auth=(USER, PW) , verify=False, headers=headers, data = data)
get_response = requests.get(url, headers=headers, auth=(USER, PW), verify=False)

print(post_response.text)
print(get_response.text)
