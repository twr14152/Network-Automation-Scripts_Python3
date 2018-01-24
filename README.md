# Network-Automation-Scripts using Python3
# Libraries: Pyeapi, Netmiko, Napalm, Telnetlib
Network automation scripts I've written using various python libraries

Python client for eapi (pyeapi) for Arista devices
 - Interactive config script for multiple devices (multi_device_script.py)
 - hidden host config file, needs to be located in ~/.eapi.conf
 - created two sample scripts

Testing Netmiko module
- Created a very basic ssh script useful for discovery + updated with error handling
- Created script that can handle multiple device with multiple unique configuration files
- Added multiprocessing to speed up
    - netmiko_multi_dev_cfg.py
- Added multiprocessing Pools to scripts to speed them up
    - netmiko_script5.py
    - netmiko_show_cmds.py
    - netmiko speed comparison between serial and multi-processing pools
- netmiko_script#.py
- capture output of scripts

Napalm for eos
- Tested with ipython(python3.6) -> EOS_lab_Napalm_test_results
- napalm_eos_script1.py

Napalm for cisco ios
- Tested with python3.4 napalm_base and napalm_ios
- Believe the ios image I am running in GNS3 is problematic with Napalm. 
    - C7200-ADVENTERPRISEK9-M, Version 15.2(4)S7
- Work a round as been to comment out code thats problematic with the ios version I'm running
- napalm_script1.py will execute show commands while looping through devices
- Have yet to get merge code functionality to work on my devices

Testing Telnetlib module
- Use python3 telnetlib module
- capture output of scripts



