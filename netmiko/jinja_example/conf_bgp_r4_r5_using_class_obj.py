from netmiko import Netmiko
from getpass import getpass
from jinja2 import Environment, FileSystemLoader
from pprint import pprint


ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("ebgp_neighbor_template.j2")


class bgp_conf(object):

    def __init__(self, asn, loop0_ip, neighbor_address, peer_asn, remote_router_name, password):
        self.asn = asn
        self.loop0_ip = loop0_ip
        self.neighbor_address = neighbor_address
        self.peer_asn = peer_asn
        self.remote_router_name = remote_router_name
        self.password = password

'''
This is just being used for reference to help you build your class definition

router bgp {{ bgp.asn }}
 bgp log-neighbor-changes
 network {{ bgp.loop0_ip }} mask 255.255.255.255
 neighbor {{ bgp.neighbor_address }} remote-as {{ bgp.peer_asn }}
 neighbor {{ bgp.neighbor_address }} description ebgp-to-{{ bgp.remote_router_name }}
 neighbor {{ bgp.neighbor_address }} password {{ bgp.password }}
 neighbor {{ bgp.neighbor_address }} timers 1 3
 neighbor {{ bgp.neighbor_address }} advertisement-interval 1

'''

my_device = {
    "host": "r4",
    "username": "admin",
    "password": "automate",
    "device_type": "cisco_ios"
}

net_conn = Netmiko(**my_device)

print(net_conn.find_prompt())

# Populating variables in class bgp_conf()
bgp_cfg_r4 = bgp_conf("4", "4.4.4.4", "10.0.4.5", "5", "r5", "real_secure_pass")

output = template.render(bgp=bgp_cfg_r4)

print(output)
print(type(output))

pprint(net_conn.send_config_set(output))
show_run_r4 = net_conn.send_command("show run | beg router bgp")
show_ip_bgp_summ_r4 = net_conn.send_command("show ip bgp summ")


ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("ebgp_neighbor_template.j2")

my_device = {
    "host": "r5",
    "username": "admin",
    "password": "automate",
    "device_type": "cisco_ios"
}

net_conn = Netmiko(**my_device)

print(net_conn.find_prompt())

# Populating variables in class bgp_conf()
bgp_cfg_r5 = bgp_conf("5", "5.5.5.5", "10.0.4.4", "4", "r4", "real_secure_pass")

print(bgp_cfg_r5)

output = template.render(bgp=bgp_cfg_r5)

print(output)
print(type(output))

pprint(net_conn.send_config_set(output))

print("*" * 50)
print("Configuration verification step")


show_run_r4 = net_conn.send_command("show run | beg router bgp")
show_ip_bgp_summ_r4 = net_conn.send_command("show ip bgp summ")

pprint(show_run_r4)
pprint(show_ip_bgp_summ_r4)

print("*" * 50)
print("Configuration verification step")



show_run_r5 = net_conn.send_command("show run | beg router bgp")
show_ip_bgp_summ_r5 = net_conn.send_command("show ip bgp summ")

pprint(show_run_r5)
pprint(show_ip_bgp_summ_r5)
