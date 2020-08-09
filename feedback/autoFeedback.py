#This is program that automates the feedback for the 4th semester CS dept

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException


#    _______ _            _                       _     _               _  ___     _ 
#   |__   __| |          | |                     | |   (_)             | |/ (_)   | |
#      | |  | |__   ___  | |     __ _ _   _  __ _| |__  _ _ __   __ _  | ' / _  __| |
#      | |  | '_ \ / _ \ | |    / _` | | | |/ _` | '_ \| | '_ \ / _` | |  < | |/ _` |
#      | |  | | | |  __/ | |___| (_| | |_| | (_| | | | | | | | | (_| | | . \| | (_| |
#      |_|  |_| |_|\___| |______\__,_|\__,_|\__, |_| |_|_|_| |_|\__, | |_|\_\_|\__,_|
#                                            __/ |               __/ |               
#                                           |___/               |___/ 

#Take students registration number and password
studentId = input("Enter your registration number: ")
studentPassword =  input("Enter your password: ")

browser = Chrome("F:/webdriver/chromedriver.exe")
browser.get("http://111.68.99.200/SRA-n/")


#NOTE: I am continuously using find_by_element instead of storing it in a variable
#because our universities bad coding practices resest the entire DOM and makes the
#variable invalid

# navigate to the page
select = Select(browser.find_element_by_id("ddlDegreeProg"))
print ([o.text for o in select.options]) # these are string-s
select.select_by_visible_text("BS Computer and Information Sciences")

id = browser.find_element_by_id("txtRegNo")
id.send_keys(studentId)
password = browser.find_element_by_id("a63542B5")
password.send_keys(studentPassword,Keys.RETURN)

(browser.find_element_by_id("cmdViewTranscript")).send_keys(Keys.RETURN)
(browser.find_element_by_id("btnfeedback")).send_keys(Keys.RETURN)

course_id = Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))
courses = course_id.options
print(len(courses))

#Loops through the entire feedback and sets the value of 3 for every question
for name in range(len(courses) - 1):
    (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlCourse"))).select_by_index(name)

    (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))).select_by_index(0)

    if name == 6:
        (Select(browser.find_element_by_id("_ctl0_ContentPlaceHolder1_ddlContributor"))).select_by_index(1)

    for i in range(0,18):
        score = "_ctl0_ContentPlaceHolder1_txt" + (chr(ord('A') + i))
        (browser.find_element_by_id(score)).send_keys("3")#You can change the value here and set it between 1-5

#Writes the messages in the two text areas. You can change the messages
    (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtComments")).send_keys("""This is written using an automated script since no one reads our feedback.\n
I will write actual feedback when you are willing to read this.""")
    (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_txtCommentsCourse")).send_keys("""This is written using an automated script since no one reads our feedback.\n
I will write actual feedback when you are willing to read this.""")

    (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdSubmit")).send_keys(Keys.RETURN)
    (browser.find_element_by_id("_ctl0_ContentPlaceHolder1_cmdReset")).send_keys(Keys.RETURN)

