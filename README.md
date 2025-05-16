# Bioinfo Shell Dojo

This repository contains materials and exercises related to learning and
practicing command‑line skills relevant to bioinformatics. It is based mainly on
the Software Carpentry “Unix Shell” lesson, with extra examples tailored to
common bioinformatics workflows.

## Contents

* **Software Carpentry Notes:** Markdown summaries for Episodes 1‑3 plus a lab
  book.
* **Loops in Bash:** A `loops.sh` script that demonstrates basic `for` loops.
* **FASTQ ID Extraction:** A one‑liner for listing unique identifiers inside
  FASTQ files.
* **Text‑processing Mini‑Exercise:**  
  * `show_fastq_ids.sh` – extract sequence IDs from a FASTA file.
* **Phred‑score Utility:**  
  * `qbase.py` – calculate the mean Phred score per read in a FASTQ file.

## Getting Started

Clone the repo and explore the directories. All scripts assume a Unix‑like
environment (Linux, macOS, or Windows + WSL).

### Prerequisites

* **Bash** for shell scripts (`.sh`).  
* **Python 3** for `qbase.py`.

### Usage

1. **Notes:** Open the Markdown files and work through the examples in your own
   terminal.
2. **Run `loops.sh`:**

   ```bash
   bash loops.sh
   ```

3. **FASTQ ID one‑liner:** Adjust the command to match your file layout; a
   typical pattern is:

   ```bash
   grep '^@' reads.fastq | cut -d ' ' -f 1 | sort -u
   ```

4. **`show_fastq_ids.sh`:**

   ```bash
   bash show_fastq_ids.sh
   ```

5. **`qbase.py`:**

   ```bash
   python3 qbase.py
   ```

## Reflections & Learning

These materials capture my progress in mastering fundamental Unix‑shell
commands and scripting. The examples highlight practical skills in file
manipulation, data extraction, and lightweight bioinformatic analysis.

## Further Exploration

* Revisit the Software Carpentry lesson to deepen understanding.
* Tweak the provided scripts to solve your own problems.
* Learn more command‑line power‑tools (`awk`, `sed`, `cut`, `head`, `tail`, …).
* Study advanced Bash scripting to automate end‑to‑end bioinformatics pipelines.

## License

MIT
