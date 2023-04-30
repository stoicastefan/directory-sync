# Directory Synchronizer
Directory Synchronizer is a Python application that synchronizes two folders: a source folder and a replica folder. The program ensures that the replica folder maintains a full and identical copy of the source folder.

# Installation
Clone this repository to your local machine.

You need Python version 3.0 or higher .

# Usage
The application can be run from the command line using the following command:

python run_synchronizer.py --source_path SOURCE_FOLDER --target_path REPLICA_FOLDER --interval NUMBER_OF_SECONDS

Where SOURCE_FOLDER is the path to the source folder, REPLICA_FOLDER is the path to the replica folder and NUMBER_OF_SECONDS is the number of seconds between synchronizations.

# Excemple:
python run_synchronizer.py --source_path C:/Users/Stoica/Desktop/source --target_path C:/Users/Stoica/Desktop/replica --interval 7


The program will compare the contents of the two folders and copy any missing or modified files from the source folder to the replica folder. It will also delete any files in the replica folder that are not present in the source folder.

# Features
Synchronizes two folders, maintaining an identical copy of the source folder at the replica folder
Detects and copies new and modified files from the source folder to the replica folder
Deletes files in the replica folder that are not present in the source folder
Can be run from the command line with easy-to-use arguments


# Contact
If you have any questions or concerns about the Folder Synchronizer, please contact the maintainer at stoica.stefan14@yahoo.ro.
