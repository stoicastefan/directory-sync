import os
import shutil


class UpdateFiles:

    @staticmethod
    def copy_file(source_path, destination_path, file_name):
        print(file_name)

        UpdateFiles.delete_file_if_exists(destination_path + "/" + file_name)


        src_path = source_path + "/" + file_name
        dst_path = destination_path + "/" + file_name
        print(src_path + " VS " + dst_path)

        shutil.copy(src_path, dst_path)


    @staticmethod
    def copy_directory(source_dir, destination_dir):
        print(source_dir + " VS " + destination_dir)

        shutil.rmtree(destination_dir, ignore_errors=True)
        shutil.copytree(source_dir, destination_dir)

    @staticmethod
    def delete_file_if_exists(path_to_file):
        try:
            if os.path.exists(path_to_file):
                os.remove(path_to_file)
        except PermissionError:
            shutil.rmtree(path_to_file)

    @staticmethod
    def delete_list_of_files_from_the_same_directory(directory_path, files):
        for file in files:
            path_to_file = f"{directory_path}/{file.name}"
            UpdateFiles.delete_file_if_exists(path_to_file)


