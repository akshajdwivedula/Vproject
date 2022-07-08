import os
import zipfile
import docx2txt
from selenium import webdriver
from selenium.webdriver.support.select import Select


#https://www.lambdatest.com/blog/automated-web-bot-with-selenium-python/
#https://www.toolsqa.com/selenium-webdriver/find-element-selenium/
#https://www.tutorialspoint.com/how-to-select-a-drop-down-menu-option-value-with-selenium-python#:~:text=The%20Select%20class%20in%20Selenium%20is%20used%20to,we%20have%20to%20import%20selenium.webdriver.support.select.Select%20in%20our%20code.
#https://www.tutorialspoint.com/click-a-href-button-with-selenium-and-python


# global Options
# # setting up options and creating file reader to read off a daily script
# Options = [287, 286, 285, 291, 294, 64, 289, 292]

driver = webdriver.Edge()
driver.implicitly_wait(20)

# #sets up path to include location where all the docs are
# #IMPORTANT: THIS WORKED ONLY WHEN USING THE r and the \\, when  changing directories keep that in mind
os.chdir(r'C:\\Users\\adwiv\\OneDrive - The University of Chicago\\Research\\George\\')

#
driver.get('https://www.legalmatch.com/find-lawyers.html')

# #reads through daily script document that tells what category to begin with
## Will need to make this read just one line that way I can set up this script to send us to the pertinent location
result = docx2txt.process("DailyScript.docx").lower()
##Text below likely obsolete, keeping it in case proves useful later
# if "family" in result:
#     #chooses value in list that corresponds to correct url and opens that url
#     x = str(Options[0])

#Need to make "Family" a variable that pulls from the script, but right now, it's taking us to correct url
link = driver.find_element_by_partial_link_text('Family')
#clicks on link
link.click()
#prints url to check we are ending up at correct link
print(driver.current_url)


#Keep in end
driver.quit()


#When using partial link text, it uses the text on the page itself, so we can focus on that for links, for buttons and other things, it will be different
#need to add more options, but finally we have set it up to select something we want ... now we'll need to better optimize the DailyScript to match
#Next steps: Set up doc to program reading, find out how to select checkboxes, and then how to fill in forms with information