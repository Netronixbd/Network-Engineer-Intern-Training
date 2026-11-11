# Subnetting, CIDR, VLSM | হাতে calculation

## 1. Why subnetting?
একটি বড় network-কে ছোট broadcast domain/address allocation zone-এ ভাগ করে manage ও secure করা। Subnetting ভুল হলে overlapping routes, wrong ARP assumptions এবং outage হতে পারে।

## 2. Formula
- IPv4 host bits = `32 − prefix`।
- Total addresses = `2^(host bits)`।
- Traditional usable host count = `2^(host bits) − 2` **for /0–/30 subnet arithmetic**, যদিও /0-এর practical use ভিন্ন।
- **/31 point-to-point exception:** RFC 3021 অনুযায়ী দুই endpoint address usable (supported L3 point-to-point links)।
- **/32:** একটি host route / single address; conventional subnet-এর broadcast নেই।

| Prefix | Mask | Total | Conventional usable |
|---|---|---:|---:|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |
| /31 | 255.255.255.254 | 2 | 2 for point-to-point |
| /32 | 255.255.255.255 | 1 | 1 address |

## 3. Block size shortcut
Interesting octet = যে octet-এ netmask 255 বা 0 নয়। Block size = `256 − mask-octet`। উদাহরণ `/26` mask last octet 192 → block 64 → starts `0,64,128,192`।

### Example A: `192.168.10.130/26`
- Mask `255.255.255.192`, block 64। `130` falls within `128–191`।
- Network `192.168.10.128`
- First usable `192.168.10.129`
- Last usable `192.168.10.190`
- Broadcast `192.168.10.191`
- Total 64, usable 62।

### Example B: `10.10.5.73/28`
- /28 mask `255.255.255.240`, block 16। `73` falls `64–79`।
- Network `10.10.5.64`, first `10.10.5.65`, last `10.10.5.78`, broadcast `10.10.5.79`।

### Example C: `172.16.7.9/30`
- /30 block 4: ... 0–3, 4–7, 8–11।
- Network `172.16.7.8`, usable `.9/.10`, broadcast `.11`।

## 4. VLSM: different-sized segments allocate করা
Requirement: Staff 50 users, Guest 25, Management 10, two router P2P links 2 hosts each। Base `192.168.50.0/24`। Largest first:

| Requirement | Allocation | Usable hosts | Gateway/Use |
|---|---|---:|---|
| Staff 50 | `192.168.50.0/26` | 62 | .1 |
| Guest 25 | `192.168.50.64/27` | 30 | .65 |
| Mgmt 10 | `192.168.50.96/28` | 14 | .97 |
| P2P-1 | `192.168.50.112/30` | 2 | .113/.114 |
| P2P-2 | `192.168.50.116/30` | 2 | .117/.118 |

Allocated blocks overlap করছে কি? না। Remaining space future extension-এর জন্য রাখো। Real deployment-এ role-based summarization, DHCP ranges, reserved IP ও routing design বিবেচনা করতে হবে।

## 5. Binary shortcut
`/26` mask শেষ octet = `11000000` binary = 192। `130` binary `10000010`, bitwise AND gives `10000000` = 128। Subnetting calculator check করা যাবে, কিন্তু exam-এ হাতে calculate।

## 6. Exercises (ক্যালকুলেটর ছাড়া)
1. `192.168.4.77/27`: network/broadcast/usable?
2. `10.20.30.241/28`: first/last host?
3. `172.20.2.6/30`: usable endpoints?
4. 120 hosts-এর জন্য smallest conventional prefix?
5. 30 hosts-এর জন্য /27 কি যথেষ্ট?
6. `/31`-এ কেন 2টি usable endpoint হতে পারে?

**Answer key:** 1. `.64`, `.95`, `.65–.94`; 2. network `.240`, first `.241`, last `.254`, broadcast `.255`; 3. network `.4`, hosts `.5/.6`, broadcast `.7`; 4. `/25`; 5. Yes, 30; 6. RFC 3021 P2P special handling।

নিজে check করতে [subnet_calculator.py](../scripts/subnet_calculator.py) run করো।
