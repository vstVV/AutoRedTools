import os

root_dir = input("Enter root directory path: ")

if not os.path.isdir(root_dir):
    print("Invalid directory path.")
else:
    for dirpath, _, filenames in os.walk(root_dir):
        if "requirements.txt" in filenames:
            os.system(f"pip install -r {os.path.join(dirpath, 'requirements.txt')}")
        elif "requirement.txt" in filenames:
            os.system(f"pip install -r {os.path.join(dirpath, 'requirement.txt')}")
