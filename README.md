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
6. CSS Style can be changed by pasting a css link.

# STEPS To RUN Waypoint

Waypoint will not run without specifying a folder or file as it requires a path. if the path does not exist it will create either the folder or the file. 
A series of questions would be asked in order to process a file and convert it from txt to html.

**Please ensure you have python isntalled**
*if not please downlaod* (https://www.python.org/downloads/)

## Creating  / Processing a File
If the file is already present then it will process the file from txt to html, otherwise it will create the file

1. Place this in the terminal to create a file
    ```python waypoint.py version.txt```

2.  If you want to try and process an example. there is a file titled test.txt. Just run this program
    ```python waypoint.py test.txt```

## Creating / Processing a folder

1. If the folder is already present then it will process the files from txt to html, otherwise it will create the folder and ask to create a single file
    ```python waypoint.py version```
   
2. If you want to try and process an example. there is a folder titled test that has multiple file. Just run this program
    ```python waypoint.py test```

## Changing CSS style

Once the question of pasting CSS link shows you can place this.
(https://www.w3schools.com/html/styles.css)
