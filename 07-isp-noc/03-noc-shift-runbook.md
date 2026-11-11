# NOC Shift Runbook, Escalation, SLA & Communication

## First 15 minutes of a new shift
1. Previous shift handover, active incidents, maintenance windows পড়ো।
2. Critical links/OLT/routers/BGP/LACP state dashboard check।
3. Check alert freshness: graph timestamp, poll failure, stale data।
4. Link utilization/CRC/packet drops/optical alarm abnormal changes check।
5. Ticket priorities/SLA clock, planned escalations note।

## Incident priority (sample, adapt by office policy)
| Priority | Description | Example |
|---|---|---|
| P1 | Wide outage or critical core impact | Core uplink down, broad subscriber outage |
| P2 | Major degradation with many users | Regional packet loss, high congestion |
| P3 | Limited service impact | One distribution switch/few clients |
| P4 | Minor issue/request | Documentation, routine check |

## Evidence standard
- **Time:** ISO 8601 local offset or clearly `Asia/Dhaka (UTC+06:00)`; logs may be UTC।
- **Source/Destination:** Source IP/interface, destination IP/domain; redact private user info।
- **Symptoms:** Loss %, latency min/avg/max, bandwidth graph, interface counters, optical Rx/Tx, severity।
- **Scope:** Single user / VLAN / POP / upstream / specific application।
- **Change history:** Any recent approved changes? Confirm causality, do not assume।
- **Action & next step:** Tested, expected vs actual, owner, next update।

## Triage: isolate fault domain
1. **Access:** Customer CPE/ONU/OLT/last mile?
2. **Aggregation:** Uplink VLAN/LACP/CRC/congestion?
3. **Core/Services:** BNG, AAA, routing, NAT, DNS?
4. **Upstream:** P2P ICMP loss measured from both ends, BGP, path?
5. **Destination:** Only one app/site/CDN fail?

## Escalation example (English)
> Subject: Packet Loss Observed on P2P Link | POP-A to POP-B
>
> Dear Team, We are observing intermittent packet loss on the P2P link between POP-A and POP-B since 14:20 BDT. Current loss: 7% over 100 probes (source interface confirmed). Customer traffic is impacted. Please investigate and share your findings, ETA, and RCA. Attached: timestamped ping/traceroute and interface counter details.

## Handover template
```text
Shift: Morning / Evening
Date & Timezone:
Engineer:
Open incidents (ID, severity, impact):
Current status and last confirmed evidence:
Pending vendor/field actions:
Planned maintenance / approval:
Next update deadline:
Risks / rollback notes:
```

## RCA vs workaround
**Workaround** restores service; **Root Cause Analysis (RCA)** explains mechanism/cause with evidence; after service restored, don't prematurely close without verifying recurring cause/monitoring।
