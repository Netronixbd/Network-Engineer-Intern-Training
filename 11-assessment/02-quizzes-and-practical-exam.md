# Weekly Quizzes, Practical Exams & Mentor Evaluation

## Week 1: Core Fundamentals (10 questions, 2 marks each)
1. Define LAN and WAN with examples.
2. Explain the difference between MAC address and IP address.
3. Name OSI layers in ascending order.
4. What happens when a host ARPs for its gateway?
5. Find network ID for `192.168.10.130/26`.
6. Compute usable hosts in a `/27`.
7. List three RFC1918 blocks.
8. Static IP vs DHCP IP: what changes at configuration time?
9. What does `169.254.x.x` suggest on a Windows PC?
10. Why might ping fail while HTTPS still works?

**Answer key:** 1. Local vs geographically spread networking, with concrete examples; 2. MAC local L2 delivery vs IP logical L3 routing; 3. Physical, Data Link, Network, Transport, Session, Presentation, Application; 4. ARP maps next-hop IPv4 to MAC; 5. `192.168.10.128`; 6. 30; 7. 10/8,172.16/12,192.168/16; 8. manual vs DHCP lease; 9. DHCP failure/link-local fallback likely; 10. ICMP policy/path differs।

## Week 2: Switching / Routing (10 questions, 2 marks each)
1. Define VLAN and explain broadcast domain.
2. Access vs 802.1Q trunk port.
3. Why is VLAN10-to-VLAN20 ping blocked before routing?
4. What problem does STP solve?
5. Why is a single TCP flow not guaranteed to use all 2×10G LACP bandwidth?
6. What is default route and its notation?
7. What is longest prefix match?
8. What happens if R2 misses return route to R1 LAN?
9. OSPF vs BGP use case.
10. Why must both ends of trunk agree on allowed VLANs?

**Answer key:** 1. L2 segmentation; 2. one untagged user VLAN vs multiple tagged VLANs; 3. Layer3 gateway missing; 4. layer2 loop; 5. per-flow hash; 6. 0.0.0.0/0 or ::/0; 7. most-specific matched route; 8. asymmetric/one-way loss; 9. internal IGP vs policy/inter-AS; 10. otherwise tagged traffic dropped/misclassified।

## Week 3: Services / ISP / NOC (10 questions, 2 marks each)
1. DHCPv4 DORA steps.
2. What is DNS A vs AAAA?
3. Why NAT does not replace firewall?
4. What is PPPoE session state vs Internet service state?
5. Compare OLT and ONU.
6. Is `-25 dBm` universally bad?
7. Name three causes of LACP bundle not coming up.
8. What should a packet loss ticket contain?
9. Define SNMPv3 and why you prefer it over public SNMPv2c.
10. Why synchronize device clocks using NTP?

**Answer key:** 1. Discover/Offer/Request/Acknowledge; 2. IPv4/IPv6 records; 3. NAT translation ≠ access policy; 4. PPP active != L3/DNS healthy; 5. provider side/customer side; 6. depends on optics/ODN spec; 7. mode/member/MTU-speed config; 8. timestamps, source/destination, count/loss, impact, evidence; 9. auth/privacy capability; 10. timeline correlation।

## Final practical exam (60 marks)
| Task | Marks | Pass evidence |
|---|---:|---|
| Design 3 VLAN IP plan with CIDR | 10 | No overlap, correct gateway |
| Switch VLAN10/VLAN20/trunk | 10 | VLAN/trunk outputs + tests |
| Router inter-VLAN route | 10 | Bidirectional ping, return path |
| DHCP and NAT lab simulation | 10 | DHCP lease, route, NAT counter |
| Diagnose inserted fault | 10 | Hypothesis → proof → repair |
| Write NOC incident report | 10 | Clear timestamp, impact, output, RCA status |

## Mentor rubric
**Excellent (90–100):** independently explains reasons, verifies edge cases, safely records rollback. **Good (75–89):** accurate procedures with minor prompting. **Developing (60–74):** understands theory, needs help with verification. **Needs support (<60):** revisit foundations and labs. Unsafe production action always triggers separate review regardless of grade।

## Interview challenge pool
- Explain step-by-step journey when typing `https://example.com` into a browser.
- Build `192.168.100.0/24` VLSM plan for 50, 20, 10 and 2 hosts.
- Read a route table with connected, default and static prefixes and choose next hop.
- Explain how a wrong switch trunk allowed VLAN list breaks only some clients.
- Compare PPPoE `online`, ONU `online`, and actual Internet `usable`.
- Draft a neutral RCA request to upstream including packet-loss evidence.
