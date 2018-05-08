from jinja2 import Environment, FileSystemLoader
import yaml
from pprint import pprint as pp
from netmiko import Netmiko

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("ebgp_neighbor_template.j2")


with open("bgp_template_r4.yaml") as r4:
    r4_bgp = yaml.load(r4)
    print(r4_bgp)

with open("bgp_template_r5.yaml") as r5:
    r5_bgp = yaml.load(r5)
    print(r5_bgp)



output_r4 = template.render(bgp=r4_bgp)
output_r5 = template.render(bgp=r5_bgp)


my_device_r4 = {
    "host": "r4",
    "username": "admin",
    "password": "automate",
    "device_type": "cisco_ios"
}

my_device_r5 = {
    "host": "r5",
    "username": "admin",
    "password": "automate",
    "device_type": "cisco_ios"
}

net_conn_r4 = Netmiko(**my_device_r4)

print(net_conn_r4.find_prompt())

pp(net_conn_r4.send_config_set(output_r4))

net_conn_r5 = Netmiko(**my_device_r5)

print(net_conn_r5.find_prompt())

pp(net_conn_r5.send_config_set(output_r5))

