import requests
from getpass import getpass
from pprint import pprint as pp


user = ''
pwd = getpass("enter password: " )

with open('host_file2') as f:
    host_list = f.read().splitlines()

print(host_list)

for host in host_list:
    with open('snow_device_facts_'+ host + '.json', 'r', encoding='utf-8') as device:
        # Set the request parameters
        url = 'https://<>.<>.com/api/adx/external_ci_import/createCI'
        #url = 'https://<>.<>.com/api/now/table/cmdb_ci_netgear'
        # Set proper headers
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        # Do the HTTP request
        print(device)
        print(host)
        response = requests.post(url, auth=(user, pwd), headers=headers , data=device)
        # Check for HTTP codes 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        data = response.json()
        print(data)

