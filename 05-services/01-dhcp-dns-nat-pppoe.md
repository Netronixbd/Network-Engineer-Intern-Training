# DHCP, DNS, NAT/PAT, PPPoE | Service Foundations

## 1. DHCP
DHCPv4 client সাধারণত DORA exchange করে। Router-এ DHCP server থাকলে interface/subnet, pool, gateway, DNS and lease ranges match করতে হবে। **Relay (ip helper)** লাগে যখন clients ও DHCP server different broadcast domains-এ। Rogue DHCP wrong gateway দিতে পারে।

**Failure example:** VLAN 20-এ user `169.254.x.x` পাচ্ছে → client request VLAN 20 থেকে relay/server পর্যন্ত যায়? Pool exhausted? DHCP service running? Port policy blocking? Packet capture দেখো।

## 2. DNS
Name (`example.com`) → IP answer। Resolver cache, recursive resolver, authoritative nameserver আলাদা role। Common records:
- **A:** IPv4 answer
- **AAAA:** IPv6 answer
- **CNAME:** alias to another name
- **MX:** mail routing preference
- **TXT:** verification/SPF or other text
- **NS:** authoritative delegation information
- **PTR:** reverse IP-to-name mapping

Troubleshoot: `nslookup example.com`, `dig example.com A`, `dig @<resolver> example.com`। DNS success service reachability guarantee করে না। `/etc/hosts` override বা DNS cache confusion হতে পারে।

## 3. NAT/PAT
Private client `192.168.10.50:52341` Internet-bound হলে edge NAT source IP/port translate করতে পারে: `192.0.2.2:30001` (simulated example WAN address)। **PAT** অনেক internal flow এক external address দিয়ে unique source port ব্যবহার করে। NAT is **not a firewall security policy substitute**। Return packets mapping + firewall state অনুযায়ী transit করে।

- **Source NAT/masquerade:** Outbound many-to-one।
- **Destination NAT/port forward:** Inbound traffic specific internal server-এ map; access controls গুরুত্বপূর্ণ।
- **CGNAT:** ISP large subscriber populations-এর জন্য shared public IP; logging, port allocation, traceability obligations থাকতে পারে।

## 4. PPPoE (ISP)
PPP over Ethernet: client PPPoE discovery (`PADI → PADO → PADR → PADS`) এবং session stage-এ authentication/network parameters। Typical ISP chain: ONU/ONT bridge → subscriber router PPPoE client → access/aggregation VLAN → BNG/PPPoE server → AAA/RADIUS → IP assignment/service policy।

**User active but no Internet?** PPP session established হলেও assigned IP, RADIUS profile, route, NAT/CGNAT, DNS, policy/shaping, uplink path সমস্যা থাকতে পারে। `online` ≠ end-to-end healthy।

## 5. Compare services
| Question | Protocol to inspect | Basic evidence |
|---|---|---|
| IP assign হয়নি | DHCP | DORA/leases/scope/relay |
| Domain opens না, IP reachable | DNS | Query/response, resolver |
| LAN reaches gateway, not external | NAT/route/firewall | Route, translations, connection tracking |
| ISP client PPPoE active but unusable | PPPoE/AAA/routing | Session, IP, profile, traffic counters |

## Lab exercises
1. DHCP pool configure করে 2 PCs-কে different leases দাও।
2. Local server `lab.example` (lab DNS) resolve করাও।
3. One-LAN NAT simulation-এ translation table observe করো।
4. PPPoE data-plane diagnosis checklist লিখো; production credentials ব্যবহার নয়।
