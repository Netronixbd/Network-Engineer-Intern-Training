# MikroTik RouterOS v7: Initial Router Setup (Lab)

> RouterOS v7 syntax; **fresh isolated configuration** assumed. Factory default often already has LAN bridge/DHCP/NAT/firewall; duplicate objects may break network. Never paste into production router. `ether1` WAN, `ether2` LAN।

## 1. Inspect & export (no changes)
```routeros
/system resource print
/interface print
/ip address print
/ip route print detail
/ip dhcp-client print detail
/ip dhcp-server print detail
/ip firewall nat print
/ip firewall filter print
/export hide-sensitive
```
`hide-sensitive` হলেও exports review/redact before publishing; other sensitive metadata remain possible। Safe Mode (WinBox Ctrl+X / terminal Ctrl+X where supported) remotely experimenting-এর আগে ব্যবহার করো।

## 2A. WAN Dynamic IP (DHCP client)
```routeros
/ip dhcp-client add interface=ether1 add-default-route=yes disabled=no
/ip dhcp-client print detail
```
**Alternative 2B:** WAN static IP (same WAN-এ DHCP client আর static address একসঙ্গে intended নয়):
```routeros
/ip address add address=192.0.2.2/30 interface=ether1 comment="LAB-WAN"
/ip route add dst-address=0.0.0.0/0 gateway=192.0.2.1 comment="LAB-UPSTREAM"
/ip dns set servers=192.0.2.1
```
`192.0.2.0/24` documentation range; WAN simulator ছাড়া real Internet route expect করবে না। DNS server `192.0.2.1`-এ running থাকতে হবে; না থাকলে configured resolver must be chosen।

## 3. LAN interface, pool and DHCP server
```routeros
/ip address add address=192.168.10.1/24 interface=ether2 comment="LAB-STAFF-LAN"
/ip pool add name=staff-pool ranges=192.168.10.100-192.168.10.199
/ip dhcp-server network add address=192.168.10.0/24 gateway=192.168.10.1 dns-server=192.168.10.1
/ip dhcp-server add name=staff-dhcp interface=ether2 address-pool=staff-pool lease-time=12h disabled=no
/ip dns set allow-remote-requests=yes
/ip address print
/ip dhcp-server lease print
```
This is one simple isolated LAN port, **not** a multiport bridge. DNS recursion to router enabled; restrict access with firewall and only trusted LAN clients. Upstream DNS and reachability must exist।

## 4. NAT/PAT
```routeros
/ip firewall nat add chain=srcnat src-address=192.168.10.0/24 out-interface=ether1 action=masquerade comment="LAB-STAFF-NAT"
/ip firewall nat print
```
If WAN is PPPoE interface or VLAN instead of ether1, `out-interface` must match actual egress. NAT alone **does not** supply safe firewall filter rules।

## 5. Minimal example INPUT protection for a clean lab
**Do not append blindly to existing rules:** first-match firewall order matters। In a new isolated test router only, after verifying SSH/WinBox access via LAN and Safe Mode:
```routeros
/ip firewall filter add chain=input connection-state=established,related action=accept comment="LAB-INPUT-EST"
/ip firewall filter add chain=input connection-state=invalid action=drop comment="LAB-INPUT-INVALID"
/ip firewall filter add chain=input in-interface=ether2 src-address=192.168.10.0/24 action=accept comment="LAB-LAN-MGMT"
/ip firewall filter add chain=input in-interface=ether1 action=drop comment="LAB-BLOCK-WAN-MGMT"
```
**Note:** Complete production firewall must address IPv4/IPv6, forward chain, exceptions, DNS service, link-local/control-plane, service exposure and policy. These lines are educational, **not a production firewall blueprint**।

## 6. Static route to another private LAN
For an additional router at `192.168.10.2` serving `192.168.20.0/24`:
```routeros
/ip route add dst-address=192.168.20.0/24 gateway=192.168.10.2 comment="LAB-REMOTE-LAN"
/ip route print detail
```
Return route on remote router required।

## 7. Verification and backup
```routeros
/ip address print
/ip route print detail
/ip dhcp-client print detail
/ip dhcp-server lease print
/ip firewall nat print stats
/ping 192.168.10.100 count=4
/tool traceroute 192.168.20.10
/system backup save name=lab-before-change
```
Binary backup contains sensitive configuration; **don't share publicly**. Restore requires compatible device/version awareness।

References: [RouterOS First Time Configuration](https://manual.mikrotik.com/docs/getting-started/first-time-configuration/) · [DHCP Server](https://manual.mikrotik.com/docs/network-management/dhcp/server/) · [DHCP Client](https://manual.mikrotik.com/docs/network-management/dhcp/client/)
