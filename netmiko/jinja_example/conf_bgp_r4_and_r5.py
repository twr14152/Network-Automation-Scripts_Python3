from netmiko import Netmiko
from getpass import getpass
from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import time

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("ebgp_neighbor_template.j2")

my_device = {
    "host": "r4",
    "username": "admin",
    "password": "automate",
    "device_type": "cisco_ios"
}

net_conn = Netmiko(**my_device)

print(net_conn.find_prompt())

r4_bgp_nei_dict = {
    "asn": "4",
    "loop0_ip": "4.4.4.4",
    "neighbor_address": "10.0.4.5",
    "peer_asn": "5",
    "remote_router_name": "r5",
    "password": "real_secure_pass",
    }

'''
router bgp {{ bgp.asn }}
 bgp log-neighbor-changes
 network {{ bgp.loop0_ip }} mask 255.255.255.255
 neighbor {{ bgp.neighbor_address }} remote-as {{ bgp.peer_asn }}
 neighbor {{ bgp.neighbor_address }} description ebgp-to-{{ bgp.remote_router_name }}
 neighbor {{ bgp.neighbor_address }} password {{ bgp.password }}
 neighbor {{ bgp.neighbor_address }} timers 1 3
 neighbor {{ bgp.neighbor_address }} advertisement-interval 1

'''


print(r4_bgp_nei_dict)


output = template.render(bgp=r4_bgp_nei_dict)

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


r5_bgp_nei_dict = {
    "asn": "5",
    "loop0_ip": "5.5.5.5",
    "neighbor_address": "10.0.4.4",
    "peer_asn": "4",
    "remote_router_name": "r4",
    "password": "real_secure_pass",
    }

'''
router bgp {{ bgp.asn }}
 bgp log-neighbor-changes
 network {{ bgp.loop0_ip }} mask 255.255.255.255
 neighbor {{ bgp.neighbor_address }} remote-as {{ bgp.peer_asn }}
 neighbor {{ bgp.neighbor_address }} description ebgp-to-{{ bgp.remote_router_name }}
 neighbor {{ bgp.neighbor_address }} password {{ bgp.password }}
 neighbor {{ bgp.neighbor_address }} timers 1 3
 neighbor {{ bgp.neighbor_address }} advertisement-interval 1

'''



print(r5_bgp_nei_dict)

output = template.render(bgp=r5_bgp_nei_dict)

print(output)
print(type(output))

pprint(net_conn.send_config_set(output))

print("*" * 50)
print("Configuration verification step")
print("Waiting 10 secs for bgp to come up")
time.sleep(10)

show_ip_bgp_summ_r4 = net_conn.send_command("show ip bgp summ")
show_ip_rt_r4 = net_conn.send_command("show ip route")

pprint(show_ip_bgp_summ_r4)
pprint(show_ip_rt_r4)

print("*" * 50)
print("Configuration verification step")
print("Waiting 5 secs for bgp to come up")
time.sleep(5)


show_ip_bgp_summ_r5 = net_conn.send_command("show ip bgp summ")
show_ip_rt_r5 = net_conn.send_command("show ip route")

pprint(show_ip_bgp_summ_r5)
pprint(show_ip_rt_r5)
