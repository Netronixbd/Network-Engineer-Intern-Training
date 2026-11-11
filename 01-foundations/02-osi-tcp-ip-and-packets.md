# OSI, TCP/IP, Packet Journey এবং Ports

## 1. OSI 7 Layers (মুখস্থ নয়, সমস্যা isolate করার জন্য)
| Layer | Name | Typical job/example | PDU/Term | Basic tool |
|---|---|---|---|---|
| 7 | Application | HTTP, DNS, SMTP, SSH | Data | `curl`, `dig`, browser |
| 6 | Presentation | Data encoding, TLS-related presentation concepts | Data | TLS inspection |
| 5 | Session | Session establishment/management concept | Data | Connection tracking |
| 4 | Transport | TCP/UDP, ports, reliability | Segment/Datagram | `ss`, `netstat` |
| 3 | Network | IPv4/IPv6, routing, ICMP | Packet | `ping`, `traceroute` |
| 2 | Data Link | Ethernet, MAC, VLAN, ARP interaction | Frame | MAC table, `arp -a` |
| 1 | Physical | Fiber/copper, optics, signal | Bits | Link LEDs, optical readings |

OSI হলো একটি **reference model**, exact protocol implementation diagram নয়। TCP/IP বাস্তবে বেশি ব্যবহৃত suite: Application, Transport, Internet, Link। TCP/IP Application layer-এ OSI-এর upper-layer functions overlap করে।

## 2. Encapsulation / de-encapsulation
Client HTTP request বানায় → TCP header + port → IP header (source/destination IP) → Ethernet header (source/destination MAC) → cable-এ bits। Router পার হলে সাধারণত **Layer-2 header per-hop পরিবর্তিত হয়**, end-to-end IP destination সাধারণত একই থাকে, NAT থাকলে আলাদা। TTL কমে, frame MAC নতুন next hop-এর হয়। Server reverse direction-এ reply পাঠায়।

## 3. TCP vs UDP
- **TCP:** Connection-oriented, sequence/acknowledgment, retransmission, flow/congestion control। Example HTTPS (সাধারণ TCP-based HTTP/1.1 বা HTTP/2), SSH।
- **UDP:** Connectionless transport, lower overhead; app নিজে reliability implement করতে পারে। Example DNS query, VoIP, QUIC/HTTP3।
- **ICMP:** TCP বা UDP নয়, network diagnosis/control; echo request/reply ping-এ ব্যবহৃত।

## 4. Ports cheat sheet (default/typical, configurable)
| Service | Port/transport | Operational purpose |
|---|---|---|
| HTTP | TCP/80 | Unencrypted web (redirect হতে পারে) |
| HTTPS | TCP/443, QUIC UDP/443 | Web encrypted transport |
| SSH | TCP/22 | Secure device/server management |
| DNS | UDP/53, TCP/53 | Name resolution, large answers/zone transfer |
| DHCPv4 | UDP/67 server, UDP/68 client | IP assignment |
| NTP | UDP/123 | Time sync |
| SNMP | UDP/161 queries, UDP/162 traps | Monitoring |
| SMTP | TCP/25, submission 587, SMTPS 465 | Mail transport/submission |
| IMAP | TCP/143, TLS 993 | Mailbox access |
| BGP | TCP/179 | Inter-domain routing session |
| RDP | TCP/3389 typically | Windows remote desktop |
| Syslog | UDP/514 typical, TLS TCP/6514 | Centralized logs |

**Important:** Port open মানেই service safe নয়। Firewall, authentication, encryption, scope সব check করতে হয়।

## 5. HTTP website not opening: layer-by-layer thought process
1. L1: PC link connected? Wi-Fi association OK?
2. L2: Correct VLAN? Gateway MAC resolve হচ্ছে?
3. L3: IP/mask/gateway/route ঠিক? Ping gateway? remote IP?
4. L4: TCP 443 connect হয়? ACL/firewall drop করছে?
5. L7: DNS answer, HTTPS certificate, HTTP error, server application health কেমন?

## 6. ARP and neighbor discovery
IPv4 LAN-এ neighbor-এর MAC জানতে **ARP** ব্যবহৃত হয়; IPv6-তে ICMPv6 **Neighbor Discovery**। ARP cache stale হলে same-subnet connectivity সমস্যা হতে পারে। ARP কোনো global Internet address lookup service নয়।

## 7. Mini-quiz
- Destination MAC আর destination IP এক নয় কেন?
- DNS UDP ছাড়াও TCP ব্যবহার করে কখন?
- Ping success হলেও website fail হতে পারে কেন?
