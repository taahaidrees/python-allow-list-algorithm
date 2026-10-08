# Python Algorithm for Updating an IP Allow List

**Simulated cybersecurity training project | Google Cybersecurity Professional Certificate**

## Overview
This project demonstrates how Python can maintain a file-based IP allow list for a restricted healthcare subnetwork. Addresses designated for removal are deleted from the list, and the updated list is written to disk.

## Skills demonstrated
Python file I/O (`with`, `open`, `read`, `write`), string/list conversion (`split`, `join`), `for` loops, conditional membership checks, and list mutation.

## Repository files
- `update_allow_list.py` — runnable Python algorithm using illustrative removal addresses
- `ALGORITHM_REPORT.md` — detailed portfolio explanation
- `allow_list_sample.txt` — illustrative starting file for safe testing

## Run locally
1. Copy `allow_list_sample.txt` to `allow_list.txt` in the same directory as the script.
2. Run `python update_allow_list.py`.
3. Inspect `allow_list.txt` and confirm only `192.168.1.10` and `192.168.1.30` remain.

**Important:** The script overwrites `allow_list.txt`. Use a disposable test copy, not a production access-control file. The sample IP addresses and removal list are illustrative, not supplied from the original Google lab. A changed file does not by itself establish enforcement by a network device.

## Training context
This is a simulated course scenario, not an account of production security work. No original Google lab execution or screenshots are claimed.
