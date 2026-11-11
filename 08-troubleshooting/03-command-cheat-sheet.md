# Read-Only Command Cheat Sheet | Quick NOC Reference

**Commands are examples, interface/VRF/subcommands vary by software release. Do not paste blindly.**

| Goal | Windows | Linux |
|---|---|---|
| IP/mask/gateway | `ipconfig /all` | `ip -br addr; ip route` |
| Ping | `ping 192.168.10.1` | `ping -c 5 192.168.10.1` |
| Path | `tracert 192.168.20.10` | `traceroute 192.168.20.10` |
| DNS | `nslookup example.com` | `dig example.com` |
| ARP/neighbor | `arp -a` | `ip neigh` |
| Listening sockets | `netstat -ano` | `ss -tulpn` |
| TCP 443 | `Test-NetConnection example.com -Port 443` (PS) | `curl -I https://example.com` |

## Cisco IOS/IOS XE
```text
show version
show ip interface brief
show interfaces
show interfaces counters errors
show vlan brief
show interfaces trunk
show mac address-table
show ip arp
show ip route
show ip ospf neighbor
show ip bgp summary   ! platform dependent
show logging
```

## MikroTik RouterOS v7
```routeros
/system resource print
/interface print detail
/interface ethernet print stats
/ip address print
/ip arp print
/ip route print detail
/ip dhcp-server lease print
/ip firewall connection print count-only
/routing bgp session print
/log print
```

## Junos
```text
show version
show interfaces terse
show interfaces extensive ge-0/0/0
show route
show arp
show bgp summary
show ospf neighbor
show log messages | last 30
show configuration | display set
```

## Huawei VRP (example syntax)
```text
display version
display interface brief
display ip interface brief
display vlan
display mac-address
display arp
display ip routing-table
display ospf peer brief
display bgp peer
display logbuffer
```

## Linux capture and system health
```bash
ip -s link show dev eth0
sudo ethtool eth0              # if installed
sudo tcpdump -ni eth0 'icmp or arp'   # authorized capture only
journalctl -u NetworkManager --since '1 hour ago'  # if service exists
```

## Verification hierarchy
`Physical link` → `VLAN/ARP` → `IP route` → `NAT/firewall` → `DNS` → `Application`। একটি command success/fail দিয়ে all-layers verdict দিও না।
