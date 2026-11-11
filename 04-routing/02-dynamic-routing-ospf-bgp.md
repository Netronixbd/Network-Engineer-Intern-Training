# Dynamic Routing: OSPF, BGP, RIP | Beginner → ISP Intro

## 1. Dynamic routing কী?
Routers protocol-driven control plane দিয়ে reachability exchange/compute করে। Link failure হলে protocol converge করে alternate path select করতে পারে, তবে convergence time/design/failure scope matter। Dynamic routing **DHCP dynamic IP-এর সঙ্গে সম্পর্কযুক্ত নয়**।

| Protocol | Type | Common use | Core concept |
|---|---|---|---|
| RIP | Distance vector (legacy) | Education/legacy | Hop count, limited scale |
| OSPF | Link-state IGP | Enterprise/ISP internal | LSDB, SPF, areas, cost |
| IS-IS | Link-state IGP | Large ISP/core | Levels, adjacencies, SPF |
| BGP | Path vector policy protocol | ISP/AS peering, large fabric | ASN, AS_PATH, policy, prefixes |

## 2. OSPF foundation
- Neighbor adjacency forms using hello/dead timers and matching network/area parameters (other conditions apply)।
- Areas: backbone Area 0; design scales flooding/LSDB scope।
- Router ID: unique 32-bit identification।
- Cost: path selection input; not simply 'fewest hops'।
- Verify: neighbor `Full` state as appropriate, routes installed, interfaces included, passive interfaces, auth, MTU, area mismatch।

## 3. BGP foundation (ISP focus)
- **ASN:** Autonomous System Number, identifies administrative routing domain।
- **eBGP:** Between different ASNs; **iBGP:** within same ASN।
- **Prefix advertisement:** You advertise permitted networks subject to routing/policy conditions।
- **AS_PATH:** Inter-AS path attribute, loop prevention and policy consideration।
- **Local Preference:** Common intra-AS outbound policy lever; higher generally preferred (subject to other selection steps)।
- **MED:** Optional hint for ingress path selection; not universally honored।
- **Import/export policy:** Safety-critical; incorrect policy can leak routes or withdraw intended service।
- **RPKI/IRR/prefix filters/max-prefix:** Route security hygiene; vendor-specific implementation।

## 4. BGP case illustration
Customer AS 65010 ↔ Provider AS 65020 over `192.0.2.0/30` (**documentation addresses**). Customer prefix `198.51.100.0/24` is example-only, **must not** advertise on Internet। Lab asks: neighbor established? route in RIB? outbound prefix-policy matched? BGP session active হলেও prefix না আসতে পারে।

## 5. When to use what?
Single router + default gateway → static default often enough। Several interconnected routers → OSPF/IS-IS may simplify internal routing। Two different ISPs exchanging policies/prefixes → BGP। More protocols ≠ automatically better design।

## 6. Troubleshoot protocol (read-only first)
- Interface/P2P reachable?
- Correct source interface, ASN, peer IP?
- TCP/179 permitted (BGP)? OSPF hellos and L2 adjacency?
- Neighbor/session state, timers, auth, MTU?
- Import/export policies and route filters?
- Installed route vs learned route vs advertised route আলাদা verify?
- Next-hop resolution, return path, route preference?

## Scenario
`BGP Established`, but client complains route unreachable: local RIB, advertised/received prefixes, next-hop, filters, data-plane drops, traceroute and upstream confirmation collect করো। **Without change approval, do not reset BGP session.**
