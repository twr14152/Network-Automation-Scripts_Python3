#!/usr/bin/python3
#
#This script will allow up to update a group of hosts with common config shared by all
#
#getpass will not display password
from getpass import getpass
#ConnectionHandler is the function used by netmiko to connect to devices
from netmiko import ConnectHandler

#create variables for username and password
#create variables for configs and hosts
uname = input("Username: ")
passwd = getpass("Password: ")
cmd = input("Enter config commands seperated by ',': ")
host = input("Enter the DNS hostnames or IPs seperated by a space: ")

#This will allow you to just press enter
#This sets default values Not recommanded in any place but a lab
if len(uname) < 1 : uname = "automate"
if len(passwd) < 1 : passwd = "automation"

#create lists of hosts and cmds to iterate through
#This list can contain show or config commands show commands require "do + command"
hosts = host.split()
cmds = cmd.split(",")

#For loop used to iterate through the devices
for host in hosts:
    host_ip = host
    ios_rtr = {
        "device_type": "cisco_ios",
        "ip": host_ip,
        "username": uname,
        "password": passwd,
        }
    #connect to the device via ssh
    net_connect = ConnectHandler(**ios_rtr)
    #print the device IP to identify which device is being configured
    print("Connected to host:", host_ip)
    #this variable is used to capture the output of cmds sent to device
    output = net_connect.send_config_set(cmds)
    #print the output
    print(output)




