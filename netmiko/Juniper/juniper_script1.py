from netmiko import ConnectHandler

# This example shows how to issue show and config commands on a juniper device

rtr1 = {
    'device_type': 'juniper',
    'ip':   '127.0.0.1',
    'username': 'admin',
    'password': 'Juniper',
    'port': 2222,
    'verbose': False
}

# This is the same device in my lab just using it to demonstrate what multiple devices would look like
rtr2 = {
    'device_type': 'juniper',
    'ip':   '127.0.0.1',
    'username': 'admin',
    'password': 'Juniper',
    'port': 2222,
    'verbose': False
}


routers = [rtr1, rtr2]

for dev in routers:  
    net_connect = ConnectHandler(**dev)
    print("************Show commands*************")
    output1 = net_connect.send_command("show config| display set")
    output2 = net_connect.send_command("show system information | match Hostname:")
    print(output1)
    print(output2)
    print("*******" * 10)
    print("***********Config mode********")
    net_connect.config_mode()
    config_output1 = net_connect.send_command("set interfaces et-0/0/0 description netmiko_juniper_test_script") 
    print(config_output1)
    #Commit commands
    commit = net_connect.commit(and_quit=True)
    print(commit)
    print("************Show command*************")
    output3 = net_connect.send_command("show interfaces description")
    print(output3)

