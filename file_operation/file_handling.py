"""
Problem: Extract Emails, MAC Addresses, and IP Addresses from a File

You are given a text file that may contain random text along with
email addresses, MAC addresses, and IPv4 addresses.

Write a program to read the file and extract:

1. All valid email addresses
2. All valid MAC addresses
3. All valid IPv4 addresses

You must implement TWO approaches:

1. Line-by-line reading
   - Read the file one line at a time
   - Use regular expressions to extract matches
   - Memory efficient for large files

2. Full file reading
   - Read entire file content at once
   - Use regular expressions to extract matches
   - Faster for small/medium files but uses more memory

Return:
    Tuple (emails, mac_addresses, ip_addresses)

Example:

Input file content:
    Contact: test@example.com
    MAC: AA:BB:CC:DD:EE:FF
    IP: 192.168.1.1

Output:
    Emails: ['test@example.com']
    MAC: ['AA:BB:CC:DD:EE:FF']
    IP: ['192.168.1.1']

Constraints:
- File size may be large
- Multiple matches per line possible
- Patterns must be validated using regex

Follow-up Questions:

1. Which approach is more memory efficient and why?
2. How would you validate IPv4 range (0–255)?
3. How would you handle very large files (GB size)?
4. How would you remove duplicate matches?
5. How to extend for IPv6 detection?
6. How to stream file processing in real-time?
7. What is time complexity of regex extraction?

Goal:
Practice file handling, regex extraction, and memory vs performance trade-offs.
"""

import re

def file_handling_by_line():
    emails = []
    mac_addresses = []
    ip_addresses = []
    with open("C:/Users/adi18/Downloads/file.txt", "r") as f:
        for line in f:
            emails.extend(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", line))
            mac_addresses.extend(re.findall(r"(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}", line))
            ip_addresses.extend(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line))
    return emails, mac_addresses, ip_addresses

def file_handling():
    with open("C:/Users/adi18/Downloads/file.txt", "r") as f:
        content = f.read()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
        mac_addresses = re.findall(r"(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}", content)
        ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content)

    return emails, mac_addresses, ip_addresses

print(file_handling_by_line())
print(file_handling())