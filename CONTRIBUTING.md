# Contributing

First and foremost, thank you for considering contributing to Waypoint.

Please follow these guidelines to ensure a smooth and collaborative contribution process.

## What Can I Contribute?

Waypoint is a tool for creating a journal using a text file or even converting the text to HTML. When contributing, you can consider the following:

- Enhancing the program's functionality.
- Helping with existing issues or creating new ones.
- Sharing your ideas and suggestions.
- Reporting any bugs you encounter.
- Improving documentation, including incomplete or missing sections.

## Responsibilities

When contributing, please ensure that your code runs correctly. If you plan to make significant changes or enhancements, create issues to discuss and plan the changes. Transparent communication is essential for effective collaboration.

## Before You Contribute

Before you start contributing, it's important to understand how the program works. Follow these steps:

### Uploading Files

If you want to process a single file, please upload it to the appropriate folder:

- Text files should be placed in `test/txtFiles`.
- Markdown (md) files should be placed in `test/mdFiles`.
- TOML files should be placed in `test/tomlFiles`.

1. To process a file or a folder, you can use the following commands:

   - To process a file:

     ```
     python waypoint.py test.txt
     ```

     or

     ```
     python waypoint.py 1stmd.md
     ```

   - To process a folder:

     ```
     python waypoint.py test
     ```

2. To specify a different output directory, use one of these commands:

   ```
   python waypoint.py test.txt -o newDirectory
   ```

   or

   ```
   python waypoint.py test.md -o newDirectory
   ```

3. To provide a TOML-formatted config file when processing a file, use one of these commands:

   ```
   python waypoint.py version.txt -c config.toml
   ```

   or

   ```
   python waypoint.py version.txt -config config.toml
   ```

## Contributing

### Step 1: Clone the Repository

```
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

```
pip install black
```

To format the code:

```
black ./waypoint.py
```

#### Ruff Lint

Ruff is a Python linter and code formatter, similar to Black, and it is used alongside Black. It will defer implementing stylistic rules that are obviated by automated formatting.

Please ensure Ruff Linter is installed:

```
pip install ruff
```

To run Ruff:

```
ruff check .   # Lint all files in the current directory.
ruff format .  # Format all files in the current directory.
```

Please note that Black and Ruff Linter will also run automatically on save, and a pre-commit hook is installed to ensure the quality and consistency of the code and its formatting.

### Testing

To run a single test for a function, use the following code:

```
python -m unittest discover -k [name of the function]
```

For example:

```
python -m unittest discover -k test_config
```

Or, if you want to test the entire module, use:

```
nose2
```
Or, if you want to test a the single function you can use


```
python -m unittest discover -k "test_txt" # To test a string
python -m unittest discover -k "test_txtfile" # To test a txt file
python -m unittest discover -k "test_tomlfile" # To test a toml file
python -m unittest discover -k "test_folder" # To test a folder file
```

Code Coverage Analysis

You can also use code coverage analysis to ensure all tests are done which in this case is 9 tests, you can use the following.

```
coverage run -m unittest discover
```

### For the sake of testing I added a testunit that will fail "test_tofail" please ignore if this is the only fail in the testing

Please ensure you have the right name inside the quotation mark to ensure that you will run the test properly.

### Step 6: Commit Your Changes

Commit the changes and push to a branch.

### Step 7: Sending a Pull Request

Please ensure that the program is running correctly before sending a pull request. After a successful contribution, we can finally merge the changes.

# Thank you for your contribution!
