import os
from collections import defaultdict
import hashlib

def group_file_by_size(directory):
    #Group file by size
    size_map = defaultdict(list)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size_map[os.path.getsize(file_path)].append(file_path)

    #Group by Hash
    result = defaultdict(list)
    for size, file_paths in size_map.items():
        if len(file_paths) > 1:
            for path in file_paths:
                h = hashlib.md5(open(path, 'rb').read()).hexdigest()
                result[(size,h)].append(path)

    #File duplicate by Hash
    duplicates = []
    for size, h in result.items():
        if len(h) > 1:
            duplicates.append(hash)
    return duplicates
