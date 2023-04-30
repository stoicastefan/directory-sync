import os


class ScanDirectory:

    @staticmethod
    def get_directory_content(directory):
        files = []

        all_files = os.scandir(directory)
        for file in all_files:
            files.append(file)

        return files



