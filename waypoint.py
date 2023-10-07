
import os
import sys
import tomli
VERSION = "2" # current version of the tool

def process_folder(folder_path):
    # Process all .txt files in a folder
    items = os.listdir(folder_path)
    new_title=f"Waypoint Title"
    
    
    if not items:
        print("The folder is empty.")
        

    print("Items in the folder:")
    for i, item in enumerate(items, start=1):
        if item.endswith(".txt") or item.endswith(".md"):
            print(f"{i}. {item}")

        ## Markdown support: Allows for .md files in directories to work
        if item.endswith(".txt") or item.endswith(".md"):
            # Create the new HTML file name
            newfile = os.path.splitext(item)[0] + ".html"

            # Read the content from the txt file
            with open(os.path.join(folder_path, item), 'r') as file:
                file_contents = file.read()

            ## Markdown support: Adding different writing methods for each different type of file
            if is_markdown(item):
                new_file = write_markdown_to_html(file_contents, new_title, )
            else:
                new_file = write_text_to_html(file_contents, new_title, )

            # Write the content to the html file
            with open(os.path.join(folder_path, newfile), 'w') as html_file:
                html_file.write(new_file)

            




def process_file(file_path): # process the file from txt to HTML
    with open(file_path, 'r') as file: # this opens the file inorder and 
        file_contents = file.read()
    
        
        new_title=os.path.splitext(file_path)[0] 

        new_content = file_contents
         

        ## Markdown support changing new filename based on what type of file is it
        html_newfile_path = ""
        if is_markdown(file_path):
            html_newfile_path = file_path.replace('.md', '.html')
        else: 
            html_newfile_path = file_path.replace('.txt', '.html')

        ## Markdown support: changing which function gets called for each different filetype
        html_contents = ""
        if is_markdown(file_path):
            html_contents = write_markdown_to_html(new_content,new_title, )
        else:
            html_contents = write_text_to_html(new_content,new_title, )

        with open(html_newfile_path, 'w') as html_file: # this will write the contents to the new html file
            html_file.write(html_contents)
        
        print(f"Text from '{file_path}' converted to HTML '{html_newfile_path}'.")



        print("Okay Bye!")

# this provides the layout of the html with an editable title, content and css style
def write_text_to_html(new_content, new_title, ): 

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
 

  <title>{new_title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <p>{new_content}</p>
</body>
</html>"""
    return html_content


def outputToDir(file_path, outputpath):
    # Create the output folder if it doesn't exist
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)

    with open(file_path, 'r') as file:
        file_contents = file.read()

        # Define the output file path within the output folder
        output_file_name = os.path.basename(file_path)  # Get the file name without the path
        output_file_name_without_extension, _ = os.path.splitext(output_file_name)
        output_html_file_name = f"{output_file_name_without_extension}.html"
        output_html_path = os.path.join(outputpath, output_html_file_name)

        new_title = output_file_name_without_extension  # You can customize this as needed
        new_content = file_contents
         

        ## Markdown support: changing which function gets called for each different filetype
        html_contents = ""
        if is_markdown(file_path):
            html_contents = write_markdown_to_html(new_content, new_title  )
        else:
            html_contents = write_text_to_html(new_content, new_title  )

        with open(output_html_path, 'w') as html_file:
            html_file.write(html_contents)

        print(f"Text from '{file_path}' converted to HTML and saved as '{output_html_path}'.")

# Markdown support functions here:
#
# Similiar to the text variant this function writes converts the markdown into HTML with some of the included features (headings, bolding, italics)
# Interacts similar to text
def write_markdown_to_html(new_content, new_title, ):
    
    # Markdown conversion
    converted_md = ""
    lines = new_content.splitlines()    # Spliting each line of the new_content into a list


    i = 0
    for  curr_line in lines:        # Going through each line
       
        if '#' in curr_line:                        # Checking for titles
            if curr_line.startswith("###"):
                curr_line = "<h3>" + curr_line.lstrip('#') + "</h3>\n"
            elif curr_line.startswith("##"):                             
                curr_line = "<h2>" + curr_line.lstrip('#') + "</h2>\n"
            else:
                curr_line = "<h1>" + curr_line.lstrip('#') + "</h1>\n"

        elif '`' in curr_line:                        # Checking for titles
            if curr_line.startswith("```") and curr_line.endswith("```"):
                curr_line = "<code>" + curr_line.strip('`') + "</code>\n\n"
            elif curr_line.startswith("`") and curr_line.endswith("`"):                             
                 curr_line = "<code>" + curr_line.strip('`') + "</code>\n\n"
            else:
                curr_line = "<p>" + curr_line + "</p>\n"

        elif '-' in curr_line:                        # Checking for titles
            if curr_line.startswith("---") :
                curr_line = '<hr> \n'
            else:
                curr_line = '</br>'

        elif '*' in curr_line:                                              # Checking for bold or itialized text
            if curr_line.startswith('**') and curr_line.endswith('**'):
                curr_line = "<b>" + curr_line.strip('*') + "</b><br/>\n"
            elif curr_line.startswith('*') and curr_line.endswith("*"):
                curr_line = "<i>" + curr_line.strip('*') + "</i><br/>\n"
            else:
                curr_line = "<p>" + curr_line + "</p>\n"
        elif len(curr_line) > 0:                                     # Checking for regular text
            curr_line = "<p>" + curr_line + "</p>\n"     
        else:
            curr_line = '\n'       # Ignoring spaces

        converted_md += curr_line       # adding change to final conversion

    # Creating HTML file contents
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{new_title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  {converted_md}                                                    
</body>
</html>"""
    return html_content

def is_markdown(file_name):
    return (".md" in  file_name)

def parse_TOML(config_file):
    # parses input TOML-formatted config file
    with open(config_file, 'rb') as f:
        data:dict = tomli.load(f)
        return data
    
def main(): # this is the main function
    if len(sys.argv) > 1:
        if ('-c' in sys.argv) or ('-config' in sys.argv): # check for -c or -config flags
            # Parse config file, override all other flags
            print("checking for toml file")
        elif sys.argv[1] == '-h' or sys.argv[1] == '-help':
            # Display help message
            print("Help message goes here.")
        elif sys.argv[1] == '-v' or sys.argv[1] == '-version':
            # Display version
            print("Version: 1.0")  # Replace with your actual version
        elif len(sys.argv) == 2:
            input_path = sys.argv[1]

            if not os.path.exists(input_path):
                print("FILE/DOCUMENT DOES NOT EXIST")
            elif os.path.isfile(input_path):
                process_file(input_path)
            elif os.path.isdir(input_path):
                process_folder(input_path)
            else:
                print(f"Error: '{input_path}' is not a file or a folder.")
        elif sys.argv[2] == '-o' or sys.argv[2] == '-O' or sys.argv[2] == '-output' or sys.argv[2] == '-Output':
            input_path = sys.argv[1]
            output_folder  = sys.argv[3]
            outputToDir(input_path, output_folder )


        else:
            print("Invalid argument provided!")
    else:
        print('Invalid argument provided!')
        print('Use --help or -h flag for more info')

         




if __name__ == "__main__": # this starts the main program

    check = main() # this begins with a argument of either a file or a

    if check == True:
        print("Files has been processed GOOD BYE")
    elif check == False:
        print("Files has Not been processed, please create the file / document before converting. GOOD BYE")

        


    
    
