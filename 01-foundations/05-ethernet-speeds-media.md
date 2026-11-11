# Ethernet 1G/10G/25G/40G/100G, LAN Cable ও SFP/QSFP

**Core idea:** `link speed`, `throughput`, `traffic utilization`, `duplex`, `fiber optics`, `connector`, `autonegotiation` আলাদা জিনিস।

## 1. Speed বুঝি
- **1G** = nominal 1,000,000,000 bits/sec (1 Gbps); **10G** = 10 Gbps; **100G** = 100 Gbps। Decimal SI speed: 1 Gbps ≈ 125 MB/s theoretical before protocol overhead।
- **Link speed** interface negotiated speed; **payload throughput** frame/packet overhead, congestion, CPU ও protocol-এর কারণে কম। 10G port-এ 300 Mbps graph মানে ওই মুহূর্তে usage 3% approximately; link 300 Mbps নয়।
- **Full duplex** simultaneous TX/RX; oversubscription, queue, CRC, FCS, discards আলাদা করে দেখবে।
- 1G ↔ 10G connecting সরাসরি সম্ভব কিনা optics/port capability, downshift support এবং hardware অনুযায়ী। `SFP` slot-এ `SFP+` 10G module সবসময় কাজ করে না।

| Standard/family | Typical medium | Key consideration |
|---|---|---|
| 1000BASE-T | copper twisted-pair, RJ45 | 1G, 100 m channel design |
| 10GBASE-T | Cat6A recommended | 10G, 100 m; Cat6 often shorter depending installation |
| 1000BASE-SX | multimode fiber | optics+fiber-specific distance |
| 1000BASE-LX | single-mode/qualified fiber | 1310 nm class |
| 10GBASE-SR | multimode | short-reach, length fiber grade dependent |
| 10GBASE-LR | single-mode | commonly 10 km class; verify vendor |
| 100GBASE-SR4 | multimode parallel lanes | MPO/MTP fiber polarity matters |
| 100GBASE-LR4 | single-mode WDM lanes | commonly 10 km class; verify vendor |

These are **families/examples**, not universal interoperability promises; consult datasheet for optical budget, wavelength, lane count, FEC, breakout, and platform compatibility।

## 2. Copper: Cat5e, Cat6, Cat6A, Cat7/8
| Cable | Typical teaching expectation | Notes |
|---|---|---|
| Cat5e | 1GbE up to 100m | certified cabling; 2.5/5G varies |
| Cat6 | 1GbE up to 100m, 10GbE limited length | 10G reach depends alien crosstalk/environment; often 55m scenario |
| Cat6A | 10GbE up to 100m | recommended 10G horizontal cable |
| Cat8 | high-speed short data center runs | not necessary for ordinary office network |

**Straight-through vs crossover:** Modern auto-MDI/MDIX typically makes special crossover unnecessary। For T568B both ends, pin order 1–8: `white-orange, orange, white-green, blue, white-blue, green, white-brown, brown`। T568A swaps orange/green pairs. Pair twist maintain near termination; tester দিয়ে wiremap, split pairs, length ও return-loss test ideally করবে।

```mermaid
flowchart LR
  A[PC NIC 1G RJ45] -->|Cat6 patch cable| B[Access Switch 1G]
  B -->|10G SFP+ SR/LR as matched| C[Aggregation Switch 10G]
  C -->|100G QSFP28 optics matched| D[Core Router 100G]
```

## 3. Fiber
- **Single-mode (SMF):** long distance; commonly OS2, often LC UPC connectors; wavelength 1310/1550 nm etc depending optics।
- **Multimode (MMF):** usually shorter data center links; OM3/OM4/OM5 choices। SMF optic ও MMF fiber mismatch করা উচিত নয়।
- **Simplex / Duplex:** BiDi single fiber different wavelengths TX/RX; standard duplex optic usually two strands; same transceiver model/paired wavelengths verify।
- **SFP/SFP+ / SFP28 / QSFP+ / QSFP28:** form factors, respectively commonly 1G/10G/25G/40G/100G, **but capability always transceiver + switch + licensing** dependent।

## 4. 5-minute field checklist
1. Port `up/up`? Speed/duplex auto negotiate correct?
2. Correct cable category/length? RJ45 termination & tester?
3. SFP vendor support, matching wavelength/fiber type, optical levels, FEC?
4. CRC/FCS/error/discard counters increment হচ্ছে?
5. Traffic direction? 1G link at 95%+ peak sustained congestion?
6. Change before: both ends config, backups, LACP status check।

## Viva
- **Q:** 10G মানে কি always 10Gbps application speed? **A:** No, physical line rate vs application throughput different।
- **Q:** RJ45 10G 100m recommended cable? **A:** Cat6A (suitable certified installation)।
- **Q:** 10GBASE-SR mostly which fiber? **A:** Multimode।
- **Q:** RX dBm low হলে first check? **A:** optics budget, patch cord/connector, fiber loss, TX peer, module compatibility।
- **Q:** 100G QSFP28 always 100G with any optic? **A:** Not necessarily; vendor support/FEC/lane mapping matters।

**References:** [IEEE Ethernet 802.3](https://www.ieee802.org/3/) · [Fluke Networks Copper Cabling](https://www.flukenetworks.com/blog/cabling-chronicles) · [Fiber glossary](../07-isp-noc/06-fiber-dbm-link-budget.md).
