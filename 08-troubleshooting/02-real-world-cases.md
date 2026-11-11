# 15 Real-World NOC / Office Fault Scenarios

প্রতিটি case-এ **Symptom → Likely checks → Proof → Fix path** follow করো। Symptom alone root cause নয়।

### Case 01: Wi-Fi connected, no Internet
Check SSID-to-VLAN mapping, DHCP lease, gateway ping, DNS and captive portal. Verify AP uplink trunk and guest firewall. Avoid concluding ISP down before L2/L3 tests।

### Case 02: PC receives `169.254.x.x`
Likely DHCPv4 lease failure. Check DHCP service/scope, relay, VLAN, filtering, physical path. Packet capture DORA; don't randomly assign production IP।

### Case 03: Same VLAN PCs cannot ping
Check correct mask, client firewall, switch access VLAN, ARP, port isolation, MAC limit, port security। Switch MAC table shows learned correct ports?

### Case 04: VLAN 10 can ping gateway, VLAN 20 cannot
Check VLAN20 allowed on trunk, SVI/subinterface, STP and DHCP. Interface may be UP but wrong VLAN tagging।

### Case 05: Static route configured, remote LAN unreachable
Check route on forward and return path, next-hop ARP/reachability, host gateway, ACL. Use source-specific ping on router if supported।

### Case 06: DNS name fails, IP works
Check DNS configured, resolver reachability on UDP/TCP53, internal split DNS, cache, record, firewall। Avoid replacing office DNS blindly।

### Case 07: PPPoE session `active`, traffic not passing
Check assigned address, rate profile, session counters, route, CGNAT/NAT, upstream, RADIUS attributes, MTU/MSS, DNS. Session active only proves part of chain।

### Case 08: ONU online but PPPoE offline
Check customer CPE power/PPPoE settings, VLAN service map, account status, BNG discovery, AAA reject logs. Fiber online does not prove VLAN delivery।

### Case 09: Optical level worsens significantly
Compare historical Rx/Tx and thresholds; inspect splitter/splice/patch/fiber path. Check area correlation, LOS, connector type. Approved physical SOP only।

### Case 10: LACP member links up, aggregate down
LACP mode mismatch, ports in different LAG IDs, incompatible speed/MTU/VLAN config, negotiation. Read both ends, do not bounce bundle first।

### Case 11: Interface graph near capacity, users see jitter
Compare 1/5-minute average with shorter interval and queue drops, utilization percent, microbursts, shaping and QoS. Upgrade not always sole fix।

### Case 12: BGP Established but expected prefix absent
Check prefix exists locally, export/import policy, route filters, max-prefix, next-hop, community. Separate *learned* from *installed* routes।

### Case 13: Port up, high CRC/FCS errors
Investigate cable/fiber/optics/transceiver, duplex/speed/FEC, damaged connector. Correlate both sides and timestamps।

### Case 14: One site slow, other sites fine
DNS answer/CDN selection, regional path congestion, firewall, app server, TCP retransmits, MTU and client browser diagnostics। Avoid declaring total Internet outage।

### Case 15: IP duplicate, intermittent access
ARP instability, duplicate static assignment or DHCP reservation clash. Identify owner via authorized DHCP/switch inventory; carefully reassign after approval।

## Evaluation: Each incident report must include
- Verified facts vs hypotheses; timestamp/timezone; impacted scope
- 3 relevant outputs with redaction; before/after metrics
- Root cause (or explicitly **not confirmed**); action; prevention
- Who approved change; rollback plan; next handover owner
