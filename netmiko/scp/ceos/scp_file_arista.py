#!/usr/bin/env python3
from netmiko import ConnectHandler, file_transfer


eos1 = { 
    'device_type': 'arista_eos',
    'host': 'localhost',
    'username': 'arista',
    'password': 'arista',
    'file_system': '/mnt/flash',
    'port': 2022
}

eos2 = { 
    'device_type': 'arista_eos',
    'host': 'localhost',
    'username': 'arista',
    'password': 'arista',
    'file_system': '/mnt/flash',
    'port': 2023
}

source_file = "test_file.txt"
dest_file = "test_file.txt"
direction = 'put'

for net_device in (eos1, eos2):
    file_system = net_device.pop('file_system')
    ssh_conn = ConnectHandler(**net_device)
    enable_pw = ssh_conn.enable()
    print(enable_pw)
    transfer_dict = file_transfer(ssh_conn,
                                  source_file=source_file,
                                  dest_file=dest_file,
                                  file_system=file_system,
                                  direction=direction,
                                  overwrite_file=True)
    print(transfer_dict)
    pause = input("Hit enter to continue: ")
