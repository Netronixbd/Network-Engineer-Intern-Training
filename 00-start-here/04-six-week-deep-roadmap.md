# 6-Week Deep Learning Roadmap | Intern → Junior NOC / ISP Support

> Existing [4-week starter plan](02-four-week-roadmap.md) remains available; this is the **extended 6-week version** with 20 practical labs and 220 viva Q&A. Designed for 5 teaching days/week, approx 60–90 minutes theory + 60–120 minutes supervised practice per day.

| Week | Daily outline | Lab | Expected skill |
|---|---|---|---|
| 1: Foundation | Day1 LAN/MAN/WAN, devices; D2 OSI; D3 TCP/UDP; D4 Ethernet/cabling; D5 ARP and L2/L3 | 01, 19 | Explain packet/frames, cable and ports |
| 2: Addressing | D1 private/public/CGNAT; D2 static vs DHCP; D3 /24-/30; D4 VLSM; D5 gateway/route tests | 02, 03, subnet workbook | Design and validate IP plan |
| 3: Switching | D1 VLANs; D2 tag/untag/forbidden; D3 access/trunk/hybrid; D4 L3 SVI; D5 STP/LACP | 04, 07, 15 | Make VLAN table and trace tagged path |
| 4: Routing and services | D1 static routes; D2 return path; D3 OSPF; D4 DNS/DHCP; D5 NAT/NTP | 05, 06, 08, 09, 17 | Configure small routed network and test services |
| 5: Broadband ISP | D1 CPE WAN modes; D2 PPPoE phases; D3 PPPoE lab; D4 ONU/OLT/GPON; D5 dBm and uplink | 10, 13, 14, 16 | Trace customer ONU→BNG→Core and collect evidence |
| 6: NOC advanced | D1 BGP intro; D2 1G/10G optics; D3 monitoring/syslog; D4 failure scenarios; D5 final presentation | 11, 12, 18, 20 | Fault-isolation, RCA and production safety |

## Mentor's daily flow
1. **10 min recall:** last lesson quiz + 3 rapid viva questions.
2. **30 min concept:** one real ISP example plus one diagram.
3. **20 min configuration reading:** explain every line and what breaks if wrong.
4. **60 min lab:** student operates sandbox with mentor observation.
5. **15 min RCA notebook:** issue→evidence→cause→fix→verification.
6. **5 min safety:** what must not be tried on live network.

## Suggested weekly assessment
| Criteria | Weight |
|---|---:|
| Conceptual clarity / explain with diagram | 25% |
| IP and configuration accuracy | 25% |
| Verification + troubleshooting | 25% |
| Safety/rollback/credential hygiene | 15% |
| Documentation, peer communication | 10% |

**Minimum pass:** no safety violation, can verify 2-router route/VLAN, can differentiate PPPoE discovery vs auth and ONU online vs Internet works, documents evidence rather than guessing. Unsafe production change = automatic stop and retraining.

## Day-30 capstone prompt
“A home router shows PPPoE connected, but phones cannot browse, ONU is online, ONU RX −21 dBm; where do you start?” Student must avoid concluding optical fault from a single RX value. They should check client DHCP, gateway, DNS, NAT, route, browser/connectivity, service status and timestamp, then escalate with evidence.

## Lab/simulator recommendations
- **Cisco**: Packet Tracer or appropriate licensed IOS virtual image in GNS3/EVE-NG.
- **MikroTik**: CHR with license/time-limit awareness, virtual isolated topology or spare RouterOS device.
- **OLT/ONU**: read-only lab/demo hardware or whiteboard topology unless authorized vendor simulator available.
- **No production:** never test flood/ping sweeps, bulk BGP advertisements or destructive resets on operational network.

**Reading:** [Instructor handbook](05-instructor-handbook.md) · [20 labs](../10-hands-on-labs/README.md) · [100 detailed viva](../11-assessment/03-detailed-viva-100-qa.md).
