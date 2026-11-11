# Lab 20: Capstone - ISP Subscriber Full Packet Walk & Fault Isolation

**Time:** 90–120m · **Format:** Whiteboard + supervised lab/simulator + team presentation.

```mermaid
flowchart LR
 PC[PC DHCP\n192.168.50.100] --> CPE[Wi-Fi CPE\nPPPoE + NAT]
 CPE --> ONU[Bridge ONU\nRX -20dBm example]
 ONU --> OLT[OLT PON1/1\nService VLAN300]
 OLT --> AGG[Aggregation Switch\nVLAN300 Tagged]
 AGG --> BNG[BNG\nPPPoE + AAA + Route]
 BNG --> CORE[Core / Upstream]
```

## Student tasks
1. Draw each box's **layer role**: PC L3, CPE NAT/PPP, ONU GPON/bridge, OLT optical + service mapping, aggregation VLAN, BNG authentication, core routing.
2. Trace **customer login**: PADI/PADO/PADR/PADS, PPP auth, IP address, default route, client DHCP, DNS lookup, NAT and TCP/UDP app flow.
3. Label **Uplink/Downlink** at ONU, OLT uplink, and router interfaces with observer perspective.
4. Make VLAN table: subscriber sends untagged on ONU UNI; upstream service VLAN300 tagged; BNG receives matching L2 service.
5. State why ONU `Online` and PPPoE `Connected` are two separate status levels.
6. Given one test incident, isolate and write RCA: (A) ONU LOS, (B) PPPoE no PADO, (C) Auth rejected, (D) PPP up but no DNS, (E) WAN link negotiated 100M.
7. Outline at least one verification command/counter/evidence per system, with vendor-specific caution.

## Evaluation rubric (100)
| Category | Marks |
|---|---:|
| Correct topology and L1/L2/L3 packet flow | 20 |
| IP, subnet, gateway, NAT/DNS/DHCP | 20 |
| PPPoE discovery/AAA and ONU/OLT VLAN | 20 |
| Evidence-based troubleshooting sequence | 20 |
| Clear communication, incident report, safe operations | 20 |

**Required deliverables:** topology Mermaid in `.md`, numbered test plan, redacted configuration, fault matrix, incident ticket including time, user/ONU identifiers and test outputs. No live username/password or public sensitive SN/phone in GitHub।
