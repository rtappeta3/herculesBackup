
import shutil 
import os 
import sys 
import filecmp
import time
from playsound import playsound



def fileCopy(src, dst):
    try:
        shutil.copyfile(src, dst)
       
    except:


def alarm():
    playsound("imperial march trimmed.mp3")
    
src = "longtermrun.csv"
dst = "longtermrunBACKUP"
step = 0

def makeFile():
    dst = "longtermrunBACKUP" + (str)step + ".csv"
    while os.path.isfile(dst):
        step++
        dst = "longtermrunBACKUP" + (str)step + ".csv"
    
    with open(dst, 'w') as f: #create file when file doesn't exist
            print("created file") 

makeFile()

while True:
    
    time.sleep(1)
    if not os.path.isfile(dst): #if the file doesn't exist
        makeFile()
        
    
    if not filecmp.cmp(src, dst): #if files are NOT the same
        if os.path.getsize(src) > os.path.getsize(dst): #if src is longer than dst
            fileCopy(src, dst) #overrite so dst matches src
            print("overwritten")
        
        else: #if 
            makeFile()

    else: #if files are the same
        print("alarm")
        alarm()
        x = input("Press something after files have been made again")
        #time.sleep(40)
        
        
        


