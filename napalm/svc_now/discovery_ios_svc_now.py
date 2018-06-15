import json
from napalm import get_network_driver
from multiprocessing import Pool
from pprint import pprint as pp

#router = input("Enter router seperated by spaces:  ")
#host_list = router.split()

with open('host_file') as f:
    host_list = f.read().splitlines()

un = "admin"
pw = "automate"

error_list = []

driver = get_network_driver('ios')

def run_script(host):
    rtr = driver(host, un, pw)
    try:
        rtr.open()
        print("Connected to " + host)
    except:
        print("Unables to connect to host " + host)
        error_list.append(host)

    try:
        with open('snow_device_facts_'+ host + '.json', 'w', encoding='utf-8') as device:
            rtr_facts = rtr.get_facts()
            rtr_facts2 = rtr.get_facts()
            rtr_facts['name'] = rtr_facts.pop('hostname')
            rtr_facts2['manufacturer'] = rtr_facts2.pop('vendor')
            rtr_facts['model_number'] = rtr_facts.pop('model')
            rtr_facts2['model_id'] = rtr_facts2.pop('model')
            rtr_facts["ip_address"] = host
            rtr_facts2["firmware_version"] = rtr_facts2.pop("os_version")
            rtr_interfaces = rtr.get_interfaces()
            rtr_snmp = rtr.get_snmp_information()
            rtr_all = {**rtr_facts, **rtr_facts2, **rtr_snmp, **rtr_interfaces}
            pp("*" * 70)
            json.dump(rtr_all, device, sort_keys = True, indent=4 , separators=(',', ': '))
    except:
        pass

    return error_list

if __name__ == "__main__":
   with Pool(5) as p:
        print(p.map(run_script, host_list)) 
