from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://web.whatsapp.com/"

class Whatsapp_access:
	def __init__(self):
		self.driver = webdriver.Firefox(executable_path="/home/bogo/Downloads/geckodriver")
		self.driver.get(url)

	def get_user(self, name):
		try:
			ele = self.driver.find_element_by_xpath("//span[@title='" + name + "']")
			ele.click()
		except:
			print("The contact does not exist.")

	def search_user(self, name):
		try:
			ele = self.driver.find_element_by_css_selector("input#input-chatlist-search")

			mouse = webdriver.ActionChains(self.driver)
			mouse.move_to_element(ele).click().perform()
			mouse.send_keys(name).perform()
			mouse.perform()
			self.driver.find_element_by_class_name("chat-body").click()
		except:
			print("The contact does not exist.")

	def send_msg(self, msg):
		try:
			ele = self.driver.find_element_by_xpath("//div[@class='pluggable-input-body copyable-text selectable-text']")
			ele.click()
			ele.send_keys(msg)
			ele.send_keys(Keys.RETURN)
		except e:
			print(e)

	def spam(self, name, interval=5):
		msg = "Dikha"
		try:
			self.get_user(name)
			ele = self.driver.find_element_by_xpath("//div[@class='pluggable-input-body copyable-text selectable-text']")
			while True:
				sleep(interval)
				ele.click()
				ele.send_keys(msg)
				ele.send_keys(Keys.RETURN)
		except KeyboardInterrupt as e:
			print("Safely exited.")		

# To open new tab
# driver.execute_script('''window.open("http://bings.com","_blank");''')
