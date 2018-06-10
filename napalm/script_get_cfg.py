from napalm import get_network_driver
driver = get_network_driver('ios')
from multiprocessing import Pool
import json

#router = input("Enter router seperated by spaces:  ")

#host_list = router.split()

# or 


with open('/home/todd/automation/napalm_stuff/host_file') as f:
    host_list = f.read().splitlines()

un = "admin"
pw = "automate"

error_list = []
cmd_fail = []


def run_script(host):
    rtr = driver(host, un, pw)
    try:
        rtr.open()
        print("Connected to " + host)
    except:
        print("Unables to connect to host " + host)
        error_list.append(host)

    try:
        with open('config_'+ host, 'w') as conf:
            rtr_configs = rtr.get_config()
            print(host , "startup and running config saved")
            json.dump(rtr_configs, conf, sort_keys = True, indent=4 , separators=(',', ': '))
            print("*" * 52)
    except Exception as cmd_err:
        print("Command failed", host)
        print(cmd_err)
        cmd_fail.append(cmd_err)
        pass

    return error_list, cmd_fail


if __name__ == "__main__":
   with Pool(5) as p:
        print("*********************************************************************")
        print("This script will save the startup and running configs in json format")
        print("*********************************************************************")
        print(p.map(run_script, host_list)) 


