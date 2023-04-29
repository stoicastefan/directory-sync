import hashlib
import os

from scan_directory import ScanDirectory
from update_files import UpdateFiles


class DirectoriesComparator:
    @staticmethod
    def compare_directories(source_path, target_path):
        source_dir_content = ScanDirectory.get_directory_content(source_path)
        target_dir_content = ScanDirectory.get_directory_content(target_path)

        for source_file in source_dir_content:
            is_source_file_present_in_target_file = False
            source_file_path = f"{source_path}/{source_file.name}"

            for target_file in target_dir_content:
                target_file_path = f"{target_path}/{target_file.name}"

                if DirectoriesComparator.check_if_files_have_the_same_name(source_file, target_file):
                    if os.path.isdir(source_file) and os.path.isdir(target_file):
                        DirectoriesComparator.compare_directories(source_file_path, target_file_path)
                        target_dir_content.remove(target_file)
                        is_source_file_present_in_target_file = True
                    elif DirectoriesComparator.check_if_files_have_the_same_content(source_file, target_file):
                        target_dir_content.remove(target_file)
                        is_source_file_present_in_target_file = True

            if not is_source_file_present_in_target_file:
                if os.path.isdir(source_file):
                    UpdateFiles.copy_directory(
                        source_file_path,
                        f"{target_path}/{source_file.name}",
                    )
                else:
                    UpdateFiles.copy_file(
                        source_path,
                        target_path,
                        source_file.name
                    )
        UpdateFiles.delete_list_of_files_from_the_same_directory(target_path, target_dir_content)

    @staticmethod
    def check_if_files_are_equivalent(file1, file2):
        if DirectoriesComparator.check_if_files_have_the_same_name(file1, file2):
            if DirectoriesComparator.check_if_files_have_the_same_content(file1, file2):
                return True
        return False

    @staticmethod
    def check_if_files_have_the_same_name(file1, file2):
        if file1.name == file2.name:
            return True
        return False

    @staticmethod
    def check_if_files_have_the_same_content(file1, file2):
        file1_hash = hashlib.md5(open(file1, 'rb').read()).hexdigest()
        file2_hash = hashlib.md5(open(file2, 'rb').read()).hexdigest()

        if file1_hash == file2_hash:
            return True
        return False
