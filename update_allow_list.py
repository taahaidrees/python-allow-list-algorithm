"""Simulated cybersecurity training: update an IP allow-list file."""

import_file = "allow_list.txt"

with open(import_file, "r", encoding="utf-8") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()

# Illustrative test values; replace with the authorized removal list.
remove_list = ["192.168.1.20", "192.168.1.40"]

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w", encoding="utf-8") as file:
    file.write(ip_addresses)
