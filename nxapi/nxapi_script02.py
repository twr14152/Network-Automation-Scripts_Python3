"""
File - nxapi_script02.py
Author - Todd Riemenschneider
Date - 03.26.2020
"""
# Requests library is necessary to interface with nxapi
import requests
# Json is the data format we are using to communicate over http/https
import json
# Getpass is optional and is used to hide passwords
from getpass import getpass
# pprint is used to improve json readability
from pprint import pprint as pp
# This was used to disable annoying SSL Warning legitament or otherwise
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# This line actually disabled the warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

UN = "admin"
PW = "Admin_1234!"
target = 'sbx-nxos-mgmt.cisco.com'
#UN = input("Username: ")
#PW = getpass("Password: ")
#target = input("target host ip or dns name: ")

#if len(target) <= 0:
#    target = 'sbx-nxos-mgmt.cisco.com'

# This is where you enter your commands
commands = input('Commands seperate with ",":  ')
# This turns your text strings into list format separating commands on the ","
cmds = commands.split(',')

# This is the target hosts your connecting to
url='https://' + target + '/ins'
print(url)

# This lets the target host know what type of data to expect
myheaders={'content-type':'application/json-rpc'}
# Created empty list to hold dictionary that will be expanding as we iterate through commands
payload = []
# This was used to number the json instance id's as well iterate through the commands
instance_id = 0
# iterate through the cmds lists
for command in cmds:
    # add one to instance_id to number json instance
    instance_id += 1
    # This dictionary will grow with each command that gets looped through
    payload_dict = {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            # This is where the individual command gets entered into the dictionary
          "cmd": command,
          "version": 1
        },
        # This is were the instance_id is applied to keep track of the json instances your commands create
        "id": instance_id,
      }
    # This command then applies the dictionary to the empty payload list that was created above the for loop
    # This gets added to every iteration through the for loop
    payload.append(payload_dict)
    pp(command)

# This applied the commands to the target device to execute, also the verify=False is necessary to work in lab
# SSL set up is ok for lab, you would potentially want the verify process in production
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(UN,PW),verify=False).json()
#Prints output in a more readable way
print(json.dumps(response, indent=2, sort_keys=True))
