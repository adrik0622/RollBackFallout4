#!/usr/bin/python3
# Simple script that automates roll backs for fallout4
import os
import shutil
import logging

# Set up logging
logging.basicConfig(filename='/home/adrikingston/tools/RollBackFallout4/logs/rollback.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the source and destination directories
source_dir = "/home/adrikingston/.steam/debian-installation/ubuntu12_32/steamapps/content/app_377160"
dest_dir = "/home/adrikingston/.steam/debian-installation/steamapps/common/Fallout 4"
backup_dir = "/home/adrikingston/tools/RollBackFallout4/backups"

def merge_directories(src, dst):
    for dirpath, dirnames, filenames in os.walk(src):
        rel_path = os.path.relpath(dirpath, src)
        dest_path = os.path.join(dst, rel_path)
        os.makedirs(dest_path, exist_ok=True)

        for file in filenames:
            src_file = os.path.join(dirpath, file)
            dest_file = os.path.join(dest_path, file)

            if os.path.isfile(dest_file):
                logging.info(f"Overwriting: {dest_file}")
            else:
                logging.info(f"Copying: {dest_file}")

            shutil.copy2(src_file, dest_file)

def move_specific_files(dst, backup_dst):
    data_dir = os.path.join(dst, "Data")
    if os.path.exists(data_dir):
        for file in os.listdir(data_dir):
            if file.startswith("ccBG"):
                src_file = os.path.join(data_dir, file)
                dest_file = os.path.join(backup_dst, file)
                shutil.move(src_file, dest_file)
                logging.info(f"Moved {src_file} to {dest_file}")

# Start merging the directories
merge_directories(source_dir, dest_dir)
move_specific_files(dest_dir, backup_dir)
logging.info("Merge and backup complete!")

