<!-- markdownlint-disable MD013 -->
# Unix Shell — Episodes 1‑3 Notes

> Summaries based on the Software Carpentry *Shell Novice* course  
> *Episode 1 – Introducing the Shell*  
> *Episode 2 – Navigating Files & Directories*  
> *Episode 3 – Working with Files & Directories*

---

## Episode 1 · Introducing the Shell

| Concept | Key Points |
|---------|------------|
| **What is a shell?** | A command‑line interpreter that lets us type text commands to the computer, ideal for **automation**, **reproducibility**, and **remote work**. |
| **Command anatomy** | `command [options] [arguments]` — e.g. `ls -l /home/nasir`. |
| **Prompt & Cursor** | The **prompt** (e.g. `$`) tells us the shell is ready; typing executes when we press **Enter**. |
| **Getting help** | `command --help`, `man command`, or online docs. |
| **Tab completion** | Press **Tab** to auto‑complete filenames/commands. |
| **Command history** | ↑ / ↓ to navigate; `Ctrl‑R` to search; `history` to list. |
| **Interrupt / EOF** | `Ctrl‑C` stops a running job; `Ctrl‑D` sends End‑of‑File. |

> **Take‑away:** The shell excels at chaining simple tools into powerful workflows.

---

## Episode 2 · Navigating Files & Directories

### 1. Where am I?

```bash
pwd          # print working directory
/home/nasir/projects
```

### 2. Listing contents

```bash
ls           # names only
ls -F        # classify: '/' for dirs, '*' for executables
ls -a        # include hidden files (.*)
```

### 3. Moving around

| Command  | Action              |
|----------|---------------------|
| `cd dir` | change into **dir** |
| `cd ..`  | up one level        |
| `cd ~`   | back to home        |
| `cd -`   | toggle to previous dir |

### Absolute vs Relative Paths

* **Absolute**: starts with `/` (root) — e.g. `/var/log`.  
* **Relative**: interpreted from current location — e.g. `../data`.  
* `.` = current dir, `..` = parent dir.

---

## Episode 3 · Working with Files & Directories

### 1. Creating & Removing

```bash
mkdir results          # new directory
touch notes.txt        # new empty file (or update timestamp)
rm notes.txt           # delete file (no undo!)
rm -r old_results/     # recursively remove directory
```

### 2. Copying & Moving

```bash
cp report.txt backup/report.txt   # copy file
mv draft.txt report.txt           # rename/move
mv *.csv data/                    # move group via wildcard
```

### 3. Viewing File Contents

| Command     | Use                                       |
|-------------|-------------------------------------------|
| `cat file`  | dump whole file to screen                 |
| `less file` | page through text (q to quit)             |
| `head -n k` | first *k* lines                           |
| `tail -n k` | last *k* lines; `-f` follows live updates |

### 4. Globbing (Wildcards)

| Pattern | Matches                  | Example                                   |
|---------|--------------------------|-------------------------------------------|
| `*`     | any string (incl. empty) | `*.sh` → `run.sh`, `build.sh`             |
| `?`     | exactly one char         | `?.md` → `a.md`, not `readme.md`          |
| `[abc]` | one char in set          | `file[12].txt` → `file1.txt`, `file2.txt` |

### 5. File‑Naming Conventions

* Avoid spaces (`my file.txt`); prefer `my_file.txt`.  
* Extensions (e.g. `.txt`, `.csv`) are conventions; the shell cares more about file content.

---

### Handy Keyboard Shortcuts (Recap)

| Shortcut | Effect               |
|----------|----------------------|
| `Ctrl‑C` | Kill current process |
| `Ctrl‑L` | Clear terminal       |
| `Ctrl‑R` | Reverse‑search history |

---

_Last updated: 12 May 2025_
