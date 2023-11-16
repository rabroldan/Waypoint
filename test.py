import tempfile
import unittest
from waypoint import process_text, process_file, set_config, write_markdown_to_html
from testing import argtest


class TestSum(unittest.TestCase):
    def test_help(self):
        argh = "-h"
        self.assertTrue(argtest(argh))

    def test_version(self):
        argv = "-v"
        self.assertTrue(argtest(argv))

    def test_config(self):
        argc = "-c"
        self.assertTrue(argtest(argc))


class Testtext(unittest.TestCase):
    def test_txt(self):  # Corrected method name
        self.assertTrue(
            process_text(
                "This is to test the program to work calling in a function from main called process_text. with this we can ensure that the program is working properly and the test units are working properly with a simple texts"
            )
        )

    # this is to test txt files
    def test_txtfile(self):
        file_path = "testtxt.txt"
        self.assertTrue(process_file(file_path))

    # this is to test md files
    def test_mdfile(self):
        file_path = "testmd.md"
        self.assertTrue(process_file(file_path))

    # this is to test toml files
    def test_tomlfile(self):
        file_path = "test.toml"
        self.assertTrue(set_config(file_path))

    # this is to test folders files
    def test_folder(self):
        file_path = "test/txtFiles"
        self.assertTrue(process_file(file_path, number=1))

class TestMdConversion(unittest.TestCase):
    def setUp(self):

        self.input = ("**Hello World**\n"
                      "*Hello*\n"
                      "`This is a code line`\n"
                      "```This is another code line, but with 3 backticks```\n"
                      "### This is a h3 tag\n"
                      "## This is a h2 tag\n"
                      "# This is a h1 tag\n\n"
                      "---")

    def test_convert_md(self):
        html_contents = write_markdown_to_html(self.input, "file1")

        self.expected_output = (
            f"<!DOCTYPE html>\n"
            f'<html lang="en">\n'
            f"<head>\n"
            f'  <meta charset="utf-8">\n'
            f"  <title>file1</title>\n"
            f'  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f"</head>\n"
            f"<body>\n"
            f"  <b>Hello World</b><br/>\n"
            f"<i>Hello</i><br/>\n"
            f"<code>This is a code line</code>\n\n"
            f"<code>This is another code line, but with 3 backticks</code>\n\n"
            f"<h3> This is a h3 tag</h3>\n"
            f"<h2> This is a h2 tag</h2>\n"
            f"<h1> This is a h1 tag</h1>\n\n"
            f"<hr> \n                                                    \n" # Had to add the white spaces as the program would add it
            f"</body>\n"
            f"</html>"
        )

        self.assertEqual(html_contents, self.expected_output)

if __name__ == "__main":
    unittest.main()
