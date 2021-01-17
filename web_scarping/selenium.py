from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os



def Scrapping(str):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

	driver.get("https://medium.com/search?q="+str) 
	elements=driver.find_elements_by_class_name("graf--title")
	output=[]

	for element in elements:
		output.append(element.text)

	return output
