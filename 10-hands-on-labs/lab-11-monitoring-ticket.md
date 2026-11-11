# Lab 11: NOC Monitoring → Incident Ticket → Handover

**Duration:** 60–75 minutes · **Tool:** Any demo monitoring dashboard or supplied synthetic metrics

## Synthetic measurements
- Access uplink utilization: 960 Mbps on 1 Gbps port for 15 minutes
- Interface input drops: increasing by 5,000 over 15 minutes
- Ping RTT to downstream: baseline 2 ms, current avg 38 ms
- Loss: 4% of 100 ICMP probes (source and destination documented)
- Link stays UP, no CRC errors

## Tasks
1. Compute utilization: `960 / 1000 × 100 = 96%`।
2. Separate congestion hypothesis from physical error hypothesis. High utilization + drop counters supports congestion investigation; not absolute proof।
3. Find possible peak time and traffic classes (authorized flow statistics only)।
4. Write concise vendor/team ticket with graphs and time window।
5. Write handover with next update and change decision pending।

## Sample ticket
```text
Subject: High Utilization & Packet Loss | LAB-ACCESS-UPLINK
Time: 2026-11-11 14:00-14:15 BDT (sample)
Impact: Sample customer segment, scope being checked
Evidence: Avg utilization 960/1000 Mbps (96%); 4/100 ICMP probes lost;
          input drops increased 5,000; CRC unchanged
Current hypothesis: Egress congestion / queue dropping (not yet confirmed)
Action: Compare short-interval graphs, QoS/queue counters, traffic mix,
        capacity and affected subscriber tests
Owner: NOC Lead; next update after validated measurements
```

## Mentor grading (10)
- 2 for accurate calculation
- 3 for separating facts/hypotheses
- 2 for appropriate next tests
- 2 for concise report
- 1 for privacy/redaction
