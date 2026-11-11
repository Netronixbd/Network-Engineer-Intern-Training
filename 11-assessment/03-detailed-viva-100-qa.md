# 100 Detailed Network Engineering Viva Questions & Answers (Bangla + English)

> Fresher/interview/NOC intern practice; short but reasoned answers. **Do not memorize commands without running labs.**

**How to use:** Student answers first → mentor expands packet flow/diagram → verify in lab → mark correct/partial/need revision.

## 01 — OSI, TCP/UDP, L1–L3 basics

### Q001. OSI model কয়টি layer এবং কেন শিখব?

**Answer:** Seven layers: Physical, Data Link, Network, Transport, Session, Presentation, Application। Real protocol stack সবসময় textbook layering follow না করলেও fault isolation-এ এটি একটি effective mental model।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q002. IP packet কি MAC ছাড়া LAN-এ যায়?

**Answer:** Ethernet LAN-এ IP packet সাধারণত Ethernet frame-এর ভেতর যায়; next-hop MAC resolved by ARP (IPv4) বা NDP (IPv6)। Router hop বদলালে L2 source/destination MAC বদলায়, IP destination সাধারণত আগেরটাই থাকে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q003. Layer-2 switch কী দেখে forwarding করে?

**Answer:** Destination MAC and VLAN context দেখে; MAC learning table source MAC থেকে populate হয়। Unknown unicast/broadcast traffic VLAN-এর permitted ports-এ flood হতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q004. Layer-3 router কী দেখে?

**Answer:** Destination IP-এর সবচেয়ে specific matching route (longest prefix match) নির্বাচন করে। Next hop adjacent কিনা, ARP/NDP resolution এবং firewall/policy requirements-ও প্রয়োজন।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q005. TCP vs UDP পার্থক্য কী?

**Answer:** TCP connection-oriented ordered reliable byte stream প্রদান করে; retransmission/flow control আছে। UDP connectionless datagram দেয়, guarantee application-এর হাতে; QUIC UDP-র উপর reliability যোগ করে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q006. Ping pass কিন্তু HTTPS fail কেন?

**Answer:** Ping ICMP reachability পরীক্ষা করে, TCP/443 বা UDP/443, TLS certificate ও DNS নয়। Firewall, TCP handshake, MTU, server process বা application error আলাদাভাবে check করবে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q007. TCP three-way handshake কী?

**Answer:** Client SYN পাঠায়, server SYN+ACK, client ACK দেয়; তারপর application data exchange। Half-open/timeout হলে ACL, SYN rate-limit, route বা service state পরীক্ষা।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q008. Packet loss এবং latency এক জিনিস?

**Answer:** না। Latency হলো delay, loss হলো packet হারানো; jitter হলো delay variation। ICMP rate-limit-এর কারণে intermediate hop loss দেখলেও end-to-end forwarding ঠিক থাকতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q009. Full duplex কী?

**Answer:** একই সময়ে একই link-এর send ও receive সক্ষমতা, যেমন 1G TX + 1G RX। Directional utilization আলাদা দেখবে; TX+RX sum এক direction-এর percent নয়।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q010. ARP কেন দরকার?

**Answer:** IPv4 same L2 segment-এ next-hop IPv4-এর MAC জানতে ARP ব্যবহার হয়। ARP fail হলে gateway IP সঠিক থাকা সত্ত্বেও local frame delivery ব্যর্থ হতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 02 — IP, CIDR, subnet, public/private

### Q011. Static IP আর Static Route কি same?

**Answer:** না। Static IP হলো interface/host address manually configure; static route হলো destination prefix-এ forwarding next-hop configure। Router-এর static IP থাকলেও remote network path automatically জানা যায় না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q012. Dynamic IP কিভাবে পাওয়া যায়?

**Answer:** DHCP server lease দিয়ে IP/mask/gateway/DNS দেয়, PPPoE session থেকেও dynamic WAN IP assign হতে পারে। Dynamic assignment মানেই every reconnect নতুন IP নয়।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q013. /24 subnet কত usable IPv4?

**Answer:** Conventional /24 = 256 total, 254 usable host addresses; network ও broadcast reserved। Exception rules apply for /31 point-to-point এবং /32 host route।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q014. /26-এর mask এবং total?

**Answer:** Mask 255.255.255.192, block of 64 addresses, conventionally 62 hosts। Last-octet boundaries .0/.64/.128/.192।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q015. 192.168.10.130/26 network কোনটি?

**Answer:** Network 192.168.10.128, broadcast .191, usable .129-.190। 256−192=64 block; .130 .128-.191 block-এর মধ্যে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q016. Default gateway local subnet-এ হওয়া প্রয়োজন?

**Answer:** সাধারণ IPv4 host design-এ gateway directly reachable L2 neighbor হতে হয়। Gateway remote subnet-এর IP হলে host ARP/route problem হয়, special on-link config exceptions aside।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q017. 100.64.0.0/10 কি RFC1918 private?

**Answer:** না। এটি RFC6598 Shared Address Space, ISP CGNAT link-এর জন্য; globally routable customer public IPv4 নয়। 10/8, 172.16/12, 192.168/16 হলো RFC1918।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q018. 172.32.10.1 কি RFC1918 private?

**Answer:** না। RFC1918 172 range হলো 172.16.0.0 থেকে 172.31.255.255; `172.32` range-এর বাইরে। তবে publicly usable কিনা IANA allocation/route/filter যাচাই করতে হবে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q019. /31 কোন অবস্থায় দুই address usable?

**Answer:** RFC3021-supported **point-to-point IPv4** interface-এ /31-এর দুই address endpoint হিসেবে ব্যবহার করা যায়। সাধারণ LAN/broadcast-host subnet-এ /31 blindly use করবে না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q020. Duplicate IP হলে লক্ষণ?

**Answer:** ARP entries flip, intermittent reachability, address conflict alerts, random sessions drop হতে পারে। ARP, DHCP leases, switch port MAC mapping এবং static assignment pool overlap যাচাই।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 03 — VLAN, Port types, Switching

### Q021. VLAN কী সমস্যা সমাধান করে?

**Answer:** এক physical switch-এ logical separate L2 broadcast domains করে segmentation দেয়। Different VLANs IP traffic exchange করতে router/L3 switch এবং policy লাগে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q022. VLAN Tagging মানে encryption?

**Answer:** না। 802.1Q Ethernet frame-এ VLAN ID metadata যোগ করে; payload secrecy দেয় না। Separate security control/ACL/VPN দরকার।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q023. PVID কী?

**Answer:** Port VLAN ID maps **untagged ingress** frames to selected VLAN (depending vendor behavior)। Wrong PVID হলে user ভুল DHCP scope/VLAN-এ যেতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q024. Tagged বনাম Untagged?

**Answer:** Tagged egress retains/adds 802.1Q VLAN header; untagged egress removes it। Access ports commonly untagged, trunks commonly tagged for multiple VLANs।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q025. Forbidden VLAN member কী?

**Answer:** কিছু switch GUI-তে Port-VLAN relationship নিষিদ্ধ/not-member বোঝায়, egress forwarding হয় না; exact term vendor-specific। Ingress filtering এবং allowed list-ও যাচাই প্রয়োজন।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q026. Access vs trunk port?

**Answer:** Access port সাধারণত একটি untagged data VLAN-এ end device যুক্ত করে। Trunk port একাধিক permitted VLAN carry করে 802.1Q tagging দিয়ে, native VLAN handling পৃথক হতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q027. Hybrid port কী?

**Answer:** এক physical port-এ একটি VLAN untagged, অন্যগুলো tagged সহ flexible membership; Huawei/managed switch designs-এ দেখা যায়। Cisco standard Catalyst CLI-তে generic hybrid mode command assume করা যাবে না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q028. Native VLAN mismatch কেন risk?

**Answer:** Trunk-এর untagged traffic দুই পাশে ভিন্ন VLAN হিসেবে interpret হতে পারে। Connectivity ও VLAN hopping/security issue হতে পারে; explicit design/allowed-list management দরকার।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q029. STP blocked port মানে fault?

**Answer:** না। Redundant L2 topology-তে loop prevention-এর জন্য STP port forwarding না করাতে পারে। Root bridge, role, topology changes ও alternate path যাচাই।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q030. LACP দুটি 10G মানেই single TCP flow 20G?

**Answer:** না। সাধারণভাবে per-flow hash একটি member link select করে; aggregate multiple flows-এর capacity বাড়ায়। LACP status, hashing, peer configuration এবং total member utilization দেখবে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 04 — Routing, OSPF and BGP

### Q031. Longest prefix match কী?

**Answer:** একাধিক route same destination match করলে সবচেয়ে specific prefix নির্বাচন হয়, যেমন /24 over /16 over /0। Route-source AD/preference selection same-prefix competing routes-এর আলাদা বিষয়।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q032. Default route কী?

**Answer:** `0.0.0.0/0` all unmatched IPv4 destinations-এর fallback। Upstream next hop reachable, return route/NAT/firewall সঠিক না থাকলে শুধু default route দিয়ে Internet হবে না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q033. Return route না থাকলে কী হবে?

**Answer:** Forward packet destination-এ গেলেও reply ফিরে আসতে না পারলে end-to-end session fail। Two-router lab-এ উভয় পাশে destination subnet-এর static route দরকার।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q034. Static routing vs OSPF?

**Answer:** Static route manually maintained, small/simple topology-তে manageable। OSPF dynamically learns topology and computes SPF paths, but area design, adjacency and cost understanding লাগে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q035. OSPF neighbor stuck হলে first কী দেখবে?

**Answer:** L3 reachability, area ID, interface hello/dead timers, network type, authentication, MTU and ACL। Only `show neighbor` দেখে root cause claim করবে না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q036. BGP কী?

**Answer:** BGP-4 internet/ISP AS reachability ও policy-driven route exchange করে। Peering generally TCP/179; session Established required, but prefix acceptance/export separate policy।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q037. eBGP vs iBGP?

**Answer:** Different AS peer = eBGP; same AS = iBGP। iBGP has specific route propagation rules (full mesh/route-reflector) and often uses IGP/next-hop reachability।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q038. Local Preference কী?

**Answer:** BGP-এর within-AS outbound route preference attribute; higher local-pref generally preferred when compared under policy/selection sequence। Inbound traffic directly control করে না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q039. Prefix-list কেন?

**Answer:** Allowed advertised/received networks explicitly constrain করে; accidental route leak, private/documentation prefix advertising কমায়। Production-এ max-prefix, RPKI/ROA and monitored policiesও দরকার।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q040. BGP established কিন্তু 0 route কেন?

**Answer:** Neighbor connectivity ঠিক থাকতে পারে কিন্তু network statement exact RIB route নেই, AF inactive, prefix filters, route policies বা nexthop invalid। Advertisement/received routes verify করো।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 05 — DHCP, DNS, NAT, NTP

### Q041. DHCP DORA ব্যাখ্যা?

**Answer:** Discover→Offer→Request→Acknowledge; server a lease assigns IP/mask/router/DNS options। DORA complete মানেই Internet reachable নয়; gateway and route must work।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q042. DHCPv4 ports?

**Answer:** Client UDP/68 and server UDP/67। Initial request may broadcast, so routed VLAN often DHCP relay needs correct scope and return route।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q043. Option 3 vs Option 6?

**Answer:** DHCP option 3 is router/default gateway list; option 6 supplies DNS resolvers। Wrong option 6 হলে IP ping works কিন্তু name fails হতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q044. 169.254.x.x address মানে কী?

**Answer:** IPv4 link-local/self-assigned address, often when DHCP lease could not be obtained। VLAN/DHCP server/client NIC investigate; APIPA by itself Internet route দেয় না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q045. DNS A vs AAAA?

**Answer:** A record resolves hostname to IPv4, AAAA to IPv6। Correct DNS response পেলেও service down/TLS/route failures separate।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q046. DNS NXDOMAIN বনাম SERVFAIL?

**Answer:** NXDOMAIN normally name doesn’t exist in DNS context; SERVFAIL indicates resolver/server could not complete processing। Split DNS, delegation, DNSSEC or upstream issues distinguish।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q047. NAT vs PAT?

**Answer:** NAT changes source/destination addresses; PAT/NAT overload maps multiple inside flows via port translations। State, return path and firewall policies matter।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q048. CGNAT থাকলে home port forward কেন fail?

**Answer:** Home router-এর private/shared WAN upstream CGNAT-এর আড়ালে থাকে; upstream mapping ছাড়া unsolicited inbound path নেই। ISP public IPv4 or secured IPv6/VPN solution প্রয়োজন হতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q049. NTP কেন NOC-এ দরকার?

**Answer:** Logs, syslog, monitoring and RCA timestamps align করে। Time zone selection (Asia/Dhaka +06) and actual clock sync two separate steps।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q050. Ping IP কাজ করে, domain কাজ করে না কেন?

**Answer:** Most likely DNS resolution/path issue; check `nslookup`/`dig`, configured DNS server, ACL and upstream resolver। Also verify host proxy/DoH and browser specifics।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 06 — PPPoE and Dial-up

### Q051. PPPoE কী?

**Answer:** PPP packets Ethernet-এর উপর encapsulate করে subscriber session/authentication; home router client এবং ISP AC/BNG server থাকে। OLT/ONU L2 access transport দিতে পারে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q052. PPPoE discovery four messages?

**Answer:** PADI, PADO, PADR, PADS। Then PPP LCP, authentication and NCP/IPCP negotiation; session ID assigned during discovery।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q053. PADI পাঠালেও PADO না এলে কী?

**Answer:** Physical link, ONU LOS, LAN/bridge, VLAN tagging/service-port/OLT uplink, AC service-name and PPPoE server enabled status যাচাই। Password change PADO absence-এর primary fix নয়।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q054. PADO আছে কিন্তু authentication fail?

**Answer:** Discovery path reached server. Username/password, RADIUS user status, PPP profile, service permissions, allowed auth protocol and logs examine।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q055. PPPoE 1492 MTU কেন?

**Answer:** Typical 1500-byte Ethernet payload থেকে PPPoE/PPP overhead 8 bytes বাদ দিলে IPv4 PPP link MTU 1492। RFC4638 and larger Ethernet frames can allow exceptions।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q056. Dial-up শব্দ আজও কেন ব্যবহার হয়?

**Answer:** Historical telephone modem dialing-এর term modern router UI-তে PPP session setup বোঝাতে থাকে। Ethernet/fiber PPPoE connection actual phone number dial করে না।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q057. PPPoE client NAT out-interface কোনটা?

**Answer:** If RouterOS PPPoE interface named `pppoe-out1`, source NAT egress should match `pppoe-out1`, not physical ether1। Firewall policy separately configure করতে হবে।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q058. PPPoE up but no Internet causes?

**Answer:** IPCP assigned address, default route, NAT, DNS, BNG/ISP forwarding, policies, ACL, PMTUD/MTU and service outage check। PADS/session up only authentication progress shows।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q059. PPPoE user from MAC mapping automatically ONU identify করে?

**Answer:** না। BNG PPP session user/MAC information এবং OLT ONU/port/optical mappings different systems থেকে correlate করতে হয়। Per-vendor OLT inventory essential।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q060. PPPoE vs DHCP WAN selection?

**Answer:** ISP provisioning method dictates it: PPPoE uses credentials/session, DHCP provides IP lease on L2, static uses manually supplied IP parameters। One correct WAN service design per interface should be chosen।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 07 — Home Router and Broadband

### Q061. Bridge ONU vs Router ONU?

**Answer:** Bridge ONU forwards Ethernet PPPoE service to downstream CPE, while router ONU can terminate PPPoE/NAT/DHCP itself। Home Wi-Fi router roles differ and double NAT can arise।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q062. Home router WAN vs LAN?

**Answer:** WAN is upstream facing link, LAN is local client network in usual CPE layout। WAN type DHCP/static/PPPoE determined by ISP; LAN DHCP usually assigned private addressing।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q063. AP mode কখন ব্যবহার করব?

**Answer:** When upstream router already performs routing/DHCP/NAT, Wi-Fi box can be used as access point/bridge। Prevent duplicate DHCP server and unnecessary double NAT।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q064. Wi-Fi full bars but browsing slow?

**Answer:** Wi-Fi RSSI alone does not prove WAN throughput. Check channel/interference, backhaul negotiation 100M vs 1G, WAN utilization, DNS, packet loss and subscriber shaping।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q065. Router LED WAN up কিন্তু PPPoE fail?

**Answer:** Layer1 Ethernet link up only; PPPoE discovery/authentication distinct higher-stage checks। VLAN, AC and credentials examine using logs. 

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q066. LAN clients get wrong 192.168 subnet কেন?

**Answer:** An unexpected/rogue DHCP server or multiple router mode devices can offer leases. Check DORA server identifier, switch VLAN/PVID and active DHCP pools।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q067. Home router public IPv4 absence diagnosing?

**Answer:** Examine WAN IP; if RFC1918 or 100.64/10, CGNAT/shared service likely. Compare router WAN vs public IP view, avoiding VPN/proxy ambiguity।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q068. Cannot access router management safely?

**Answer:** Confirm local management subnet, gateway, port, ACL, service enabled and remote mode. Avoid exposing router admin to public Internet; use secure VPN and least privilege।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q069. Static WAN gateway wrong হলে?

**Answer:** WAN interface may be up and IP configured yet no off-subnet reachability. Check prefix, gateway adjacent neighbor, ARP, route and ISP-issued allocation।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q070. ONU online কিন্তু CPE no IP?

**Answer:** ONU PON registration success does not prove Ethernet UNI, VLAN bridge, PPPoE or DHCP success. Isolate from port status to session negotiation and IP allocation।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 08 — GPON / OLT / ONU / dBm

### Q071. OLT কী?

**Answer:** Optical Line Terminal at ISP access aggregation; controls PON ONUs and delivers services to uplink/BNG. Specific OLT commands vary by vendor/firmware।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q072. ONU vs ONT?

**Answer:** Both describe optical network termination units; ONT generally customer premises type. ONU can be bridge or routed depending model/profile।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q073. ONU LOS মানে কী?

**Answer:** Loss of optical signal/alarm, inspect fiber, splitter, connector, bending, PON card and optical budget. Alarm handling vendor dependent; no unsafe laser staring।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q074. GPON shared bandwidth কী?

**Answer:** Classical GPON nominal downstream 2.488Gbps/upstream 1.244Gbps shared on PON before overhead, with DBA/service policy. Each ONU does not get full nominal rate simultaneously।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q075. ONU RX vs ONU TX কোন direction?

**Answer:** ONU RX receives downstream power from OLT; ONU TX emits upstream toward OLT. OLT per-ONU RX is separate measurement and may not be available on all equipment।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q076. −18dBm vs −25dBm stronger?

**Answer:** −18 dBm optical power is stronger. Delta 7 dB corresponds roughly 5× difference in mW; judge safe/unsafe only against actual optic datasheet thresholds।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q077. dB vs dBm?

**Answer:** dB is power ratio/attenuation, while dBm is absolute power relative to 1mW। Rx = Tx dBm − path loss dB for simplified optical power budget।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q078. Splitter ratio 1:32 means 32 user each exact 1/32 traffic?

**Answer:** No. Optical splitter divides optical energy while packet scheduling/service profiles determine data throughput. Shared PON capacity and oversubscription need monitoring।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q079. ONU online but PPPoE no PADO?

**Answer:** Verify ONU LAN bridge state, service VLAN mapping, OLT uplink tagging, aggregation trunk and BNG AC. Do not immediately assume optical RX bad if stable/within spec।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q080. Optical power suddenly more negative?

**Answer:** Likely higher attenuation, verify fiber event and peer TX before root cause. Record before/after RX, PON/ONU IDs, timestamp, splitter scope and alarms।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 09 — Cabling, Ethernet speed, interface health

### Q081. 1Gbps vs 1GB/s?

**Answer:** 1 Gbps is 1 billion **bits** per second, theoretical 125MB/s before overhead. Application throughput depends on protocol, disk, CPU, congestion and device।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q082. Cat6 vs Cat6A 10Gbps?

**Answer:** Cat6A certified deployment targets 10GBASE-T 100m; Cat6 10GbE reach depends on environment and is typically shorter. Never guarantee from label alone; certify cable।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q083. 10GBASE-SR vs LR?

**Answer:** SR is short-reach typically multimode; LR typically single-mode with longer reach. Check exact optic wavelength, power budget, fiber and connector compatibility per model।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q084. SFP port accepts any SFP+ 10G module?

**Answer:** No. Slot form factor/speed support, optic interoperability, FEC and license/vendor restrictions vary. Inspect product datasheet before buying/configuring।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q085. 10G link 2Gbps graph মানে?

**Answer:** The current measured directional traffic is 2Gbps, roughly 20% of a 10Gbps link, not a physical 2G negotiation. Confirm actual port speed/counters।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q086. Why CRC/FCS errors?

**Answer:** Potential cabling, optics, interference, duplex mismatch, hardware faults or physical signal issues. Correlate with interface resets, temperature, RX/Tx and both-end counters।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q087. LACP member down yet port-channel up?

**Answer:** Some members may remain active so bundle stays up at reduced aggregate capacity. Review each member operation operational state and LACP neighbors, hashing and min-links policy।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q088. Uplink/downlink confusion?

**Answer:** Direction is relative to observer: OLT uplink goes to aggregation, PON downstream goes toward ONU; interface IN/OUT maps to configured port viewpoint. Record exactly which device and direction।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q089. What is a microburst?

**Answer:** Brief high-rate traffic spike causing buffer overflow/discards despite moderate multi-minute graph averages. Need granular counters/telemetry to diagnose।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q090. Auto MDI/MDIX meaning?

**Answer:** Modern Ethernet PHY can adapt TX/RX pair roles, so crossover cabling often unnecessary. Still require proper wiremap, certified pair integrity and negotiated speed।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

## 10 — NOC troubleshooting & operations scenarios

### Q091. “User active but cannot use Internet” first 5 checks?

**Answer:** Check PPPoE active with valid IP/route, customer CPE WAN and LAN DHCP, gateway reachability, DNS vs external IP path, NAT/firewall/session counters. Record exact time/user/OLT before making changes।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q092. “Only one VLAN fails” prioritize কী?

**Answer:** Compare working VLAN and failed VLAN across access PVID, trunk allowed VLAN, tagged/untagged membership and SVI/gateway. Distinguish L2 failure from ACL/host firewalls।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q093. “All OLT users offline” one-by-one ONU reset?

**Answer:** No. Check shared OLT uplink, PON port/feeder fiber, power, aggregator VLAN/BNG, monitoring alarms and change window first. Avoid mass disruptive resets without evidence।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q094. “Only DNS domain fails” immediate action?

**Answer:** Test A/AAAA from configured resolver and approved alternate, identify NXDOMAIN vs SERVFAIL vs timeout; compare resolver caches/authoritative. Never globally replace DNS without understanding corporate split DNS।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q095. “P2P shows RX -24dBm” severity?

**Answer:** Cannot judge from number alone: inspect transceiver part number and RX min/max specifications, wavelength, port counters and trend. Compare both ends and time, do not assume all optics same budget।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q096. “BGP Established but traffic drops” কী হবে?

**Answer:** Check installed best route, forwarding next-hop, policy, return path, MTU, traffic graphs and filters; Established only control-plane peer state। Verify advertisement and route selected in RIB/FIB।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q097. “Ping 8.8.8.8 fails” Internet down নিশ্চিত?

**Answer:** Not necessarily: ICMP filtered/rate-limited, host/network policy or specific destination issues can produce loss। Test permitted destinations/protocols and traceroute alongside reachability indicators।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q098. “Switch loop suspected” evidence?

**Answer:** MAC flapping, broadcast/unknown-unicast spikes, STP topology changes, CPU high and redundant cables. Isolate safely with change approval and avoid pulling random core uplinks।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q099. “Link down after 10G optic change” checklist?

**Answer:** Check module compatibility, wavelength, fiber type/polarity, Tx/Rx power, FEC and port admin/speed settings at both ends. Record original module/settings and revert safely on a scheduled test link।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

### Q100. RCA report-এ কি must?

**Answer:** Impact/time window (Asia/Dhaka), affected customers/devices, evidence/logs/ping/optical/counters, confirmed cause vs hypothesis, mitigation, recovery validation and prevention owner। Never present guesses as confirmed root cause।

**Follow-up to ask:** বাস্তব topology বা verification command দিয়ে ১টি উদাহরণ ব্যাখ্যা করো।

---

**Official reading:** [RFCs and vendor references](../12-career/03-learning-resources.md) · [20 labs](../10-hands-on-labs/README.md).
