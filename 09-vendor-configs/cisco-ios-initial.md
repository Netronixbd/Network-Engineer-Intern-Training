# Cisco IOS / IOS XE: Initial Router & Switch Configuration (Lab)

> **Scope:** Generic IOS syntax; adjust interface `GigabitEthernet0/0`, `GigabitEthernet1/0/1`, SVI feature and license for actual device. A Layer-2-only switch cannot route multiple VLANs by just creating SVIs।

## A. Discover and backup (read-only)
```text
enable
show version
show running-config
show ip interface brief
show interfaces status
show vlan brief
```
Export sanitized config to a protected location. **Do not upload credentials/keys to GitHub.**

## B. Router LAN + simulated WAN
Router R1: LAN `192.168.10.1/24` on Gi0/1, lab WAN `192.0.2.2/30` on Gi0/0, upstream `192.0.2.1` (another simulated router required for verification)।
```cisco
configure terminal
hostname LAB-R1
no ip domain-lookup
interface GigabitEthernet0/1
 description LAB-STAFF-LAN
 ip address 192.168.10.1 255.255.255.0
 no shutdown
exit
interface GigabitEthernet0/0
 description LAB-UPSTREAM-ONLY
 ip address 192.0.2.2 255.255.255.252
 no shutdown
exit
ip route 0.0.0.0 0.0.0.0 192.0.2.1
end
show ip interface brief
show ip route
```

## C. Optional NAT overload (only if upstream simulator/return connectivity exists)
```cisco
configure terminal
interface GigabitEthernet0/1
 ip nat inside
exit
interface GigabitEthernet0/0
 ip nat outside
exit
access-list 10 permit 192.168.10.0 0.0.0.255
ip nat inside source list 10 interface GigabitEthernet0/0 overload
end
show ip nat translations
show ip nat statistics
```
This NAT ACL example matches source IPs for translation; it **does not act as an inbound firewall**।

## D. Switch: VLAN 10/20, access ports and trunk
```cisco
configure terminal
hostname LAB-SW1
vlan 10
 name STAFF
vlan 20
 name GUEST
vlan 99
 name MANAGEMENT
exit
interface GigabitEthernet1/0/1
 description PC-STAFF
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
exit
interface GigabitEthernet1/0/2
 description PC-GUEST
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
exit
interface GigabitEthernet1/0/24
 description UPLINK-TO-ROUTER-OR-SWITCH
 switchport mode trunk
 switchport trunk allowed vlan 10,20,99
exit
end
show vlan brief
show interfaces trunk
```
`spanning-tree portfast` only for known host-facing edge ports। Some platforms require `switchport trunk encapsulation dot1q`; modern Catalyst commonly uses fixed 802.1Q and command may not exist।

## E. Inter-VLAN routing (router-on-a-stick alternative)
If one physical Gi0/1 connects to VLAN trunk and **no plain IP** exists on physical interface, use subinterfaces:
```cisco
configure terminal
interface GigabitEthernet0/1
 no ip address
 no shutdown
exit
interface GigabitEthernet0/1.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
exit
interface GigabitEthernet0/1.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
exit
interface GigabitEthernet0/1.99
 encapsulation dot1Q 99
 ip address 192.168.99.1 255.255.255.0
end
show ip interface brief
```
**Important:** B (plain Gi0/1 LAN) এবং E (router-on-a-stick) mutually alternative; same interface design-এ মিশিও না। Existing NAT inside placed on physical Gi0/1 হলে VLAN-subinterface design অনুযায়ী NAT inside placement adjust করতে হবে।

## F. Verification, save & rollback
```text
show interfaces
show ip arp
show ip route
show mac address-table
show running-config
copy running-config startup-config
```
Save only after tests and approval। Rollback in lab: individual `no` commands; saved clean config restore in supervised environment। `reload` is disruptive, never casually use।

## Security after connectivity (separate exercise)
SSH key, local accounts/AAA, management ACL, encrypted secrets, logging and NTP configured via vendor/platform-approved guide। এখানে sample passwords ইচ্ছাকৃতভাবে দেওয়া হয়নি।

References: [Cisco VLAN trunking](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/vlan/vlan-configuration-guide/configure-vlan-trunks.html) · [Cisco static routes](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-routing/b-ip-routing/m_iri-ip-prot-indep-0.html)
