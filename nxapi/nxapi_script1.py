import requests
import json
from getpass import getpass
from pprint import pprint as pp
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

UN = input("Username: ")
PW = getpass("Password: ")

commands = input('Commands seperate with ",":  ')
cmds = commands.split(',')

url='https://64.103.37.14/ins'
print(url)

myheaders={'content-type':'application/json-rpc'}
payload = []
instance_id = 0
for command in cmds:
    instance_id += 1
    payload_dict = {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": command,
          "version": 1
        },
        "id": instance_id,
      }
    payload.append(payload_dict)
    pp(command)

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(UN,PW),verify=False).json()
pp(response)

