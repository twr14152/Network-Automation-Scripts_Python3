#!/home/toddriemenschneider/myenv_py3.11/bin/python
from netmiko import ConnectHandler

'''
╭───────────────────┬─────────────────────────────────┬─────────┬───────────────────╮
│        Name       │            Kind/Image           │  State  │   IPv4/6 Address  │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-ce1     │ ceos                            │ running │ 172.20.20.5       │
│                   │ ceosimage:latest                │         │ 3fff:172:20:20::5 │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-ce2     │ ceos                            │ running │ 172.20.20.2       │
│                   │ ceosimage:latest                │         │ 3fff:172:20:20::2 │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-client1 │ linux                           │ running │ 172.20.20.6       │
│                   │ ghcr.io/hellt/network-multitool │         │ 3fff:172:20:20::6 │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-client2 │ linux                           │ running │ 172.20.20.8       │
│                   │ ghcr.io/hellt/network-multitool │         │ 3fff:172:20:20::8 │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-core1   │ linux                           │ running │ 172.20.20.9       │
│                   │ quay.io/frrouting/frr:10.3.1    │         │ 3fff:172:20:20::9 │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-core2   │ linux                           │ running │ 172.20.20.4       │
│                   │ quay.io/frrouting/frr:10.3.1    │         │ 3fff:172:20:20::4 │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-d1      │ linux                           │ running │ 172.20.20.7       │
│                   │ quay.io/frrouting/frr:10.3.1    │         │ 3fff:172:20:20::7 │
├───────────────────┼─────────────────────────────────┼─────────┼───────────────────┤
│ clab-lab2-d2      │ linux                           │ running │ 172.20.20.3       │
│                   │ quay.io/frrouting/frr:10.3.1    │         │ 3fff:172:20:20::3 │
╰───────────────────┴─────────────────────────────────┴─────────┴───────────────────╯
'''

core_rtrs = ['clab-lab2-core1', 'clab-lab2-core2']
dist_rtrs = ["clab-lab2-d1", "clab-lab2-d2"]
access_rtrs = ["clab-lab2-ce1", "clab-lab2-ce2"]

ans1 = input("Login to core routers (y/n):")
ans2 = input("Login to dist routers (y/n):")
ans3 = input("Login to access routers (y/n):")
ans4 = input("Configure access routers (y/n):")

if ans1 == 'y':
    for host in core_rtrs:
        device = {
        'device_type': 'linux', 
        'ip': host,
        'username': 'admin',
        'password': 'admin',
        }
        print(f"connecting to: {host}" )
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
    

if ans2 == 'y':
    for host in dist_rtrs:
        device = {
        'device_type': 'linux', 
        'ip': host,
        'username': 'admin',
        'password': 'admin',
        }
        print(f"connecting to: {host}" )
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

if ans3 == 'y':
    for host in access_rtrs:
        device = {
        'device_type': 'arista_eos',
        'ip': host,
        'username': 'admin',
        'password': 'admin',
        'secret' : 'admin',
        }
        print(f"connecting to: {host}" )
        commands = input("Enter commands: ")
        cmds = commands.split(",")

        for cmd in cmds:
            net_connect = ConnectHandler(**device)
            net_connect.enable()
            output = net_connect.send_command(cmd)
            print(output)


if ans4 == 'y':
    for host in access_rtrs:
        device = {
        'device_type': 'arista_eos',
        'ip': host,
        'username': 'admin',
        'password': 'admin',
        'secret' : 'admin',
        }
        print(f"connecting to: {host}" )
        commands = input("Enter commands: ")
        cmds = commands.split(",")
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_config_set(cmds)
        print(output)
        output = net_connect.send_command("show running-config")
        print(output)


