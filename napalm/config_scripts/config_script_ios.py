from napalm import get_network_driver
from pprint import pprint as pp
from multiprocessing import Pool

routers = ['r1', 'r2', 'r3', 'r4', 'r5']

def run_script(router):
    driver = get_network_driver('ios')
    rtr = driver(router, 'admin', 'automate')
    rtr.open()
    print("Connected to: ", (rtr.hostname))
    pp(rtr.device.send_config_from_file('/home/todd/automation/napalm_stuff/ACL.cfg'))
    pp(rtr.device.send_config_from_file('/home/todd/automation/napalm_stuff/global_config.cfg'))
    pp(rtr.device.send_command('write memory'))

if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(run_script, routers))
    



    

