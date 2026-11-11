# Lab 09: DNS vs IP Connectivity

**Duration:** 45 minutes · **Tool:** 2 VMs or lab DNS server/router simulator

## Objective
“Internet নেই” complaint-এ DNS vs L3 vs application issue isolate করা।

## Procedure
1. Host IP/mask/GW correct করো, gateway and routed lab server IP ping করো।
2. Local DNS server-এ lab zone `training.example`/record `app.training.example → 192.168.10.200` configure (simulator ability অনুযায়ী)।
3. Run `nslookup app.training.example <LAB-DNS-IP>` (Windows) or `dig @<LAB-DNS-IP> app.training.example` (Linux)।
4. Test HTTP service on lab host (if running), e.g., `curl -I http://192.168.10.200` and by hostname।
5. Change client DNS server to intentionally invalid **isolated** address `192.168.10.254`; record name fail but direct IP may work. Restore DNS।

## Evidence
| Test | DNS valid | DNS intentionally wrong |
|---|---|---|
| Gateway reachable | PASS | PASS |
| Remote service IP | PASS (if service up) | PASS |
| Name resolution | PASS | FAIL/time out |
| Web by hostname | PASS | May fail |

**Important:** `training.example` reserved example domain patterns appropriate for lab; set local DNS override or server zone. No actual public service expected।

**Deliverable:** Commands, test results, short customer-facing explanation without blaming upstream prematurely।
