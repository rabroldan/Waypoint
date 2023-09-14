import argparse
import os
import webbrowser

VERSION = "0.1"

def process_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(file_contents)

    user_input = input("Do you wish to Edit?  Y(Yes) or N(NO): ")

    if user_input == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):

        new_title=f"Waypoint Title"
        new_content = file_contents
        new_cssstyle = "https://www.w3schools.com/html/styles.css"

        editTitle = input('Do you want to edit title?  Y(Yes) or N(NO): ')

        if editTitle == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):

            new_title = input('What is the title?: ')
        
    


        html_newfile_path = file_path.replace('.txt', '.html')

        edit_content = input('Do you want to edit content? Y(Yes) or N(NO): ')

        if edit_content == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):

            new_content = input('What do you want to write?: ')
        

        edit_css = input('Do you want to edit style with css?Y(Yes) or N(NO): ')
        
        if edit_css == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):

            httml_css = input('Paste CSS link here: ')
            new_cssstyle = httml_css
        

        html_contents = write_text_to_html(new_content,new_title,new_cssstyle)

        with open(file_path, 'w') as txt_file:
            txt_file.write(new_content)

        with open(html_newfile_path, 'w') as html_file:
            html_file.write(html_contents)
        
        print(f"Text from '{file_path}' converted to HTML '{html_newfile_path}'.")


    else:
        print("Okay Bye!")

          

    html_file_path =  html_newfile_path


    webbrowser.open(html_file_path)

      




def write_text_to_html(new_content, new_title,new_cssstyle):

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href={new_cssstyle}>
  <title>{new_title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <p>{new_content}</p>
</body>
</html>"""
    return html_content



def process_folder(folder_path):
    # Process all .txt files in a folder
    for item in folder_path:
        print(item)

    openedfile = input("Which file do you want to open?: ")

    if not os.path.exists(openedfile):
        file_folder_creation(openedfile)

def file_folder_creation(input_path):
    print("Path does not exist")
    ccreate_directoru = input("Do You want to create a new folder then? Y(yes) N(no): ")
    
    if ccreate_directoru == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
        folder_title = input('What is the name of your folder?: ')
        x = os.makedirs(folder_title)

        create_afile = input("Do You want to create a new file then? Y(yes) N(no)")
        
        if create_afile == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
                create_afile = input('What is the name of your file?: ')
        else:
            return

    else:
        create_afile = input("Do You want to create a new file then? Y(yes) N(no)")
        
        if create_afile == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
                create_afile = input('What is the name of your file?: ')
        else:
            return

    while not create_afile.endswith(".txt"):
        create_afile = input('Please enter a file name ending with ".txt": ')



    xyz = open(input_path,'w')
    
    return True
                

def main():

    parsedobject = argparse.ArgumentParser(description="Waypoints to follow,  Please open README")

    # -version or -v flag 
    parsedobject.add_argument('--version', '-v', action='version', version=f'%(prog)s {VERSION}')

    parsedobject.add_argument('input', metavar='input', type=str, help='Specify the input file or folder path')

    args = parsedobject.parse_args()

    input_path = args.input

    # Add the input file or folder
   
        
    # If path does not exist
    if not os.path.exists(input_path):
        if input_path.endswith(".txt"):
            create_afile = input("Do You want to create a new file then? Y(yes) N(no): ")
        
            if create_afile == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
                create_afile = input('What is the name of your file?: ')

                z = open(input_path,'w')

            f = open(input_path,'w')
        else:
            bollean_rarr = file_folder_creation(input_path)

            if  bollean_rarr is True:
                process_file(input_path)
    



    # if the input is a file 
    if os.path.isfile(input_path):
        process_file(input_path)
    # if the input is a folder
    elif os.path.isdir(input_path):
        process_folder(input_path)
    else:
        print(f"Error: '{input_path}' is not a file or a folder.")

if __name__ == "__main__":
    main()

    answer = input("Do You want to process file again? Y(yes) N(no): ")
        
    if answer == ('y' or 'Y' or 'yes' or 'YES' or 'Yes' or 'yeS'):
            answer = main()

    else:
        print("GOOD BYE")
      
    
