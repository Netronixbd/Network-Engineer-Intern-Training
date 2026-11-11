# Lab 16: Optical dBm & GPON Link Budget Worksheet

**Time:** 45m · **No live fiber re-patching required.**

```mermaid
flowchart LR
 TX[OLT TX +3 dBm example] --> F[8 km fiber\n2.8 dB loss]
 F --> S[1:32 Splitter\n17 dB example]
 S --> J[Connectors + Splices\n1.8 dB example]
 J --> RX[ONU RX?]
```

## Tasks
1. Define dBm vs dB, RX vs TX, direction ONU→OLT and OLT→ONU.
2. Calculate illustrative path loss: 2.8+17+1.8 = **21.6 dB**.
3. Predicted RX for TX +3 dBm: **−18.6 dBm**. If planning 3 dB margin, optical budget requirement becomes 24.6 dB but do not subtract margin again to claim measured Rx.
4. Change splitter assumption to 1:16 **using vendor-rated insertion loss**, not simply halve the dB number. Recalculate based on chosen datasheet.
5. Consider actual recorded ONU RX day1 −18 dBm vs day2 −25 dBm: delta 7dB deterioration; provide checklist and compare real optical spec. Don't say either value always pass/fail.

## Evidence
Worksheet: TX, loss/distance, connectors/splices, splitter class, predicted RX, module min/max RX, reserve, measurements, possible fault. Include time, port/ONU id, fiber safety.

**Pass criteria 20:** formula (5), calculation (5), units (3), vendor spec caution (3), RCA notes (4).
