#!/usr/bin/python3
import shutil
import os

while True:
  # set source and destination directories
  site = input('Site Directory: ')
  src_dir = f'/home/{site}/backup'
  dst_dir = "/home/backup"

  if os.path.exists(src_dir):
    for file_name in os.listdir(src_dir):
      # create full path of source file
      src_file = os.path.join(src_dir, file_name)
      # create full path of destination file
      dst_file = os.path.join(dst_dir, file_name)
      # move the file from source to destination directory
      shutil.move(src_file, dst_file)
      print("All files moved successfully!")
  else:
      print('Not a Valid Path')
