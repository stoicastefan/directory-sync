import os
import shutil
from logger import Logger


class UpdateFiles:

    @staticmethod
    def create_log(message):
        logger = Logger()
        logger.create_info_log(message)

    @staticmethod
    def copy_file(source_path, destination_path, file_name):
        message = f"Copy file {source_path}/{file_name} to {destination_path}/{file_name}"
        UpdateFiles.create_log(message)

        UpdateFiles.delete_file_if_exists(destination_path + "/" + file_name)

        src_path = source_path + "/" + file_name
        dst_path = destination_path + "/" + file_name

        shutil.copy(src_path, dst_path)

    @staticmethod
    def copy_directory(source_dir, destination_dir):
        message = f"Copy directory {source_dir} to {destination_dir}"
        UpdateFiles.create_log(message)

        shutil.rmtree(destination_dir, ignore_errors=True)
        shutil.copytree(source_dir, destination_dir)

    @staticmethod
    def delete_file_if_exists(path_to_file):
        try:
            if os.path.exists(path_to_file):
                os.remove(path_to_file)

                message = f"Delete file {path_to_file}"
                UpdateFiles.create_log(message)
        except PermissionError:
            shutil.rmtree(path_to_file)

    @staticmethod
    def delete_list_of_files_from_the_same_directory(directory_path, files):
        for file in files:
            path_to_file = f"{directory_path}/{file.name}"
            UpdateFiles.delete_file_if_exists(path_to_file)
