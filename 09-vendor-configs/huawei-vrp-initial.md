# Huawei VRP: Initial Switch/Router Configuration (Lab)

> Examples use common Huawei enterprise VRP-style commands; exact interface naming, VLAN/Route features and system-view syntax model/release-dependent. Verify vendor manual and authorized lab console before execution।

## 1. Inspect
```text
display version
display current-configuration
display ip interface brief
display interface brief
display vlan
display ip routing-table
```

## 2. Create VLAN, access and trunk (sample switch)
```text
system-view
sysname LAB-HW-SW1
vlan batch 10 20 99
interface GigabitEthernet0/0/1
 description LAB-STAFF-PC
 port link-type access
 port default vlan 10
 quit
interface GigabitEthernet0/0/2
 description LAB-GUEST-PC
 port link-type access
 port default vlan 20
 quit
interface GigabitEthernet0/0/24
 description LAB-UPLINK
 port link-type trunk
 port trunk allow-pass vlan 10 20 99
 quit
return
display vlan
display interface brief
```
Trunk default VLAN/PVID and allowed-VLAN behavior verify both peers; platform may need default allowed VLAN adjustments।

## 3. VLAN-interface (if device supports Layer 3 VLANIF)
```text
system-view
interface Vlanif10
 ip address 192.168.10.1 255.255.255.0
 quit
interface Vlanif20
 ip address 192.168.20.1 255.255.255.0
 quit
return
display ip interface brief
```
Only if routed VLANIF gateway desired and device capable. Otherwise upstream router provides gateway।

## 4. Static default route example (lab uplink next hop reachable)
```text
system-view
ip route-static 0.0.0.0 0.0.0.0 192.168.99.254
return
display ip routing-table
```
Next hop must actually be reachable. Without matching connected `192.168.99.0/24` interface/route, static route may not become active। This gateway is a **separate hypothetical lab design**, not automatically compatible with above VLANIF sample unless management VLANIF/uplink are configured।

## 5. Saving and checking
```text
display current-configuration
display ip routing-table
save
```
Some systems prompt for confirmation. Save only after mentor verifies desired behavior। Rollback: platform-specific undo commands or saved backup after review; never use blanket reset on live equipment।

Reference: [Huawei route verification & ip route-static example](https://info.support.huawei.com/network/ptmngsys/Web/tsrev_security/en/content/security/29_edesk_net_server_access_intarnet_server_failed_V5R1/edesk_net_server_access_intarnet_server_failed_edesk005.html)
