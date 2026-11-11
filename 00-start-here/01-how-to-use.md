# শুরু করার আগে | How to Use This Repository

> **Target audience:** 0–6 মাসের intern, fresh graduate, new NOC/ISP support engineer। ভাষা: বাংলা explanation + standard English networking terms।

## Learning outcome
এই repository শেষ করে একজন learner যেন (১) ছোট LAN topology আঁকতে পারে, (২) IP/subnet নিজে calculate করতে পারে, (৩) DHCP ও static IP setup করতে পারে, (৪) VLAN, trunk, static route ও basic NAT বুঝে lab-এ configure করতে পারে, (৫) ping/traceroute/DNS test দিয়ে fault isolate করতে পারে, (৬) incident ticket evidence-সহ লিখতে পারে। **Production network-এ independent change অনুমোদিত নয়**; lab competency মানেই production authorization নয়।

## শেখার নিয়ম: Read → Draw → Configure → Verify → Explain

1. **Read:** প্রতিটি chapter-এর key term নিজের ভাষায় ব্যাখ্যা করো।
2. **Draw:** topology দেখে না এঁকে নিজে diagram তৈরি করো; subnet/gateway লিখবে।
3. **Configure:** Packet Tracer, EVE-NG, GNS3, CHR বা isolated lab device ব্যবহার করো।
4. **Verify:** `show`, `print`, `display`, `ping`, `traceroute`, `nslookup` ইত্যাদি দিয়ে result capture করো।
5. **Explain:** কী কাজ করেছ, কেন কাজ করেছে, কীভাবে rollback করবে, mentor-কে বলো।

## Suggested prerequisites
- Basic PC usage, keyboard, terminal/command prompt, file explorer
- Binary number-এর basic, সাধারণ যোগ-বিয়োগ
- Lab tool: Cisco Packet Tracer **or** GNS3/EVE-NG; Windows/Linux VM (optional)
- GitHub account এবং Git-এর basic ধারণা

## Lab rules (অত্যন্ত জরুরি)
- **Production router/switch/OLT-তে commands paste করা যাবে না।** Mentor approval এবং change window ছাড়া config নয়।
- নমুনার সব IP **lab/example**; `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` documentation-only; real public Internet-এ route করা যাবে না। Internal lab-এর জন্য `192.168.x.x` private address ব্যবহার করা হয়েছে।
- CLI syntax model/software অনুযায়ী বদলাতে পারে। Help (`?`), vendor manual, `show version`/`/system resource print` দেখে মিলিয়ে নেবে।
- Password/PPPoE secret/SNMP community/API token/backup কখনো public GitHub repo-তে commit করবে না।
- Live routing বা firewall change-এর আগে backup, impact assessment, management access এবং rollback plan বাধ্যতামূলক।
- Configuration example-এ interface number তোমার device-এর সঙ্গে মিলিয়ে না নিলে link drop হতে পারে।

## Suggested documentation style
প্রতিটি lab submission-এ লিখো: Objective, Topology, IP Plan, Configuration, Verification, Result, Troubleshooting, Rollback/Learning.

## Self-check
- `ping gateway` fail হলে কেন DNS test করার আগে L1/L2 check করবে?
- `192.168.10.130/26` কোন network-এ পড়ে?
- Access port বনাম trunk port কী?
- Static IP assignment আর static routing কি এক জিনিস?
- DHCP address পেলেই Internet guaranteed? কেন নয়?
