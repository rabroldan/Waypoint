# Waypoint
Is a tool to create a journal with the use of a txt file, or even convert the file from text to html. Users can utilise this tool to record their ideas, encounters, and recollections in  text, making them easily accessible and compatible with a wide range of platforms and devices. By utilising the capabilities of Waypoint, people may concentrate on the substance of their journal entries without being distracted by difficult formatting, which streamlines and improves the journaling process.


## Installation
Download ZIP or clone Waypoint to your local computer
*If Downloaded by ZIP extract file*

Open with with your preferred code editor

## Features

1. Create a Text File.
2. Create a Folder for Text File to be stored.
3. Process a Text file, with in a folder or not and convert it from text to html.
4. Change The title of the document.
5. Add an Entry within the document.
6. Add a Option to output directory
7. Create a markdown file 
8. Convert a markdown file to a HTML file

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


