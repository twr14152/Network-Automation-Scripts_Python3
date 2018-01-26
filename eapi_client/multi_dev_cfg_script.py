import pyeapi
from pprint import pprint as pp

cmds1 = input('Enter commands for veos1 seperate with ",": ')
cmds2 = input('Enter commands for veos2 seperate with ",": ') 
cmds3 = input('Enter commands for veos3 seperate with ",": ') 

hosts = input('Enter hosts seperated by spaces: ')
devices = hosts.split()
commands1 = cmds1.split(',')
commands2 = cmds2.split(',')
commands3 = cmds3.split(',')

err_host = []

for host in devices:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Pre-change State: ", host)
    try:
        node = pyeapi.connect_to(host)
        pp(node.enable(['show running-config']))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    except Exception as unknown_error:
        print("************************************")
        print("Unable to log into this device:", host)
        print(unknown_error)
        err_host.append(host)
        print("Errors logging into:", err_host)
        print("************************************")
        continue
    if host == 'veos1':
        try:
            pp(node.config(commands1))
            print("Post-change state: ", host)
            pp(node.enable(['show running-config']))
        except Exception as cmd_error:
            print("Command not working, make sure syntax is correct")
            print("Problem with commands on: ", host)
            print(cmd_error)
            continue
    elif host == 'veos2':
        try:
            pp(node.config(commands1))
            print("Post-change state: ", host)
            pp(node.enable(['show running-config']))
        except Exception as cmd_error:
            print("Command not working, make sure syntax is correct")
            print("Problem with commands on: ", host)
            print(cmd_error)
            continue
    elif host == 'veos3':
        try:
            pp(node.config(commands1))
            print("Post-change state: ", host)
            pp(node.enable(['show running-config']))
        except Exception as cmd_error:
            print("Command not working, make sure syntax is correct")
            print("Problem with commands on: ", host)
            print(cmd_error)
            continue
       
print('Problems connecting to these hosts: ',  err_host)
