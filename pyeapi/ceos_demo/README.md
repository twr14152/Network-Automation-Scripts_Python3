###CEOS DEMO

# Configure the ceos devices

```
Todds-MBP:arista_ceos_stuff toddriemenschneider$ python3 script1.py 
[{'architecture': 'i386',
  'bootupTimestamp': 1541170802.35,
  'cEosToolsVersion': '1.0',
  'hardwareRevision': '',
  'internalBuildId': '4d6b4859-39b5-4581-993b-f84ac0736664',
  'internalVersion': '4.20.5F-8127914.4205F',
  'isIntlVersion': False,
  'memFree': 733736,
  'memTotal': 2046932,
  'modelName': 'cEOSSim',
  'serialNumber': 'N/A',
  'systemMacAddress': '02:42:ac:11:3e:b8',
  'version': '4.20.5F'},
 {'cmds': {'hostname ceos1': None,
           'interface Ethernet1': {'cmds': {'ip address 10.0.0.1/24': None,
                                            'no switchport': None},
                                   'comments': []},
           'interface Ethernet2': {'cmds': {}, 'comments': []},
           'interface Loopback1': {'cmds': {'description router-id': None,
                                            'ip address 1.1.1.1/32': None},
                                   'comments': []},
           'ip domain lookup source-interface Loopback1': None,
           'ip name-server vrf default 8.8.8.8': None,
           'ip routing': None,
           'management api http-commands': {'cmds': {'no shutdown': None},
                                            'comments': []},
           'no aaa root': None,
           'router ospf 1': {'cmds': {'max-lsa 12000': None,
                                      'network 1.1.1.1/32 area 0.0.0.0': None,
                                      'network 10.0.0.0/24 area 0.0.0.0': None,
                                      'router-id 1.1.1.1': None},
                             'comments': []},
           'spanning-tree mode mstp': None,
           'transceiver qsfp default-mode 4x10G': None,
           'username arista privilege 15 secret sha512 $6$kz6Isvzir9f844fZ$BaPsDgJocIxmho3.N9FaPlkX4Mf5rMkwNd5Oq/TorAF01EMotGYFptjjXwYgrr3jY0u7Y.QmC7pZ2QW0TMNRJ0': None},
  'comments': [],
  'header': ['! device: ceos1 (cEOSSim, EOS-4.20.5F)\n!\n']},
 {'bytesIn': 31189,
  'bytesOut': 195399,
  'commandCount': 583,
  'corsOrigins': [],
  'dscpValue': 0,
  'enabled': True,
  'executionTime': 36.19167950200426,
  'fipsEnabled': False,
  'hitCount': 175,
  'httpServer': {'configured': False, 'port': 80, 'running': False},
  'httpsServer': {'configured': True, 'port': 443, 'running': True},
  'iframeAncestors': [],
  'lastHitTime': 1541184385.6256552,
  'localHttpServer': {'configured': False, 'port': 8080, 'running': False},
  'logLevel': 'none',
  'requestCount': 172,
  'tlsProtocol': ['1.0', '1.1', '1.2'],
  'unixSocketServer': {'configured': False, 'running': False},
  'urls': ['Ethernet1   : https://10.0.0.1:443',
           'Loopback1   : https://1.1.1.1:443'],
  'users': {'arista': {'bytesIn': 31189,
                       'bytesOut': 195399,
                       'lastHitTime': 1541184385.6260946,
                       'requestCount': 172}},
  'vrf': 'default',
  'vrfs': ['default']}]
[{'architecture': 'i386',
  'bootupTimestamp': 1541170802.87,
  'cEosToolsVersion': '1.0',
  'hardwareRevision': '',
  'internalBuildId': '4d6b4859-39b5-4581-993b-f84ac0736664',
  'internalVersion': '4.20.5F-8127914.4205F',
  'isIntlVersion': False,
  'memFree': 731864,
  'memTotal': 2046932,
  'modelName': 'cEOSSim',
  'serialNumber': 'N/A',
  'systemMacAddress': '02:42:ac:d6:6f:11',
  'version': '4.20.5F'},
 {'cmds': {'hostname ceos2': None,
           'interface Ethernet1': {'cmds': {'ip address 10.0.0.2/24': None,
                                            'no switchport': None},
                                   'comments': []},
           'interface Ethernet2': {'cmds': {}, 'comments': []},
           'interface Loopback1': {'cmds': {'description router-id': None,
                                            'ip address 2.2.2.2/32': None},
                                   'comments': []},
           'ip domain lookup source-interface Loopback1': None,
           'ip name-server vrf default 8.8.8.8': None,
           'ip routing': None,
           'management api http-commands': {'cmds': {'no shutdown': None,
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
           'username arista privilege 15 secret sha512 $6$vzylRMR/wLVjNXt0$om9qYPMJa4YU53KToYV4qDZyQTm38Nfssj1IFKNzLyS2N4KXLZBRCgZRRDRCHWRo5fZtKnY9P3T5ebN6LPVb/1': None},
  'comments': [],
  'header': ['! device: ceos2 (cEOSSim, EOS-4.20.5F)\n!\n']},
 {'bytesIn': 29257,
  'bytesOut': 157609,
  'commandCount': 562,
  'corsOrigins': [],
  'dscpValue': 0,
  'enabled': True,
  'executionTime': 28.07780302898027,
  'fipsEnabled': False,
  'hitCount': 162,
  'httpServer': {'configured': False, 'port': 80, 'running': False},
  'httpsServer': {'configured': True, 'port': 8443, 'running': True},
  'iframeAncestors': [],
  'lastHitTime': 1541184385.7127335,
  'localHttpServer': {'configured': False, 'port': 8080, 'running': False},
  'logLevel': 'none',
  'requestCount': 162,
  'tlsProtocol': ['1.0', '1.1', '1.2'],
  'unixSocketServer': {'configured': False, 'running': False},
  'urls': ['Ethernet1   : https://10.0.0.2:8443',
           'Loopback1   : https://2.2.2.2:8443'],
  'users': {'arista': {'bytesIn': 29257,
                       'bytesOut': 157609,
                       'lastHitTime': 1541184385.7128985,
                       'requestCount': 162}},
  'vrf': 'default',
  'vrfs': ['default']}]
#############################################
Printing results of ping to loopbacks advertised via ospf
[{'messages': ['PING 1.1.1.1 (1.1.1.1) 72(100) bytes of data.\n'
               '80 bytes from 1.1.1.1: icmp_seq=1 ttl=64 time=0.074 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=2 ttl=64 time=0.047 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=3 ttl=64 time=0.045 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=4 ttl=64 time=0.046 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=5 ttl=64 time=0.045 ms\n'
               '\n'
               '--- 1.1.1.1 ping statistics ---\n'
               '5 packets transmitted, 5 received, 0% packet loss, time 0ms\n'
               'rtt min/avg/max/mdev = 0.045/0.051/0.074/0.013 ms, ipg/ewma '
               '0.110/0.062 ms\n']},
 {'messages': ['PING 2.2.2.2 (2.2.2.2) 72(100) bytes of data.\n'
               '80 bytes from 2.2.2.2: icmp_seq=1 ttl=64 time=10.1 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=2 ttl=64 time=9.89 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=3 ttl=64 time=12.9 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=4 ttl=64 time=11.9 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=5 ttl=64 time=9.46 ms\n'
               '\n'
               '--- 2.2.2.2 ping statistics ---\n'
               '5 packets transmitted, 5 received, 0% packet loss, time 42ms\n'
               'rtt min/avg/max/mdev = 9.466/10.877/12.954/1.345 ms, pipe 2, '
               'ipg/ewma 10.744/10.482 ms\n']}]
Running-Config ceos1
['! Command: show running-config',
 '! device: ceos1 (cEOSSim, EOS-4.20.5F)',
 '!',
 'transceiver qsfp default-mode 4x10G',
 '!',
 'hostname ceos1',
 'ip domain lookup source-interface Loopback1',
 'ip name-server vrf default 8.8.8.8',
 '!',
 'spanning-tree mode mstp',
 '!',
 'no aaa root',
 '!',
 'username arista privilege 15 secret sha512 '
 '$6$kz6Isvzir9f844fZ$BaPsDgJocIxmho3.N9FaPlkX4Mf5rMkwNd5Oq/TorAF01EMotGYFptjjXwYgrr3jY0u7Y.QmC7pZ2QW0TMNRJ0',
 '!',
 'interface Ethernet1',
 '   no switchport',
 '   ip address 10.0.0.1/24',
 '!',
 'interface Ethernet2',
 '!',
 'interface Loopback1',
 '   description router-id',
 '   ip address 1.1.1.1/32',
 '!',
 'ip routing',
 '!',
 'router ospf 1',
 '   router-id 1.1.1.1',
 '   network 1.1.1.1/32 area 0.0.0.0',
 '   network 10.0.0.0/24 area 0.0.0.0',
 '   max-lsa 12000',
 '!',
 'management api http-commands',
 '   no shutdown',
 '!',
 'end',
 '']
#############################################
Printing results of ping to loopbacks advertised via ospf
[{'messages': ['PING 1.1.1.1 (1.1.1.1) 72(100) bytes of data.\n'
               '80 bytes from 1.1.1.1: icmp_seq=1 ttl=64 time=10.9 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=2 ttl=64 time=18.1 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=3 ttl=64 time=20.4 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=4 ttl=64 time=23.8 ms\n'
               '80 bytes from 1.1.1.1: icmp_seq=5 ttl=64 time=28.9 ms\n'
               '\n'
               '--- 1.1.1.1 ping statistics ---\n'
               '5 packets transmitted, 5 received, 0% packet loss, time 54ms\n'
               'rtt min/avg/max/mdev = 10.982/20.469/28.958/5.976 ms, pipe 2, '
               'ipg/ewma 13.732/16.138 ms\n']},
 {'messages': ['PING 2.2.2.2 (2.2.2.2) 72(100) bytes of data.\n'
               '80 bytes from 2.2.2.2: icmp_seq=1 ttl=64 time=0.077 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=2 ttl=64 time=0.047 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=3 ttl=64 time=0.046 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=4 ttl=64 time=0.045 ms\n'
               '80 bytes from 2.2.2.2: icmp_seq=5 ttl=64 time=0.054 ms\n'
               '\n'
               '--- 2.2.2.2 ping statistics ---\n'
               '5 packets transmitted, 5 received, 0% packet loss, time 0ms\n'
               'rtt min/avg/max/mdev = 0.045/0.053/0.077/0.015 ms, ipg/ewma '
               '0.155/0.065 ms\n']}]
Running-Config ceos2
['! Command: show running-config',
 '! device: ceos2 (cEOSSim, EOS-4.20.5F)',
 '!',
 'transceiver qsfp default-mode 4x10G',
 '!',
 'hostname ceos2',
 'ip domain lookup source-interface Loopback1',
 'ip name-server vrf default 8.8.8.8',
 '!',
 'spanning-tree mode mstp',
 '!',
 'no aaa root',
 '!',
 'username arista privilege 15 secret sha512 '
 '$6$vzylRMR/wLVjNXt0$om9qYPMJa4YU53KToYV4qDZyQTm38Nfssj1IFKNzLyS2N4KXLZBRCgZRRDRCHWRo5fZtKnY9P3T5ebN6LPVb/1',
 '!',
 'interface Ethernet1',
 '   no switchport',
 '   ip address 10.0.0.2/24',
 '!',
 'interface Ethernet2',
 '!',
 'interface Loopback1',
 '   description router-id',
 '   ip address 2.2.2.2/32',
 '!',
 'ip routing',
 '!',
 'router ospf 1',
 '   router-id 2.2.2.2',
 '   network 2.2.2.2/32 area 0.0.0.0',
 '   network 10.0.0.0/24 area 0.0.0.0',
 '   max-lsa 12000',
 '!',
 'management api http-commands',
 '   protocol https port 8443',
 '   no shutdown',
 '!',
 'end',
 '']
[{'messages': ['PING 8.8.8.8 (8.8.8.8) 72(100) bytes of data.\n'
               '80 bytes from 8.8.8.8: icmp_seq=1 ttl=37 time=31.5 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=2 ttl=37 time=27.8 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=3 ttl=37 time=27.7 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=4 ttl=37 time=26.8 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=5 ttl=37 time=26.4 ms\n'
               '\n'
               '--- 8.8.8.8 ping statistics ---\n'
               '5 packets transmitted, 5 received, 0% packet loss, time 124ms\n'
               'rtt min/avg/max/mdev = 26.442/28.097/31.505/1.794 ms, ipg/ewma '
               '31.007/29.706 ms\n']}]
[{'messages': ['PING 8.8.8.8 (8.8.8.8) 72(100) bytes of data.\n'
               '80 bytes from 8.8.8.8: icmp_seq=1 ttl=37 time=152 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=2 ttl=37 time=36.6 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=3 ttl=37 time=26.9 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=4 ttl=37 time=31.2 ms\n'
               '80 bytes from 8.8.8.8: icmp_seq=5 ttl=37 time=28.0 ms\n'
               '\n'
               '--- 8.8.8.8 ping statistics ---\n'
               '5 packets transmitted, 5 received, 0% packet loss, time 536ms\n'
               'rtt min/avg/max/mdev = 26.955/55.015/152.247/48.732 ms, '
               'ipg/ewma 134.231/101.809 ms\n']}]
```               
               
# Show command validation               
               
```               
Todds-MBP:arista_ceos_stuff toddriemenschneider$ python3 script2.py 
[{'vrfs': {'default': {'allRoutesProgrammedHardware': True,
                       'allRoutesProgrammedKernel': True,
                       'defaultRouteState': 'notSet',
                       'routes': {'1.1.1.1/32': {'directlyConnected': True,
                                                 'hardwareProgrammed': True,
                                                 'kernelProgrammed': True,
                                                 'routeAction': 'forward',
                                                 'routeType': 'connected',
                                                 'vias': [{'interface': 'Loopback1'}]},
                                  '10.0.0.0/24': {'directlyConnected': True,
                                                  'hardwareProgrammed': True,
                                                  'kernelProgrammed': True,
                                                  'routeAction': 'forward',
                                                  'routeType': 'connected',
                                                  'vias': [{'interface': 'Ethernet1'}]},
                                  '2.2.2.2/32': {'directlyConnected': False,
                                                 'hardwareProgrammed': True,
                                                 'kernelProgrammed': True,
                                                 'metric': 20,
                                                 'preference': 110,
                                                 'routeAction': 'forward',
                                                 'routeType': 'OSPF',
                                                 'vias': [{'interface': 'Ethernet1',
                                                           'nexthopAddr': '10.0.0.2'}]}},
                       'routingDisabled': False}}},
 {'vrfs': {'default': {'instList': {'1': {'ospfNeighborEntries': [{'adjacencyState': 'full',
                                                                   'details': {'areaId': '0.0.0.0',
                                                                               'backupDesignatedRouter': '10.0.0.1',
                                                                               'bfdRequestSent': False,
                                                                               'bfdState': 'adminDown',
                                                                               'designatedRouter': '10.0.0.2',
                                                                               'grHelperTimer': None,
                                                                               'grLastRestartTime': None,
                                                                               'grNumAttempts': 0,
                                                                               'inactivityDefers': 0,
                                                                               'numberOfStateChanges': 7,
                                                                               'retransmissionCount': 1,
                                                                               'stateTime': 1541177643.571044},
                                                                   'drState': 'DR',
                                                                   'inactivity': 1541184436.570939,
                                                                   'interfaceAddress': '10.0.0.2',
                                                                   'interfaceName': 'Ethernet1',
                                                                   'options': {'demandCircuitsSupport': False,
                                                                               'doNotUseInRouteCalc': False,
                                                                               'externalRoutingCapability': True,
                                                                               'linkLocalSignaling': False,
                                                                               'multicastCapability': False,
                                                                               'multitopologyCapability': False,
                                                                               'nssaCapability': False,
                                                                               'opaqueLsaSupport': False},
                                                                   'priority': 1,
                                                                   'routerId': '2.2.2.2'}]}}}}}]
[{'vrfs': {'default': {'allRoutesProgrammedHardware': True,
                       'allRoutesProgrammedKernel': True,
                       'defaultRouteState': 'notSet',
                       'routes': {'1.1.1.1/32': {'directlyConnected': False,
                                                 'hardwareProgrammed': True,
                                                 'kernelProgrammed': True,
                                                 'metric': 20,
                                                 'preference': 110,
                                                 'routeAction': 'forward',
                                                 'routeType': 'OSPF',
                                                 'vias': [{'interface': 'Ethernet1',
                                                           'nexthopAddr': '10.0.0.1'}]},
                                  '10.0.0.0/24': {'directlyConnected': True,
                                                  'hardwareProgrammed': True,
                                                  'kernelProgrammed': True,
                                                  'routeAction': 'forward',
                                                  'routeType': 'connected',
                                                  'vias': [{'interface': 'Ethernet1'}]},
                                  '2.2.2.2/32': {'directlyConnected': True,
                                                 'hardwareProgrammed': True,
                                                 'kernelProgrammed': True,
                                                 'routeAction': 'forward',
                                                 'routeType': 'connected',
                                                 'vias': [{'interface': 'Loopback1'}]}},
                       'routingDisabled': False}}},
 {'vrfs': {'default': {'instList': {'1': {'ospfNeighborEntries': [{'adjacencyState': 'full',
                                                                   'details': {'areaId': '0.0.0.0',
                                                                               'backupDesignatedRouter': '10.0.0.1',
                                                                               'bfdRequestSent': False,
                                                                               'bfdState': 'adminDown',
                                                                               'designatedRouter': '10.0.0.2',
                                                                               'grHelperTimer': None,
                                                                               'grLastRestartTime': None,
                                                                               'grNumAttempts': 0,
                                                                               'inactivityDefers': 0,
                                                                               'numberOfStateChanges': 6,
                                                                               'retransmissionCount': 1,
                                                                               'stateTime': 1541177643.691679},
                                                                   'drState': 'BDR',
                                                                   'inactivity': 1541184431.691581,
                                                                   'interfaceAddress': '10.0.0.1',
                                                                   'interfaceName': 'Ethernet1',
                                                                   'options': {'demandCircuitsSupport': False,
                                                                               'doNotUseInRouteCalc': False,
                                                                               'externalRoutingCapability': True,
                                                                               'linkLocalSignaling': False,
                                                                               'multicastCapability': False,
                                                                               'multitopologyCapability': False,
                                                                               'nssaCapability': False,
                                                                               'opaqueLsaSupport': False},
                                                                   'priority': 1,
                                                                   'routerId': '1.1.1.1'}]}}}}}]
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
```



# Running and startup config diff


```
Todds-MBP:arista_ceos_stuff toddriemenschneider$ python3 script3.py 
'****************************************'
'The Running-Config'
['! Command: show running-config',
 '! device: ceos1 (cEOSSim, EOS-4.20.5F)',
 '!',
 'transceiver qsfp default-mode 4x10G',
 '!',
 'hostname ceos1',
 'ip domain lookup source-interface Loopback1',
 'ip name-server vrf default 8.8.8.8',
 '!',
 'spanning-tree mode mstp',
 '!',
 'no aaa root',
 '!',
 'username arista privilege 15 secret sha512 '
 '$6$kz6Isvzir9f844fZ$BaPsDgJocIxmho3.N9FaPlkX4Mf5rMkwNd5Oq/TorAF01EMotGYFptjjXwYgrr3jY0u7Y.QmC7pZ2QW0TMNRJ0',
 '!',
 'interface Ethernet1',
 '   no switchport',
 '   ip address 10.0.0.1/24',
 '!',
 'interface Ethernet2',
 '!',
 'interface Loopback1',
 '   description router-id',
 '   ip address 1.1.1.1/32',
 '!',
 'ip routing',
 '!',
 'router ospf 1',
 '   router-id 1.1.1.1',
 '   network 1.1.1.1/32 area 0.0.0.0',
 '   network 10.0.0.0/24 area 0.0.0.0',
 '   max-lsa 12000',
 '!',
 'management api http-commands',
 '   no shutdown',
 '!',
 'end',
 '']
'++++++++++++++++++++++++++++++++++++++++'
'The Startup-Config'
''
'************************************************************************************************************************'
'The Running-Config'
['! Command: show running-config',
 '! device: ceos2 (cEOSSim, EOS-4.20.5F)',
 '!',
 'transceiver qsfp default-mode 4x10G',
 '!',
 'hostname ceos2',
 'ip domain lookup source-interface Loopback1',
 'ip name-server vrf default 8.8.8.8',
 '!',
 'spanning-tree mode mstp',
 '!',
 'no aaa root',
 '!',
 'username arista privilege 15 secret sha512 '
 '$6$vzylRMR/wLVjNXt0$om9qYPMJa4YU53KToYV4qDZyQTm38Nfssj1IFKNzLyS2N4KXLZBRCgZRRDRCHWRo5fZtKnY9P3T5ebN6LPVb/1',
 '!',
 'interface Ethernet1',
 '   no switchport',
 '   ip address 10.0.0.2/24',
 '!',
 'interface Ethernet2',
 '!',
 'interface Loopback1',
 '   description router-id',
 '   ip address 2.2.2.2/32',
 '!',
 'ip routing',
 '!',
 'router ospf 1',
 '   router-id 2.2.2.2',
 '   network 2.2.2.2/32 area 0.0.0.0',
 '   network 10.0.0.0/24 area 0.0.0.0',
 '   max-lsa 12000',
 '!',
 'management api http-commands',
 '   protocol https port 8443',
 '   no shutdown',
 '!',
 'end',
 '']
'++++++++++++++++++++++++++++++++++++++++'
'The Startup-Config'
''
Are running and startup configs the same y or n ?: n
[{'messages': ['Copy completed successfully.']}]
[{'messages': ['Copy completed successfully.']}]
Now they are...
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
Todds-MBP:arista_ceos_stuff toddriemenschneider$ python3 script3.py 
'****************************************'
'The Running-Config'
['! Command: show running-config',
 '! device: ceos1 (cEOSSim, EOS-4.20.5F)',
 '!',
 'transceiver qsfp default-mode 4x10G',
 '!',
 'hostname ceos1',
 'ip domain lookup source-interface Loopback1',
 'ip name-server vrf default 8.8.8.8',
 '!',
 'spanning-tree mode mstp',
 '!',
 'no aaa root',
 '!',
 'username arista privilege 15 secret sha512 '
 '$6$kz6Isvzir9f844fZ$BaPsDgJocIxmho3.N9FaPlkX4Mf5rMkwNd5Oq/TorAF01EMotGYFptjjXwYgrr3jY0u7Y.QmC7pZ2QW0TMNRJ0',
 '!',
 'interface Ethernet1',
 '   no switchport',
 '   ip address 10.0.0.1/24',
 '!',
 'interface Ethernet2',
 '!',
 'interface Loopback1',
 '   description router-id',
 '   ip address 1.1.1.1/32',
 '!',
 'ip routing',
 '!',
 'router ospf 1',
 '   router-id 1.1.1.1',
 '   network 1.1.1.1/32 area 0.0.0.0',
 '   network 10.0.0.0/24 area 0.0.0.0',
 '   max-lsa 12000',
 '!',
 'management api http-commands',
 '   no shutdown',
 '!',
 'end',
 '']
'++++++++++++++++++++++++++++++++++++++++'
'The Startup-Config'
('! Command: show startup-config\n'
 '! Startup-config last modified at  Fri Nov  2 18:47:05 2018 by arista\n'
 '! device: ceos1 (cEOSSim, EOS-4.20.5F)\n'
 '!\n'
 'transceiver qsfp default-mode 4x10G\n'
 '!\n'
 'hostname ceos1\n'
 'ip domain lookup source-interface Loopback1\n'
 'ip name-server vrf default 8.8.8.8\n'
 '!\n'
 'spanning-tree mode mstp\n'
 '!\n'
 'no aaa root\n'
 '!\n'
 'username arista privilege 15 secret sha512 '
 '$6$kz6Isvzir9f844fZ$BaPsDgJocIxmho3.N9FaPlkX4Mf5rMkwNd5Oq/TorAF01EMotGYFptjjXwYgrr3jY0u7Y.QmC7pZ2QW0TMNRJ0\n'
 '!\n'
 'interface Ethernet1\n'
 '   no switchport\n'
 '   ip address 10.0.0.1/24\n'
 '!\n'
 'interface Ethernet2\n'
 '!\n'
 'interface Loopback1\n'
 '   description router-id\n'
 '   ip address 1.1.1.1/32\n'
 '!\n'
 'ip routing\n'
 '!\n'
 'router ospf 1\n'
 '   router-id 1.1.1.1\n'
 '   network 1.1.1.1/32 area 0.0.0.0\n'
 '   network 10.0.0.0/24 area 0.0.0.0\n'
 '   max-lsa 12000\n'
 '!\n'
 'management api http-commands\n'
 '   no shutdown\n'
 '!\n'
 'end')
'************************************************************************************************************************'
'The Running-Config'
['! Command: show running-config',
 '! device: ceos2 (cEOSSim, EOS-4.20.5F)',
 '!',
 'transceiver qsfp default-mode 4x10G',
 '!',
 'hostname ceos2',
 'ip domain lookup source-interface Loopback1',
 'ip name-server vrf default 8.8.8.8',
 '!',
 'spanning-tree mode mstp',
 '!',
 'no aaa root',
 '!',
 'username arista privilege 15 secret sha512 '
 '$6$vzylRMR/wLVjNXt0$om9qYPMJa4YU53KToYV4qDZyQTm38Nfssj1IFKNzLyS2N4KXLZBRCgZRRDRCHWRo5fZtKnY9P3T5ebN6LPVb/1',
 '!',
 'interface Ethernet1',
 '   no switchport',
 '   ip address 10.0.0.2/24',
 '!',
 'interface Ethernet2',
 '!',
 'interface Loopback1',
 '   description router-id',
 '   ip address 2.2.2.2/32',
 '!',
 'ip routing',
 '!',
 'router ospf 1',
 '   router-id 2.2.2.2',
 '   network 2.2.2.2/32 area 0.0.0.0',
 '   network 10.0.0.0/24 area 0.0.0.0',
 '   max-lsa 12000',
 '!',
 'management api http-commands',
 '   protocol https port 8443',
 '   no shutdown',
 '!',
 'end',
 '']
'++++++++++++++++++++++++++++++++++++++++'
'The Startup-Config'
('! Command: show startup-config\n'
 '! Startup-config last modified at  Fri Nov  2 18:47:05 2018 by arista\n'
 '! device: ceos2 (cEOSSim, EOS-4.20.5F)\n'
 '!\n'
 'transceiver qsfp default-mode 4x10G\n'
 '!\n'
 'hostname ceos2\n'
 'ip domain lookup source-interface Loopback1\n'
 'ip name-server vrf default 8.8.8.8\n'
 '!\n'
 'spanning-tree mode mstp\n'
 '!\n'
 'no aaa root\n'
 '!\n'
 'username arista privilege 15 secret sha512 '
 '$6$vzylRMR/wLVjNXt0$om9qYPMJa4YU53KToYV4qDZyQTm38Nfssj1IFKNzLyS2N4KXLZBRCgZRRDRCHWRo5fZtKnY9P3T5ebN6LPVb/1\n'
 '!\n'
 'interface Ethernet1\n'
 '   no switchport\n'
 '   ip address 10.0.0.2/24\n'
 '!\n'
 'interface Ethernet2\n'
 '!\n'
 'interface Loopback1\n'
 '   description router-id\n'
 '   ip address 2.2.2.2/32\n'
 '!\n'
 'ip routing\n'
 '!\n'
 'router ospf 1\n'
 '   router-id 2.2.2.2\n'
 '   network 2.2.2.2/32 area 0.0.0.0\n'
 '   network 10.0.0.0/24 area 0.0.0.0\n'
 '   max-lsa 12000\n'
 '!\n'
 'management api http-commands\n'
 '   protocol https port 8443\n'
 '   no shutdown\n'
 '!\n'
 'end')
Are running and startup configs the same y or n ?: y
Cool!
Todds-MBP:arista_ceos_stuff toddriemenschneider$ 
```
