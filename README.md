
# Linux Permissions Lab

## Overview

This lab helps you learn and practice Linux file permissions. You will:

* Read permission instructions inside files
* Translate descriptions into `chmod` numeric values
* Apply permissions using `chmod`
* Run a checker script to verify your work

---

## Project Structure

```text
permissions-lab/
├── check.py
├── level-1/
├── level-2/
├── level-3/
├── level-4/
├── level-5/
└── file#.txt
```

Each level contains three files with permission challenges.

---

## Setup Instructions

### 1. Run the setup script

```bash
python3 setup.py
```

This will generate the full lab automatically.

---

### 2. Enter the lab directory

```bash
cd permissions-lab
```

---

### 3. Start the lab

Use the following commands to explore files:

```bash
ls -l
cat level-1/file1.txt
```

---

## Task Instructions

For each file:

1. Open/Read the file using `cat`
2. Read the permission description
3. Convert it into a numeric `chmod` value
4. Apply the correct permissions

Example:

```text
Owner: Full access (read, write, execute)
Group: Can read and execute, cannot edit
Others: Can read and execute, cannot edit
```

Becomes:

```bash
chmod 755 file.txt
```

---

## Running the Checker

After completing all files:

```bash
python3 check.py
```

The output will show:

* PASS for correct permissions
* FAIL for incorrect permissions

---

## Permission Reference

| Symbol | Meaning     |
| ------ | ----------- |
| r      | read (4)    |
| w      | write (2)   |
| x      | execute (1) |

### Common values

| Value | Meaning                                 |
| ----- | --------------------------------------- |
| 755   | owner full, group/others read + execute |
| 644   | owner read/write, others read           |
| 600   | private file                            |

---

## Learning Goals

* Understanding Linux file permissions
* Using `chmod` with numeric values
* Reading and interpreting file instructions
* Debugging permission errors
* Using basic Linux terminal commands

