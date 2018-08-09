from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.functions.text import print_result


target = input("Pick group of devices to configure core, distribution, access: ")
cfgs = input("Enter configuration lines seperated by ',': ")
cfgs_items = cfgs.split(",")
print(cfgs_items)

nr = InitNornir()
target_host = nr.filter(site=target)


result = target_host.run(
    task=netmiko_send_config,
     config_commands=cfgs_items
)

print_result(result)
