# Switching: MAC Table, ARP, VLAN, Access & Trunk

## 1. Switch forwarding
L2 switch frame source MAC দেখে MAC table/CAM table learn করে: `(VLAN, source MAC) → ingress port`। Destination MAC known হলে নির্দিষ্ট egress port-এ forward; unknown unicast সাধারণত VLAN scope-এ flood হয়। MAC aging/loop/broadcast storms গুরুত্বপূর্ণ operational concerns।

## 2. Broadcast domain vs VLAN
একটি **VLAN** logical L2 separation দেয়। VLAN 10-এ PC1 ও PC2 communicate করতে পারে যদি IP subnet, port membership ও host firewall OK থাকে। VLAN 10 থেকে VLAN 20-এ traffic দিতে **L3 gateway / inter-VLAN routing** লাগবে। শুধু switch trunk দিলেই inter-VLAN routing হয় না।

## 3. Access port vs Trunk port
| Access | Trunk |
|---|---|
| Usually one user VLAN | Multiple VLANs over one link |
| সাধারণভাবে end-host-facing | Switch-to-switch, switch-to-router, AP uplink |
| Host সাধারণত untagged Ethernet পাঠায় | 802.1Q tag দিয়ে VLAN identity carry |
| Cisco: `switchport mode access` | Cisco: `switchport mode trunk` |

**Native VLAN:** 802.1Q trunk-এ default untagged VLAN behavior platform-dependent; two ends mismatch হলে leakage/security issue হতে পারে। Explicit allowed VLAN list, dedicated/unused native VLAN policy, standardized configs keep করো।

## 4. ARP + MAC learning: same subnet example
PC-A `192.168.10.10` wants PC-B `192.168.10.20`। PC-A ARP request broadcast করে, switch VLAN 10-এ flood করে। PC-B ARP reply unicast দেয়, PC-A MAC learn করে। Switch sender MAC table learn করে; future frames specific port-এ যায়।

Different subnet হলে PC-A **default gateway MAC** resolve করে (remote host MAC নয়), frame gateway-তে যায়।

## 5. Troubleshooting matrix
| Symptom | Possible cause | What to verify |
|---|---|---|
| Link up, no ping in same VLAN | VLAN mismatch, wrong IP, host firewall | VLAN table, ARP, NIC IP |
| One VLAN works, another fails across trunk | VLAN not allowed, STP blocked | Trunk allowed VLAN, STP |
| Broadcast spike | L2 loop, bad endpoint | STP logs, MAC moves, rate graphs |
| Inter-VLAN fail | Missing SVI/route/ACL | Gateway SVI, route, ACL |
| MAC address moving ports | Loop, dual-homing, LAG issue | CAM logs, topology, port-channel |

**Mini-lab:** 1 managed switch, VLAN 10 & 20, two PCs in same VLAN and one in different VLAN; create ping success/fail matrix before introducing routing।
