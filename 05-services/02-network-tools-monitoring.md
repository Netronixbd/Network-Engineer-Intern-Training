# Network Tools, Monitoring, Logs, NTP, SNMP

## Core commands
| Platform | Read-only commands | Purpose |
|---|---|---|
| Windows | `ipconfig /all`, `route print`, `arp -a`, `tracert`, `nslookup` | Host addressing, route, neighbor, DNS |
| Linux | `ip a`, `ip r`, `ip neigh`, `ss`, `ping`, `traceroute`, `dig`, `tcpdump` | Host/service isolation |
| Cisco | `show ip interface brief`, `show interfaces`, `show vlan brief`, `show ip route` | Router/switch status |
| MikroTik | `/ip address print`, `/interface print`, `/ip route print` | Current state |
| Juniper | `show interfaces terse`, `show route`, `show bgp summary` | Physical/L3/BGP |
| Huawei | `display ip interface brief`, `display interface`, `display ip routing-table` | Current status |

## Monitoring signals
- **Availability:** ICMP/SNMP/API reachability, with explicit monitoring path caveats।
- **Traffic:** Inbound/outbound bandwidth per interface, peak and baseline।
- **Error counters:** CRC, drops, discards, overruns, FCS errors, queue drops।
- **Resource:** CPU, RAM, temperature, PSU, fan।
- **Fiber:** Rx/Tx dBm, alarms, LOS, OLT PON status।
- **Session:** BGP states, PPPoE active count, OSPF neighbors, LACP members।

## NOC tool examples
Zabbix, LibreNMS, Cacti, Prometheus/VictoriaMetrics + Grafana, syslog, NetFlow/IPFIX/sFlow collectors। Tool names নয়, **what is monitored, interval, threshold, data freshness, alert routing** বুঝবে।

## SNMP essentials
- SNMPv3 auth + privacy and restricted ACL preferred where supported; SNMPv2c community strings sensitive, never public repo-তে লিখবে না।
- `ifHCInOctets`/`ifHCOutOctets` (64-bit counters) polling interval ও counter rate থেকে bandwidth estimate করা যায়।
- Polling `ifIndex` device reboot পরে change হতে পারে; persistent mapping verify।

## NTP & syslog
Device clocks sync না থাকলে event correlation কঠিন। NTP source, timezone, UTC timestamps, log retention, privacy and access controls defined থাকুক। Syslog central server-এ log volume and rotation plan দরকার।

## Packet capture (authorized lab only)
```bash
sudo tcpdump -ni eth0 'arp or icmp'
sudo tcpdump -ni eth0 'udp port 67 or udp port 68'
sudo tcpdump -ni eth0 'tcp port 179'
```
`eth0` placeholder। Capture credentials, user data or private content থাকতে পারে; permission ছাড়া network sniffing নয়।

## Monitoring scenario
Interface graph 850 Mbps কিন্তু customer slow: shared congestion, policer, burst, packet loss, CPU, peering/CDN path, wireless condition, customer device bottleneck check। Graph average 5-minute হলে microburst দেখাতে নাও পারে।
