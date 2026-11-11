# Uplink & Downlink: ISP Topology, Capacity, Utilization and Bottlenecks

## Uplink / Downlink perspective
**OLT uplink:** OLT→aggregation/Core; **PON downlink:** OLT→ONU; **Subscriber uplink:** ONU/home router→ISP. In dashboards, `input/output` depends on the port's frame direction; do not assume graph **IN = upload for user** without mapping interface direction।

```mermaid
flowchart LR
 CUSTOMER[Subscriber LAN] <-->|100M/1G Ethernet| ONU[ONU]
 ONU <-->|Shared GPON ODN| OLT[OLT]
 OLT <-->|10G uplink example| AGG[Aggregation]
 AGG <-->|100G core example| CORE[Core / BNG]
 CORE <-->|10G / 100G upstream example| ISP[Upstream]
```

## Utilization example
One OLT uplink is **10 Gbps full duplex**. Current TX utilization `7.5 Gbps` = **75%** of its rated 10G direction; RX `4 Gbps` = 40%. Full duplex means TX and RX can operate simultaneously; `7.5+4=11.5` is not “115% utilization” of one direction। Bursty queues/microbursts may drop even if 5-min average is 60%; peak and discards matter।

## Oversubscription
Suppose 64 subscribers have packages of 100 Mbps: total sold rate = 6.4 Gbps, but actual simultaneous use may be much less. This **doesn't** guarantee or prove a 1G uplink is sufficient; busy-hour demand and SLA drive design।

## Checklist
- Layer1 negotiates correct speed and module/FEC.
- Monitor `bps`, `pps`, `errors`, `discards`, interface resets, 95th percentile, peak-hour burst.
- For LACP check all member ports, distribution hash and operational bundle state.
- For GPON check PON aggregate nominal up/down rate and DBA/service caps.
- For broadband complaint compare wired CPE test vs Wi-Fi test and ONU/OLT counters.
- Distinguish service bottleneck (shaper) vs physical bottleneck (uplink) vs CPU/queue bottleneck (router).

## Viva
- **Q:** Downlink always OLT uplink opposite? **A:** Direction depends on measurement point; define the endpoint।
- **Q:** 10G link 8Gbps = utilization? **A:** 80% in that direction।
- **Q:** Two 10G LACP single flow 20G? **A:** Usually no, flow hashing।
- **Q:** Microburst? **A:** Very short traffic spike that average graphs can hide।
- **Q:** ONU GPON 2.488Gbps every ONU? **A:** No, shared PON nominal aggregate downstream।

**References:** [IEEE Ethernet Task Force](https://www.ieee802.org/3/) · [GPON](05-olt-onu-gpon-design.md).
