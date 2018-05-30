import json
from napalm import get_network_driver
driver = get_network_driver('eos')
veos_sw = driver('veos5', 'arista', 'arista')
veos_sw.open()

print ('Connecting to veos device')
veos_sw.load_merge_candidate(filename='config_file.cfg')
veos_sw.commit_config()
veos_sw.close()

