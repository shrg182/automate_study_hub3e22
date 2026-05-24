# Directories

This folder contains a basic directory-tree script.

## Scripts

| Script | Purpose |
| --- | --- |
| `directory_tree.py` | Prints a directory structure as a text tree, similar to the Unix `tree` command. |

## Usage

```bash
python3 basics/directories/directory_tree.py
python3 basics/directories/directory_tree.py /path/to/project
```

## Related Scripts Created Elsewhere

| Related script | Relationship |
| --- | --- |
| `tools/utility_files/list_chapter_directories.py` | Duplicates and adapts the tree-printing idea from `directory_tree.py` for listing chapter directories. |
| `tools/utility_files/populate_utility_files_in_chapters.py` | Includes its own `make_directory_tree()` helper while creating README.md, USAGE.md, and utils.py files for chapter folders. |

