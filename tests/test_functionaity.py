import os
import shutil
import sys
import time
import unittest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from directories_synchronizer import DirectoriesSynchronizer
from scan_directory import ScanDirectory


class TestFunctionality(unittest.TestCase):
    def setUp(self):
        self.absolute_path = os.path.abspath(os.path.dirname(__file__))

        self.source_dir = os.path.join(self.absolute_path, 'source')
        os.mkdir(self.source_dir)

        self.target_dir = os.path.join(self.absolute_path, 'target')
        os.mkdir(self.target_dir)

    def test_general_functionality(self):
        # Add content to source directory
        with open(os.path.join(self.source_dir, "test_file1.txt"), 'w') as f:
            f.write("Hello from source")

        inner_source_dir = os.path.join(self.source_dir, 'inner_source_dir')
        os.mkdir(inner_source_dir)

        with open(os.path.join(inner_source_dir, "test_file2.txt"), 'w') as f:
            f.write("Hello from source inner directory")

        # Add content to target directory
        with open(os.path.join(self.target_dir, "test_file3.txt"), 'w') as f:
            f.write("Hello from target")

        inner_target_dir = os.path.join(self.target_dir, 'inner_target_dir')
        os.mkdir(inner_target_dir)

        time.sleep(5)
        DirectoriesSynchronizer.synchronize_directories(self.source_dir, self.target_dir)
        time.sleep(5)

        source_directory_content = ScanDirectory.get_directory_content(self.source_dir)
        target_directory_content = ScanDirectory.get_directory_content(self.target_dir)

        # Compare elements
        for source_file in source_directory_content:
            for target_file in target_directory_content:
                if os.path.isdir(source_file) and os.path.isdir(target_file):
                    self.check_if_inner_directories_match(source_file, target_file)
                    target_directory_content.remove(target_file)
                have_same_content = DirectoriesSynchronizer.check_if_files_have_the_same_name(
                    source_file,
                    target_file
                )

                self.assertTrue(have_same_content)

    def check_if_inner_directories_match(self, inner_source_dir, inner_target_dir):
        inner_source_dir_content = ScanDirectory.get_directory_content(inner_source_dir)
        inner_target_dir_content = ScanDirectory.get_directory_content(inner_target_dir)

        self.assertEqual(inner_source_dir.name, inner_target_dir.name)
        self.assertEqual(len(inner_source_dir_content), 1)
        self.assertEqual(len(inner_target_dir_content), 1)

        have_same_content = DirectoriesSynchronizer.check_if_files_have_the_same_name(
            inner_source_dir_content[0],
            inner_target_dir_content[0]
        )

        self.assertTrue(have_same_content)
