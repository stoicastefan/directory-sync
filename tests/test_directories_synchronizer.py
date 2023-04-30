import os
import shutil
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from directories_synchronizer import DirectoriesSynchronizer
from scan_directory import ScanDirectory


class TestDirectoriesSynchronizer(unittest.TestCase):
    def setUp(self):
        self.absolute_path = os.path.abspath(os.path.dirname(__file__))

        self.source_dir = os.path.join(self.absolute_path, 'source')
        os.mkdir(self.source_dir)

        self.target_dir = os.path.join(self.absolute_path, 'target')
        os.mkdir(self.target_dir)

    def test_compare_files_with_the_same_name(self):
        open(os.path.join(self.source_dir, "test_file.txt"), 'w').close()
        open(os.path.join(self.target_dir, "test_file.txt"), 'w').close()

        source_directory_content = ScanDirectory.get_directory_content(self.source_dir)
        target_directory_content = ScanDirectory.get_directory_content(self.target_dir)

        self.assertTrue(
            DirectoriesSynchronizer.check_if_files_have_the_same_name(
                source_directory_content[0],
                target_directory_content[0]
            )
        )



    def test_compare_files_with_different_name(self):
        open(os.path.join(self.source_dir, "test_file1.txt"), 'w').close()
        open(os.path.join(self.target_dir, "test_file2.txt"), 'w').close()

        source_directory_content = ScanDirectory.get_directory_content(self.source_dir)
        target_directory_content = ScanDirectory.get_directory_content(self.target_dir)

        self.assertFalse(
            DirectoriesSynchronizer.check_if_files_have_the_same_name(
                source_directory_content[0],
                target_directory_content[0]
            )
        )

    def test_compare_content_of_empty_files(self):
        open(os.path.join(self.source_dir, "test_file.txt"), 'w').close()
        open(os.path.join(self.target_dir, "test_file.txt"), 'w').close()

        source_directory_content = ScanDirectory.get_directory_content(self.source_dir)
        target_directory_content = ScanDirectory.get_directory_content(self.target_dir)

        self.assertTrue(
            DirectoriesSynchronizer.check_if_files_have_the_same_content(
                source_directory_content[0],
                target_directory_content[0]
            )
        )

    def test_compare_files_with_same_content(self):
        with open(os.path.join(self.source_dir, "test_file.txt"), 'w') as f:
            f.write("Some text")
            f.close()
        with open(os.path.join(self.target_dir, "test_file.txt"), 'w') as f:
            f.write("Some text")
            f.close()

        source_directory_content = ScanDirectory.get_directory_content(self.source_dir)
        target_directory_content = ScanDirectory.get_directory_content(self.target_dir)

        self.assertTrue(
            DirectoriesSynchronizer.check_if_files_have_the_same_content(
                source_directory_content[0],
                target_directory_content[0]
            )
        )

    def test_compare_files_with_different__content(self):
        with open(os.path.join(self.source_dir, "test_file.txt"), 'w') as f:
            f.write("Some text")
            f.close()
        with open(os.path.join(self.target_dir, "test_file.txt"), 'w') as f:
            f.write("Some text")
            f.close()

        source_directory_content = ScanDirectory.get_directory_content(self.source_dir)
        target_directory_content = ScanDirectory.get_directory_content(self.target_dir)

        self.assertTrue(
            DirectoriesSynchronizer.check_if_files_have_the_same_content(
                source_directory_content[0],
                target_directory_content[0]
            )
        )

    def tearDown(self):
        source_dir = os.path.join(self.absolute_path, 'source')
        target_dir = os.path.join(self.absolute_path, 'target')

        if os.path.isdir(source_dir):
            shutil.rmtree(source_dir)

        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
