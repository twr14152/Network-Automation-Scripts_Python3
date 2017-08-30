#!/usr/bin/python3
#This script will allow for user pick hosts and enter show commands interactively
#
#Enable Multiprocessing
from multiprocessing import Pool
#getpass will not display password
from getpass import getpass
#ConnectionHandler is the function used by netmiko to connect to devices
from netmiko import ConnectHandler
#Time tracker
from time import time

#create variables for username and password
#create variables for configs and hosts
uname = input("Username: ")
passwd = getpass("Password: ")
cmd = input("Enter config commands seperated by ',': ")
host = input("Enter the host IPs seperate with space: ")

#This will allow you to just press enter
#This sets default values Not recommanded in any place but a lab
if len(uname) < 1 : uname = "automate"
if len(passwd) < 1 : passwd = "automation"

#This will put hosts and commands entered into list format
hosts = host.split()
cmds = cmd.split(",")

starting_time = time()

#this for loop is used to iterate through the devices
def run_script(host_ip):
    ios_rtr = {
        "device_type": "cisco_ios",
        "ip": host_ip,
        "username": uname,
        "password": passwd,
        }
    #connect to the device via ssh
    net_connect = ConnectHandler(**ios_rtr)
    #print the device IP or Hostname
    print("Connected to host:", host_ip)
    #this for loop is used to iterate through the show commands
    for show_commands in cmds:
        output = net_connect.send_command(show_commands)
        print(output)
        print('\n---- Elapsed time=', time()-starting_time)

if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(run_script, hosts))

