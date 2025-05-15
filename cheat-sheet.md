# Bioinfo Shell Dojo Cheatsheet

This cheatsheet contains a list of useful Unix shell and Git commands used during the Bioinfo Shell Dojo exercises.

## Unix Shell Commands

1.  `cd <directory>`: Changes the current working directory to the specified `<directory>`.
    ```bash
    cd /Users/nasir/Projects/core\ bioinformatics/bioinfo-shell-dojo/
    ```
2.  `ls -al`: Lists all files and directories in the current directory, including hidden ones, with detailed information (permissions, size, modification date, etc.).
    ```bash
    ls -al ~/.ssh
    ```
3.  `rm <file>`: Removes the specified `<file>`. Be cautious, as this is permanent!
    ```bash
    rm .git/index.lock
    ```
4.  `cat <file>`: Displays the content of the specified `<file>` on the terminal.
    ```bash
    cat ~/.ssh/id_rsa.pub
    ```
5.  `touch <file>`: Creates an empty file with the specified name.
    ```bash
    touch cheat-sheet.md
    ```
6.  `bash <script.sh>`: Executes the Bash script `<script.sh>`.
    ```bash
    bash loops.sh
    bash grep_bla_ids.sh example.fasta
    ```
7.  `python <script.py>`: Executes the Python script `<script.py>`.
    ```bash
    python qbase
    ```
8.  `grep "<pattern>" <file>`: Searches for lines containing the `<pattern>` within the specified `<file>`.
9.  `head <file>`: Displays the first few lines (default is 10) of the specified `<file>`.
10. `tail <file>`: Displays the last few lines (default is 10) of the specified `<file>`.


## Git Commands

11. `git add <file>`: Adds the specified `<file>` to the staging area, preparing it for the next commit.
    ```bash
    git add cheat-sheet.md
    git add .
    ```
12. `git commit -m "<commit message>"`: Creates a new commit with the provided `<commit message>`, recording the changes in the staging area.
    ```bash
    git commit -m "feat: Add comprehensive README.md file"
    ```
13. `git status`: Displays the current state of the working directory and the staging area.
14. `git checkout <branch>`: Switches to the specified `<branch>`.
    ```bash
    git checkout main
    ```
15. `git checkout -b <new_branch>`: Creates a new branch named `<new_branch>` and switches to it.
    ```bash
    git checkout -b feature/cheatsheet
    ```
16. `git push <remote> <branch>`: Uploads your local commits on the specified `<branch>` to the `<remote>` repository.
    ```bash
    git push origin feature/cheatsheet
    git push -u origin main
    ```
17. `git pull <remote> <branch>`: Downloads changes from the specified `<branch>` of the `<remote>` repository and integrates them into your current branch.
    ```bash
    git pull origin main
    git pull --rebase origin main
    ```
18. `git remote -v`: Lists the configured remote repositories.