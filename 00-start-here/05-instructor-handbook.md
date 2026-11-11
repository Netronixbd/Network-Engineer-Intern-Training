# Instructor Handbook: How to Teach Network Interns (Bangla + English)

## Training principle
প্রতিটি lesson একই pattern-এ নাও: **What → Why → Diagram → Configure → Verify → Break in lab → Repair → Report**. The goal is not copying commands, but knowing *why* each command changes forwarding and what evidence proves success.

## Example 35-minute lesson: Static IP and Gateway
**Minute 0–5:** Ask a student to say why IP address != gateway. Draw PC `192.168.10.10/24`, router `192.168.10.1`, remote PC `192.168.20.10`।

**5–15:** Explain subnet mask, host local vs remote decision, ARP gateway, longest match; show default route and return route.

**15–25:** Cisco `show ip interface brief`, then configure `ip address` + static route in simulator; MikroTik `/ip address print` + `/ip route print detail` equivalent.

**25–30:** Deliberately delete return route and ask them to diagnose, not reconfigure randomly.

**30–35:** Collect mini RCA, exact test command and observed failure, restore baseline.

## Lesson prompt matrix
| Ask interns | Good answer must include |
|---|---|
| `No PADO` কী? | L2/VLAN/AC reachability before password |
| ONU online means Internet? | Separate PON and PPPoE/service states |
| What is /26? | mask .192, block size 64, hosts 62 |
| What is native VLAN? | Untagged classification on trunk, vendor defaults |
| 1G port 900Mbps RX? | 90% directional utilization, possible congestion |
| −27 dBm okay? | Cannot judge without module min/max thresholds |
| BGP session Established but 0 prefix? | route filters, AF, RIB exact prefix, policy |
| DHCP giving wrong network? | Rogue DHCP/relay/scope/PVID |
| LAN works Internet fails? | gateway/route/NAT/PPPoE/DNS/upstream |
| Why need NTP? | Consistent logs and incident timelines |

## Practical assessment technique
Give student **known-good topology**. Change only **one fault** at a time, such as wrong VLAN membership, missing return route, wrong DNS or disabled PPPoE server. Ask for (1) symptom, (2) evidence, (3) suspected layer, (4) verified root cause, (5) fix, (6) test. Always reset to baseline and obtain mentor sign-off.

## Production network guardrails
- Lab routers separate from real ISP uplink; no copied client credentials or customer identifying details.
- Keep baseline backup, management path, change/rollback plan, never disable remote bridge VLAN filtering prematurely.
- Don't run unknown scripts/commands on real switch/router/OLT.
- Read-only inspection should be default in office NOC shadowing; write permission given only after approval.
- Avoid remote `reset-configuration`, `reload`, `no shutdown` on wrong ports, `route policy` changes, BGP session changes and mass ONU actions without proper change control.
- Sensitive examples in README are documentation IPs, not real upstream addresses.

## Mentor feedback sample
```markdown
### Daily assessment
Student ID: (internal only)
Lesson/date (Asia/Dhaka):
Topology and hypothesis:
Commands chosen (read-only vs write):
Expected:
Observed:
Root cause (confirmed/evidence):
Correction/rollback:
Score (0-20):
Strength:
Next improvement:
Mentor sign-off:
```

**Next:** [6-week roadmap](04-six-week-deep-roadmap.md) · [Scenario playbook](../08-troubleshooting/04-subscriber-end-to-end-fault-tree.md).
