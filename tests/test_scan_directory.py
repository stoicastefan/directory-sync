import os
import shutil
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scan_directory import ScanDirectory


class TestScanDirectory(unittest.TestCase):

    def setUp(self):
        self.absolute_path = os.path.abspath(os.path.dirname(__file__))

    def test_get_directory_content_returns_files_in_directory(self):
        test_dir = os.path.join(self.absolute_path, 'test_dir')
        os.mkdir(test_dir)

        open(os.path.join(test_dir, 'test_file1.txt'), 'w').close()
        open(os.path.join(test_dir, 'test_file2.txt'), 'w').close()
        inner_test_dir = os.path.join(test_dir, 'inner_test_dir')
        os.mkdir(inner_test_dir)

        directory_content = ScanDirectory.get_directory_content(test_dir)

        expected_files = ['test_file1.txt', 'test_file2.txt', 'inner_test_dir']
        actual_files = [file.name for file in directory_content]
        self.assertCountEqual(expected_files, actual_files)

    def test_get_directory_content_returns_no_files_in_empty_directory(self):
        empty_dir = os.path.join(self.absolute_path, 'test_dir')
        os.mkdir(empty_dir)

        directory_content = ScanDirectory.get_directory_content(empty_dir)

        self.assertEqual(0, len(directory_content))

    def tearDown(self):
        test_dir = os.path.join(self.absolute_path, 'test_dir')
        if os.path.isdir(test_dir):
            shutil.rmtree(test_dir)


if __name__ == '__main__':
    unittest.main()
