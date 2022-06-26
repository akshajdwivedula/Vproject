# Adapted Code - optimized and altered from NC_StepOne_March13_2019.py
# Libraries - adding all that might be necessary, may not use them all

import os
import pandas as pd

path = "C:\\Users\\adwiv\\OneDrive - The University of Chicago\\Research\\George\\AOC\\01012006 - 12312010\\Criminal\\temp\\"
os.chdir(path)
# with zipfile.ZipFile("CROFFNFF.ZIP", "r") as zip:
#     zip.extract("AOCP\\CR\\PROD\\NEWSALLA")
with open("hello.txt", "r") as file:
    firstline = file.readline()
print(firstline)
