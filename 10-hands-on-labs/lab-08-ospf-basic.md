# Lab 08: OSPF Single-Area (Optional Intermediate Lab)

**Duration:** 90 minutes · **Tool:** IOS router simulator supporting OSPF

## Objective
Manual static route vs dynamically learned route compare; neighbor discovery, area 0, router IDs and protocol routes observe।

## Topology / IP plan
R1 LAN `192.168.10.0/24`, R1–R2 P2P `10.0.0.0/30`, R2 LAN `192.168.20.0/24`। Same as Lab 05।

## Steps (router interfaces from Lab 05 assumed)
Use isolated routers with **old static remote-LAN routes removed for this experiment**, so OSPF-learned routes visible। On R1:
```cisco
router ospf 1
 router-id 1.1.1.1
 network 192.168.10.0 0.0.0.255 area 0
 network 10.0.0.0 0.0.0.3 area 0
 passive-interface GigabitEthernet0/1
```
On R2:
```cisco
router ospf 1
 router-id 2.2.2.2
 network 192.168.20.0 0.0.0.255 area 0
 network 10.0.0.0 0.0.0.3 area 0
 passive-interface GigabitEthernet0/1
```
**Interface warning:** Assumes LAN is `GigabitEthernet0/1`, P2P is another interface. If your interface map differs, update passive-interface to the correct LAN-facing port before deploying।

## Verification
```text
show ip ospf neighbor
show ip protocols
show ip route ospf
show ip ospf interface brief
```
Remote LAN should be learned as OSPF route where supported. Routers do not form adjacency on passive LAN interface; they must form on P2P interface।

## Troubleshooting exercise
In simulator, put one P2P side in Area 1, inspect no adjacency and restore Area 0. Verify routing after convergence and explain why mismatch matters।

**Deliverable:** OSPF neighbor state, route codes, comparison with Lab 05 static routes, note convergence time depends on design।
