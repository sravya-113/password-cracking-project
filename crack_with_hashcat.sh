#!/bin/bash
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt --show
