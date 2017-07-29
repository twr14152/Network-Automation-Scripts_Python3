#getpass will not display password
from getpass import getpass
#ConnectionHandler is the function used by netmiko to connect to devices
from netmiko import ConnectHandler

#create variables for username and password
uname = input("Username: ")
passwd = getpass("Password: ")

#with is used to open and automatically close files
#The commands.txt has all configuration commands
#To view status use the do + show command
with open("commands.txt") as f:
    cmds_to_send = f.read().splitlines()

#dictionary is used to define a device
#the device_type is key to the connection type with netmiko ssh vs api
#call the login variables

ios_rtr1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.1",
    "username": uname,
    "password": passwd,
}

ios_rtr2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.2",
    "username": uname,
    "password": passwd,
}

ios_rtr3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.3",
    "username": uname,
    "password": passwd,
}
#create a list of all the devices you will be calling in your script
devices = [ios_rtr1, ios_rtr2, ios_rtr3]
#use a for loop to iterate through the devices
for device in devices:
    #connect to the device via ssh
    net_connect = ConnectHandler(**device)
    #print the device IP to identify which device is being configured
    print(device["ip"])
    #this variable is used to capture the output of cmds sent to device
    output = net_connect.send_config_set(cmds_to_send)
    #print the output
    print(output)


