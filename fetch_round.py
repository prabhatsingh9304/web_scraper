from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep 
import os
import sys
browser = webdriver.Chrome("./chromedriver")
label="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

contest_number=sys.argv[1]
parentdir="./"+ contest_number 
os.mkdir(parentdir)
l=0
while l<=26:
	PATH=parentdir + '/' + label[l]
	url="https://codeforces.com/problemset/problem/"+ contest_number + '/' + label[l]
	browser.get(url)
	get_url = browser.current_url 
	if get_url == url:
		pass
	else:
		break
	os.mkdir(PATH)
	sleep(2)
	element=browser.find_element_by_xpath('//*[@id="pageContent"]/div[3]/div[2]/div')
	element.screenshot(PATH + "/problem.png")
	text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[1]/pre").text
	f=open(PATH + "/input1.txt","w")
	f.write(text)
	f.close()
	text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[2]/pre").text
	f=open(PATH + "/output1.txt","w")
	f.write(text)
	f.close()
	try:
		text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[3]/pre").text
		f=open(PATH + "/input2.txt","w")
		f.write(text)
		f.close()
	except NoSuchElementException:
		pass
	else:
		text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[4]/pre").text
		f=open(PATH + "/output2.txt","w")
		f.write(text)
		f.close()
	try:
		text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[5]/pre").text
		f=open(PATH + "/input3.txt","w")
		f.write(text)
		f.close()
	except NoSuchElementException:
		pass
	else:
		text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[6]/pre").text
		f=open(PATH + "/output3.txt","w")
		f.write(text)
		f.close()
	try:
		text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[7]/pre").text
		f=open(PATH + "/input4.txt","w")
		f.write(text)
		f.close()
	except NoSuchElementException:
		pass
	else:
		text=browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[8]/pre").text
		f=open(PATH + "/output4.txt","w")
		f.write(text)
		f.close()	

	l=l+1 
browser.quit()


 
