
def compare_large_files(file1, file2, chunk_size=8192):

    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        chunk1 = f1.read(chunk_size)
        chunk2 = f2.read(chunk_size)
        if chunk1 != chunk2:
            return False
        if not chunk1 and not chunk2:
            return True
        

