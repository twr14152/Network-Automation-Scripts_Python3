from nornir.core import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.plugins.functions.text import print_result

nr = InitNornir()

result = nr.run(
              napalm_get,
              getters=['get_facts', 'get_config',])              

print_result(result)
