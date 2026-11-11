# Lab 03: Subnetting & VLSM IP Plan

**Duration:** 45–60 minutes · **Tools:** Paper/Excel/Python helper

## Business requirement
A small office has Staff 55 users, Guest 24, CCTV 12, Management 6, and 2 P2P router links. Base `192.168.80.0/24`। Provide network, mask, usable, gateway and IP allocation. No overlapping subnets।

## Task
1. Sort largest to smallest (VLSM rule)।
2. Choose smallest network prefix that fits required host endpoints **plus gateway** for LANs where relevant।
3. Allocate consecutive blocks; leave spare for future।
4. Mark DHCP and static ranges; don't use network/broadcast addresses for conventional IPv4 LANs।
5. Verify each subnet using [helper](../scripts/subnet_calculator.py) and manual calculation।

## Sample answer (one valid solution)
| Network | CIDR | Usable | Gateway/Link |
|---|---|---:|---|
| Staff | 192.168.80.0/26 | 62 | .1 |
| Guest | 192.168.80.64/27 | 30 | .65 |
| CCTV | 192.168.80.96/28 | 14 | .97 |
| Mgmt | 192.168.80.112/28 | 14 | .113 |
| P2P A | 192.168.80.128/30 | 2 | .129/.130 |
| P2P B | 192.168.80.132/30 | 2 | .133/.134 |

**Discussion:** 55 staff + gateway = 56, /26 enough। /28 CCTV has 14 total usable, 12 cameras + gateway still fits।/28 Mgmt allows room for growth।

## Quiz
`192.168.80.114/28` → network `.112`, broadcast `.127`; `/26` has 64 total addresses; `.0` is network ID in `/26` allocation।

**Deliverable:** `ip-plan.csv` with columns: Department, VLAN, CIDR, Gateway, DHCP From, DHCP To, Static Reserved, Notes।
