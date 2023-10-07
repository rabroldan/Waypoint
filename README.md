# Waypoint
Is a tool to create a journal with the use of a txt file, or even convert the file from text to html. Users can utilise this tool to record their ideas, encounters, and recollections in  text, making them easily accessible and compatible with a wide range of platforms and devices. By utilising the capabilities of Waypoint, people may concentrate on the substance of their journal entries without being distracted by difficult formatting, which streamlines and improves the journaling process.


## Installation
Download ZIP or clone Waypoint to your local computer
*If Downloaded by ZIP extract file*

Open with with your preferred code editor

## Features

3. **Convert Text to HTML:** Process individual text files, whether they are in a folder or not, and convert their content to HTML format for improved readability.

6. **Specify Output Directory:** Provide users with the option to specify a custom output directory where HTML files will be saved. If the directory doesn't exist, create it automatically.

7. **Create Markdown Files:** Allow users to create new Markdown files for flexible and structured text formatting.

8. **Markdown Formatting Features:**
   - **Bold Text:** Support for formatting text as **bold**.
   - **Italicized Text:** Support for formatting text as *italicized*.
   - **Inline Code Blocks:** Enable users to include inline code with either single backticks (`) or triple backticks (```) and ensure proper code formatting.
   - **Horizontal Rules:** Offer support for horizontal rules to visually separate content sections in Markdown.

9. **Config File Support:** Provide users with the ability to specify optional arguments in a [TOML](https://toml.io/en/) configuration file instead of passing them as command line arguments

## To Run Waypoint

**Please ensure you have Python installed.**

If not, please download it [here](https://www.python.org/downloads/).

1. To process a file or a folder, you can try one of the following:

   - To process a file:
     ```
     python waypoint.txt version.txt
     ```
     or
     ```
     python waypoint.py version.md
     ```

   - To process a folder:
     ```
     python waypoint.txt version
     ```

  
2. If you want to try one of the examples:

   - To process the file for the example:
     ```
     python waypoint.txt test.txt
     ```

   - To process the folder for the example:
     ```
     python waypoint.txt test
     ```
3. To process To process a file or a folder to a different output try the following
  
    ```
     python waypoint.py version.txt -o newDirectory
     ```
     or
     ```
     python waypoint.py version.md -o newDirectory
     ```
4. To pass a TOML-formatted config file when processing a file try the following
      ```
      python waypoint.py version.txt -c config.toml
      ```
   or
      ```
      python waypoint.py version.txt -config config.toml
      ```
   
