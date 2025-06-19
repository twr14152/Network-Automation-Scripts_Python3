# This script is a sample used to connect to FRR device in containerlabs
# Because of the vtysh syntax its use can be for show or config commands

from netmiko import ConnectHandler


device = {
    'device_type': 'linux', 
    'ip': ' 172.20.20.9',
    'username': 'admin',
    'password': 'admin',
}

commands = input("Enter commands: ")
cmds = commands.split(",")

vtysh_command = 'vtysh '

for cmd in cmds:
    vtysh_command += f' -c "{cmd}"'


print("+++")
print(vtysh_command)
print("+++")


net_connect = ConnectHandler(**device)
output = net_connect.send_command(vtysh_command)

print(output)

