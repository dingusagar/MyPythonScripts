import os
import glob
import shutil
import argparse


def moveFileToDir(file,dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    shutil.move(file,dir)

path = os.curdir
files = glob.glob('*.mp4')
# print(files)



for file in files:
    print(file)
    date = file.split('_')[1]
    print(date)
    moveFileToDir(file,date)