#The purpose of this script is to show how to configure a juniper from a seperate config file
from netmiko import ConnectHandler


rtr1 = {
    'device_type': 'juniper',
    'ip':   '127.0.0.1',
    'username': 'admin',
    'password': 'Juniper',
    'port': 2222,
    'verbose': False
}

net_connect = ConnectHandler(**rtr1)
print("************Show commands*************")
output1 = net_connect.send_command("show config| display set")
output2 = net_connect.send_command("show system information | match Hostname:")
print(output1)
print(output2)
print("*******" * 10)
print("***********Config mode********")
config_output = net_connect.send_config_from_file("config.txt")
print(config_output)
config_output1 = net_connect.config_mode()
print(config_output1)
config_output2 = net_connect.send_command("show|compare")
print(config_output2)
validate = input("Does everything look correct? (y/n): ")
if validate == 'y':
    commit = net_connect.commit()
    print(commit)
    output3 = net_connect.disconnect()
    print(output3)
else:
    output4 = net_connect.disconnect()
    print(output4)
    print("Somethings wrong with your config")
