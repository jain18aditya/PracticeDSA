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