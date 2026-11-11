# Network Security Basics, Firewall, ACL & Safe Change

## 1. Basic principles
- **Least privilege:** User/device/service যতটা দরকার ততটা access।
- **Segmentation:** Guest/Staff/Management VLAN/VRF separation, L3 firewall policy। VLAN alone complete security boundary নয়।
- **Defense in depth:** Strong authentication, SSH, firewall, ACL, patching, monitoring, backups।
- **Secure management:** Avoid plain-text Telnet/HTTP, prefer SSH/HTTPS, management ACL, MFA where supported।
- **Secrets:** No credentials in README/config snapshots, code or screenshots; redaction before sharing।

## 2. ACL / Firewall logic
ACL often stateless ordered match, firewall stateful connection tracking possible; exact vendor behavior differs। `allow 192.168.10.0/24 to DNS server UDP/TCP 53`, `deny Guest to Management`, then required Internet services। Rule order and implicit deny important।

## 3. Common security issues
- **Rogue DHCP:** Unauthorized client gets wrong gateway/DNS; mitigation DHCP snooping (switch support), edge port policies।
- **ARP spoofing:** Attacker tries wrong IP-to-MAC mapping; mitigation DAI where supported, segmentation。
- **L2 loop:** Broadcast storm, CPU spike; STP/BPDU protection।
- **Open management plane:** WAN-exposed Winbox/SSH/SNMP insecure; management access restricted।
- **Unpatched software:** Vulnerabilities may persist; approved upgrade/test/backup।
- **Misconfigured BGP export:** Route leak; prefix filters, max-prefix, RPKI validation।

## 4. Change management checklist
1. Request/ticket ID; scope & impact; owner; approved maintenance window।
2. Capture current state + backup, out-of-band/console path and tested rollback।
3. Make minimal change, one logical unit at a time।
4. Verify expected result + unaffected traffic and metrics।
5. Document timestamp, commands, output, incident close/next action।

## 5. Safe example policy
Staff VLAN 10 may query DNS and access Internet; Guest VLAN 20 can access Internet but not management VLAN 99; NOC management jump host only can SSH network devices। Need explicit IPv4 **and IPv6** policy to avoid dual-stack bypass।

## 6. Never do on live network without authorization
- `reset`, `reboot`, `disable`, `clear counters`, `shutdown`, BGP session reset, disable firewalls, change WAN IP, remove VLAN/trunk, dynamic routing changes।
- Blindly run `curl | bash` from unreviewed sources or import public config scripts।
- Copy real `export show-sensitive`, secrets or subscriber data into public GitHub।

Security is part of troubleshooting: use read-only evidence first, then smallest safe change after approval।
