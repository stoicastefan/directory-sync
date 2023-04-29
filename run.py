import os
import time

from directories_comparator import DirectoriesComparator
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for directory sync')

    parser.add_argument('-s', '--source_path', type=str, required=True, help='path to the source directory')
    parser.add_argument('-t', '--target_path', type=str, required=True, help='path to the target directory')
    parser.add_argument('-i', '--interval', type=int, default=3600, help='interval in seconds to synchronize the directories')

    args = parser.parse_args()

    #source_path = "C:/Users/Stoica/Desktop/source"
    #target_path = "C:/Users/Stoica/Desktop/replica"
    while True:
        if not os.path.isdir(args.source_path):
            print("Invalid source path.")
            break

        if not os.path.isdir(args.target_path):
            print("Invalid target path.")
            break
        DirectoriesComparator.compare_directories(args.source_path, args.target_path)
        time.sleep(args.interval)



