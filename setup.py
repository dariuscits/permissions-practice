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
# Create check.sh
# ----------------------------------------

checker = """#!/bin/bash

echo "Checking permissions..."
echo

check() {
    file="$1"
    expected="$2"
    actual=$(stat -c "%a" "$file")

    if [ "$actual" = "$expected" ]; then
        echo "PASS  $file"
    else
        echo "FAIL  $file"
        echo "      Expected: $expected"
        echo "      Found:    $actual"
    fi
}

"""

for path, _, permission in files:
    checker += f'check "{path}" "{permission}"\n'

write_file(ROOT / "check.sh", checker)

# ----------------------------------------
# Set Incorrect Permissions
# ----------------------------------------

for path, _, _ in files:
    os.chmod(ROOT / path, 0o777)

# Make checker NOT executable
os.chmod(ROOT / "check.sh", 0o644)

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
print("4. Make the checker executable:")
print("      chmod +x check.sh")
print("5. Run the checker:")
print("      ./check.sh")
