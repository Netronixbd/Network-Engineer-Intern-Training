# MikroTik RouterOS v7: PPPoE Server + Client + DHCP LAN + NAT

**Only isolated lab hardware/CHR with a dedicated cable.** Neither side should already be in a conflicting bridge or DHCP WAN setup. Production PPPoE server rollout needs AAA/RADIUS, rate/queue policy, lawful logging/policy, authentication security, accounting, capacity planning and firewall hardening; these commands alone are not production ready।

## Topology
```mermaid
flowchart LR
 PC[PC\nLAN DHCP 192.168.88.x] -->|ether2| C[MT-CLIENT\nPPPoE Client on ether1\nLAN 192.168.88.1/24]
 C <-->|Ethernet ether1↔ether3\nPPPoE discovery and session| S[MT-SERVER\nPPPoE Server on ether3\nPPP local 10.100.0.1\nClient gets 10.100.0.2+]
 S -.->|Optional separate WAN/uplink, not set up here| ISP[Lab upstream]
```

## 1. Server: user pool, PPP profile, secret, PPPoE AC
Run on isolated `MT-SERVER`, keep `ether3` **without ordinary static/DHCP IP** for PPPoE discovery. Password is visibly **lab-only** and should be replaced and never committed if real।
```routeros
/system identity set name=LAB-PPPOE-SERVER
/ip pool add name=pppoe-pool ranges=10.100.0.2-10.100.0.50
/ppp profile add name=pppoe-lab local-address=10.100.0.1 remote-address=pppoe-pool
/ppp secret add name=intern01 password="CHANGE-ME-ONLY-LAB" profile=pppoe-lab service=pppoe
/interface pppoe-server server add interface=ether3 service-name=TRAINING-ISP default-profile=pppoe-lab disabled=no
/interface pppoe-server server print detail
/ppp active print detail
```
Interface names, device defaults and support depend on RouterOS release. On server interface don't run concurrent DHCP clients or ordinary IP config for this PPPoE test।

## 2. Client: PPPoE dial
Run on isolated `MT-CLIENT`, `ether1` connects server `ether3` directly or through correct L2 VLAN transport:
```routeros
/system identity set name=LAB-PPPOE-CLIENT
/interface pppoe-client add name=pppoe-out1 interface=ether1 user=intern01 password="CHANGE-ME-ONLY-LAB" service-name=TRAINING-ISP add-default-route=yes use-peer-dns=no disabled=no
/interface pppoe-client print detail
/ip address print
/ip route print detail
```
Expected client session running; PPP address from profile pool, route points to PPPoE logical interface. `add-default-route=yes` only if this is the desired primary WAN and no preexisting competing default route।

## 3. Client LAN DHCP + NAT to PPPoE
Here `ether2` is dedicated LAN, **not** a factory bridge member:
```routeros
/ip address add address=192.168.88.1/24 interface=ether2 comment="LAB-CLIENT-LAN"
/ip pool add name=lan88 ranges=192.168.88.100-192.168.88.199
/ip dhcp-server network add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1
/ip dhcp-server add name=dhcp88 interface=ether2 address-pool=lan88 disabled=no
/ip dns set allow-remote-requests=yes
/ip firewall nat add chain=srcnat src-address=192.168.88.0/24 out-interface=pppoe-out1 action=masquerade comment="LAB-PPPOE-NAT"
```
**Important:** LAN DNS server forwarding must have an upstream resolver and firewall that restricts DNS access to trusted LAN. The isolated server here does **not** connect to Internet, so browser Internet test won't succeed just from these commands। For client access to a real service behind server, configure server's other-side routes/NAT/firewall accordingly।

## 4. Verify: Is PPPoE really working?
Client:
```routeros
/interface pppoe-client monitor pppoe-out1 once
/ip address print
/ip route print detail
/ping 10.100.0.1 count=5
/ip dhcp-server lease print
/ip firewall nat print stats
/log print where message~"pppoe"
```
Server:
```routeros
/ppp active print detail
/interface pppoe-server server print detail
/log print where message~"ppp"
```
Expected: `running=yes` on client, `ppp active` session on server, LAN PC gets lease. `10.100.0.1` peer ping subject to firewall. No actual public Internet expected।

## 5. Debug checklist
- No PADO: check `ether1` ↔ `ether3` physical cable, link status, service-name, transport VLAN; packet capture if needed.
- Authentication rejected: credentials, profile, server log and secret service setting.
- Connected but no IPv4 address: profile pool/PPP IPCP, RADIUS conflict.
- Connected but Internet absent: in this lab there is **no upstream**; in a real design check BNG route, client NAT, DNS and firewall.
- Some websites hang: PPPoE MTU normally 1492 vs Ethernet 1500, PMTUD/MSS and actual access network support.

## 6. Security and rollback
- Don't expose PPPoE services on arbitrary WAN ports or untrusted VLANs.
- Use strong unique credentials, AAA accounting, rate limits, logs, firmware update, monitored service capacity.
- Do not put live passwords into repository; example credential above is non-secret training placeholder.
- Review changes in Safe Mode and keep a management access route out-of-band.

## Q&A
- **Q:** PPPoE server and DHCP server identical? **A:** No; PPPoE auth/session vs LAN lease provisioning।
- **Q:** `out-interface=ether1` or `pppoe-out1` for client NAT? **A:** PPPoE logical interface `pppoe-out1` in this design।
- **Q:** PPPoE discovery requires IP on server interface? **A:** No, L2 discovery; MikroTik documentation warns against normal IP on server-facing interface।
- **Q:** PADO না আসলে username change করলেই হবে? **A:** No, L2/VLAN/server availability first।
- **Q:** Is this a production configuration? **A:** No, isolated lab minimal example।

**References:** [RouterOS PPPoE official documentation](https://manual.mikrotik.com/docs/virtual-private-networks/pppoe/) · [RFC 2516](https://www.rfc-editor.org/info/rfc2516/) · [Theory](../05-services/05-pppoe-dialup-client-server.md).
