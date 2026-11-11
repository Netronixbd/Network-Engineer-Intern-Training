# Lab 14: Home Router WAN DHCP vs Static vs PPPoE

**Time:** 75m · **Prerequisite:** [WAN/LAN home concept](../07-isp-noc/04-home-router-wan-lan-setup.md).

## Topology
```mermaid
flowchart LR
 U[Upstream lab router\none of DHCP/Static/PPPoE] -->|WAN| R[Home Router\nWAN one method\nLAN 192.168.50.1/24]
 R -->|LAN DHCP| PC[Client 192.168.50.x]
```

## Tasks
1. Make WAN inventory: DHCP or Static or PPPoE? Identify who supplies creds/IP/VLAN. Only one WAN at a time.
2. For **DHCP WAN**, enable DHCP client; confirm `bound`, lease and dynamic default route.
3. Change test upstream to static: remove/disable DHCP client, set `192.0.2.2/30`, gateway `192.0.2.1`; verify ARP and ping.
4. For **PPPoE**, use separate isolated PPPoE server of Lab13; disable other WAN modes, configure client username/password, verify session.
5. Common LAN: use subnet `192.168.50.0/24` and DHCP range `.100-.200`; NAT outbound to active WAN type only.
6. Explain why browser may not work with reserved documentation prefix or a lab upstream without real Internet.

Use complete [MikroTik WAN mode config](../09-vendor-configs/10-mikrotik-home-router-wan-modes.md) and select relevant section. No reset or factory change to office router।

## Troubleshooting inject
- Wrong gateway `.254`: check route and neighbor ping.
- Wrong DNS: compare IP-ping vs hostname resolution.
- NAT out-interface intentionally wrong: `nat print stats` with supervisor, identify return/translation issue then restore.

## Pass criteria
Correct interface IP/mask, one valid default route, active WAN mode, LAN DHCP lease, accurate NAT egress, written troubleshooting report. **20 marks:** mode 5, LAN 5, tests 5, fault handling 5।
