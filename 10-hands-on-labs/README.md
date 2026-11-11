# 20 Hands-on Labs | Beginner to Real ISP/NOC

> **Lab/simulator only.** Never apply commands to production switch, router, ONU or OLT without backup, mentor approval, planned maintenance and rollback.

| Lab | Topic | Difficulty | Expected evidence |
|---|---|---|---|
| [01](lab-01-two-pc-lan.md) | Two PC LAN / ARP | Easy | Ping + ARP |
| [02](lab-02-static-dhcp.md) | Static IP & DHCP | Easy | Lease and static IP |
| [03](lab-03-subnet-vlsm.md) | Subnet / VLSM | Easy | Address plan |
| [04](lab-04-vlan-trunk.md) | VLAN & Trunk | Medium | VLAN test matrix |
| [05](lab-05-static-routing.md) | Two-router Static Routing | Medium | Routes + ping |
| [06](lab-06-dhcp-nat.md) | DHCP + NAT/PAT | Medium | Lease + NAT stats |
| [07](lab-07-router-on-a-stick.md) | Router on a Stick | Medium | Inter-VLAN routing |
| [08](lab-08-ospf-basic.md) | OSPF Intro | Medium | Neighbors and routes |
| [09](lab-09-dns-service-check.md) | DNS Service Check | Easy | DNS evidence |
| [10](lab-10-fiber-pppoe-triage.md) | Fiber / PPPoE Fault | Medium | Optical + PPP RCA |
| [11](lab-11-monitoring-ticket.md) | Monitoring & Ticket | Medium | Actionable NOC ticket |
| [12](lab-12-capstone.md) | Mini Capstone | Hard | Diagram + config |
| [13](lab-13-pppoe-client-server.md) | PPPoE Server & Client | Medium | PADI→PPP→IP |
| [14](lab-14-home-router-wan.md) | Home Router WAN Modes | Medium | DHCP/Static/PPPoE |
| [15](lab-15-vlan-tagged-hybrid.md) | VLAN Tag/Untag/Hybrid | Medium | Port membership map |
| [16](lab-16-optical-budget.md) | Optical dBm & Loss Budget | Medium | Optical worksheet |
| [17](lab-17-dns-dhcp-ntp.md) | DHCP, DNS & NTP | Medium | DORA + resolver + time |
| [18](lab-18-bgp-two-as.md) | Two-AS BGP Peering | Advanced Intro | Filtered eBGP session |
| [19](lab-19-copper-fiber-1g-10g.md) | Copper/Fiber 1G/10G/100G | Easy | Interface/media checklist |
| [20](lab-20-final-isp-path.md) | ISP Customer Path Capstone | Hard | Full service RCA |

## Standard lab submission template

```markdown
# Lab ID / Name
Date/time (Asia/Dhaka):
Student ID (internal only):
Lab equipment/simulator version:
Objective and topology (Mermaid):
IP plan / VLAN table:
Expected result:
Observed commands/output (redacted):
Fault injected:
Root cause confirmed from:
Fix/verification:
Rollback and baseline restore:
Mentor sign-off:
```

**Passing:** Explain every command, show traffic/path evidence, recover one deliberately broken state and protect credentials.
