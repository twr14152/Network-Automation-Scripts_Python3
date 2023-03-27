import requests
import json


url = "http://localhost:58000/api/v1"

headers = {"Content-Type": "application/json"}
data = json.dumps({"username": "admin", "password": "cisco123!"})
resp = requests.post(url + "/ticket", data=data, headers=headers)

print(f"\nStatus code: {resp.status_code}\n")
result = resp.json()
#print(json.dumps(result, indent=4))

ticket = result["response"]["serviceTicket"]
print(f"\nTicket value to use is {ticket}\n")

# Add a serversg

headers = {"X-Auth-Token": ticket, "Content-Type": "application/json"}
data = json.dumps({
    "aaa": {
        "ipAddress": "10.10.0.22",
        "key": "Test_key"
        },
    "dns": {
        "ipAddress": "10.10.0.22",
            "name": "testlab.com"
        },
    "netflow": {
        "port": "9995",
            "reflectionIp": "10.10.0.22"
        },

    "ntp" : {"serverIp": "10.10.0.22"},
    "syslog" : [
        {"serverIp": "5.5.5.5"},
	{"serverIp": "6.6.6.6"},
	{"serverIp": "7.7.7.7"},
   ],
})

resp = requests.put(url+"/wan/network-wide-setting", headers=headers, data=data)

print(f"\nStatus code: {resp.status_code}\n")
result = resp.json()
print(json.dumps(result, indent=4))

'''
toddriemenschneider@Todds-MacBook-Pro-2 % python3 update_device_config.py

Status code: 201


Ticket value to use is NC-104-57a16f693cb447f5b678-nbi


Status code: 200

{
    "response": {
        "aaa": {
            "ipAddress": "10.10.0.22",
            "key": "Test_key"
        },
        "dns": {
            "ipAddress": "10.10.0.22",
            "name": "testlab.com"
        },
        "netflow": {
            "port": "9995",
            "reflectionIp": "10.10.0.22"
        },
        "ntp": {
            "serverIp": "10.10.0.22"
        },
        "syslog": [
            {
                "serverIp": "5.5.5.5"
            },
            {
                "serverIp": "6.6.6.6"
            },
            {
                "serverIp": "7.7.7.7"
            }
        ]
    },
    "version": "1.0"
}
toddriemenschneider@Todds-MacBook-Pro-2 %
'''
