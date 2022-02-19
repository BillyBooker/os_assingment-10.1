import json 
import os 
import os.path



isdir = os.path.isdir(input("Please enter the directory you would like to save your file :"))
 
if isdir is True:
    print("This directory exists.")
else:
    print("This is not a valid entry, try again.")
    isdir

file_name = (input("Please enter the name of your file : "))


with open(os.path.join(isdir, file_name, "w")) as f:
    f.write(input("Please enter your name : "))
    f.write(input("PLease enter your adress : "))
    f.write(input("Please enter your phone number : "))






