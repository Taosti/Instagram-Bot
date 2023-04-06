#bots_list = ["follow", "my bio", "I post", "I'm public", "follower", "our bio", "i accept", "my page"]

from selenium import webdriver
from time import sleep

chromedriverpath = (r'C:\Users\bot25\Downloads\chromedriver_win32\chromedriver.exe')

class InstaBot:
	def __init__(self, username, pw):
		self.driver = webdriver.Chrome(executable_path=chromedriverpath)
		self.username = username
		self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
			.send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(pw)
		self.driver.find_element_by_xpath('//button[@type="submit"]')\
			.click()
		sleep(4)
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
			.click()
		sleep(2)
		
		#a = 0
		#while(a < 10): 
		#	self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")\
		#		.click()
		#	a += 1
		
		self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format('explore'))\
			.click()
		sleep(2)
		self.driver.find_element_by_xpath('//input[@type="text"]')\
			.send_keys('taosti')
		sleep(2)
		self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format('taosti'))\
			.click()
		sleep(3)
			
		#self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(''))\
		#	.click()
		self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format('p/B9UbgNShMQ51XZp6VGzqX9bQf5Oq38BUKPiCG00'))\
			.click()
		sleep(2)
		
		a = 1
		
		while(a < 20):
			self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")\
				.click()
			sleep(1)
			self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")\
				.send_keys('Botted')
			sleep(1)
			self.driver.find_element_by_xpath('//button[@type="submit"]')\
				.click()
				
			a += 1
			sleep(15)
			
			
		self.driver.quit()
	
my_bot = InstaBot('reporting_pybot', 'python04')
