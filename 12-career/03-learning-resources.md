# Sources & Further Learning | Official & Standards References

> Book material is written in original explanatory wording; vendor commands are educational examples, not a replacement for exact device release documentation. Curated reference links for November 2026; web pages and syntax can change later, so always check the current vendor release guide।

## Standards
- [RFC 1918, Private IPv4](https://www.rfc-editor.org/info/rfc1918/)
- [RFC 5737, Documentation IPv4 ranges](https://www.rfc-editor.org/info/rfc5737/)
- [RFC 3849, Documentation IPv6 prefix](https://www.rfc-editor.org/info/rfc3849/)
- [RFC 3021, /31 P2P IPv4](https://www.rfc-editor.org/info/rfc3021/)
- [RFC 4632, Classless Inter-domain Routing](https://www.rfc-editor.org/info/rfc4632/)
- [RFC 2131, DHCP](https://www.rfc-editor.org/info/rfc2131/)
- [RFC 2328, OSPFv2](https://www.rfc-editor.org/info/rfc2328/)
- [RFC 4271, BGP-4](https://www.rfc-editor.org/info/rfc4271/)
- [RFC 8200, IPv6 Specification](https://www.rfc-editor.org/info/rfc8200/)

## Vendor documentation
- [MikroTik RouterOS First Time Configuration](https://manual.mikrotik.com/docs/getting-started/first-time-configuration/)
- [MikroTik DHCP Server](https://manual.mikrotik.com/docs/network-management/dhcp/server/)
- [MikroTik DHCP Client](https://manual.mikrotik.com/docs/network-management/dhcp/client/)
- [Cisco IOS XE VLAN trunking](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/vlan/vlan-configuration-guide/configure-vlan-trunks.html)
- [Cisco IOS XE static routing](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-routing/b-ip-routing/m_iri-ip-prot-indep-0.html)
- [Juniper Junos static routes](https://www.juniper.net/documentation/us/en/software/junos/static-routing/topics/topic-map/config_static-routes.html)
- [Huawei static route check](https://info.support.huawei.com/network/ptmngsys/Web/tsrev_security/en/content/security/29_edesk_net_server_access_intarnet_server_failed_V5R1/edesk_net_server_access_intarnet_server_failed_edesk005.html)

## Lab tools and manuals
- Cisco Packet Tracer via Cisco Networking Academy official offerings (account/license policies apply)
- EVE-NG official website & installation guide: https://www.eve-ng.net/
- GNS3 official documentation: https://docs.gns3.com/
- Wireshark official user guide: https://www.wireshark.org/docs/wsug_html_chunked/
- Ubuntu Netplan docs: https://netplan.readthedocs.io/

## Recommended study path
1. **Foundations:** OSI/TCP-IP, Ethernet, IP, subnetting.
2. **CCNA-level concepts:** VLAN/STP, routing/OSPF, DHCP/NAT, security.
3. **Vendor CLI:** Cisco + MikroTik then Juniper/Huawei differences.
4. **ISP field:** GPON/PPPoE, optical budget, LACP, BGP policy, NOC tickets.
5. **Advanced:** IPv6 design, MPLS/EVPN/VxLAN, RPKI, observability, automation (after fundamentals).

## How to confirm examples
Search exact software release, platform family, feature availability, existing config and interface map. Review vendor manuals rather than guessing undocumented commands।

## Extended references used for the deep-dive chapters (2026-11-11)
- [RFC 9293 TCP](https://www.rfc-editor.org/info/rfc9293/), [RFC 768 UDP](https://www.rfc-editor.org/info/rfc768/), [RFC 2516 PPPoE](https://www.rfc-editor.org/info/rfc2516/), [RFC 4638 PPPoE MTU](https://www.rfc-editor.org/info/rfc4638/)
- [RFC 1034 and RFC 1035 DNS](https://www.rfc-editor.org/info/rfc1034/), [RFC 2131 DHCP](https://www.rfc-editor.org/info/rfc2131/), [RFC 5905 NTP](https://www.rfc-editor.org/info/rfc5905/)
- [RFC 6598 CGNAT Shared Space](https://www.rfc-editor.org/info/rfc6598/), [RFC 6890 Special-Purpose Addresses](https://www.rfc-editor.org/info/rfc6890/)
- [RouterOS PPPoE v7](https://manual.mikrotik.com/docs/virtual-private-networks/pppoe/), [RouterOS Bridge VLAN Filtering](https://manual.mikrotik.com/docs/bridging-and-switching/), [RouterOS first time setup](https://manual.mikrotik.com/docs/getting-started/first-time-configuration/)
- [IEEE 802.1Q VLAN](https://1.ieee802.org/802-1q/), [IEEE 802.1AX Link Aggregation](https://1.ieee802.org/802-1ax/), [IEEE 802.3 Ethernet](https://www.ieee802.org/3/)
- [ITU-T G.984 GPON](https://www.itu.int/rec/T-REC-G.984/), [ITU-T G.9807 XGS-PON](https://www.itu.int/rec/T-REC-G.9807/)

**Authorship** is credited once in the repository README footer. Vendor syntax examples are tutorials for lab/simulators, not vendor-certified configurations on each physical platform.
