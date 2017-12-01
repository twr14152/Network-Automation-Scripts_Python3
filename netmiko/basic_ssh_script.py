from getpass import getpass
from netmiko import ConnectionHandler

uname = input("Username: ")
passwd = getpass("Password: ")
cmd = input("Enter show commands separated by ',': ")
host = input("Enter the host IPs separate with space: ")

if len(uname) < 1: uname = "<default>"
if len(passwd) < 1: passwd = "<default>"

hosts = host.split()
cmds = cmd.split(",")

for ip in hosts:
    hp_rtr = {
        "device_type": "hp_procurve",
        "ip": ip,
        "username": uname,
        "password": passwd,
        }

    net_connect = ConnectHandler(**hp_rtr)
    print("Connected to host", ip)
    for show_commands in cmds:
        output = net_connect.send_command(show_commands)
        print("Command issued:",show_commands)
        print(output)
        print("++++++++++++++++++++++++++++++++++++++++++++++")
    print("End of output for show command on device ", ip)
