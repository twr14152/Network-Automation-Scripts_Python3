#!/usr/bin/python3

from getpass import getpass
from netmiko import ConnectHandler
from multiprocessing import Pool
from time import time

username = input('Enter username: ')
password = getpass('Enter password: ')

if len(username) < 1 : username = "automate"
if len(password) < 1 : password = "automation"

with open('commands_file_r1') as f:
    commands_list_r1 = f.read().splitlines()

with open('commands_file_r2') as f:
    commands_list_r2 = f.read().splitlines()

with open('commands_file_r3') as f:
    commands_list_r3 = f.read().splitlines()

with open('commands_file_r4') as f:
    commands_list_r4 = f.read().splitlines()

with open('commands_file_r5') as f:
    commands_list_r5 = f.read().splitlines()

with open('commands_file_r6') as f:
    commands_list_r6 = f.read().splitlines()

with open('commands_file_r7') as f:
    commands_list_r7 = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

print("----The devices being configured----")
print(devices_list)

starting_time = time()

# Updated /etc/hosts to use dns names rather than host ips

def run_script(hostname):
    print ('Connecting to device: ' + hostname)
    ip_address_of_device = hostname
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }

    net_connect = ConnectHandler(**ios_device)
    if hostname  == 'r1':
        print("hostname == r1:", hostname == 'r1')
        output = net_connect.send_config_set(commands_list_r1)
        print(output)
    elif hostname  == 'r2':
        print ("hostname == r2:", hostname == 'r2')
        output = net_connect.send_config_set(commands_list_r2)
        print(output)
    elif hostname  == 'r3':
        print ("hostname == r3: ", hostname == 'r3')
        output = net_connect.send_config_set(commands_list_r3)
        print(output)
    elif hostname  == 'r4':
        print ("hostname == r4:",  hostname == 'r4')
        output = net_connect.send_config_set(commands_list_r4)
        print(output)
    elif hostname  == 'r5':
        print ("hostname == r5:", hostname == 'r5')
        output = net_connect.send_config_set(commands_list_r5)
        print(output)
    elif hostname  == 'r6':
        print ("hostname == r6: ", hostname == 'r6')
        output = net_connect.send_config_set(commands_list_r6)
        print(output)
    elif hostname  == 'r7':
        print ("hostname == r7: ", hostname == 'r7')
        output = net_connect.send_config_set(commands_list_r7)
        print(output)
    
    print('\n---- Elapsed time=', time()-starting_time)

if __name__ == "__main__":
    with Pool(7) as p:
        print(p.map(run_script, devices_list))

