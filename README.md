# Waypoint
Is a tool to create a journal with the use of a txt file, or even convert the file from text to html. Users can utilise this tool to record their ideas, encounters, and recollections in  text, making them easily accessible and compatible with a wide range of platforms and devices. By utilising the capabilities of Waypoint, improving their readability. The tool also allows you to create new Markdown files and offers features like italicised and bold text, horizontal rules, inline code blocks, and the convenience of configuring optional arguments through a TOML configuration file rather than command line arguments. It can also display the contents of the file in the terminal.

## Features

3. **Convert Text to HTML:** Process individual text files, whether they are in a folder or not, and convert their content to HTML format for improved readability.

6. **Specify Output Directory:** Provide users with the option to specify a custom output directory where HTML files will be saved. If the directory doesn't exist, create it automatically.

7. **Create Markdown Files:** Allow users to create new Markdown files for flexible and structured text formatting.

8. **Markdown Formatting Features:**
   - **Bold Text:** Support for formatting text as **bold**.
   - **Italicized Text:** Support for formatting text as *italicized*.
   - **Inline Code Blocks:** Enable users to include inline code with either single backticks (`) or triple backticks (```) and ensure proper code formatting.
   - **Horizontal Rules:** Offer support for horizontal rules to visually separate content sections in Markdown.

9. **Config File Support:** Provide users with the ability to specify optional arguments in a [TOML](https://toml.io/en/) configuration file instead of passing them as command line arguments this will print the TOML files in the terminal showing its contents

## To Run Waypoint
Waypoint uses the [tomllib](https://docs.python.org/3/library/tomllib.html) library, which was added to the Python Standard Library as of Python 3.11 via [PEP 680](https://peps.python.org/pep-0680/).

**Please ensure you have Python 3.11 or later installed.**

If not, please download it [here](https://www.python.org/downloads/).

## Installation
Download ZIP or clone Waypoint to your local computer

```
git clone https://github.com/rabroldan/Waypoint
```

or

```
you can download and select one of the packages https://github.com/rabroldan/Waypoint/releases/tag/v2.3
```
*If Downloaded by ZIP extract file*

Open with with your preferred code editor

## If you want to process a single file and please upload it to the properly folder

text files goes to = ```test/txtFiles```
md files goes to = ```test/mdFiles```
TOML files goes to = ```test/tomlFiles```

1. To process a file or a folder, you can try one of the following:

   - To process a file:
     ```
     python waypoint.py test.txt
     ```
     or
     ```
     python waypoint.py test.md
     ```

   - To process a folder:
     ```
     python waypoint.py test
     ```

  
2. To process To process a file or a folder to a different output try the following
  
    ```
     python waypoint.py test.txt -o newDirectory
     ```
     or
     ```
     python waypoint.py test.md -o newDirectory
     ```

3. To pass a TOML-formatted config file when processing a file try the following
      ```
      python waypoint.py version.txt -c config.toml
      ```
   or
      ```
      python waypoint.py version.txt -config config.toml
      ```


   
