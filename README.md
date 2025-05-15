# Bioinfo Shell Dojo

This repository contains materials and exercises related to learning and practicing command-line skills relevant to bioinformatics. It's primarily based on the Software Carpentry "The Unix Shell" lesson, with additional exercises and utilities tailored for bioinformatics workflows.

## Contents

This repository is organized as follows:

* **Software Carpentry Exercises:** Contains notes, command examples, and reflections from working through sections 1-3 and the lab book of the Software Carpentry "The Unix Shell" lesson.
* **Loops in Bash:** Includes a `loops.sh` script (`loops.sh`) demonstrating the use of loops in Bash scripting.
* **FASTQ ID Extraction:** Features a one-liner command for listing unique identifiers within FASTQ files.
* **Text Processing Mini-Exercise:**
    * `show_fastq_ids.sh`: A Bash script designed to extract sequence IDs from a FASTA file.
* **Phred Score Utility:**
    * `qbase`: A utility script (Python) that calculates the mean Phred score per read in a FASTQ file.

## Getting Started

To explore the contents of this repository, simply navigate through the directories and files. The scripts are intended to be executed in a Unix-like environment (Linux, macOS, or Windows with WSL).

### Prerequisites

* **Bash:** For running the shell scripts (`.sh`).
* **Python:** Ensure Python 3 is installed on your system.

### Usage

1.  **Software Carpentry Notes:** Review the markdown files containing notes and reflections on the Software Carpentry lessons. Execute the command examples in your own terminal to practice.
2.  **`loops.sh`:** Navigate to the repository directory in your terminal and run:
    ```bash
    bash loops.sh
    ```
3.  **FASTQ ID One-liner:** This is a command to be executed in the terminal. The exact command will depend on the structure of your FASTQ files (e.g., using `grep`, `awk`, `sed`, and `sort -u`).
4.  **`show_fastq_ids.sh`:**
    ```bash
    bash show_fastq_ids.sh
    ```
   
5.  **`qbase`:**
        python3 qbase.py

## Reflections and Learning

This repository serves as a record of learning and applying fundamental Unix shell commands and scripting techniques relevant to bioinformatics. The exercises and utilities demonstrate practical skills in file manipulation, data extraction, and basic bioinformatic analysis.

## Further Exploration

* Revisit the Software Carpentry "The Unix Shell" lesson for a deeper understanding of the concepts covered.
* Experiment with modifying the provided scripts and one-liners to handle different bioinformatics tasks.
* Explore other powerful command-line tools commonly used in bioinformatics, such as `awk`, `sed`, `cut`, `head`, `tail`, and more.
* Consider learning more advanced Bash scripting for automating complex bioinformatics workflows.

## License

[MIT License]