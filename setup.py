import os
import shutil
from pathlib import Path

ROOT = Path("permissions-lab")


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


# ----------------------------------------
# Remove old lab if it exists
# ----------------------------------------

if ROOT.exists():
    shutil.rmtree(ROOT)

# ----------------------------------------
# Create folders
# ----------------------------------------

for i in range(1, 6):
    (ROOT / f"level-{i}").mkdir(parents=True)

# ----------------------------------------
# File Definitions
# ----------------------------------------

files = [
    # ---------------- Level 1 ----------------
    ("level-1/file1.txt", "Permission required: 644\n", "644"),
    ("level-1/file2.txt", "Permission required: 600\n", "600"),
    ("level-1/file3.txt", "Permission required: 755\n", "755"),

    # ---------------- Level 2 ----------------
    ("level-2/file4.txt", "Permission required: 640\n", "640"),
    ("level-2/file5.txt", "Permission required: 700\n", "700"),
    ("level-2/file6.txt", "Permission required: 744\n", "744"),

    # ---------------- Level 3 ----------------
    (
        "level-3/file7.txt",
        """Permission required:

Owner: Full access (read, write, execute)
Group: Can read and execute, cannot edit
Others: Can read and execute, cannot edit
""",
        "755",
    ),
    (
        "level-3/file8.txt",
        """Permission required:

Owner: Can read and write
Group: Can only read
Others: Can only read
""",
        "644",
    ),
    (
        "level-3/file9.txt",
        """Permission required:

Owner: Can read and write
Group: No access
Others: No access
""",
        "600",
    ),

    # ---------------- Level 4 ----------------
    (
        "level-4/file10.txt",
        """Permission required:

Owner: Full access (read, write, execute)
Group: No access
Others: No access
""",
        "700",
    ),
    (
        "level-4/file11.txt",
        """Permission required:

Owner: Can read and write
Group: Can only read
Others: No access
""",
        "640",
    ),
    (
        "level-4/file12.txt",
        """Permission required:

Owner: Full access (read, write, execute)
Group: Can only read
Others: Can only read
""",
        "744",
    ),

    # ---------------- Level 5 ----------------
    (
        "level-5/file13.txt",
        """Permission required:

Owner: Can read and write
Group: Can read and write
Others: Can only read
""",
        "664",
    ),
    (
        "level-5/file14.txt",
        """Permission required:

Owner: Full access (read, write, execute)
Group: Can read and execute, cannot edit
Others: No access
""",
        "750",
    ),
    (
        "level-5/file15.txt",
        """Permission required:

Owner: Can only read
Group: No access
Others: No access
""",
        "400",
    ),
]

# ----------------------------------------
# Create Files
# ----------------------------------------

for path, content, _ in files:
    write_file(ROOT / path, content)

# ----------------------------------------
# Create check.py
# ----------------------------------------

checker = '''#!/usr/bin/env python3

from pathlib import Path
import stat

ROOT = Path(__file__).parent

FILES = [
'''

for path, _, permission in files:
    checker += f'    ("{path}", "{permission}"),\n'

checker += '''

]

GREEN = "\\033[92m"
RED = "\\033[91m"
YELLOW = "\\033[93m"
CYAN = "\\033[96m"
BOLD = "\\033[1m"
RESET = "\\033[0m"


def get_permissions(path):
    mode = path.stat().st_mode
    return oct(stat.S_IMODE(mode))[2:]


def main():
    passed = 0
    failed = 0

    print(f"{CYAN}{'=' * 40}{RESET}")
    print(f"{BOLD}Linux Permissions Lab Checker{RESET}")
    print(f"{CYAN}{'=' * 40}{RESET}\\n")

    for file, expected in FILES:
        path = ROOT / file

        if not path.exists():
            print(f"{YELLOW}MISSING{RESET}: {file}")
            failed += 1
            continue

        actual = get_permissions(path)

        if actual == expected:
            print(f"{GREEN}PASS{RESET}: {file}")
            passed += 1
        else:
            print(f"{RED}FAIL{RESET}: {file}")
            failed += 1

    print()
    print(f"{CYAN}{'=' * 40}{RESET}")
    print(f"{BOLD}Results{RESET}")
    print(f"{CYAN}{'=' * 40}{RESET}")
    print(f"{GREEN}Passed:{RESET} {passed}")
    print(f"{RED}Failed:{RESET} {failed}")
    print()

    if failed == 0:
        print(f"{GREEN}Congratulations! All file permissions are correct.{RESET}")
    else:
        print(f"{RED}Some file permissions are incorrect.{RESET}")
        print("Review the files that failed, update their permissions, and run the checker again.")


if __name__ == "__main__":
    main()
'''

write_file(ROOT / "check.py", checker)

# ----------------------------------------
# Set Incorrect Permissions
# ----------------------------------------

for path, _, _ in files:
    os.chmod(ROOT / path, 0o777)

# Make checker executable 
os.chmod(ROOT / "check.py", 0o755)

# ----------------------------------------
# Done
# ----------------------------------------

print("=" * 40)
print(" Linux Permissions Lab Created!")
print("=" * 40)
print()
print("Next steps:")
print("1. cd permissions-lab")
print("2. Use cat to read each file.")
print("3. Change the permissions with chmod.")
print("4. Run the checker:")
print("      python3 check.py")
