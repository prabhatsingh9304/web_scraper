from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import re
PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)
usrn=sys.argv[1]
print("Enter Password:-")
passwd=input()
driver.get("https://moodle.iitd.ac.in/login/index.php")
usrname = driver.find_element_by_id("username")
password=driver.find_element_by_id("password")
text = driver.find_element_by_id("login").text
cap=driver.find_element_by_id("valuepkg3")
Number = [int(s) for s in re.findall(r'-?\d+\.?\d*', text)]
if 'add' in text:
    result=Number[0]+Number[1]
elif 'subtract' in text:
    result=Number[0]-Number[1]
elif 'first' in text:
    result=Number[0]
else:
    result=Number[1]
usrname.send_keys(usrn)
password.send_keys(passwd)
cap.send_keys(result)
submit=driver.find_element_by_id("loginbtn")
submit.click()


