from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time
import json

TIMEOUT = 60
sugar_secret = "/Users/crmonlinegraph/Documents/Scripts/sugar_secret.json"

class TestSugarMethods(unittest.TestCase):	
	def setUp(self):
		self.browser = webdriver.Chrome()
		with open(sugar_secret) as json_file:
			self.data = json.load(json_file)

	def test_login_success(self):
		browser = self.browser
		browser.get("https://bpi8.crmonline.com.au")
		login_page = self.get_element(browser, "//p[@id='version']")
		self.assertTrue(login_page.is_displayed())
		data = self.data
		username = self.get_element(browser, "//input[@placeholder='User Name']")
		username.send_keys(data["username"])
		password = self.get_element(browser, "//input[@placeholder='Password']")
		password.send_keys(data["crm_password"])
		log_in = self.get_element(browser, "//a[@name='login_button']")
		log_in.click()
		user_action_btn = self.get_element(browser, "//li[@id='userActions']//div[@class='btn-group']")
		self.assertTrue(user_action_btn.is_displayed())
	
	def tearDown(self):		
		self.browser.close()


	def press_any_key(self):
		input("\nPress any key...")

	def get_element(self, browser, element_attrib):
		i=0
		while True:
			try:
				crm_version = WebDriverWait(browser, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, element_attrib)))
				return crm_version
				break
			except TimeoutException:
				print("Could not find element: {}".format(element_attrib))
				self.press_any_key()
				break;


if __name__ == '__main__':
	unittest.main(verbosity=2)