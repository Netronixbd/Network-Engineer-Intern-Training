# STP, RSTP, LACP, PoE & Wi-Fi Basics

## STP/RSTP
L2 network-এ redundant links থাকলে Ethernet frame-এর TTL নেই; loop হলে broadcast storm/MAC flapping সৃষ্টি হয়। **Spanning Tree Protocol (STP)** logical loop-free topology তৈরি করতে কিছু port block/discard করে। RSTP faster convergence design করে।

- Root bridge নির্বাচন গুরুত্বপূর্ণ; priority সেট করে planned core root রাখো।
- Edge/PortFast শুধু host-facing port-এ, switch uplink-এ ভুলভাবে নয়।
- BPDU Guard edge-facing protection-এর অংশ হতে পারে; platform policies অনুসরণ করো।
- STP port blocking **link broken** বোঝায় না, designed behavior হতে পারে।

## LACP / Link Aggregation
Multiple compatible physical links aggregate করে logical port-channel/AE/bond বানানো যায়; redundancy এবং multiple-flow load distribution হয়। **একটি single flow সাধারণত সব link speed যোগ করে পায় না**, hashing policy-র কারণে।

Check both ends: speed/duplex, VLAN allowed list, MTU, LACP mode (`active/passive`), aggregation ID, member status, optics। LACP up না হলে physical link up হলেও bundle down থাকতে পারে।

## Wireless networking
- SSID হলো Wi-Fi network name; security WPA2-AES/WPA3 policy follow করো।
- 2.4 GHz coverage ভালো কিন্তু congestion বেশি; 5/6 GHz higher capacity environment-dependent।
- Channel overlap, co-channel contention, RSSI/SNR, AP placement, client count, backhaul capacity matter।
- Guest SSID সাধারণত separate VLAN + firewall policy, management network থেকে isolated।

## PoE and endpoint planning
PoE switch-এর **overall power budget** আছে; 24 ports থাকলেই সব port-এ full power একই সময়ে দিতে পারবে এমন নয়। AP/camera wattage estimate করো; UPS backup and cable quality check।

## Mini troubleshooting
1. Two 10G ports link up but LACP bundle down: start with both-end mode, LAG member state, speed/MTU/VLAN consistency।
2. Wi-Fi connected but IP missing: AP bridge SSID-to-VLAN, DHCP relay, uplink trunk check।
3. Camera rebooting: PoE budget, voltage/cable, device logs check।
