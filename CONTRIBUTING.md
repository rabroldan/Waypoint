# Contributing

First of all, thank you for considering contributing to Waypoint.

Please follow these guidelines to ensure a smooth and cooperative contribution process.

## What Can I Contribute?

Waypoint is a tool for creating a journal using a text file or even converting the text to HTML. To contribute, you can consider the following:

- Enhance the program's functionality.
- Help with existing issues or create new ones.
- Share your ideas and suggestions.
- Report any bugs you encounter.
- Improve documentation, including incomplete or missing sections.

## Responsibilities

When contributing, please make sure that your code runs correctly. If you plan to make significant changes or enhancements, create issues to discuss and plan the changes. Transparent communication is essential for effective collaboration.

## Before You Contribute

Before you start contributing, it's important to understand how the program works. Follow these steps:

### Uploading Files

If you want to process a single file, please upload it to the appropriate folder:

- Text files should be placed in `test/txtFiles`.
- Markdown (md) files should be placed in `test/mdFiles`.
- TOML files should be placed in `test/tomlFiles`.

1. To process a file or a folder, you can use the following commands:

   - To process a file:

     ```bash
     python waypoint.py test.txt
     ```

     or

     ```bash
     python waypoint.py 1stmd.md
     ```

   - To process a folder:

     ```bash
     python waypoint.py test
     ```

2. To specify a different output directory, use one of these commands:

   ```bash
   python waypoint.py test.txt -o newDirectory
   ```

   or

   ```bash
   python waypoint.py test.md -o newDirectory
   ```

3. To provide a TOML-formatted config file when processing a file, use one of these commands:

   ```bash
   python waypoint.py version.txt -c config.toml
   ```

   or

   ```bash
   python waypoint.py version.txt -config config.toml
   ```

## Contributing

### Step 1: Clone the Repository

```bash
git clone https://github.com/rabroldan/Waypoint.git
```

### Step 2: Build the Project

Create a branch and start adding your contributions or other enhancements you want to include.

### Step 3: Testing

Continuously test to ensure that any updates or features added are running correctly.

### Step 4: Update README.md

Please make sure that the README.md is updated before committing the changes.

### Step 5: Pre-commit

#### Python Black

This project uses Python Black, which provides automatic style formatting following PEP8 guidelines, the default Python style guide.

Ensure Python is installed:

```bash
pip install black
```

To format the code:

```bash
black ./waypoint.py
```

#### Ruff Lint

Ruff is a Python linter and code formatter, similar to Black, and it is used alongside Black. It will defer implementing stylistic rules that are obviated by automated formatting.

Please ensure Ruff Linter is installed:

```bash
pip install ruff
```

To run Ruff:

```bash
ruff check .   # Lint all files in the current directory.
ruff format .  # Format all files in the current directory.
```

Please note that Black and Ruff Linter will also run automatically on save and A pre-commit hook is also installed to ensure the quality and consistency of the code and its formatting.

### Step 6: Commit Your Changes

Commit the changes and push to a branch.

### Step 7: Sending a Pull Request

Please ensure that the program is running correctly before sending a pull request. After a successful contribution, we can finally merge the changes.

# Thank you for your contribution!
