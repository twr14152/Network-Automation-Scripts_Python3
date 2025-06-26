from netmiko import ConnectHandler


core_rtrs = ['clab-lab2-core1', 'clab-lab2-core2']
dist_rtrs = ["clab-lab2-d1", "clab-lab2-d2"]

with open('core1.cfg') as f:
    commands_core1 = f.read().splitlines()

with open('core2.cfg') as f:
    commands_core2 = f.read().splitlines()

with open('d1.cfg') as f:
    commands_d1 = f.read().splitlines()

with open('d2.cfg') as f:
    commands_d2 = f.read().splitlines()


ans1 = input("Login to core routers (y/n):")
ans2 = input("Login to dist routers (y/n):")



if ans1 == 'y':
    for host in core_rtrs:
        device = {
        'device_type': 'linux', 
        'ip': host,
        'username': 'admin',
        'password': 'admin',
        }
        print(f"connecting to: {host}" )

        vtysh_command = 'vtysh '

        if host == 'clab-lab2-core1':
            print(f"Configuring: {host}")
            for cmd in commands_core1:
                vtysh_command += f' -c "{cmd}"'

        if host == 'clab-lab2-core2':
            print(f"Configuring: {host}")
            for cmd in commands_core2:
                vtysh_command += f' -c "{cmd}"'
       


        print("+++")
        print(vtysh_command)
        print("+++")

        net_connect = ConnectHandler(**device)
        output = net_connect.send_command(vtysh_command)
        print(output)
        print("+++  New Config +++")
        show_run = net_connect.send_command("vtysh -c 'show running-config'")
        print(show_run)
        print("+++ End Config +++")
    

if ans2 == 'y':
    for host in dist_rtrs:
        device = {
        'device_type': 'linux', 
        'ip': host,
        'username': 'admin',
        'password': 'admin',
        }
        print(f"connecting to: {host}" )

        vtysh_command = 'vtysh '

        if host == 'clab-lab2-d1':
            print(f"Configuring: {host}")
            for cmd in commands_d1:
                vtysh_command += f' -c "{cmd}"'

        if host == 'clab-lab2-d2':
            print(f"Configuring: {host}")
            for cmd in commands_d2:
                vtysh_command += f' -c "{cmd}"'
       


        print("+++")
        print(vtysh_command)
        print("+++")

        net_connect = ConnectHandler(**device)
        output = net_connect.send_command(vtysh_command)
        print(output)
        print("+++  New Config +++")
        show_run = net_connect.send_command("vtysh -c 'show running-config'")
        print(show_run)
        print("+++ End Config +++")


