# Explanation: populate_utility_files_in_chapters.py

## Purpose

`populate_utility_files_in_chapters.py` creates or updates standard utility files inside chapter folders:

- `README.md`
- `USAGE.md`
- `utils.py`

It scans the `chapters/` directory, finds target directories, renders template files with chapter-specific values, and writes the rendered files into each target directory.

The script is designed for maintaining a consistent structure across chapter folders and their subdirectories.

## Main Features

- Discovers chapter directories automatically from the filesystem.
- Optionally includes the root `chapters/` directory with `--include-root`.
- Loads reusable templates from `tools/utility_files/templates/`.
- Supports table-of-contents metadata from `tools/web_scraping/out/atbs3e_toc.json`.
- Renders placeholders such as `{chapter_title}`, `{directory_name}`, and `{generated_at}`.
- Skips cache, data, output, hidden, and explicitly excluded chapter directories.
- Protects selected chapters from overwrite even when `--overwrite` is used.
- Supports `--dry-run` to preview actions without writing files.
- Prints per-directory results and a final status summary.

## Important Constants

### `PROJECT_ROOT`

Stores the project root directory.

It is calculated from the script location:

```python
Path(__file__).resolve().parents[2]
```

This lets the script work from any current working directory as long as the project structure stays the same.

### `DEFAULT_CHAPTERS_DIR`

Points to the default chapter folder:

```python
PROJECT_ROOT / "chapters"
```

This is where the script searches for chapter directories.

### `DEFAULT_TEMPLATE_DIR`

Points to the template directory:

```python
PROJECT_ROOT / "tools" / "utility_files" / "templates"
```

The script expects the template files to be located there unless another directory is passed with `--template-dir`.

### `DEFAULT_TOC_FILE`

Points to the optional table-of-contents JSON file:

```python
PROJECT_ROOT / "tools" / "web_scraping" / "out" / "atbs3e_toc.json"
```

When this file exists, the script uses it to enrich chapter titles and URLs.

### `TEMPLATE_TO_OUTPUT`

Maps template filenames to the generated output filenames:

```python
{
    "README.md.template": "README.md",
    "USAGE.md.template": "USAGE.md",
    "utils.py.template": "utils.py",
}
```

Each template is rendered once for every target directory.

### `SKIPPED_DIRECTORY_NAMES`

Contains directory names that should not receive generated utility files.

Examples include:

- `.git`
- `__pycache__`
- `data`
- `output`
- cache directories

### `EXCLUDE_CHAPTERS`

Contains chapter directory names that are skipped completely during discovery.

These chapters do not receive generated utility files from this script.

## Data Definition

### `ChapterMetadata`

`ChapterMetadata` is a frozen dataclass used to store chapter information.

```python
@dataclass(frozen=True)
class ChapterMetadata:
    chapter_number: int | None
    chapter_title: str
    chapter_url: str
```

Fields:

- `chapter_number`: The numeric chapter value, such as `1` or `18`.
- `chapter_title`: The human-readable chapter title.
- `chapter_url`: The source URL for the chapter.

Because the dataclass is frozen, its values cannot be changed after creation.

## Command-Line Arguments

The `parse_args()` function defines the script's command-line interface.

### `--chapters-dir`

Sets the directory that contains chapter folders.

Default:

```text
chapters
```

### `--template-dir`

Sets the directory that contains template files.

Default:

```text
tools/utility_files/templates
```

### `--toc-file`

Sets the optional JSON table-of-contents file.

Default:

```text
tools/web_scraping/out/atbs3e_toc.json
```

### `--include-root`

Also generates files directly inside the root `chapters/` directory.

Without this option, only subdirectories are targeted.

### `--use-exclude-chapters`

Uses the built-in `EXCLUDE_CHAPTERS` set during directory discovery.

This is the default behavior, so you usually do not need to type this option.

### `--no-exclude-chapters`

Turns off the built-in `EXCLUDE_CHAPTERS` set during directory discovery.

Use this when you want the script to include chapters that are normally skipped.

Example:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py --no-exclude-chapters
```

### `--overwrite`

Allows existing generated files to be overwritten.

Without this option, existing `README.md`, `USAGE.md`, and `utils.py` files are skipped.

### `--exclude-overwrite-chapters`

Protects specific chapter directories from overwrite.

This only matters when `--overwrite` is also used.

Values can be separated by spaces or commas.

Example:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py \
  --overwrite \
  --exclude-overwrite-chapters chapter_00_introduction,chapter_01_python_basics
```

### `--dry-run`

Shows what the script would do without writing any files.

This is useful for checking the target directories and overwrite behavior before making changes.

## Function Overview

### `load_toc_metadata(toc_file)`

Loads chapter metadata from a JSON table-of-contents file.

Behavior:

- Returns an empty dictionary if the file does not exist.
- Requires the JSON root value to be a list.
- Reads `chapter_num`, `title`, and `url` fields from each item.
- Falls back to `extract_chapter_number()` when `chapter_num` is missing.
- Returns a dictionary keyed by chapter number.

### `extract_chapter_number(title, url="")`

Finds a chapter number inside a title, URL, or directory-like string.

Supported patterns include:

- `chapter_03`
- `chapter 03`
- `chapter-03`
- `chapter3.html`

Returns an integer when found, otherwise `None`.

### `clean_chapter_title(title)`

Removes a leading chapter prefix from a title.

Example:

```text
Chapter 3 - Loops
```

becomes:

```text
Loops
```

### `prettify_directory_name(directory_name)`

Converts directory names into title-style display text.

Example:

```text
chapter_03_loops
```

becomes:

```text
Chapter 03 Loops
```

### `should_skip_directory(path)`

Returns `True` when a directory should be ignored.

A directory is skipped when:

- Its name starts with `.`
- Its name is in `SKIPPED_DIRECTORY_NAMES`
- Its name is in `EXCLUDE_CHAPTERS` and the exclude switch is enabled

### `discover_target_directories(chapters_dir, include_root)`

Finds all directories that should receive utility files.

Behavior:

- Verifies that the chapter directory exists.
- Adds the root directory when `include_root` is enabled.
- Recursively scans with `rglob("*")`.
- Skips ignored directories and anything inside ignored directories.
- Returns a sorted list of target paths.

### `parse_excluded_chapter_names(raw_values)`

Normalizes chapter names passed to `--exclude-overwrite-chapters`.

It handles:

- Space-separated values
- Comma-separated values
- Trailing slashes
- Full or relative paths

Only the final directory name is kept.

### `is_overwrite_protected(target_dir, chapters_dir, excluded_chapter_names)`

Checks whether a target directory belongs to a protected chapter.

If the top-level chapter directory is listed in `excluded_chapter_names`, all directories inside that chapter are protected from overwrite.

### `make_directory_tree(root)`

Builds a simple one-level text tree for a directory.

This value is used by templates through the `{directory_tree}` placeholder.

### `load_templates(template_dir)`

Loads every template listed in `TEMPLATE_TO_OUTPUT`.

If any required template file is missing, the function raises `FileNotFoundError`.

### `render_template(template, context)`

Replaces simple placeholder tokens in a template.

Example:

```text
{chapter_title}
```

is replaced with the matching value from the context dictionary.

The function only replaces identifier-like placeholders. This protects literal braces that may appear in Python code inside templates.

### `find_chapter_directory(path, chapters_dir)`

Returns the top-level chapter directory for a target path.

For example, if the target path is:

```text
chapters/chapter_03_loops/practice
```

the chapter directory is:

```text
chapters/chapter_03_loops
```

### `build_context(target_dir, chapters_dir, toc_metadata)`

Creates the dictionary of placeholder values used by templates.

Important context keys include:

- `chapter_title`
- `chapter_clean_title`
- `chapter_number`
- `chapter_url`
- `directory_name`
- `directory_title`
- `directory_tree`
- `generated_at`
- `parent_directory_name`
- `relative_chapter_directory`
- `relative_directory`

This function combines filesystem information with optional TOC metadata.

### `write_rendered_file(output_path, content, overwrite, overwrite_protected, dry_run)`

Writes one generated file and returns a status string.

Possible statuses:

- `created`
- `overwritten`
- `skipped`
- `protected`
- `would create`
- `would overwrite`

The function respects `--overwrite`, `--dry-run`, and overwrite protection.

### `populate_directory(...)`

Generates all configured utility files for one target directory.

For each template:

1. Builds rendered content.
2. Chooses the output filename.
3. Writes or skips the file.
4. Stores the result status.

Returns a dictionary like:

```python
{
    "README.md": "created",
    "USAGE.md": "created",
    "utils.py": "skipped",
}
```

### `main()`

Coordinates the full script.

Main steps:

1. Parse command-line arguments.
2. Resolve paths.
3. Load templates.
4. Load TOC metadata.
5. Parse overwrite-protected chapter names.
6. Discover target directories.
7. Populate each target directory.
8. Print per-directory results.
9. Print a final summary.

## Processing Flow

The script follows this sequence:

```text
parse args
  -> load templates
  -> load optional TOC metadata
  -> discover target directories
  -> build context for each directory
  -> render templates
  -> write, skip, protect, or preview files
  -> print summary
```

## Template Placeholder System

Templates use simple placeholders wrapped in braces.

Example:

```text
# {directory_title}

Generated at: {generated_at}
```

The renderer replaces placeholders only when the name exists in the context dictionary.

Unknown placeholders are left unchanged.

This makes the renderer safer for `utils.py.template`, where normal Python code may contain braces.

## How README.md Content Is Created

Each chapter `README.md` file is created from this template:

```text
tools/utility_files/templates/README.md.template
```

The script does not manually write each README line by line. Instead, it loads the template, builds a context dictionary for the current chapter directory, replaces placeholders in the template, and writes the final rendered text to `README.md`.

The main steps are:

1. `load_templates()` reads `README.md.template`.
2. `discover_target_directories()` finds chapter folders and subfolders.
3. `build_context()` creates values such as `chapter_title`, `chapter_page_url`, `atbs_chapter_url`, `directory_name`, and `generated_datetime`.
4. `render_template()` replaces placeholders like `{chapter_title}` and `{chapter_page_url}`.
5. `write_rendered_file()` writes the finished content to `README.md`.

The chapter URL comes from:

```text
tools/web_scraping/out/atbs3e_toc.json
```

For the URL to appear in a generated README, the script must be able to match the chapter directory name to a chapter number. For example, `chapter_01_python_basics` must be recognized as chapter `1`, so the script can look up chapter `1` in the TOC JSON and use its `url` field.

If the README shows a blank chapter URL, the usual causes are:

- The TOC JSON file is missing.
- The TOC JSON record does not include a URL.
- The chapter number could not be extracted from the directory name.
- The README was generated before the URL lookup logic was fixed.

After fixing the lookup logic, regenerate existing README files with `--overwrite` if you want old blank URLs to be replaced.

## Overwrite Behavior

Default behavior is conservative.

If a file already exists and `--overwrite` is not used, the file is skipped.

When `--overwrite` is used, existing files are replaced unless the target directory belongs to a chapter listed in `--exclude-overwrite-chapters`.

When `--dry-run` is used, no files are written. The script reports what would happen instead.

## Coding Skills Used in This Script

This script demonstrates several practical Python coding skills that are useful for automation, command-line tools, and project maintenance.

### 1. Writing Command-Line Programs

The script uses the `argparse` module to create a command-line interface.

Important skills shown:

- Defining optional flags.
- Setting default argument values.
- Accepting paths from the user.
- Creating boolean switches such as `--dry-run`, `--overwrite`, and `--include-root`.

Example from the script:

```python
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Show intended actions without writing files.",
)
```

This teaches how to make a Python script flexible instead of hard-coding every behavior.

### 2. Working with Files and Directories

The script uses `pathlib.Path` for filesystem work.

Important skills shown:

- Building paths with `/`.
- Checking whether files and directories exist.
- Reading text files.
- Writing text files.
- Resolving absolute paths.
- Scanning directories recursively.

Examples from the script:

```python
template_path.is_file()
template_path.read_text(encoding="utf-8")
output_path.write_text(content, encoding="utf-8")
chapters_dir.rglob("*")
```

Using `pathlib` makes file handling cleaner and more readable than manually joining strings.

### 3. Using Constants for Configuration

The script stores repeated configuration values as constants near the top of the file.

Examples:

```python
DEFAULT_CHAPTERS_DIR
DEFAULT_TEMPLATE_DIR
DEFAULT_TOC_FILE
TEMPLATE_TO_OUTPUT
SKIPPED_DIRECTORY_NAMES
EXCLUDE_CHAPTERS
```

Important skills shown:

- Keeping important settings easy to find.
- Avoiding repeated hard-coded strings.
- Making script behavior easier to update.
- Using `Final` type hints for values that should not be reassigned.

### 4. Creating Structured Data with Dataclasses

The script uses a dataclass named `ChapterMetadata`.

```python
@dataclass(frozen=True)
class ChapterMetadata:
    chapter_number: int | None
    chapter_title: str
    chapter_url: str
```

Important skills shown:

- Grouping related data into one object.
- Adding type hints to each field.
- Using `frozen=True` to make objects read-only.
- Making code easier to understand than using plain dictionaries everywhere.

### 5. Reading and Validating JSON Data

The `load_toc_metadata()` function reads chapter metadata from a JSON file.

Important skills shown:

- Loading JSON with `json.loads()`.
- Checking that the decoded data has the expected type.
- Safely handling missing or invalid fields.
- Returning an empty result when an optional file does not exist.

Example:

```python
if not toc_file.is_file():
    return {}
```

This is a useful pattern for optional data files.

### 6. Using Type Hints

The script uses type hints throughout the code.

Examples:

```python
def load_toc_metadata(toc_file: Path) -> dict[int, ChapterMetadata]:
def extract_chapter_number(title: str, url: str = "") -> int | None:
def discover_target_directories(chapters_dir: Path, include_root: bool) -> list[Path]:
```

Important skills shown:

- Making function inputs and outputs clear.
- Helping editors and type checkers detect mistakes.
- Making larger scripts easier to maintain.

### 7. Using Regular Expressions

The script uses the `re` module to find chapter numbers and replace template placeholders.

Important skills shown:

- Searching text with patterns.
- Using case-insensitive matching.
- Capturing useful parts of a match.
- Replacing text with a callback function.

Example:

```python
match = re.search(pattern, haystack, flags=re.IGNORECASE)
```

Another important example is in `render_template()`, where only safe placeholder names are replaced:

```python
re.sub(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", replace_match, template)
```

### 8. Building a Simple Template Renderer

The `render_template()` function is a small custom template system.

Important skills shown:

- Passing a dictionary of values into a renderer.
- Replacing placeholders with dynamic content.
- Leaving unknown placeholders unchanged.
- Avoiding accidental replacement of normal Python braces in template files.

This is a good example of solving a specific project problem without adding an external dependency.

### 9. Separating Code into Small Functions

The script is organized into focused functions.

Examples:

- `parse_args()` handles command-line arguments.
- `load_templates()` handles template loading.
- `build_context()` prepares template values.
- `write_rendered_file()` handles file-writing rules.
- `populate_directory()` applies templates to one directory.
- `main()` coordinates the full process.

Important skills shown:

- Keeping each function responsible for one job.
- Making the code easier to test and debug.
- Making the script easier to extend later.

### 10. Handling Safe File Generation

The script uses careful rules before writing files.

Important skills shown:

- Skipping existing files by default.
- Supporting an explicit overwrite mode.
- Supporting overwrite protection for selected chapters.
- Supporting dry-run mode.
- Returning status strings that explain what happened.

Example statuses:

```text
created
overwritten
skipped
protected
would create
would overwrite
```

This is an important automation skill because scripts that write many files should be predictable and safe.

### 11. Collecting and Reporting Results

The script tracks how many files were created, skipped, protected, or overwritten.

Important skills shown:

- Using a dictionary as a counter.
- Printing useful progress messages.
- Summarizing results at the end.

Example:

```python
status_counts[status] = status_counts.get(status, 0) + 1
```

This makes the script easier to trust because the user can see exactly what happened.

### 12. Using the `main()` Pattern

The script ends with this common Python pattern:

```python
if __name__ == "__main__":
    main()
```

Important skills shown:

- Allowing the file to run as a script.
- Keeping the main workflow inside a function.
- Making the file easier to import without immediately running the script.

## Skills Summary

By studying this script, you can practice:

- Command-line argument parsing.
- Filesystem automation.
- Template rendering.
- JSON loading.
- Regular expressions.
- Dataclasses.
- Type hints.
- Safe file writing.
- Recursive directory discovery.
- Function-based program organization.
- Status reporting and summaries.

## Example Commands

Create missing files only:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py
```

Preview changes:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py --dry-run
```

Include chapters that are normally listed in `EXCLUDE_CHAPTERS`:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py --no-exclude-chapters
```

Overwrite existing files:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py --overwrite
```

Overwrite files except inside selected chapters:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py \
  --overwrite \
  --exclude-overwrite-chapters chapter_00_introduction
```

Also populate the root `chapters/` directory:

```bash
python3 tools/utility_files/populate_utility_files_in_chapters.py --include-root
```

## Output Summary

At the end, the script prints a summary of all file statuses.

Example:

```text
Summary: created: 12, skipped: 30
```

This helps confirm whether the script created new files, skipped existing files, overwrote files, or protected selected chapters.
