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
        with open('device_facts_'+ host + '.json', 'w', encoding='utf-8') as device:
            rtr_facts = rtr.get_facts()
            pp(rtr.get_facts())
            json.dump(rtr_facts, device, sort_keys = True, indent=4 , separators=(',', ': '))
            pp("*" * 52)
    except:
        pass

    return error_list

if __name__ == "__main__":
   with Pool(5) as p:
        print(p.map(run_script, host_list)) 
