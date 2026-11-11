#!/usr/bin/env python3
"""Offline subnet calculator for intern training using Python stdlib only.

Examples:
    python3 scripts/subnet_calculator.py 192.168.10.130/26
    python3 scripts/subnet_calculator.py 10.0.0.0/31
"""
import argparse
import ipaddress


def details(cidr: str) -> dict[str, str | int]:
    interface = ipaddress.ip_interface(cidr)
    net = interface.network
    if net.version != 4:
        raise ValueError("This beginner helper supports IPv4 only")
    if net.prefixlen == 32:
        first = last = str(net.network_address)
        usable = 1
    elif net.prefixlen == 31:
        first = str(net.network_address)
        last = str(net.broadcast_address)
        usable = 2  # RFC 3021 point-to-point semantics
    else:
        first = str(net.network_address + 1)
        last = str(net.broadcast_address - 1)
        usable = max(0, net.num_addresses - 2)
    return {
        "IP": str(interface.ip),
        "Network": str(net),
        "Mask": str(net.netmask),
        "Wildcard": str(net.hostmask),
        "Broadcast": str(net.broadcast_address) if net.prefixlen < 31 else "Not applicable (/31-/32)",
        "First usable": first,
        "Last usable": last,
        "Total addresses": net.num_addresses,
        "Usable addresses": usable,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate an IPv4 subnet")
    parser.add_argument("cidr", help="host/prefix e.g. 192.168.10.130/26")
    args = parser.parse_args()
    try:
        data = details(args.cidr)
    except ValueError as exc:
        parser.error(str(exc))
    for key, value in data.items():
        print(f"{key:>18}: {value}")


if __name__ == "__main__":
    main()
