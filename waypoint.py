# testing testing
import os
import sys
import tomllib

VERSION = "2"  # current version of the tool


def process_folder(folder_path):
    # Process all .txt files in a folder
    items = os.listdir(folder_path)

    new_title = f"Waypoint Title"

    filestxt = "test/txtFiles"
    process_file(filestxt, new_title, 1)

    filesmd = "test/mdFiles"
    process_file(filesmd, new_title, 1)


def process_file(
    file_path, title=None, number=None, output=None
):  # process the file from txt to HTML
    if file_path.endswith(".txt"):
        files = "test/txtFiles"

    if file_path.endswith(".md"):
        files = "test/mdFiles"

    else:
        if file_path == "test/txtFiles":
            files = "test/txtFiles"
        if file_path == "test/mdFiles":
            files = "test/mdFiles"

    if number is None:
        new_file_path = os.path.join(files, file_path)

        with open(new_file_path, "r") as file:
            file_contents = file.read()

        if title is None:
            new_title = os.path.splitext(file_path)[0]
        else:
            new_title = title

        new_content = file_contents
        html_newfile_path = ""
        html_contents = ""
        ## Markdown support changing new filename based on what type of file is it

        if is_markdown(file_path):
            html_newfile_path = file_path.replace(".md", ".html")
        else:
            html_newfile_path = file_path.replace(".txt", ".html")

        ## Markdown support: changing which function gets called for each different filetype

        if output is not None:
            outputdirect = output
        else:
            outputdirect = "outputFolder"

        if not os.path.exists(outputdirect):
            os.makedirs(outputdirect)
            new_file_path = os.path.join(outputdirect, html_newfile_path)
        else:
            new_file_path = os.path.join(outputdirect, html_newfile_path)

        if is_markdown(file_path):
            html_contents = write_markdown_to_html(new_content, new_title)
        else:
            html_contents = write_text_to_html(new_content, new_title)

        with open(
            new_file_path, "w"
        ) as html_file:  # this will write the contents to the new html file
            html_file.write(html_contents)

    else:
        filesdirec = os.listdir(files)

        for item in filesdirec:
            process_file(item)


# this provides the layout of the html with an editable title, content and css style
def write_text_to_html(
    new_content,
    new_title,
):
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

    process_file(file_path, output=outputpath)


# Markdown support functions here:
#
# Similiar to the text variant this function writes converts the markdown into HTML with some of the included features (headings, bolding, italics)
# Interacts similar to text
def write_markdown_to_html(
    new_content,
    new_title,
):
    # Markdown conversion
    converted_md = ""
    lines = (
        new_content.splitlines()
    )  # Spliting each line of the new_content into a list

    i = 0
    for curr_line in lines:  # Going through each line
        if "#" in curr_line:  # Checking for titles
            if curr_line.startswith("###"):
                curr_line = "<h3>" + curr_line.lstrip("#") + "</h3>\n"
            elif curr_line.startswith("##"):
                curr_line = "<h2>" + curr_line.lstrip("#") + "</h2>\n"
            else:
                curr_line = "<h1>" + curr_line.lstrip("#") + "</h1>\n"

        elif "`" in curr_line:  # Checking for titles
            if curr_line.startswith("```") and curr_line.endswith("```"):
                curr_line = "<code>" + curr_line.strip("`") + "</code>\n\n"
            elif curr_line.startswith("`") and curr_line.endswith("`"):
                curr_line = "<code>" + curr_line.strip("`") + "</code>\n\n"
            else:
                curr_line = "<p>" + curr_line + "</p>\n"

        elif "-" in curr_line:  # Checking for titles
            if curr_line.startswith("---"):
                curr_line = "<hr> \n"
            else:
                curr_line = "</br>"

        elif "*" in curr_line:  # Checking for bold or itialized text
            if curr_line.startswith("**") and curr_line.endswith("**"):
                curr_line = "<b>" + curr_line.strip("*") + "</b><br/>\n"
            elif curr_line.startswith("*") and curr_line.endswith("*"):
                curr_line = "<i>" + curr_line.strip("*") + "</i><br/>\n"
            else:
                curr_line = "<p>" + curr_line + "</p>\n"
        elif len(curr_line) > 0:  # Checking for regular text
            curr_line = "<p>" + curr_line + "</p>\n"
        else:
            curr_line = "\n"  # Ignoring spaces

        converted_md += curr_line  # adding change to final conversion

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
    return ".md" in file_name


def parse_TOML(config_file):
    # parses input TOML-formatted config file
    with open(config_file, "rb") as f:
        try:
            data: dict = tomllib.load(f)
            return data
        except tomllib.TOMLDecodeError:
            print("TOML FILE COULD NOT BE PARSED. PLEASE CHECK THE FORMAT")


def set_config():
    # Parse config file, override all other flags
    print("checking for toml file")
    # store config string argument
    config = "-c" if ("-c" in sys.argv) else "-config"
    # store config string's index location in sys.argv
    config_index = sys.argv.index(config)
    # config file path immediately follows -c or -config flag (config file will exist in sys.argv[config_index+1])
    if len(sys.argv) == config_index + 1:  # if no argument follows config flag
        print("NO CONFIG FILE PROVIDED")
    elif not sys.argv[config_index + 1].endswith(
        ".toml"
    ):  # if directory or non-TOML file is provided
        print("PLEASE PROVIDE A TOML FILE")

    elif sys.argv[config_index + 1].endswith(".toml"):
        files = "test/tomlFiles"

        file_met = sys.argv[config_index + 1]

        file_path = os.path.join(files, file_met)

        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                file_contents = file.read()
            # will display toml files in the screen
            print(file_contents)
        else:
            print("TOML FILE NOT IN THE RIGHT FOLDER")


def main():  # this is the main function
    if len(sys.argv) > 1:
        if ("-c" in sys.argv) or (
            "-config" in sys.argv
        ):  # check for -c or -config flags
            set_config()
        elif sys.argv[1] == "-h" or sys.argv[1] == "-help":
            # Display help message
            print("Help message goes here.")
        elif sys.argv[1] == "-v" or sys.argv[1] == "-version":
            # Display version
            print("Version: 1.0")  # Replace with your actual version

        elif len(sys.argv) == 2:
            if sys.argv[1].endswith(".txt"):
                input_path = sys.argv[1]
                process_file(input_path)

            elif sys.argv[1].endswith(".md"):
                input_path = sys.argv[1]
                process_file(input_path)

            else:
                input_path = sys.argv[1]
                process_folder(input_path)

        elif (
            sys.argv[2] == "-o"
            or sys.argv[2] == "-O"
            or sys.argv[2] == "-output"
            or sys.argv[2] == "-Output"
        ):
            input_path = sys.argv[1]
            output_folder = sys.argv[3]
            outputToDir(input_path, output_folder)

        else:
            print("Invalid argument provided!")
    else:
        print("Invalid argument provided!")
        print("Use --help or -h flag for more info")


if __name__ == "__main__":  # this starts the main program
    check = main()  # this begins with a argument of either a file or a

    if check == True:
        print("Files has been processed GOOD BYE")
    elif check == False:
        print(
            "Files has Not been processed, please create the file / document before converting. GOOD BYE"
        )
