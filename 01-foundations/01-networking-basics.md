# Networking Basics | Network কী এবং কেন?

## 1. Computer Network কী?
দুটি বা তার বেশি endpoint যদি wired/wireless medium দিয়ে data exchange করে, সেটি network। Example: অফিসে ১০টি PC, একটি printer, একটি switch এবং একটি router। PC-গুলো local printer ব্যবহার করতে পারে; router দিয়ে remote network/Internet-এ যেতে পারে।

**Basic communication:** Source → NIC → Cable/Wi-Fi → Switch/AP → Router (when other subnet) → Destination। Receiver আবার reply পাঠায়। 

## 2. Common network types
| Type | Scope | Example | Important note |
|---|---|---|---|
| PAN | Personal area | Bluetooth headset | সাধারণত খুব ছোট range |
| LAN | Building/floor | Office PCs | একই administrative location |
| WLAN | Wireless LAN | Office Wi-Fi | Medium wireless; LAN-এর alternative নয়, অংশ |
| CAN | Campus | Multiple buildings | Multiple interconnected LANs |
| MAN | City/metro | Metro fiber network | Scope/location based term |
| WAN | Regional/global | Branch-to-HQ/MPLS/IP transit | Long-distance network |
| Internet | Global inter-network | Public services | একক company নয় |
| Intranet | Private org network | Internal portal | VPN দ্বারা remote access হতে পারে |

## 3. Devices and roles
- **NIC:** PC/server-এর network adapter; Ethernet MAC ও link connectivity দেয়।
- **Hub:** পুরোনো Layer 1 repeater; সব port-এ traffic repeat করে, আধুনিক LAN-এ প্রায় obsolete।
- **Switch:** সাধারণত Layer 2, MAC table দেখে frame forward করে; managed switch VLAN/STP support করে।
- **L3 switch:** IP routing/SVI/ACL-সহ high-speed internal gateway হতে পারে (model/license dependent)।
- **Router:** Different IP networks-এর মাঝে packet route করে; route table ব্যবহার করে।
- **Wireless AP:** Wi-Fi clients-কে wired distribution network-এ bridge করে।
- **Firewall:** Rule/state/policy অনুযায়ী traffic permit/deny করে; অনেক router firewall-ও হতে পারে।
- **Modem/ONT/ONU:** Access technology অনুযায়ী signal/connection terminate করে। GPON-এর ONT/ONU customer-facing optical terminal।
- **OLT:** GPON access network-এর central provider-side termination।
- **Server:** DHCP, DNS, web, database, authentication বা monitoring service দেয়।

## 4. Physical vs logical topology
**Physical:** কোন device কোন port/cable-এ লাগানো। **Logical:** কোন VLAN/subnet/router path দিয়ে traffic যায়। একই physical switch-এ VLAN 10 আর 20 logically separate network হতে পারে।

- **Star:** endpoint আলাদাভাবে central switch-এ, fault isolate সহজ; central switch failure বড় impact।
- **Bus:** Shared backbone (historical); collision domain issue।
- **Ring:** Device chain closed loop, specialized networks-এ protection mechanism থাকতে পারে।
- **Mesh:** Multiple redundant paths; cost/complexity বেশি।
- **Tree/Hierarchical:** Core → Distribution → Access; enterprise/ISP-তে common।

[Diagram collection দেখো](../diagrams/README.md)।

## 5. Key concepts
- **Bandwidth/Capacity:** Link কত data carry করতে পারে (Mb/s, Gb/s)।
- **Throughput:** Measurement period-এ বাস্তবে কত data deliver হয়েছে।
- **Latency:** Packet travel/response time; ping RTT in ms।
- **Jitter:** Delay variation; voice/video-তে গুরুত্বপূর্ণ।
- **Packet loss:** পাঠানো packet-এর একটি অংশ destination/reply-তে পৌঁছায়নি। ICMP reply filtered থাকলেও loss মনে হতে পারে।
- **Duplex:** Full duplex একই সঙ্গে send/receive; half duplex shared/alternating।
- **MTU:** Layer-3 packet-এর maximum supported size for interface/path (common Ethernet IP MTU 1500, context-dependent)।
- **Broadcast domain:** Layer-2 broadcast পৌঁছায় এমন scope; সাধারণত VLAN per domain।
- **Collision domain:** Shared Ethernet medium-এ contention scope; switched full-duplex link-এ historical collision model প্রযোজ্য নয়।

## 6. Real-life example
Client `192.168.10.50/24`, gateway `192.168.10.1`। Printer `192.168.10.60/24` একই subnet-এ থাকলে MAC resolution করে local switch-এ পাঠায়। Website `example.com` public IP-তে হলে DNS resolve করে, default gateway-তে frame পাঠায়, router next hop choose করে। **DNS resolve ≠ Internet connectivity guaranteed।**

## Test yourself
1. Router আর switch-এর role কীভাবে আলাদা?
2. ১ Gbps link-এ speedtest 300 Mbps কেন হতে পারে?
3. একই switch-এ দুই VLAN-এর PC সরাসরি communicate করে না কেন?
4. Physical link `up` মানেই service healthy নয় কেন?
