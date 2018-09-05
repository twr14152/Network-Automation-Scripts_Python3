from nornir.core import InitNornir                                            
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking

nr = InitNornir(config_file="config.yaml")

lab_hosts = nr.filter(site="lab", role="spline")

result = lab_hosts.run(task=networking.napalm_get,
                       getters=["facts", "config"])

print_result(result)

print(nr.inventory.hosts)
print(nr.inventory.groups)

