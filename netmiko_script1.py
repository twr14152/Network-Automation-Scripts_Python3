from getpass import getpass
from netmiko import ConnectHandler


uname = input("Username: ")
passwd = getpass("Password: ")

with open("commands.txt") as f:
    cmds_to_send = f.read().splitlines()

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

devices = [ios_rtr1, ios_rtr2, ios_rtr3]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(device["ip"])
    output = net_connect.send_config_set(cmds_to_send)
    print(output)


