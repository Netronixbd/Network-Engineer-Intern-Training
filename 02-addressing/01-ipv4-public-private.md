# IPv4 Address, Static vs Dynamic IP, Public vs Private

## 1. IPv4 address কী?
IPv4 একটি 32-bit logical address। Dotted decimal-এ লেখা হয়, যেমন `192.168.10.25`। 4 octet; প্রতিটি 0–255। Prefix `/24` মানে প্রথম 24 bit network portion; বাকি 8 bit host portion।

`192.168.10.25/24` → network `192.168.10.0`, mask `255.255.255.0`; default gateway উদাহরণ `192.168.10.1` (gateway অবশ্যই ওই subnet-এ reachable হতে হবে)।

## 2. Static IP বনাম Dynamic IP
| Topic | Static IP assignment | Dynamic IP assignment (DHCP) |
|---|---|---|
| Setup | Admin/client manually assigns fixed settings | DHCP server leases network config |
| Address continuity | Manually kept constant | Lease may renew/change |
| Typical uses | Routers, management IP, servers | PCs, phones, guest Wi-Fi |
| Strength | Predictable | Scalable, fewer manual errors |
| Risk | Duplicate IP, wrong gateway | Rogue DHCP, scope exhaustion |

**Crucial distinction:** Static IP মানে **address assignment method**; static route মানে **routing-table entry manually configured**। Dynamic routing (OSPF/BGP) আবার অন্য বিষয়।

## 3. DHCP DORA
`Discover → Offer → Request → Acknowledge` (DHCPv4 initial lease-এর simplified flow)। Lease-এর সঙ্গে IP, mask, gateway, DNS, lease time আসতে পারে। DHCP relay থাকলে server অন্য subnet-এ থাকতে পারে। Static lease/reservation হলে client DHCP-তেই থাকে কিন্তু নির্দিষ্ট address পায়।

## 4. Public vs Private IPv4
RFC 1918 অনুযায়ী private ranges:
- `10.0.0.0/8`
- `172.16.0.0/12` **(172.16–172.31)**; `172.32.0.0` private নয়।
- `192.168.0.0/16`

Private IP globally unique নয়; Internet-এ সরাসরি routed হয় না। NAT/PAT, VPN, private peering ইত্যাদির মাধ্যমে communication সম্ভব। **Public IP = Internet থেকে অবশ্যই reachable** নয়; firewall, routing, CGNAT, service listener matter।

## 5. Other important addresses
- `127.0.0.0/8`: Loopback (commonly `127.0.0.1`)।
- `169.254.0.0/16`: IPv4 link-local/APIPA; DHCP fail হলে Windows system-এ দেখা যায়।
- `0.0.0.0/0`: Default route prefix, অর্থাৎ every IPv4 destination-এর least-specific match।
- `255.255.255.255`: Limited broadcast।
- `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`: **Documentation-only ranges**; operational Internet test-এর জন্য নয়।
- CIDR `192.168.10.0/24` মানে /24 prefix, classful `Class C` terminology historical shorthand, modern planning CIDR-ভিত্তিক।

## 6. IP plan example (small office)
| Segment | VLAN | Subnet | Gateway | Allocation |
|---|---:|---|---|---|
| Staff | 10 | 192.168.10.0/24 | 192.168.10.1 | .100-.199 DHCP |
| Guest | 20 | 192.168.20.0/24 | 192.168.20.1 | .100-.220 DHCP |
| Management | 99 | 192.168.99.0/24 | 192.168.99.1 | Static/reservation |

**Good practice:** Network address (.0 in /24) ও broadcast (.255 in /24) host-এ assign করো না। `/31` point-to-point exception rules আলাদা; সাধারণ LAN-এ /31 use কোরো না।

## 7. Troubleshoot examples
- PC `169.254.20.8/16`: DHCP path/relay/server/VLAN problem suspect।
- PC `192.168.10.50/24`, GW `192.168.20.1`: Wrong default gateway subnet।
- Ping IP works, name fails: DNS likely (তবে resolver/cache/firewall সব check)।
- Two hosts same IP: Duplicate conflict, ARP flapping/intermittent connectivity।

Further reading: [RFC 1918](https://www.rfc-editor.org/info/rfc1918/) ও [RFC 5737](https://www.rfc-editor.org/info/rfc5737/)
