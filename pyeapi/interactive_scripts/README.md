# Script outputs

# show command script

```
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ python3 pyeapi_show_cmds_script.py
Number of devices to connect to: 2
Enter host device: ceos1
Enter commands for device seperate with ",": show running-config, show ip interface brief
['show running-config', ' show ip interface brief']


Enter host device: ceos2
Enter commands for device seperate with ",": show running-config, show ip interface brief
['show running-config', ' show ip interface brief']


 This is the dictionary before the loop {'ceos1': ['show running-config', ' show ip interface brief'], 'ceos2': ['show running-config', ' show ip interface brief']}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Connecting to:  ceos1
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[{'command': 'show running-config',
  'encoding': 'json',
  'result': {'cmds': {'aaa authorization exec default local': None,
                      'hostname ceos1': None,
                      'interface Ethernet1': {'cmds': {'ip address 10.0.0.1/24': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Ethernet2': {'cmds': {'description test': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Loopback1': {'cmds': {'ip address 1.1.1.1/32': None},
                                              'comments': []},
                      'interface Loopback20': {'cmds': {'description test5': None},
                                               'comments': []},
                      'ip access-list test': {'cmds': {'10 permit ip host 1.1.1.1 any log ': None,
                                                       '20 permit ip host 2.2.2.2 any log ': None,
                                                       '30 permit ip host 3.3.3.3 any log ': None,
                                                       '40 permit ip host 4.4.4.4 any log ': None,
                                                       '50 permit ip host 5.5.5.5 any log ': None},
                                              'comments': []},
                      'ip name-server vrf default 8.8.4.4': None,
                      'ip name-server vrf default 8.8.8.8': None,
                      'ip route 0.0.0.0/0 192.168.1.1': None,
                      'ip routing': None,
                      'management api http-commands': {'cmds': {'no shutdown': None,
                                                                'protocol http': None},
                                                       'comments': []},
                      'no aaa root': None,
                      'router ospf 1': {'cmds': {'max-lsa 12000': None,
                                                 'network 1.1.1.1/32 area 0.0.0.0': None,
                                                 'network 10.0.0.0/24 area 0.0.0.0': None,
                                                 'router-id 1.1.1.1': None},
                                        'comments': []},
                      'spanning-tree mode mstp': None,
                      'transceiver qsfp default-mode 4x10G': None,
                      'username arista privilege 15 secret sha512 $6$Zk81mKYy3oxaBEqL$X5XeBneDLn9Rz7n5IbL/bre8zsxHjCfTBSayolwhciQa4B.gP9oILW8wycYAZITc/OE5xqPWZ4HTDVqmRBKpe/': None},
             'comments': [],
             'header': ['! device: ceos1 (cEOSSim, EOS-4.20.5F)\n!\n']}},
 {'command': ' show ip interface brief',
  'encoding': 'text',
  'result': {'output': 'Interface              IP Address         Status     '
                       'Protocol         MTU\n'
                       'Ethernet1              10.0.0.1/24        up         '
                       'up              1500\n'
                       'Ethernet2              unassigned         up         '
                       'up              1500\n'
                       'Loopback1              1.1.1.1/32         up         '
                       'up             65535\n'
                       'Loopback20             unassigned         up         '
                       'up             65535\n'}}]
Post-change state:  ceos1
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Connecting to:  ceos2
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[{'command': 'show running-config',
  'encoding': 'json',
  'result': {'cmds': {'aaa authorization exec default local': None,
                      'hostname ceos2': None,
                      'interface Ethernet1': {'cmds': {'ip address 10.0.0.2/24': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Ethernet2': {'cmds': {'description test': None},
                                              'comments': []},
                      'interface Loopback1': {'cmds': {'ip address 2.2.2.2/32': None},
                                              'comments': []},
                      'interface Loopback20': {'cmds': {'description test5': None},
                                               'comments': []},
                      'ip access-list test': {'cmds': {'10 permit ip host 1.1.1.1 any log ': None,
                                                       '20 permit ip host 2.2.2.2 any log ': None,
                                                       '30 permit ip host 3.3.3.3 any log ': None,
                                                       '40 permit ip host 4.4.4.4 any log ': None,
                                                       '50 permit ip host 5.5.5.5 any log ': None},
                                              'comments': []},
                      'ip name-server vrf default 8.8.4.4': None,
                      'ip name-server vrf default 8.8.8.8': None,
                      'ip route 0.0.0.0/0 192.168.1.1': None,
                      'ip routing': None,
                      'management api http-commands': {'cmds': {'no shutdown': None,
                                                                'protocol http': None,
                                                                'protocol https port 8443': None},
                                                       'comments': []},
                      'no aaa root': None,
                      'router ospf 1': {'cmds': {'max-lsa 12000': None,
                                                 'network 10.0.0.0/24 area 0.0.0.0': None,
                                                 'network 2.2.2.2/32 area 0.0.0.0': None,
                                                 'router-id 2.2.2.2': None},
                                        'comments': []},
                      'spanning-tree mode mstp': None,
                      'transceiver qsfp default-mode 4x10G': None,
                      'username arista privilege 15 secret sha512 $6$Z.tWRcMmY0M7BxW/$HHDfbdeM.foQCO7pDAAEzSqgPpWuP6nAOLrbA0/kSkuQ6rvPVWLjJa.jqh6b51eCjRdTJIipS7IMGsEU5u.7z0': None},
             'comments': [],
             'header': ['! device: ceos2 (cEOSSim, EOS-4.20.5F)\n!\n']}},
 {'command': ' show ip interface brief',
  'encoding': 'text',
  'result': {'output': 'Interface              IP Address         Status     '
                       'Protocol         MTU\n'
                       'Ethernet1              10.0.0.2/24        up         '
                       'up              1500\n'
                       'Loopback1              2.2.2.2/32         up         '
                       'up             65535\n'
                       'Loopback20             unassigned         up         '
                       'up             65535\n'}}]
Post-change state:  ceos2
Problems connecting to these hosts:  []
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ 
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ 
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ 
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ 
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ 


# config script

```
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ python3 pyeapi_config_script.py 
Number of devices to configure: 2
Enter host device: ceos1
Enter commands for device seperate with ",": interface loopback 15, description test       
['interface loopback 15', ' description test']


Enter host device: ceos2
Enter commands for device seperate with ",": interface loopback 15, description test
['interface loopback 15', ' description test']


 This is the dictionary before the loop {'ceos1': ['interface loopback 15', ' description test'], 'ceos2': ['interface loopback 15', ' description test']}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Pre-change State:  ceos1
[{'command': 'show running-config',
  'encoding': 'json',
  'result': {'cmds': {'aaa authorization exec default local': None,
                      'hostname ceos1': None,
                      'interface Ethernet1': {'cmds': {'ip address 10.0.0.1/24': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Ethernet2': {'cmds': {'description test': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Loopback1': {'cmds': {'ip address 1.1.1.1/32': None},
                                              'comments': []},
                      'interface Loopback20': {'cmds': {'description test5': None},
                                               'comments': []},
                      'ip access-list test': {'cmds': {'10 permit ip host 1.1.1.1 any log ': None,
                                                       '20 permit ip host 2.2.2.2 any log ': None,
                                                       '30 permit ip host 3.3.3.3 any log ': None,
                                                       '40 permit ip host 4.4.4.4 any log ': None,
                                                       '50 permit ip host 5.5.5.5 any log ': None},
                                              'comments': []},
                      'ip name-server vrf default 8.8.4.4': None,
                      'ip name-server vrf default 8.8.8.8': None,
                      'ip route 0.0.0.0/0 192.168.1.1': None,
                      'ip routing': None,
                      'management api http-commands': {'cmds': {'no shutdown': None,
                                                                'protocol http': None},
                                                       'comments': []},
                      'no aaa root': None,
                      'router ospf 1': {'cmds': {'max-lsa 12000': None,
                                                 'network 1.1.1.1/32 area 0.0.0.0': None,
                                                 'network 10.0.0.0/24 area 0.0.0.0': None,
                                                 'router-id 1.1.1.1': None},
                                        'comments': []},
                      'spanning-tree mode mstp': None,
                      'transceiver qsfp default-mode 4x10G': None,
                      'username arista privilege 15 secret sha512 $6$Zk81mKYy3oxaBEqL$X5XeBneDLn9Rz7n5IbL/bre8zsxHjCfTBSayolwhciQa4B.gP9oILW8wycYAZITc/OE5xqPWZ4HTDVqmRBKpe/': None},
             'comments': [],
             'header': ['! device: ceos1 (cEOSSim, EOS-4.20.5F)\n!\n']}}]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[{}, {}]
Post-change state:  ceos1
[{'command': 'show running-config',
  'encoding': 'json',
  'result': {'cmds': {'aaa authorization exec default local': None,
                      'hostname ceos1': None,
                      'interface Ethernet1': {'cmds': {'ip address 10.0.0.1/24': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Ethernet2': {'cmds': {'description test': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Loopback1': {'cmds': {'ip address 1.1.1.1/32': None},
                                              'comments': []},
                      'interface Loopback15': {'cmds': {'description test': None},
                                               'comments': []},
                      'interface Loopback20': {'cmds': {'description test5': None},
                                               'comments': []},
                      'ip access-list test': {'cmds': {'10 permit ip host 1.1.1.1 any log ': None,
                                                       '20 permit ip host 2.2.2.2 any log ': None,
                                                       '30 permit ip host 3.3.3.3 any log ': None,
                                                       '40 permit ip host 4.4.4.4 any log ': None,
                                                       '50 permit ip host 5.5.5.5 any log ': None},
                                              'comments': []},
                      'ip name-server vrf default 8.8.4.4': None,
                      'ip name-server vrf default 8.8.8.8': None,
                      'ip route 0.0.0.0/0 192.168.1.1': None,
                      'ip routing': None,
                      'management api http-commands': {'cmds': {'no shutdown': None,
                                                                'protocol http': None},
                                                       'comments': []},
                      'no aaa root': None,
                      'router ospf 1': {'cmds': {'max-lsa 12000': None,
                                                 'network 1.1.1.1/32 area 0.0.0.0': None,
                                                 'network 10.0.0.0/24 area 0.0.0.0': None,
                                                 'router-id 1.1.1.1': None},
                                        'comments': []},
                      'spanning-tree mode mstp': None,
                      'transceiver qsfp default-mode 4x10G': None,
                      'username arista privilege 15 secret sha512 $6$Zk81mKYy3oxaBEqL$X5XeBneDLn9Rz7n5IbL/bre8zsxHjCfTBSayolwhciQa4B.gP9oILW8wycYAZITc/OE5xqPWZ4HTDVqmRBKpe/': None},
             'comments': [],
             'header': ['! device: ceos1 (cEOSSim, EOS-4.20.5F)\n!\n']}}]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Pre-change State:  ceos2
[{'command': 'show running-config',
  'encoding': 'json',
  'result': {'cmds': {'aaa authorization exec default local': None,
                      'hostname ceos2': None,
                      'interface Ethernet1': {'cmds': {'ip address 10.0.0.2/24': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Ethernet2': {'cmds': {'description test': None},
                                              'comments': []},
                      'interface Loopback1': {'cmds': {'ip address 2.2.2.2/32': None},
                                              'comments': []},
                      'interface Loopback20': {'cmds': {'description test5': None},
                                               'comments': []},
                      'ip access-list test': {'cmds': {'10 permit ip host 1.1.1.1 any log ': None,
                                                       '20 permit ip host 2.2.2.2 any log ': None,
                                                       '30 permit ip host 3.3.3.3 any log ': None,
                                                       '40 permit ip host 4.4.4.4 any log ': None,
                                                       '50 permit ip host 5.5.5.5 any log ': None},
                                              'comments': []},
                      'ip name-server vrf default 8.8.4.4': None,
                      'ip name-server vrf default 8.8.8.8': None,
                      'ip route 0.0.0.0/0 192.168.1.1': None,
                      'ip routing': None,
                      'management api http-commands': {'cmds': {'no shutdown': None,
                                                                'protocol http': None,
                                                                'protocol https port 8443': None},
                                                       'comments': []},
                      'no aaa root': None,
                      'router ospf 1': {'cmds': {'max-lsa 12000': None,
                                                 'network 10.0.0.0/24 area 0.0.0.0': None,
                                                 'network 2.2.2.2/32 area 0.0.0.0': None,
                                                 'router-id 2.2.2.2': None},
                                        'comments': []},
                      'spanning-tree mode mstp': None,
                      'transceiver qsfp default-mode 4x10G': None,
                      'username arista privilege 15 secret sha512 $6$Z.tWRcMmY0M7BxW/$HHDfbdeM.foQCO7pDAAEzSqgPpWuP6nAOLrbA0/kSkuQ6rvPVWLjJa.jqh6b51eCjRdTJIipS7IMGsEU5u.7z0': None},
             'comments': [],
             'header': ['! device: ceos2 (cEOSSim, EOS-4.20.5F)\n!\n']}}]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[{}, {}]
Post-change state:  ceos2
[{'command': 'show running-config',
  'encoding': 'json',
  'result': {'cmds': {'aaa authorization exec default local': None,
                      'hostname ceos2': None,
                      'interface Ethernet1': {'cmds': {'ip address 10.0.0.2/24': None,
                                                       'no switchport': None},
                                              'comments': []},
                      'interface Ethernet2': {'cmds': {'description test': None},
                                              'comments': []},
                      'interface Loopback1': {'cmds': {'ip address 2.2.2.2/32': None},
                                              'comments': []},
                      'interface Loopback15': {'cmds': {'description test': None},
                                               'comments': []},
                      'interface Loopback20': {'cmds': {'description test5': None},
                                               'comments': []},
                      'ip access-list test': {'cmds': {'10 permit ip host 1.1.1.1 any log ': None,
                                                       '20 permit ip host 2.2.2.2 any log ': None,
                                                       '30 permit ip host 3.3.3.3 any log ': None,
                                                       '40 permit ip host 4.4.4.4 any log ': None,
                                                       '50 permit ip host 5.5.5.5 any log ': None},
                                              'comments': []},
                      'ip name-server vrf default 8.8.4.4': None,
                      'ip name-server vrf default 8.8.8.8': None,
                      'ip route 0.0.0.0/0 192.168.1.1': None,
                      'ip routing': None,
                      'management api http-commands': {'cmds': {'no shutdown': None,
                                                                'protocol http': None,
                                                                'protocol https port 8443': None},
                                                       'comments': []},
                      'no aaa root': None,
                      'router ospf 1': {'cmds': {'max-lsa 12000': None,
                                                 'network 10.0.0.0/24 area 0.0.0.0': None,
                                                 'network 2.2.2.2/32 area 0.0.0.0': None,
                                                 'router-id 2.2.2.2': None},
                                        'comments': []},
                      'spanning-tree mode mstp': None,
                      'transceiver qsfp default-mode 4x10G': None,
                      'username arista privilege 15 secret sha512 $6$Z.tWRcMmY0M7BxW/$HHDfbdeM.foQCO7pDAAEzSqgPpWuP6nAOLrbA0/kSkuQ6rvPVWLjJa.jqh6b51eCjRdTJIipS7IMGsEU5u.7z0': None},
             'comments': [],
             'header': ['! device: ceos2 (cEOSSim, EOS-4.20.5F)\n!\n']}}]
Problems connecting to these hosts:  []
Todds-MBP-3:pyeapi_stuff toddriemenschneider$ 
```
