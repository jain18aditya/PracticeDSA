import os
import sys

def remove_mac_metadata_files(root_path):
    if not os.path.exists(root_path):
        print(f"Path does not exist: {root_path}")
        return

    removed_count = 0

    for dirpath, dirnames, filenames in os.walk(root_path):
        for file in filenames:
            if file.startswith("._"):
                full_path = os.path.join(dirpath, file)
                try:
                    os.remove(full_path)
                    print(f"Removed: {full_path}")
                    removed_count += 1
                except Exception as e:
                    print(f"Failed to remove {full_path}: {e}")

    print(f"\nDone. Removed {removed_count} file(s).")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_mac_metadata.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    remove_mac_metadata_files(folder_path)
