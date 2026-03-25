# file-structure-generator

A Python CLI tool that scans a directory and generates a markdown-friendly tree view.
The tool writes the output to a file (default: tree.md) wrapped in a code fence so it can be pasted directly into documentation.

## Requirements

- Python 3.8+

## Install from GitHub Repo

Recommended: install directly from GitHub without cloning first:

```bash
python -m pip install "git+https://github.com/jtutor26/file-structure-generator.git"
```

Repo URL:

- https://github.com/jtutor26/file-structure-generator

## Other install options (optional)

If you prefer to clone and install locally:

```bash
git clone https://github.com/jtutor26/file-structure-generator.git
cd file-structure-generator
python -m pip install .
```

After installation, the CLI command is available as:

```bash
generate-tree
```

## Usage

### Basic usage

Generate a tree for a target directory and write it to tree.md:

```bash
generate-tree /path/to/target-directory
```

### Custom output file

Write output to a custom markdown file:

```bash
generate-tree /path/to/target-directory --output structure.md
```

You can also use the short flag:

```bash
generate-tree /path/to/target-directory -o structure.md
```

## What gets generated

The output markdown file contains:

- A fenced code block with the directory tree
- A short helper message at the end

Example tree content:

```text
my-project
├── app.py
└── docs
	└── guide.md
```

## Run tests

Install test dependencies and run pytest:

```bash
python -m pip install -e .[test]
pytest
```

## Future releases

- More info to display on tree
- Automatically generate tree from current root directiory if no filepath is given
