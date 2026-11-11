# Cabling, Fiber, Optics এবং Device Hardware

## Copper Ethernet
- **UTP/STP:** Unshielded/Shielded twisted pair; environment/grounding অনুযায়ী নির্বাচন।
- **Cat5e:** সাধারণত 1GBASE-T পর্যন্ত typical 100m channel; implementation constraints check করো।
- **Cat6:** 1G typical 100m; 10G short distances environment-dependent।
- **Cat6A:** 10GBASE-T up to 100m certified channel-এর জন্য intended।
- **RJ-45 (8P8C):** Twisted-pair Ethernet connector। T568A ও T568B wire order; **দুই পাশে একই standard** = straight-through, differing = crossover (Auto-MDI/MDIX devices-এ often not needed)।
- **PoE:** Ethernet cable-এ power + data; 802.3af/at/bt class/budget, switch/device compatibility verify করো।

## Optical fiber
- **Single-mode (SMF):** Long-distance links, typically 1310/1550 nm families; SFP specification অনুযায়ী।
- **Multi-mode (MMF):** Shorter distances, 850 nm common, specific optics/cable standard matter।
- **LC/SC:** Connector types; **UPC/APC polish** mix করা যাবে না; green APC/blue UPC সাধারণ color hint, visual inspection যথেষ্ট নয়।
- **SFP/SFP+/QSFP:** Pluggable transceiver form factors; port, wavelength, speed, reach, DOM, vendor compatibility check।
- **Tx/Rx optical power:** Usually dBm; Rx যদি module specification-এর min sensitivity-এর নিচে যায়, bit error/loss হতে পারে। Rx overload হলেও সমস্যা। **একটি universal acceptable dBm value নেই**, optics datasheet ও OLT/ONU design budget দেখো।
- **Optical budget:** Tx output − total path loss − margins ≥ required Rx sensitivity (unit in dBm/dB carefully)। Splitter, splice, connector, fiber attenuation total loss-এ যোগ হয়।

## Common causes of link faults
Dirty connectors, bent fiber, incorrect wavelength pair, TX/RX reversal, insufficient optical power, LOS, wrong speed/FEC, SFP mismatch, damaged patch cord, disabled interface, faulty port, duplex mismatch (legacy)।

## Physical troubleshoot checklist
1. `interface admin status`, `oper status`, speed, error counters check।
2. `link up` duration এবং flap timestamp নাও।
3. Optical Rx/Tx + module threshold compare করো।
4. Fiber port labeling, patch path, ODF/splitter mapping verify করো।
5. Approved procedure অনুযায়ী spare patch cord/module swap; live fiber-এ **কখনো সরাসরি তাকাবে না**।
6. Fix-এর পরে ping/loss, CRC, interface errors, graph, customer confirmation।

## Practical
- Cat6 termination-এর color map হাতে লিখো।
- 10G LR optic এবং 1G LX optic একই link-এর দুই পাশে mix করা যাবে কি? কেন?
- Optical loss budget: Tx +2 dBm, total loss 15 dB হলে expected Rx -13 dBm। Budget margin যোগ না করলে calculation incomplete।
