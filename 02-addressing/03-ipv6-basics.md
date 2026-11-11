# IPv6 Basics | 128-bit Addressing

## IPv6 কেন?
IPv4-এর ~32-bit global address space সীমিত। IPv6-এর 128-bit addressing, SLAAC, Neighbor Discovery, improved aggregation সহ modern network deployment সম্ভব। IPv6 মানেই automatically faster/safer নয়; routing, firewall, DNS, PMTUD ঠিক লাগবে।

## Common types
- **Global unicast:** Internet-routeable prefix allocation থেকে (সাধারণত `2000::/3` context); routing/security matter।
- **Link-local:** `fe80::/10`, local link scoped, neighbor discovery/RA-তে গুরুত্বপূর্ণ; router interface ID/zone syntax লাগতে পারে।
- **Unique Local Address (ULA):** `fc00::/7`, সাধারণত locally assigned `fdxx::/8`-style, globally routed না।
- **Loopback:** `::1/128`।
- **Unspecified:** `::/128`।
- **Multicast:** `ff00::/8`; IPv6-এ traditional broadcast নেই।
- **Documentation:** `2001:db8::/32` example-only; public global assignment নয়।

## Syntax rules
- Leading zeros omit করা যায়: `2001:0db8:0000:0000:0000:0000:0000:0001` → `2001:db8::1`।
- `::` এক address-এ **একবার** ব্যবহার করে consecutive zero groups compress করা যায়।
- Typical LAN prefix `/64` SLAAC-এ very common; prefix plan site requirements অনুযায়ী।

## Address assignment
- **SLAAC:** Router Advertisement (RA)-এর information ব্যবহার করে client address derive করে।
- **DHCPv6:** Stateful/stateless configuration দিতে পারে; platform support/RA interaction আলাদা।
- **Neighbor Discovery:** ICMPv6 (NS/NA/RS/RA), IPv4 ARP নয়।

## Example lab
Router interface `2001:db8:10:1::1/64`, host `2001:db8:10:1::10/64`। Same LAN ping, gateway route ও firewall check। Documentation prefix only; external Internet-এ reachability expect কোরো না।

## Practical diagnostics
- Windows: `ipconfig /all`, `ping -6 <IPv6>`, `tracert -6 <IPv6>`
- Linux: `ip -6 addr`, `ip -6 route`, `ping -6 <IPv6>`, `ip -6 neigh`
- Device: ND/RA, route, ACL/firewall, MTU/ICMPv6 filtering examine করো। ICMPv6 indiscriminately block করলে path MTU/ND সমস্যা হতে পারে।

**Questions:** DHCPv4 DORA vs IPv6 SLAAC এক? /64 কেন common? ULA কি Internet-এ routed? Dual-stack কী?

Reference: [RFC 3849](https://www.rfc-editor.org/info/rfc3849/)
