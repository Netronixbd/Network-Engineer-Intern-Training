# Vendor Configurations: Cisco, MikroTik, Juniper, Huawei

> **Only isolated labs or simulators.** Commands are illustrative. Match device hardware, RouterOS/IOS/Junos/VRP release, interface names, licenses, existing configuration, management access, security/rollback plans. Never paste an entire example into a live production router/switch/OLT without approval.

## Basic initial configuration
| Vendor | Document | You'll practice |
|---|---|---|
| Cisco IOS/IOS XE | [Initial configuration](cisco-ios-initial.md) | IP, interface status, NAT, basic switch VLAN |
| MikroTik RouterOS v7 | [Initial configuration](mikrotik-routeros-v7.md) | IP, DHCP, NAT, safe mode / backup |
| Juniper Junos | [Initial configuration](juniper-junos-initial.md) | Interface IP, route, `commit confirmed` |
| Huawei VRP | [Initial configuration](huawei-vrp-initial.md) | VLAN and ports, VLANIF and static route |

## Extended end-to-end configuration
| Platform / focus | Deep-dive document | Topology |
|---|---|---|
| Cisco two-router IP & static route | [05 Cisco static full lab](05-cisco-static-end-to-end.md) | PC-A → R1 → R2 → PC-B |
| MikroTik two-router IP & static route | [06 MikroTik static full lab](06-mikrotik-static-end-to-end.md) | PC-A → R1 → R2 → PC-B |
| MikroTik PPPoE Server and Client | [07 PPPoE setup](07-mikrotik-pppoe-client-server.md) | Home CPE → PPPoE AC |
| Cisco VLAN access/trunk & L3 | [08 Cisco VLAN / SVI](08-cisco-vlan-l3-switch.md) | Staff/Guest → L3 GW |
| MikroTik VLAN bridge | [09 RouterOS VLAN filtering](09-mikrotik-vlan-bridge.md) | VLAN10/20 Access → Trunk |
| MikroTik WAN modes | [10 Home router](10-mikrotik-home-router-wan-modes.md) | WAN DHCP / Static / PPPoE |
| OLT/ONU | [11 Vendor-neutral provisioning SOP](11-olt-vendor-neutral-provisioning.md) | Subscriber → OLT → BNG |

## Before configuration: seven-step safety
1. Record model, serial (internally), firmware, interface map and actual design.
2. Confirm this is an isolated lab, not live production.
3. Obtain management console/recovery path and current backup.
4. Confirm lab IP addressing and reserved documentation ranges (e.g. `192.0.2.0/24`).
5. Choose one WAN mode or one network architecture per exercise. Alternative sections aren't additive.
6. Test read-only `show`/`print` commands first, then apply changes one line at a time.
7. Validate ping/route/DHCP/PPP status; save configuration only after approval and restore baseline.

## Safe lab IP plan
| Role | Network / IP |
|---|---|
| VLAN10 Staff | `192.168.10.0/24`, GW `.1` |
| VLAN20 Guest | `192.168.20.0/24`, GW `.1` |
| VLAN99 Management | `192.168.99.0/24`, GW `.1` |
| Lab P2P | `192.0.2.0/30`: .1 ↔ .2 (reserved documentation range) |
| PPPoE simulated | `10.100.0.1` server; `.2–.50` client pool |

**Next:** [20 Labs](../10-hands-on-labs/README.md) · [Vendor-independent fault tree](../08-troubleshooting/04-subscriber-end-to-end-fault-tree.md).
