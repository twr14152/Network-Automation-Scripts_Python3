The ios discovery script is meant for cisco ios ios-xe devices routers or switches.
If the device is not ios the appropriate netmiko device type will need to be specified.
For example nxos or eos. 
The command syntax may need to be tweaked to match the os type.
### Directory prior to running script ###
```
todd@ubuntu:~/automation/netmiko_stuff$ ls -l
total 96
-rw-rw-r-- 1 todd todd  3331 Jul 30 17:28 archive_discovery_script2.py
-rw-rw-r-- 1 todd todd  3395 Jul 30 17:40 archive_discovery_script3.py
-rw-rw-r-- 1 todd todd  1023 Nov 14 14:03 auto_detect_script.py
-rw-rw-r-- 1 todd todd   468 Nov 14 14:04 auto_detect_script_results.txt
-rw-rw-r-- 1 todd todd  5690 Nov 14 13:45 Connection_Errors
-rw-rw-r-- 1 todd todd  5684 Nov 14 11:41 dell_discovery_script.py
-rw-rw-r-- 1 todd todd 10043 Oct 26 11:03 discovery_script2.py
-rw-rw-r-- 1 todd todd 10619 Oct 26 11:28 discovery_script3.py
-rw-rw-r-- 1 todd todd  4053 Oct 25 15:41 discovery_script.py
-rw-rw-r-- 1 todd todd    41 Jul 31 13:41 host_file.txt
-rw-rw-r-- 1 todd todd  5688 Nov 14 11:46 hp_discovery_script.py
-rw-rw-r-- 1 todd todd  5683 Nov 14 13:46 ios_discovery_script.py
-rw-rw-r-- 1 todd todd  1574 Jul 31 11:50 show_commands.py
-rw-rw-r-- 1 todd todd   151 Oct 26 09:29 test_host
-rw-rw-r-- 1 todd todd  5677 Oct 29 08:05 test_script_001.py
todd@ubuntu:~/automation/netmiko_stuff$
```

### Run script ###
```
todd@ubuntu:~/automation/netmiko_stuff$ python3 ios_discovery_script.py 
Username: 
Password: 
************************************
Unable to log into this device: bogus_rtr
Connection to device timed-out: cisco_ios bogus_rtr:22
************************************
Connected to host: r3

---- Elapsed time= 5.3688037395477295
Connected to host: r4

---- Elapsed time= 5.393296241760254
Connected to host: r1

---- Elapsed time= 5.74307918548584
Connected to host: r2

---- Elapsed time= 5.878320932388306
Connected to host: r5

---- Elapsed time= 6.15932035446167
Connected to host: r6

---- Elapsed time= 88.73258543014526
Connected to host: r7

---- Elapsed time= 89.67249798774719
Connected to host: r8

---- Elapsed time= 91.1974241733551
Connected to host: r9

---- Elapsed time= 93.47259020805359
Connected to host: r10

---- Elapsed time= 104.87565612792969
 [None, None, None, None, None, None, None, None, None, None, None]
 ```
 
 ### Script added files to directory ###

```
todd@ubuntu:~/automation/netmiko_stuff$  ls -l
total 4376
-rw-rw-r-- 1 todd todd   3331 Jul 30 17:28 archive_discovery_script2.py
-rw-rw-r-- 1 todd todd   3395 Jul 30 17:40 archive_discovery_script3.py
-rw-rw-r-- 1 todd todd   1023 Nov 14 14:03 auto_detect_script.py
-rw-rw-r-- 1 todd todd    468 Nov 14 14:04 auto_detect_script_results.txt
-rw-rw-r-- 1 todd todd   5797 Nov 14 14:22 Connection_Errors
-rw-rw-r-- 1 todd todd   5684 Nov 14 11:41 dell_discovery_script.py
-rw-rw-r-- 1 todd todd  10043 Oct 26 11:03 discovery_script2.py
-rw-rw-r-- 1 todd todd  10619 Oct 26 11:28 discovery_script3.py
-rw-rw-r-- 1 todd todd   4053 Oct 25 15:41 discovery_script.py
-rw-rw-r-- 1 todd todd     41 Jul 31 13:41 host_file.txt
-rw-rw-r-- 1 todd todd   5688 Nov 14 11:46 hp_discovery_script.py
-rw-rw-r-- 1 todd todd   5683 Nov 14 13:46 ios_discovery_script.py
-rw-rw-r-- 1 todd todd 433203 Nov 14 14:26 r10_cmds_file.txt
-rw-rw-r-- 1 todd todd 440992 Nov 14 14:24 r1_cmds_file.txt
-rw-rw-r-- 1 todd todd 441972 Nov 14 14:24 r2_cmds_file.txt
-rw-rw-r-- 1 todd todd 434677 Nov 14 14:24 r3_cmds_file.txt
-rw-rw-r-- 1 todd todd 436756 Nov 14 14:24 r4_cmds_file.txt
-rw-rw-r-- 1 todd todd 435341 Nov 14 14:24 r5_cmds_file.txt
-rw-rw-r-- 1 todd todd 434058 Nov 14 14:25 r6_cmds_file.txt
-rw-rw-r-- 1 todd todd 435011 Nov 14 14:25 r7_cmds_file.txt
-rw-rw-r-- 1 todd todd 439256 Nov 14 14:25 r8_cmds_file.txt
-rw-rw-r-- 1 todd todd 432354 Nov 14 14:26 r9_cmds_file.txt
-rw-rw-r-- 1 todd todd   1574 Jul 31 11:50 show_commands.py
-rw-rw-r-- 1 todd todd    151 Oct 26 09:29 test_host
-rw-rw-r-- 1 todd todd   5677 Oct 29 08:05 test_script_001.py
todd@ubuntu:~/automation/netmiko_stuff$
```

### Read file 
- The output in this script is from an older version of the script.
- The current version of the scripts output is way to verbose to copy in to this file
- The same concept of the file contents and creation holds true
```

todd@ubuntu:~/$ cat r4_cmds_file.txt 
Connected to host: r4
r4#
show running-config
Building configuration...

Current configuration : 2459 bytes
!
! Last configuration change at 05:11:10 UTC Thu Oct 25 2018 by admin
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname r4
!
boot-start-marker
boot-end-marker
!
!
logging buffered 65000
!
no aaa new-model
clock timezone UTC -5 0
no ip icmp rate-limit unreachable
!
!
!
!
!
!
no ip domain lookup
ip domain name testlab.net
ip cef
no ipv6 cef
!
!
multilink bundle-name authenticated
!
!
!
!
!
!
!
username admin privilege 15 password 0 automate
username helpdesk password 0 password1
!
!
!
!
!
ip tcp synwait-time 5
ip ssh version 2
! 
!
!
!
!
!
!
!
!
interface Loopback0
 description ansible_test
 ip address 4.4.4.4 255.255.255.255
!
interface Loopback103
 description distribution-layer router
 no ip address
!
interface FastEthernet0/0
 ip address 157.130.0.3 255.255.255.254
 duplex full
!
interface FastEthernet1/0
 ip address 157.130.0.14 255.255.255.254
 speed auto
 duplex auto
!
interface FastEthernet1/1
 ip address 157.130.0.12 255.255.255.254
 speed auto
 duplex auto
!
interface FastEthernet2/0
 no ip address
 shutdown
 speed auto
 duplex auto
!
interface FastEthernet2/1
 no ip address
 shutdown
 speed auto
 duplex auto
!
router ospf 1
 router-id 4.4.4.4
 network 0.0.0.0 255.255.255.255 area 0
!
router bgp 4
 bgp router-id 4.4.4.4
 bgp log-neighbor-changes
 network 4.4.4.4 mask 255.255.255.255
 neighbor 157.130.0.2 remote-as 100
 neighbor 157.130.0.2 password test_pass
 neighbor 157.130.0.2 timers 5 15
 neighbor 157.130.0.2 advertisement-interval 1
 neighbor 157.130.0.13 remote-as 7
 neighbor 157.130.0.13 password test_pass
 neighbor 157.130.0.13 timers 5 15
 neighbor 157.130.0.13 advertisement-interval 1
 neighbor 157.130.0.15 remote-as 8
 neighbor 157.130.0.15 password test_pass
 neighbor 157.130.0.15 timers 5 15
 neighbor 157.130.0.15 advertisement-interval 1
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
!
!
snmp-server community public RO
snmp-server location r4_location
snmp-server contact Dave Albert 555-555-5555
!
!
control-plane
!
banner login ^C
Attention - This is a lab. Under no circumstances are you to take this message seriously!
^C
!
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
 stopbits 1
line aux 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
 stopbits 1
line vty 0 4
 login local
 transport input telnet ssh
line vty 5 15
 login local
 transport input telnet ssh
!
ntp server 4.4.4.4
!
end

**************************************
Connected to host: r4
r4#
show version
Cisco IOS Software, 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)S7, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Wed 01-Apr-15 20:30 by prod_rel_team

ROM: ROMMON Emulation Microcode
BOOTLDR: 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)S7, RELEASE SOFTWARE (fc4)

r4 uptime is 6 hours, 20 minutes
System returned to ROM by unknown reload cause - suspect boot_data[BOOT_COUNT] 0x0, BOOT_COUNT 0, BOOTDATA 19
System image file is "tftp://255.255.255.255/unknown"
Last reload reason: unknown reload cause - suspect boot_data[BOOT_COUNT] 0x0, BOOT_COUNT 0, BOOTDATA 19



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 7206VXR (NPE400) processor (revision A) with 491520K/32768K bytes of memory.
Processor board ID 4279256517
R7000 CPU at 150MHz, Implementation 39, Rev 2.1, 256KB L2 Cache
6 slot VXR midplane, Version 2.1

Last reset from power-on

PCI bus mb0_mb1 (Slots 0, 1, 3 and 5) has a capacity of 600 bandwidth points.
Current configuration on bus mb0_mb1 has a total of 600 bandwidth points. 
This configuration is within the PCI bus capacity and is supported. 

PCI bus mb2 (Slots 2, 4, 6) has a capacity of 600 bandwidth points.
Current configuration on bus mb2 has a total of 400 bandwidth points 
This configuration is within the PCI bus capacity and is supported. 

Please refer to the following document "Cisco 7200 Series Port Adaptor
Hardware Configuration Guidelines" on Cisco.com <http://www.cisco.com>
for c7200 bandwidth points oversubscription and usage guidelines.


5 FastEthernet interfaces
509K bytes of NVRAM.

8192K bytes of Flash internal SIMM (Sector size 256K).
Configuration register is 0x2102

**************************************
Connected to host: r4
r4#
show inventory
NAME: "Chassis", DESCR: "Cisco 7206VXR, 6-slot chassis"
PID: CISCO7206VXR      , VID:    , SN: 4279256517 

NAME: "NPE400 0", DESCR: "Cisco 7200VXR Network Processing Engine NPE-400"
PID: NPE-400           , VID:    , SN: 11111111   

NAME: "module 0", DESCR: "I/O FastEthernet (TX-ISL)"
PID: C7200-IO-FE-MII/RJ, VID:    , SN: 4294967295 

NAME: "module 1", DESCR: "Dual Port FastEthernet (RJ45)"
PID: PA-2FE-FX         , VID:    , SN: XXX00000000

NAME: "module 2", DESCR: "Dual Port FastEthernet (RJ45)"
PID: PA-2FE-FX         , VID:    , SN: XXX00000000

NAME: "Power Supply 0", DESCR: "Cisco 7200 AC Power Supply"
PID: PWR-7200-AC       , VID:    , SN:            

NAME: "Power Supply 1", DESCR: "Cisco 7200 AC Power Supply"
PID: PWR-7200-AC       , VID:    , SN:            


**************************************
Connected to host: r4
r4#
show interface description
Interface                      Status         Protocol Description
Fa0/0                          up             up       
Fa1/0                          up             up       
Fa1/1                          up             up       
Fa2/0                          admin down     down     
Fa2/1                          admin down     down     
Lo0                            up             up       ansible_test
Lo103                          up             up       distribution-layer router
**************************************
Connected to host: r4
r4#
show ip arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  157.130.0.2           137   ca01.02ec.001c  ARPA   FastEthernet0/0
Internet  157.130.0.3             -   ca04.02f0.0000  ARPA   FastEthernet0/0
Internet  157.130.0.12            -   ca04.02f0.001d  ARPA   FastEthernet1/1
Internet  157.130.0.13          126   ca07.02f3.001c  ARPA   FastEthernet1/1
Internet  157.130.0.14            -   ca04.02f0.001c  ARPA   FastEthernet1/0
Internet  157.130.0.15          115   ca08.02f4.0000  ARPA   FastEthernet1/0
**************************************
Connected to host: r4
r4#
show ip route summary
IP routing table name is default (0x0)
IP routing table maximum-paths is 32
Route Source    Networks    Subnets     Replicates  Overhead    Memory (bytes)
connected       0           7           0           420         1260
static          0           0           0           0           0
ospf 1          0           15          0           900         2760
  Intra-area: 15 Inter-area: 0 External-1: 0 External-2: 0
  NSSA External-1: 0 NSSA External-2: 0
bgp 4           0           9           0           900         1620
  External: 9 Internal: 0 Local: 0
internal        11                                              3540
Total           11          31          0           2220        9180
**************************************
Connected to host: r4
r4#
show vlan brief
            ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show vtp status
          ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show cdp neighbor
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
r7.testlab.net   Fas 1/1           133               R    7206VXR   Fas 1/0
r1.testlab.net   Fas 0/0           147               R    7206VXR   Fas 1/0
r8.testlab.net   Fas 1/0           115               R    7206VXR   Fas 0/0
**************************************
Connected to host: r4
r4#
show lldp neighbor
          ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show ip bgp summ
BGP router identifier 4.4.4.4, local AS number 4
BGP table version is 154, main routing table version 154
10 network entries using 1440 bytes of memory
17 path entries using 1360 bytes of memory
16/10 BGP path/bestpath attribute entries using 2176 bytes of memory
14 BGP AS-PATH entries using 384 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 5360 total bytes of memory
BGP activity 22/12 prefixes, 127/110 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
157.130.0.2     4          100    4422    4345      154    0    0 06:05:22        8
157.130.0.13    4            7    4266    4333      154    0    0 06:05:12        1
157.130.0.15    4            8     722     748      154    0    0 01:01:55        7
**************************************
Connected to host: r4
r4#
show ip ospf nei

Neighbor ID     Pri   State           Dead Time   Address         Interface
7.7.7.7           1   FULL/DR         00:00:38    157.130.0.13    FastEthernet1/1
8.8.8.8           1   FULL/DR         00:00:37    157.130.0.15    FastEthernet1/0
1.1.1.1           1   FULL/BDR        00:00:37    157.130.0.2     FastEthernet0/0
**************************************
Connected to host: r4
r4#
show ip eigrp nei

**************************************
Connected to host: r4
r4#
show interface status
                      ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show trunk
          ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show int trunk
             ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show etherchannel summ
         ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show mac address-table
          ^
% Invalid input detected at '^' marker.

**************************************
Connected to host: r4
r4#
show ip route 0.0.0.0
% Network not in table
**************************************
Connected to host: r4
r4#
show spanning-tree brief
                         ^
% Invalid input detected at '^' marker.

**************************************
todd@ubuntu:~/$ 
```

If the script were to have issues logging into other devices. You could run the auto_detect_script.py to determine what kind of device it is. Then use that info to update your scripts to work with the device if its supported by netmiko.


````
$ python3 auto_detect_script.py 
Username: 
Password: 
Error connecting to bogus_rtr
cisco_ios is the device_type for r3
cisco_ios is the device_type for r4
cisco_ios is the device_type for r1
cisco_ios is the device_type for r2
cisco_ios is the device_type for r5
cisco_ios is the device_type for r7
cisco_ios is the device_type for r8
cisco_ios is the device_type for r6
cisco_ios is the device_type for r9
cisco_ios is the device_type for r10
[None, None, None, None, None, None, None, None, None, None, None]
```
