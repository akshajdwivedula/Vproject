import random
import webbrowser
import os
import zipfile
import re
import docx2txt


# webbrowser.open('https://www.legalmatch.com/find-lawyers.html')
global Options
# setting up options and creating file reader to read off a daily script
Options = [287, 286, 285, 291, 294, 64, 289, 292]

os.chdir(r'C:\\Users\\adwiv\\OneDrive - The University of Chicago\\Research\\George\\')

result = docx2txt.process("DailyScript.docx").lower()
if "family" in result:
    x = Options[0]
    y = "https://www.legalmatch.com/post-case/subcategory?supCatIds="+str(x)+"&combo_loc=false"
    webbrowser.open(y)