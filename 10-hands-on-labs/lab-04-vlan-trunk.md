# Lab 04: VLAN 10/20 and Trunk Between Switches

**Duration:** 60–90 minutes · **Tool:** Cisco Packet Tracer

## Topology
```mermaid
flowchart LR
 A[PC1 VLAN10<br/>192.168.10.10/24] --> S1[SW1]
 B[PC2 VLAN20<br/>192.168.20.10/24] --> S1
 S1 ---|802.1Q trunk<br/>VLAN10,20| S2[SW2]
 S2 --> C[PC3 VLAN10<br/>192.168.10.20/24]
 S2 --> D[PC4 VLAN20<br/>192.168.20.20/24]
```

## Instructions
1. Two switches, four PCs connect; configure VLAN 10/20 on both।
2. Ports PC1/PC3 access VLAN 10; PC2/PC4 access VLAN 20।
3. Inter-switch ports `switchport mode trunk` and allow 10,20।
4. Hosts IP as diagram; no router/gateway for this exercise।
5. `show vlan brief`, `show interfaces trunk`, `show mac address-table` verify।

## Expected ping matrix
| Source | Destination | Expected |
|---|---|---|
| PC1 | PC3 | PASS (same VLAN10) |
| PC2 | PC4 | PASS (same VLAN20) |
| PC1 | PC2 | FAIL (different VLAN, no router) |
| PC3 | PC4 | FAIL (different VLAN, no router) |

## Fault insertion
Remove VLAN20 from **one end** allowed list in isolated simulator; PC2↔PC4 fail, PC1↔PC3 still passes. Restore after documenting difference।

**Deliverable:** topology screenshot, switch config snippets, trunk and VLAN output, 4 ping results, cause of inserted fault।
