So this script loaded configs for the FRR devices in my lab. I'm still learning the ins and outs of FRR. How to automate as well as configure the devices. But from a scripting standpoint looks like screen scraping with netmiko is the easiest first step. I didnt bother with error handling as being used in my lab. 

```
(myenv_py3.11) toddriemenschneider@clab:~/clabs/labs/ceos_labs/lab2/code/python_stuff/netmiko_stuff/load_config_file$ python3 load_frr_config.py 
Login to core routers (y/n):y
Login to dist routers (y/n):y
connecting to: clab-lab2-core1
Configuring: clab-lab2-core1
+++
vtysh  -c "config" -c "no interface loopback66" -c "" -c "interface lo" -c "description router_id" -c "end" -c "" -c "" -c ""
+++

+++  New Config +++
Building configuration...

Current configuration:
!
frr version 10.3.1_git
frr defaults traditional
hostname core1
no ipv6 forwarding
service integrated-vtysh-config
!
interface eth1
 description c1 to c2
 ip address 192.168.0.1/24
exit
!
interface eth2
 description c1 to d1
 ip address 192.168.1.1/24
exit
!
interface eth3
 ip address 192.168.2.1/24
exit
!
interface lo
 description router_id
 ip address 1.1.1.1/32
exit
!
router ospf
 network 1.1.1.1/32 area 0.0.0.0
 network 192.168.0.0/24 area 0.0.0.0
 network 192.168.1.0/24 area 0.0.0.0
 network 192.168.2.0/24 area 0.0.0.0
exit
!
end
+++ End Config +++
connecting to: clab-lab2-core2
Configuring: clab-lab2-core2
+++
vtysh  -c "config" -c "no interface loopback67" -c "no interface loopback66" -c "" -c "interface lo" -c "description router_id" -c "end" -c ""
+++

+++  New Config +++
Building configuration...

Current configuration:
!
frr version 10.3.1_git
frr defaults traditional
hostname core2
no ipv6 forwarding
service integrated-vtysh-config
!
interface eth1
 description c2 - c1
 ip address 192.168.0.2/24
exit
!
interface eth2
 description c2 - d2
 ip address 192.168.2.1/24
exit
!
interface lo
 description router_id
 ip address 2.2.2.2/32
exit
!
router ospf
 network 2.2.2.2/32 area 0.0.0.0
 network 192.168.0.0/24 area 0.0.0.0
 network 192.168.2.0/24 area 0.0.0.0
exit
!
end
+++ End Config +++
connecting to: clab-lab2-d1
Configuring: clab-lab2-d1
+++
vtysh  -c "config" -c "no interface loopback66" -c "interface lo" -c "description router_id" -c "end" -c ""
+++

+++  New Config +++
Building configuration...

Current configuration:
!
frr version 10.3.1_git
frr defaults traditional
hostname d1
no ipv6 forwarding
service integrated-vtysh-config
!
interface eth1
 description d1 to c1
 ip address 192.168.1.2/24
exit
!
interface eth2
 description d1 to ce1
 ip address 192.168.10.1/24
exit
!
interface lo
 description router_id
 ip address 3.3.3.3/32
exit
!
router ospf
 network 3.3.3.3/32 area 0.0.0.0
 network 192.168.1.0/24 area 0.0.0.0
 network 192.168.10.0/24 area 0.0.0.0
exit
!
end
+++ End Config +++
connecting to: clab-lab2-d2
Configuring: clab-lab2-d2
+++
vtysh  -c "config" -c "no interface loopback66" -c "interface lo" -c "description router_id" -c "end" -c ""
+++

+++  New Config +++
Building configuration...

Current configuration:
!
frr version 10.3.1_git
frr defaults traditional
hostname d2
no ipv6 forwarding
service integrated-vtysh-config
!
interface eth1
 description d2 - c2
 ip address 192.168.2.2/24
exit
!
interface eth2
 description d2 - ce2
 ip address 192.168.20.1/24
exit
!
interface lo
 description router_id
 ip address 4.4.4.4/32
exit
!
router ospf
 network 4.4.4.4/32 area 0.0.0.0
 network 192.168.1.0/24 area 0.0.0.0
 network 192.168.2.0/24 area 0.0.0.0
 network 192.168.20.0/24 area 0.0.0.0
exit
!
end
+++ End Config +++
(myenv_py3.11) toddriemenschneider@clab:~/clabs/labs/ceos_labs/lab2/code/python_stuff/netmiko_stuff/load_config_file$ 
```
