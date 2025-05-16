# Unix Shell — Lesson 5: **Loops**

Software Carpentry *shell‑novice* curriculum  
Source: <https://swcarpentry.github.io/shell-novice/05-loop.html>

---

## Why Loops Matter

* Repeat one or more commands for **every item in a list**, saving time and reducing typos.  
* Key to automation pipelines (e.g. processing hundreds of data files).  
* Complements other productivity boosters such as **wildcards** and **tab‑completion**.  

---

## Canonical `for`‑Loop Pattern

```bash
for var in list_of_items
do
    command_using "$var"
done
```

`for` starts the loop; `do … done` encloses the body.

`$var` (or `${var}`) expands to the current item.

---

### Worked Example – Extracting Classifications

```bash
for filename in basilisk.dat minotaur.dat unicorn.dat
do
    echo "$filename"
    head -n 2 "$filename" | tail -n 1
done
```

Output:

```
basilisk.dat
CLASSIFICATION: basiliscus vulgaris
...
```

Each iteration assigns one file name to `filename`, then runs the two commands.  
`echo` is used here so we can see which file is being processed (a simple debugging trick).

---

### Good Practices

* **Variable names** – Use descriptive names (`filename`, not `x`).  
* **Prompt vs Operators** – `$` and `>` are prompts when printed by the shell and operators when you type them.  
* **Quoting** – Quote `$var` if the value may contain spaces: `"$filename"`.  
* **Wildcards inside loops** – `*.pdb` is expanded each time. Write `ls "$datafile"`, not `ls *.pdb`, if you want one file per iteration.  
* **Redirection** – `>` overwrites; `>>` appends. Misplacing them inside a loop can clobber data.  
* **Dry‑runs** – Replace the real command with `echo …` inside the loop to preview actions safely.  
* **History shortcuts** – ↑ arrow, `Ctrl + R`, `!!`, `!$`, and `history` help you re‑use or edit long loops quickly.

---

### Common Loop Patterns

1. **Enumerating Numbers**

   ```bash
   for i in {0..9}; do echo $i; done
   ```

2. **Copying / Back‑ups**

   ```bash
   for f in *.dat; do cp "$f" "original-$f"; done
   ```

3. **Concatenating Many Files**

   ```bash
   for f in *.pdb; do cat "$f" >> all.pdb; done
   ```
   Use `>>` so earlier content is preserved; `>` would overwrite on each pass.

4. **Nested Loops (combinatorial directories)**

   ```bash
   for species in cubane ethane methane
   do
       for temp in 25 30 37 40
       do
           mkdir "${species}-${temp}"
       done
   done
   ```
   Creates 3 × 4 = 12 directories (`cubane-25`, …, `methane-40`).

---

### Quick Reference

| Pattern | Meaning |
|---------|---------|
| `for var in list; do …; done` | basic loop |
| `$var` or `${var}` | expand variable |
| `"$var"` | expand and protect spaces |
| `echo cmd …` | dry‑run: print instead of execute |
| `Ctrl +C` | stop a running loop |
| `Ctrl +A / Ctrl +E` | jump to start/end of command line |
| `history`, `!n`, `!!`, `!$` | command‑history tricks |

---

### Key Points Recap

* Loops iterate once per list element.  
* Use meaningful variable names and quote variables when in doubt.  
* Avoid spaces and special characters in filenames to keep loops simple.  
* Preview potentially destructive loops with `echo` dry‑runs.  
* Command history is your friend—reuse and edit instead of re‑typing.
