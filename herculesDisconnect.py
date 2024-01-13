
import shutil 
import os 
import sys 
import filecmp
import time
from playsound import playsound

#E

def fileCopy(src, dst):
    try:
        shutil.copyfile(src, dst)
       
    except:
        print("sadness")


def alarm():
    playsound('C:\Users\Owner\Downloads\imperial march.mp3')
    

src = "C:\Users\Owner\Documents\longtermrun.csv"
dst = "C:\Users\Owner\Documents\longtermrunBackup.csv"

while True:
    
    time.sleep(1)

    if not filecmp.cmp(src, dst):
        fileCopy(src, dst)

    else: 
        alarm()


