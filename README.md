====== Setup Project ======

# Python Study

This is the continuation of my Python study on automate_study_hub3e2.


## Setup

1. Step 1: Create the project folder

```bash
mkdir -p ~/Python/automate_study_hub3e22
cd ~/Python/automate_study_hub3e22
mkdir -p basics practice notes
touch README.md requirements.txt hello.py
```

2. Step 2: Create the project’s Python environment
```bash
python3 -m venv .venv
```

3. Step 3: Open the folder in VS Code

```bash
code .
```

4. Step 4: Install the Python extension in VS Code

5. Step 5: Select your project interpreter

6. Step 6: Add a project setting file

7. Step 7: Put in your first script

8. Step 8: Run it in VS Code

```text
python_study/
├── .venv/
├── .vscode/
│   └── settings.json
├── chapters/
│   ├── chapter_8_strings_and_text_editing
│   │   ├── practice_projects
│   │   ├── topic_scripts
│   │   ├── README.md
│   │   └── USAGE.md
│   ├── chapter_9_text_pattern_matching_with_regular_expressions
│   └── ...
├── practice/
│   └── practice_01.py
├── reviews/
│   └── week_01.md
├── tools/
│   └── week_01.md
├── notes/
│   └── week_01.md
├── hello.py
├── README.md
└── requirements.txt
```
Setup completed.


## .venv

```bash
mkdir -p ~/Python/automate_study_hub3e2
cd ~/Python/automate_study_hub3e2
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
code .
```



## GitHub Operations


```bash
git init
git add .
git commit -m "Initial commit"
```

```bash
git remote add origin https://github.com/shrg182/automate_study_hub3e22.git
git branch -M main
git push -u origin main
```

Go to tools/github_issues/README.md 2026-05-08 4:44 PM

## Chapter Directories

1. Scrape Table of Contents
2. Scrape Chapter Topics
3. Create Chapter Directories

These tasks are made in tools/ directory.



=== USAGE ===

## To-do list

```bash
python3 todo_list.py --todo-dir work_tasks
python3 todo_list.py --todo-dir personal_tasks
python3 todo_list.py --todo-dir chapters/chapter_11
```
