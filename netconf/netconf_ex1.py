
from ncclient import manager

conn = manager.connect(
        host='ios-xe-mgmt.cisco.com',
        port=10000,
        username="root",
        password="D_Vay!_10&",
        hostkey_verify=False,
        device_params={'name': 'default'},
        look_for_keys=False)

print("Netconf_Server_capabilities")
for data in conn.server_capabilities: 
    print(data)

print("*" * 50)

print("Netconf_Client_capabilities")
for data in conn.client_capabilities:
    print(data)
