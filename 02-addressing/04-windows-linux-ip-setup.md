# Windows ও Linux-এ Static IP, DHCP এবং Network Testing

> এগুলো host-side instructions। Interface name, distro version এবং network manager অনুযায়ী steps বদলাতে পারে। Remote SSH-এ IP change করলে session disconnect হতে পারে। VM/lab console ব্যবহার করো।

## Windows 10/11 (GUI)
1. Settings → Network & Internet → Advanced network settings → More network adapter options (UI version অনুযায়ী location বদলায়)।
2. Adapter Properties → `Internet Protocol Version 4 (TCP/IPv4)`।
3. **DHCP:** Obtain IP address automatically + DNS automatically।
4. **Static:** Use following IP: `192.168.10.50`, mask `255.255.255.0`, gateway `192.168.10.1`, DNS `192.168.10.1` (local DNS exists হলে) বা lab DNS।
5. `ipconfig /all` দিয়ে verify।

### Windows CMD/PowerShell diagnostics
```powershell
ipconfig /all
ipconfig /release
ipconfig /renew
ipconfig /flushdns
ping 192.168.10.1
tracert 192.168.20.10
nslookup example.com
arp -a
route print
Test-NetConnection example.com -Port 443
```
`release/renew` existing DHCP connectivity interrupt করতে পারে; production user workstation-এ approval নিয়ে করো।

## Ubuntu/Debian Linux: show info
```bash
ip -br addr
ip route
ip neigh
resolvectl status   # systemd-resolved থাকলে
ping -c 4 192.168.10.1
tracepath 192.168.20.10    # package installed থাকলে
getent hosts example.com
ss -tulpen
```

## Linux temporary static IP (lab only)
```bash
sudo ip address add 192.168.10.50/24 dev eth0
sudo ip link set eth0 up
sudo ip route replace default via 192.168.10.1 dev eth0
ip address show dev eth0
ip route
```
**Notes:** `eth0` placeholder; `ip -br link` দিয়ে actual NIC name দেখো। Temporary settings reboot/NetworkManager changes-এ হারাতে পারে। Existing conflicting IP/gateway থাকলে append করা নয়, clean config plan করো।

### Ubuntu Netplan sample (VM, Ubuntu server using systemd-networkd)
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp1s0:
      dhcp4: false
      addresses: [192.168.10.50/24]
      routes:
        - to: default
          via: 192.168.10.1
      nameservers:
        addresses: [192.168.10.1]
```
Save as suitable `/etc/netplan/*.yaml`; `sudo netplan try` ও local console fallback ব্যবহার করো। **Existing renderer, files ও indentation check না করে overwrite নয়**। DHCP করতে `dhcp4: true` এবং conflicting static entries remove করো।

## Distinguishing network from DNS fault
- `ping 192.168.10.1` fail → local IP/VLAN/cable/gateway diagnosis।
- Gateway works, remote lab router IP fails → routing/ACL/next hop diagnosis।
- Remote IP reachable, `nslookup example.com` fails → DNS resolver/server/path diagnosis।
- DNS resolves, TCP/443 fails → firewall/proxy/server/route/service diagnosis।
- ICMP filtering থাকতে পারে; ping fail একাই Internet down প্রমাণ নয়।
