# 120 Network Engineer Intern Viva Questions & Answers (Bangla + English)

> মুখস্থ করার বদলে নিজের ভাষায় উদাহরণসহ বোলো। সব উত্তরে context ও version-dependent caveat apply করতে হবে।

**How to use:** Daily 10 Q, mentor follow-up asks “why/how”; lab proof where applicable।

## 01. Networking Fundamentals

### Q001. Network কী?

**Answer:** দুই বা তার বেশি device data exchange করলে network তৈরি হয়। Medium হতে পারে Ethernet, fiber বা wireless; শুধু physical connection থাকলেই service operational নিশ্চিত হয় না।

### Q002. LAN ও WAN-এর difference?

**Answer:** LAN সাধারণত office/building/campus scope-এর network; WAN geographically separated LAN বা network connect করে। উদাহরণ office VLAN vs ISP backbone।

### Q003. Hub, switch, router কীভাবে আলাদা?

**Answer:** Hub physical bits repeat করে; L2 switch MAC table দেখে VLAN scope-এ frame forward করে; router IP destination/route table দিয়ে different subnets connect করে।

### Q004. Bandwidth আর throughput এক?

**Answer:** Bandwidth হলো link capacity; throughput হলো actual delivered data rate। Protocol overhead, congestion, errors, server/device bottleneck-এর জন্য throughput কম হতে পারে।

### Q005. Latency, jitter, packet loss কী?

**Answer:** Latency হলো delay/RTT, jitter হলো delay variation, loss হলো expected packet বা reply না পাওয়া। Voice/video experience-এ jitter/loss বিশেষ গুরুত্বপূর্ণ।

### Q006. Network topology কয় ধরনের?

**Answer:** Common star, bus, ring, mesh, tree। Physical topology cabling দেখায়; logical topology VLAN/subnet/routing relationship দেখায়।

### Q007. MAC address কী?

**Answer:** Ethernet interface-এর L2 identifier, সাধারণত 48-bit। Local frame delivery-তে ব্যবহৃত; VLAN/bridge forwarding-এ switch MAC learning করে।

### Q008. Duplex কী?

**Answer:** Full-duplex একই সাথে send/receive; half-duplex sharing/turn-taking। Modern switched Ethernet link সাধারণত full-duplex।

### Q009. MTU কী?

**Answer:** Interface/path-এ supported maximum IP packet size (context-dependent)। MTU mismatch ও broken Path MTU Discovery connection hang বা retransmission করতে পারে।

### Q010. Layer-2 broadcast domain কী?

**Answer:** যে scope-এ Ethernet broadcast propagate করে, managed switch-এ সাধারণত VLAN একেকটি broadcast domain। Router L2 broadcast default-এ অন্য subnet-এ forward করে না।

## 02. OSI, Protocol & Ports

### Q011. OSI layer কয়টি?

**Answer:** ৭: Physical, Data Link, Network, Transport, Session, Presentation, Application। Real-world troubleshooting-এ abstraction; TCP/IP layer model implementation-এর কাছে।

### Q012. IP কোন OSI layer?

**Answer:** IPv4/IPv6 সাধারণত Layer 3 Network। IP route selection করে; MAC/802.1Q Layer 2 relevant।

### Q013. TCP vs UDP difference?

**Answer:** TCP sequencing/acknowledgments/retransmission করে reliable ordered byte stream দেয়; UDP datagram-based and apps own reliability implement করতে পারে।

### Q014. Ping কোন protocol?

**Answer:** ICMP Echo Request/Reply (IPv4 ICMP, IPv6 ICMPv6)। Echo filtered থাকলে ping fail মানেই সব traffic fail নয়।

### Q015. ARP কী করে?

**Answer:** IPv4 local link-এ next-hop IP-এর MAC খুঁজে। Remote Internet server-এর MAC নয়, off-subnet traffic-এর জন্য default gateway MAC resolve করে।

### Q016. DNS default port?

**Answer:** UDP/53 সাধারণ queries; TCP/53-ও valid, যেমন বড় responses এবং zone transfers। Specific DNS-over-TLS/HTTPS আলাদা ports/protocol use করে।

### Q017. SSH and HTTPS ports?

**Answer:** Typically SSH TCP/22 এবং HTTPS TCP/443 (HTTP/3 QUIC UDP/443)। Ports service configuration অনুযায়ী বদলাতে পারে।

### Q018. BGP port number?

**Answer:** TCP/179 normally peer session establish করে। BGP Established মানে expected route installed or customer traffic healthy guaranteed নয়।

### Q019. HTTP vs HTTPS কী?

**Answer:** HTTP application protocol; HTTPS uses HTTP over TLS-secured transport, server identity/certificate verification important। HTTP/3 commonly QUIC-based।

### Q020. Encapsulation কী?

**Answer:** Application data transport header → IP header → Ethernet/frame header পায়। Router hop-এ generally L2 header changes; NAT থাকলে IP/port translationও হতে পারে।

## 03. IPv4 Addressing

### Q021. IPv4 কয় bit?

**Answer:** 32-bit address, চারটি octet (0–255)। Example 192.168.10.10।

### Q022. Private IPv4 ranges কী?

**Answer:** 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 (RFC1918)। Entire 172.0.0.0/8 private নয়।

### Q023. Public IPv4 মানেই reachable?

**Answer:** না। Routing, firewall, upstream ACL, NAT, server listener and policy দ্বারা reachability determined হয়।

### Q024. Static IP vs Dynamic IP?

**Answer:** Static manually assigned or intentionally fixed; dynamic typically DHCP lease থেকে আসে। DHCP reservation client-এ automatic হলেও same IP maintain করতে পারে।

### Q025. Default gateway কী?

**Answer:** Host-এর off-subnet traffic next-hop। Gateway local subnet-এ L2 reachable হওয়া দরকার (normal LAN design)।

### Q026. Network address কী?

**Answer:** Subnet prefix-এর host bits zero করা base address। Typical /24 192.168.10.0 network ID।

### Q027. Broadcast address কী?

**Answer:** Traditional IPv4 broadcast subnet-এর all-host-bits-one address; /24 .255। /31 point-to-point এবং IPv6-তে আলাদা treatment আছে।

### Q028. APIPA কী?

**Answer:** IPv4 link-local 169.254.0.0/16 address; DHCP failure/no configured address অবস্থায় certain OS নিজে assign করতে পারে।

### Q029. Loopback address কী?

**Answer:** 127.0.0.0/8 IPv4 loopback; 127.0.0.1 widely used। Host নিজেকে test করতে পারে; actual NIC path test নয়।

### Q030. 0.0.0.0/0 মানে?

**Answer:** Default route, all IPv4 destinations match করে, কিন্তু more-specific route থাকলে longest prefix wins।

## 04. CIDR & Subnetting

### Q031. /24 mask কত?

**Answer:** 255.255.255.0; total 256 addresses, conventional usable 254।

### Q032. /26 mask ও block size কত?

**Answer:** 255.255.255.192; block size 64 last octet, network starts 0/64/128/192।

### Q033. 192.168.10.130/26 network?

**Answer:** 192.168.10.128/26; broadcast .191; conventional host range .129–.190।

### Q034. 192.168.5.70/27 network?

**Answer:** /27 block size 32, 70 falls 64–95; network .64, broadcast .95, hosts .65–.94।

### Q035. /30 কত usable?

**Answer:** 4 total addresses, conventional 2 usable। Often point-to-point IPv4 link।

### Q036. /31 usable কত?

**Answer:** RFC3021-compliant P2P links-এ two endpoints usable; typical broadcast LAN assignment হিসেবে নয়।

### Q037. /32 ব্যবহার কী?

**Answer:** Single host address/host route, loopback interface বা exact host route।

### Q038. VLSM কী?

**Answer:** Variable Length Subnet Mask: differing host requirements অনুযায়ী /26, /27, /28 etc mix করে allocated blocks। Largest subnet আগে allocate করলে planning সহজ।

### Q039. 50 hosts-এর জন্য smallest usual prefix?

**Answer:** /26 (62 usable), gateway plus 50 host requirement fits। /27-এ 30 usable, insufficient।

### Q040. Subnet overlap হলে কী সমস্যা?

**Answer:** Same IP block multiple interfaces/routes conflicting interpretation, ambiguous forwarding, DHCP leakage/duplicate addressing হতে পারে।

## 05. Switching & VLAN

### Q041. Switch MAC table কীভাবে learn করে?

**Answer:** Received frame-এর source MAC+VLAN এবং ingress port দেখে dynamic MAC table learn করে। Destination MAC জানা থাকলে specific egress port-এ forward।

### Q042. Unknown unicast কী হয়?

**Answer:** Destination MAC unknown হলে সাধারণ L2 switch ওই VLAN-এর eligible ports-এ flood করে (ingress বাদে), design/security features may affect।

### Q043. VLAN কেন দরকার?

**Answer:** L2 traffic segmentation, broadcast scope separation, management/security policy organization। VLAN alone inter-subnet routing নয়।

### Q044. Access port কী?

**Answer:** সাধারণত single VLAN untagged host-facing port; VLAN membership port config থেকে determined।

### Q045. Trunk port কী?

**Answer:** এক link-এ multiple VLANs tagged 802.1Q traffic carry করে; switch-switch বা switch-router uplinks-এ common।

### Q046. Native VLAN mismatch কী risk?

**Answer:** Untagged traffic unexpected VLAN-এ land করতে পারে, connectivity/security issue। Both ends deliberate matching and allowed list verify।

### Q047. Inter-VLAN routing কী?

**Answer:** VLAN10→VLAN20 packet যাওয়ার জন্য L3 gateway (router subinterface বা L3 switch SVI) লাগে, L2 trunk যথেষ্ট নয়।

### Q048. STP কেন লাগে?

**Answer:** Redundant Layer-2 paths-এর loop prevent করতে logical tree তৈরি ও কিছু ports block/discard করে। Without STP loop broadcast storm হতে পারে।

### Q049. LACP কী?

**Answer:** Multiple links এক logical bundle-এ negotiate/aggregate করে। Single flow সব member bandwidth sum পায় না; hashing/per-flow matters।

### Q050. PortFast কোথায় use?

**Answer:** Known host-facing edge port-এ startup convergence optimize করতে; switch-to-switch uplink-এ indiscriminate ব্যবহার risk।

## 06. Routing & Protocol

### Q051. Routing table কী?

**Answer:** Destination prefixes, next hops/interfaces, metrics/preferences etc-এর forwarding decision data। Connected/static/dynamic routes coexist করে।

### Q052. Longest Prefix Match কী?

**Answer:** Destination IP match করা available prefixes-এর মধ্যে highest prefix length wins, যেমন /24 over /0।

### Q053. Static route কী?

**Answer:** Admin-defined destination prefix + next hop/outgoing interface; limited topology-তে simple, failure handling requires design।

### Q054. Default route কী?

**Answer:** 0.0.0.0/0 (IPv4), ::/0 (IPv6) route; no more specific route match হলে use হয়।

### Q055. Return route কেন জরুরি?

**Answer:** Request path up হলেও destination reply কীভাবে source-এ ফিরবে সেটা valid থাকতে হবে। Missing return route common one-way connectivity symptom।

### Q056. OSPF কী?

**Answer:** Link-state IGP, neighbor/LSDB/SPF based route calculation; intra-domain networking-এ use।

### Q057. BGP কী?

**Answer:** Path-vector policy-driven routing protocol, AS-to-AS peering and large routed networks-এ common। TCP 179 session।

### Q058. ASN কী?

**Answer:** Autonomous System Number; BGP routing-domain identifier। Private ASN can be used in lab/internal designs under applicable standards।

### Q059. BGP Established মানে route OK?

**Answer:** না। Import/export filters, route origin, next-hop, RPKI, forwarding, ACL, traffic path still check করতে হবে।

### Q060. Metric vs administrative distance?

**Answer:** Metric same-protocol path selection-এ common; administrative distance/preference multiple routing sources-এর relative trust choose করতে help করে, vendor implementation differs।

## 07. DHCP, DNS, NAT & Services

### Q061. DHCP DORA কী?

**Answer:** Discover, Offer, Request, Acknowledge; DHCPv4 initial lease-এর simplified handshake।

### Q062. DHCP relay কবে লাগে?

**Answer:** Client broadcast domain থেকে ভিন্ন subnet-এর DHCP server reach করাতে relay configured হতে পারে।

### Q063. Rogue DHCP কী?

**Answer:** Unauthorized DHCP server wrong IP/gateway/DNS distribute করতে পারে; DHCP snooping and port-level security mitigation।

### Q064. DHCP reservation কি static IP?

**Answer:** Client DHCP-ই ব্যবহার করে কিন্তু server known MAC/identifier-কে same address lease দেয়; device manual static নয়।

### Q065. DNS A vs AAAA record?

**Answer:** A maps domain to IPv4, AAAA maps domain to IPv6।

### Q066. DNS fail হলে Internet পুরো down?

**Answer:** না। Direct IP service may work; split DNS, resolver, cache, firewall, server health isolate করো।

### Q067. NAT vs PAT?

**Answer:** NAT address translation general; PAT translates address plus transport port, multiple inside sessions shared outside IP use করতে পারে।

### Q068. Masquerade কী?

**Answer:** Source NAT flavor often outgoing interface IP use করে; MikroTik dynamic WAN-এ common। Actual egress interface correct হওয়া দরকার।

### Q069. Why NAT is not firewall?

**Answer:** Address translation alone permitted vs denied flows define করে না; separate stateful firewall policy needed।

### Q070. PPPoE কী?

**Answer:** PPP session over Ethernet, ISP subscriber auth, IP/route/service profile provisioning-এর path; session active হলেও data-plane healthy নাও হতে পারে।

## 08. IPv6 & Security

### Q071. IPv6 কয় bit?

**Answer:** 128-bit, colon-hex notation। Example 2001:db8::1 reserved documentation prefix।

### Q072. IPv6 link-local prefix?

**Answer:** fe80::/10; neighbor discovery/RA and on-link communication uses it।

### Q073. IPv6-এ ARP আছে?

**Answer:** না, Neighbor Discovery (ICMPv6 NS/NA) ব্যবহৃত হয়।

### Q074. SLAAC কী?

**Answer:** Router Advertisement-এর তথ্য দিয়ে host IPv6 address/route derive করার technique; DHCPv6-এর সঙ্গে different/combined roles possible।

### Q075. IPv6-এ broadcast আছে?

**Answer:** IPv4-style broadcast নেই; multicast and neighbor discovery used।

### Q076. ULA address কী?

**Answer:** fc00::/7 unique-local range, commonly fdxx locally assigned; global Internet routing expected নয়।

### Q077. ACL কী?

**Answer:** Access Control List: traffic permit/deny matching rule set; stateless/stateful behavior platform dependent।

### Q078. Least privilege কী?

**Answer:** User/service/device-কে operationally required minimum permissions/access দেওয়া।

### Q079. SNMPv3 কেন prefer?

**Answer:** Authentication/privacy support থাকে; unprotected community-string based SNMPv2c-এর তুলনায় secure monitoring possible when properly configured।

### Q080. Management plane কীভাবে protect?

**Answer:** SSH/HTTPS, restricted management VLAN/ACL, MFA/AAA where available, patching, logging, backups; no public passwords।

## 09. Vendor CLI & Verification

### Q081. Cisco `show ip interface brief` কী দেখায়?

**Answer:** Interface names, IP assignment and status summary; exact syntax IOS platform-specific।

### Q082. Cisco `show interfaces trunk` কী কাজে?

**Answer:** Which switchports trunk এবং VLAN allowed/active state check। Trunk config exist মানেই end-to-end VLAN healthy নয়।

### Q083. Cisco `ip route` example?

**Answer:** `ip route 192.168.20.0 255.255.255.0 10.0.0.2` add static route to remote LAN, next-hop must resolve।

### Q084. MikroTik route verify command?

**Answer:** RouterOS v7 `/ip route print detail`, connected/dynamic/static entries and next-hop inspect।

### Q085. MikroTik DHCP client verify?

**Answer:** `/ip dhcp-client print detail`; bound status, address/gateway/DNS lease details examine।

### Q086. Junos `commit check` কী?

**Answer:** Candidate configuration validate করে without activating; `commit` active config update করে।

### Q087. Junos `commit confirmed` কেন?

**Answer:** Approved remote change undo safety: specified time-এর মধ্যে confirm না করলে automatic rollback, supported device behavior।

### Q088. Huawei `display ip routing-table` কী?

**Answer:** Routing entries, protocol, next-hop/interface/route flags view।

### Q089. Config save করা কেন জরুরি?

**Answer:** Device reboot পরে intended configuration persist করতে; but wrong config permanently saving is harmful, so verify first।

### Q090. Read-only command দিয়ে শুরু কেন?

**Answer:** Current state/pattern বুঝে misconfiguration risk কমে; change-first troubleshooting root cause obscure করতে পারে।

## 10. GPON & ISP

### Q091. OLT কী?

**Answer:** Optical Line Terminal, provider-side PON equipment, subscriber ONU/ONT optical access terminate/manage করে।

### Q092. ONU/ONT কী?

**Answer:** Customer-side optical terminal; bridge/routing mode depending on deployment।

### Q093. PON splitter কী?

**Answer:** Passive optical signal distribution; split count adds optical loss and capacity sharing considerations।

### Q094. Rx/Tx dBm কী বোঝায়?

**Answer:** Optical received/transmitted power levels; acceptable range transceiver/device/spec, wavelength and ODN budget dependent।

### Q095. -25 dBm কি সব ONU-তে bad?

**Answer:** না। ONU/OLT module threshold, baseline and fault rate compare না করে universal verdict ভুল।

### Q096. LOS কী?

**Answer:** Loss Of Signal event; physical optical path fault clue, timestamp and related alarm inspection needed।

### Q097. BNG/BRAS কী?

**Answer:** Broadband Network Gateway, subscriber session termination and service/policy integration edge in many ISPs।

### Q098. RADIUS কী কাজ করে?

**Answer:** AAA: Authentication, Authorization, Accounting services for network access; PPPoE access often integrates it।

### Q099. CGNAT কেন ব্যবহার হয়?

**Answer:** IPv4 conservation: many subscribers share public IPv4 with NAT; per-flow traceability/port allocation/logging operational concern।

### Q100. Upstream packet loss কিভাবে report করবে?

**Answer:** Exact source/destination IP, time/timezone, probe count/loss percent, latency and route, impact plus supporting interface/graph data; assumptions separate।

## 11. NOC & Monitoring

### Q101. NOC engineer-এর first duty কী?

**Answer:** Impact/scope identify, evidence collect, existing incidents check, accurate escalation and status communication; unsafe unapproved action নয়।

### Q102. SNMP কী?

**Answer:** Simple Network Management Protocol, device counters/state query/traps; monitoring security/auth/ACL and polling behavior important।

### Q103. CRC error কী?

**Answer:** Layer-2 frame check error; physical medium/optics/cable/port issues among possible causes, evidence correlation required।

### Q104. Graph 95% util মানেই congestion?

**Answer:** Not necessarily; drops, queue/short interval, QoS, microbursts, peak profile and time series examine।

### Q105. Interface `up` কিন্তু loss কেন?

**Answer:** Queue congestion, FEC/CRC, hardware, routing, policer, upstream path or application-level factors; link status only L1/L2 clue।

### Q106. NTP NOC-এ কেন জরুরি?

**Answer:** Different device logs একই timeline-এ correlate করতে accurate timestamps vital।

### Q107. RCA কী?

**Answer:** Root Cause Analysis, validated cause, timeline, contributing factors, preventive actions documented; mere service restoration RCA নয়।

### Q108. SLA কী?

**Answer:** Service Level Agreement-এর service commitments/metrics (availability, response etc.)। Specific contract wording matters।

### Q109. MTTR কী?

**Answer:** Mean Time To Repair/Restore (organization definition confirm); incidents across period-এর average restoration duration।

### Q110. Handover-এ কী দিতে হয়?

**Answer:** Ticket IDs, priority, user impact, last verified status, pending actions, owner, next update time and risk notes।

## 12. Practical Troubleshooting

### Q111. PC has 169.254.x.x: next step?

**Answer:** Likely DHCP failure: VLAN and cable, DHCP pool, relay, server availability, DORA packet trace and ACL inspect।

### Q112. IP ping works, domain fails: next step?

**Answer:** Test resolver IP/config, `nslookup`/`dig`, UDP/TCP53 path, split DNS, cache and authoritative record।

### Q113. Two switches link UP, VLAN20 fail: why?

**Answer:** Allowed VLAN list mismatch, tag/PVID mismatch, STP blocking, VLAN absent on one switch; both-side trunk outputs compare।

### Q114. Static route added but no reply: why?

**Answer:** Missing return path, wrong next hop, firewall, host gateway or NAT; source-specific bidirectional tests inspect।

### Q115. BGP Established but traffic blackhole: what inspect?

**Answer:** Route installed and next-hop resolution, data-plane interface errors, filters, return path, export policy and upstream peer confirmation।

### Q116. PPPoE Active but user no browsing: checks?

**Answer:** Subscriber assigned IP, session profile/queue, BNG route, DNS, CPE LAN/NAT, CGNAT, loss and service reachability test।

### Q117. Rx level drops 8 dB from baseline: next step?

**Answer:** Check ONU/OLT historical optics/alarms, patch/splice/splitter and same-PON customers, compare vendor spec; don't declare universal threshold।

### Q118. LACP down although links UP: what inspect?

**Answer:** Mode active/passive, member/bundle state, port config speed/MTU/VLAN, remote partner ID, hashing not key to LACP formation।

### Q119. A site loads slowly only at peak: what check?

**Answer:** Timestamped utilization, queue drops, loss/jitter, TCP retransmits, application origin/CDN path and microbursts।

### Q120. Before changing a production route, what must you do?

**Answer:** Approval, impact assessment, config backup, tested rollback, maintenance window, peer coordination, observability and post-change verification।

---

**Practice extension:** Wrong answer হলে corresponding chapter-এর topology নিজে আঁকো এবং 1 relevant show/print/display command দিয়ে evidence উপস্থাপন করো।
