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
        deviceInfo = i["hostname"]+" "+i["type"]+" "+i["serialNumber"]+" "+i["softwareVersion"]+" "+i["productId"]
        print(deviceInfo)
    except:
        print(f"Unable to read device {count}")
    count += 1

##########################
#To see all device info   
#print(json.dumps(i, indent=4))

'''
% python3 get_device_info.py

Ticket value to use is NC-79-571f3a0a96fe41af8dc5-nbi


Status Code: 200

Device 1
a10_s1 Switch CAT10102UG4- 15.0 2960-24TT
Device 2
Unable to read device 2
Device 3
Unable to read device 3
Device 4
core_r2 Router FDO1302WPFM- 15.4 ISR4321
Device 5
core2 MultiLayerSwitch CAT1010JRE1- 16.3.2 3650-24PS
Device 6
Core1 MultiLayerSwitch CAT101089TI- 16.3.2 3650-24PS
Device 7
core_r1 Router FDO1302887G- 15.4 ISR4321
Device 8
Unable to read device 8

'''
