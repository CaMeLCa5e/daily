import re
import time
from config import myemail, mypassword, meetup_url
from lxml import html
from tandom import randrange
from selenium import webdriver

def main():
	driver = webdriver.Firefox()

	username = driver.find_element_by_id('email')
	username.send_keys(myemail)

	password = driver.find_element_by_id('password')
	password.send_keys(mypassword)
	password.submit()

	