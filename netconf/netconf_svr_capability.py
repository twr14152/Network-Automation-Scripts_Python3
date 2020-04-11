from ncclient import manager

HOSTS =  ['ios-xe-mgmt-latest.cisco.com', 'ios-xe-mgmt.cisco.com']

for HOST in HOSTS:
    m = manager.connect(
        host= HOST,
        port=10000,
        username="developer",
        password="C1sco12345",
        hostkey_verify=False,
        device_params={'name': 'default'},
        look_for_keys=False)
        
    print("#" * 100)
    print("*" * 100)
    print("Netconf_Server_capabilities on :", HOST)
    linenum = 0
    for data in m.server_capabilities: 
        linenum += 1
        if "http://cisco.com/ns/yang/Cisco-IOS-XE-native" in data:
            print(linenum, "HERES THE XMLNS YOUR USING:" ,"-----",  data)
        else:
            print(linenum, data)
    
    print("Done with host: ", HOST)
    print("*" * 100)
    print("#" * 100)
