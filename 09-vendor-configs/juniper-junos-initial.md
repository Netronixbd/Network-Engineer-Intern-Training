# Juniper Junos: Initial Router Commands (Lab)

> Syntax illustrates Junos CLI hierarchy. `ge-0/0/0`/`ge-0/0/1` placeholder. Junos supports candidate configuration + commit; use `commit confirmed` for remote risky changes where supported।

## 1. Operational mode observation
```text
show version
show interfaces terse
show route
show arp
show configuration | display set
show log messages | last 20
```

## 2. Enter configure mode, hostname and interfaces
```junos
configure
set system host-name LAB-JUNOS-R1
set interfaces ge-0/0/0 description LAB-LAN
set interfaces ge-0/0/0 unit 0 family inet address 192.168.10.1/24
set interfaces ge-0/0/1 description LAB-P2P
set interfaces ge-0/0/1 unit 0 family inet address 10.0.0.1/30
set routing-options static route 192.168.20.0/24 next-hop 10.0.0.2
show | compare
commit check
commit confirmed 5
```
After connectivity checks, `commit` confirms the pending change within the confirmation window; otherwise rollback occurs after timeout according to platform behavior। In lab console, ordinary `commit` also possible, but disciplined validation recommended।

## 3. Verify from operational mode
```text
run show interfaces terse
run show route 192.168.20.0/24
run ping 10.0.0.2 count 4
run show route
```
`run` used from configuration mode; in operational mode commands without `run`।

## 4. Default route alternative
```junos
set routing-options static route 0.0.0.0/0 next-hop 10.0.0.2
commit check
```
Don't add a default route without understanding existing routing instances/forwarding design।

## 5. Rollback fundamentals
```text
show | compare
rollback 1
show | compare
commit check
```
`rollback 1` loads previous committed config into candidate, not active until commit। Use correct rollback generation, verify compare, follow change approval।

## 6. Beginners need to know
- `set`: Configure candidate। `delete`: Remove candidate config।
- `show | compare`: Candidate vs running committed difference।
- `commit check`: Syntax/semantic validation without activate।
- `commit`: Activate config; `commit confirmed`: pending automatic rollback unless confirmed।
- `show route` is operational, `show configuration` displays config।

Reference: [Juniper Configure Static Routes](https://www.juniper.net/documentation/us/en/software/junos/static-routing/topics/topic-map/config_static-routes.html)
