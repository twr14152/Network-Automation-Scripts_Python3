import requests

requests.packages.urllib3.disable_warnings()

HOST = "ios-xe-mgmt.cisco.com:9443"
USER = "developer"
PW = "C1sco12345"

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/interface/"
del_url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=72" 

headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json'
}

delete_response = requests.delete(url=del_url, auth=(USER, PW), verify=False, headers=headers)
get_response = requests.get(url, headers=headers, auth=(USER, PW), verify=False)

print(delete_response.text)
print(get_response.text)
