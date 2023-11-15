import unittest
from waypoint import process_text, process_file, set_config
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

    def test_tofail(self):
        # This is used for failing a test comment it out if need be
        argv = "-x"
        self.assertTrue(argtest(argv))


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


if __name__ == "__main":
    unittest.main()
