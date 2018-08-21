# Network-Automation-Scripts using Python3
# Libraries: Pyeapi, Netmiko, Napalm, Telnetlib, Restconf, Nxapi, Nornir
This repository hold various automation scripts I've written over the years. 
My goal has been to use this as a repository for knowledge retention as well knowlege sharing.
I plan to continue to grow this respository as long as I'm still doing stuff in the network automation space.

This has been a iterative learning process for me and I will be archiving or deleting scripts that no longer have value

Nornir - TestDrive
- Cisco IOS - GNS3 lab - nornir/using_netmiko_plugin
- Arista Ceos lab - nornir/using_napalm_plugin 


Nxapi
- Found this api documentation to be lacking
- Script examples I found were rigid and not very flexible
- Created a script to allow user to enter any commands (config/show) w/o having to rewrite their script.
  - nxapi_script_ex1.py

Restconf
- Still learning this api
- restconf_ex1.py

Pyeapi - Python client for Aristas eAPI
 - Posted configs and validation from demo
 - Interactive config script for multiple devices (multi_dev_cfg_script2.py )
 - hidden host config file, needs to be located in ~/.eapi.conf
 - created two sample scripts

Netmiko testing
- scp - file transfers to veos devices hosted using vagrant
- Network-Automation-Scripts_Python3/netmiko/NetworkDiscovery/two_files/
  - discovery_script.py - w/error handling and logging
  - host_file.txt
- Added 3 examples of how to use jinja templates with netmiko
 - conf_bgp_r4_r5_using_class_obj. - uses class object to populate template
 - conf_bgp_r4_r5_using_dict.py - uses dictionaries to populate template
 - conf_bgp_yaml_jinja2.py - uses yaml files to populate a jinja2 template
- Created new script that provide you a sandbox to say how many devices, what devices, and what to configure on each
    - ssh_sandbox.py
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
- napalm discovery script and post script
    - discovery_ios_svc_now.py
    - post_svc_now_rest_api.py
- created a config_scripts directory added new script
    - script_config_ios.py
- added new get_facts and get config script to directory
- Testing with python3 napalm_base and napalm_ios
- In my gns3 environment I'm using the following code
    - C7200-ADVENTERPRISEK9-M, Version 15.2(4)S7
    - IOS provides access to a subset of napalms features
    - EOS has been a more feature rich testbed with napalm

Testing Telnetlib module
- Use python3 telnetlib module
- capture output of scripts



