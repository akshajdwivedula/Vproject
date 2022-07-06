import random
import webbrowser
import os
import zipfile
import re


# webbrowser.open('https://www.legalmatch.com/find-lawyers.html')
global Options
# setting up options and creating file reader to read off a daily script
Options = [287, 286, 285, 291, 294, 64, 289, 292]
import os
file_ = 'Dailyscript.docx'

for root, dirs, files in os.walk('C:/'):
    for name in files:
        if file_ in name:
            print (os.path.abspath(os.path.join(root, name)))

# y = "https://www.legalmatch.com/post-case/subcategory?supCatIds="+str(x)+"&combo_loc=false"
# webbrowser.open(y)