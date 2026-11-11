# Lab 10: GPON & PPPoE Incident Triage (Paper/Synthetic Data)

**Duration:** 60 minutes · **Tool:** Spreadsheet or markdown ticket, fake monitoring graphs

## Scenario A
- Subscriber PPPoE active, IP assigned, last login 30 min ago
- ONU registered/online, optical Rx currently -25 dBm; prior baseline -19 dBm
- Customer says frequent intermittent drops; OLT reports 6 LOS flaps since 10:00
- OLT uplink packet errors 0, POP core stable

## Questions
1. What is **proven**? ONU online now and PPPoE active now; historical link flaps present।
2. What is **suspected**? Last-mile optical path degradation, but module-specific thresholds still required।
3. What do you check next? PON alarm history, optical values both ends, recent construction/splice, customer CPE power, similar ONUs on same splitter।
4. What not to do? Don't reboot OLT or claim '-25 dBm is universally bad'; don't share customer credentials।

## Scenario B
- ONU stable, Rx in vendor spec, no alarms
- PPPoE active, traffic counter bytes do not increase on client test
- Client assigned address and policy? **Unknown**

Next: verify session IP, RADIUS profile, BNG queue/drop policy, VLAN service mapping, default route, NAT/CGNAT, client CPE firewall and source-specific test. Avoid guessing a single cause।

## Submission template
```text
Incident ID:
Impact/scope:
Start time and timezone:
Evidence verified:
Hypothesis 1 / Hypothesis 2:
Tests requested:
Decision and escalation owner:
Possible customer update:
Root cause: confirmed / unconfirmed
```

**Pass:** Evidence and assumptions explicitly separated, correct escalation, no unjustified universal optical threshold।
