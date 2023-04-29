import hashlib
import os

from scan_directory import ScanDirectory
from update_files import UpdateFiles


class DirectoriesComparator:
    def __init__(self, source_path, target_path):
        self.source_path = source_path
        self.target_path = target_path
        self.source_dir_content = ScanDirectory.get_directory_content(self.source_path)
        self.target_dir_content = ScanDirectory.get_directory_content(self.target_path)
        self.different = []

    def compare_directories(self):
        for source_file in self.source_dir_content:
            is_source_file_in_target_file = False

            for target_file in self.target_dir_content:
                source_path = f"{self.source_path}/{source_file.name}"
                target_path = f"{self.target_path}/{target_file.name}"

                if self.check_if_files_have_the_same_name(source_file, target_file):
                    #print(source_path + " VS " + target_path)
                    if os.path.isdir(source_file) and os.path.isdir(target_file):
                        print("=====================")
                        print(source_path,"vs", target_path)

                        directory_comparator = (
                            DirectoriesComparator(
                                source_path,
                                target_path,

                            )
                        )
                        directory_comparator.compare_directories()

                    elif self.check_if_files_have_the_same_content(source_file, target_file):
                        self.target_dir_content.remove(target_file)
                        is_source_file_in_target_file = True


            if not is_source_file_in_target_file:
                if os.path.isdir(source_file):
                    print(source_path, target_path)
                    UpdateFiles.copy_directory(
                        source_path,
                        f"{self.target_path}/{source_file.name}",
                    )
                else:
                    UpdateFiles.copy_file(
                        self.source_path,
                        self.target_path,
                        source_file.name
                    )

        UpdateFiles.delete_list_of_files_from_the_same_directory(self.target_path, self.target_dir_content)



    @staticmethod
    def check_if_files_are_equivalent(file1, file2):
        if self.check_if_files_have_the_same_name(file1, file2):
            if self.check_if_files_have_the_same_content(file1, file2):
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
