import os
import time

from directories_synchronizer import DirectoriesSynchronizer
import argparse


class RunSynchronizer:
    @staticmethod
    def get_args_from_command_line():
        parser = argparse.ArgumentParser(description='Arguments for directory sync')

        parser.add_argument('-s', '--source_path', type=str, required=True, help='path to the source directory')
        parser.add_argument('-t', '--target_path', type=str, required=True, help='path to the target directory')
        parser.add_argument('-i', '--interval', type=int, default=3600,
                            help='interval in seconds to synchronize the directories')

        args = parser.parse_args()

        return args

    @staticmethod
    def start():
        args = RunSynchronizer.get_args_from_command_line()

        while True:
            if not os.path.isdir(args.source_path):
                print("Invalid source path.")
                break

            if not os.path.isdir(args.target_path):
                print("Invalid target path.")
                break

            DirectoriesSynchronizer.synchronize_directories(args.source_path, args.target_path)
            time.sleep(args.interval)


if __name__ == '__main__':
    RunSynchronizer.start()





