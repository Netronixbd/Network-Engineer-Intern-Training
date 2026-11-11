# Intern Practical Skills Checklist & Scoring Sheet

**Use:** Copy this Markdown into private company training records. Do **not** commit student full name, account, personal contact or live device credentials to public GitHub.

| Topic | Demonstration required | Score (0–5) |
|---|---|---|
| OSI | Explain each layer using browser request example | ____ |
| TCP/UDP | Explain TCP handshake and DNS/BGP ports | ____ |
| Cabling | Cat5e/6/6A, media, 1G vs 10G, RJ45 wiremap | ____ |
| IP | Set correct static IPv4/gateway/DNS | ____ |
| DHCP | Observe DORA and lease fields | ____ |
| Subnet | Solve /26, /29, VLSM /31 exceptions | ____ |
| VLAN | VLAN10/20 tag/untag/forbidden matrix | ____ |
| Ports | Access/trunk/hybrid and native VLAN | ____ |
| Routing | Two Cisco/MikroTik routers static+return routes | ____ |
| DNS | A/AAAA/MX queries and failure classification | ____ |
| NAT | Explain PAT/double NAT/CGNAT | ____ |
| PPPoE | Describe PADI/PADO/PADR/PADS, auth and IP | ____ |
| Home CPE | WAN PPPoE vs static vs DHCP, LAN DHCP, security | ____ |
| GPON | ONU/OLT mapping and RX/TX dBm vs specification | ____ |
| BGP | eBGP TCP/179, ASN, filters, safe demo | ____ |
| NTP | Time sync vs timezone, check source | ____ |
| Speed | 1G/10G/100G interface concepts, TX/RX counters | ____ |
| Troubleshooting | No-PADO/no-DNS/no-gateway case with evidence | ____ |
| Documentation | Report time, observed output, cause, fix | ____ |
| Safe operations | Backup/approval/rollback, no live secrets | ____ |

**Total:** ____ / 100; **80+** with all critical safety items passed is suggested readiness for supervised junior tasks. This is internal training guidance, not a certification.

## Oral exam sample
1. Given PC `192.168.10.130/26`, draw address plan and first/last usable.
2. Explain what a gateway MAC is and how frame changes across router.
3. Why can ONU online but PPPoE be down? Show fault tree.
4. What makes a trunk carry VLAN20? Show allowed list and egress tags.
5. Explain how a BGP peer established with 0 accepted prefixes can occur.
6. Why `-25 dBm` alone doesn't prove optical fault?
7. What do you see on 1G interface with 100Mbps negotiation?
8. How would you verify static configuration without risking office connectivity?

**Resources:** [220 Viva Q&A](03-detailed-viva-100-qa.md) · [20 Lab index](../10-hands-on-labs/README.md).
