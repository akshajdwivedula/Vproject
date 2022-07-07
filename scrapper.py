import random
import webbrowser
import os
import zipfile
import re
import docx2txt
from selenium import webdriver

#https://www.lambdatest.com/blog/automated-web-bot-with-selenium-python/
# global Options
# # setting up options and creating file reader to read off a daily script
Options = [287, 286, 285, 291, 294, 64, 289, 292]
webdriver.Edge()

# #sets up path to include location where all the docs are
# #IMPORTANT: THIS WORKED ONLY WHEN USING THE r and the \\, when  changing directories keep that in mind
os.chdir(r'C:\\Users\\adwiv\\OneDrive - The University of Chicago\\Research\\George\\')

# #reads through daily script document that tells what category to begin with
# result = docx2txt.process("DailyScript.docx").lower()
if "family" in result:
    #chooses value in list that corresponds to correct url and opens that url
    x = Options[0]
    y = "https://www.legalmatch.com/post-case/subcategory?supCatIds="+str(x)+"&combo_loc=false"
    webbrowser.open(y)
#Keep in end
webdriver.Edge.quit

##Next steps: Be able to check necessary checkboxes, be able to fill in information into locations