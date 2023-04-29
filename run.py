from directories_comparator import DirectoriesComparator
from scan_directory import ScanDirectory

from update_files import UpdateFiles

if __name__ == '__main__':
    source_path = "C:/Users/Stoica/Desktop/source"
    target_path = "C:/Users/Stoica/Desktop/replica"
    source_files = ScanDirectory.get_directory_content(source_path)
    replica_files = ScanDirectory.get_directory_content(target_path)

    directory_comparator = DirectoriesComparator(source_path, target_path)
    directory_comparator.compare_directories()



