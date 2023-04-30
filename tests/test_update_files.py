import os
import shutil
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from update_files import UpdateFiles
from scan_directory import ScanDirectory


class TestUpdateFiles(unittest.TestCase):

    def setUp(self):
        self.absolute_path = os.path.abspath(os.path.dirname(__file__))

    def test_copy_file_method(self):
        file_name = "test_file1.txt"

        source_dir = os.path.join(self.absolute_path, 'source')
        os.mkdir(source_dir)

        target_dir = os.path.join(self.absolute_path, 'target')
        os.mkdir(target_dir)

        open(os.path.join(source_dir, file_name), 'w').close()

        UpdateFiles.copy_file(source_dir, target_dir, file_name)
        source_directory_content = ScanDirectory.get_directory_content(source_dir)
        target_directory_content = ScanDirectory.get_directory_content(target_dir)

        expected_files = ['test_file1.txt']
        actual_files = [file.name for file in source_directory_content]
        self.assertCountEqual(expected_files, actual_files)

        actual_files = [file.name for file in target_directory_content]
        self.assertCountEqual(expected_files, actual_files)

    def test_copy_directory_method(self):
        source_dir = os.path.join(self.absolute_path, 'source')
        os.mkdir(source_dir)

        target_dir = os.path.join(self.absolute_path, 'target')
        os.mkdir(target_dir)

        inner_test_dir = os.path.join(source_dir, 'inner_test_dir')
        os.mkdir(inner_test_dir)
        target_dir_path = os.path.join(target_dir, 'inner_test_dir')

        UpdateFiles.copy_directory(inner_test_dir, target_dir_path)

        source_directory_content = ScanDirectory.get_directory_content(source_dir)
        target_directory_content = ScanDirectory.get_directory_content(target_dir)

        expected_files = ['inner_test_dir']
        actual_files = [file.name for file in source_directory_content]
        self.assertCountEqual(expected_files, actual_files)

        actual_files = [file.name for file in target_directory_content]
        self.assertCountEqual(expected_files, actual_files)

    def test_delete_existing_file(self):
        file_name = "test_file1.txt"

        test_dir = os.path.join(self.absolute_path, 'test_dir')
        os.mkdir(test_dir)

        open(os.path.join(test_dir, file_name), 'w').close()
        path_to_file = os.path.join(test_dir, file_name)

        UpdateFiles.delete_file_if_exists(path_to_file)

        test_dir_content = ScanDirectory.get_directory_content(test_dir)

        expected_files = []
        actual_files = [file.name for file in test_dir_content]
        self.assertCountEqual(expected_files, actual_files)

    def test_delete_not_existing_file(self):
        test_dir = os.path.join(self.absolute_path, 'test_dir')
        os.mkdir(test_dir)

        path_to_file = os.path.join(test_dir, "not_existing_file.test")

        UpdateFiles.delete_file_if_exists(path_to_file)

        test_dir_content = ScanDirectory.get_directory_content(test_dir)

        expected_files = []
        actual_files = [file.name for file in test_dir_content]
        self.assertCountEqual(expected_files, actual_files)

    def test_delete_list_of_files_from_the_same_dir(self):
        file_names = ["test_file1.txt", "test_file2.txt"]

        test_dir = os.path.join(self.absolute_path, 'test_dir')
        os.mkdir(test_dir)

        for file_name in file_names:
            open(os.path.join(test_dir, file_name), 'w').close()

        files = ScanDirectory.get_directory_content(test_dir)

        UpdateFiles.delete_list_of_files_from_the_same_directory(test_dir, files)

        test_dir_content = ScanDirectory.get_directory_content(test_dir)

        expected_files = []
        actual_files = [file.name for file in test_dir_content]
        self.assertCountEqual(expected_files, actual_files)

    def tearDown(self):
        test_dir = os.path.join(self.absolute_path, 'test_dir')
        source_dir = os.path.join(self.absolute_path, 'source')
        target_dir = os.path.join(self.absolute_path, 'target')

        if os.path.isdir(test_dir):
            shutil.rmtree(test_dir)

        if os.path.isdir(source_dir):
            shutil.rmtree(source_dir)

        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
