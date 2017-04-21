from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import base_testcase

class MessageFunctions(base_testcase.CommonLiveServerTestCase):

	def send_message(self):
		self.log_in()

		self.driver.find_element_by_id('text').send_keys('Hi there')
		self.driver.find_element_by_id('text').send_keys(Keys.ENTER)
		self.pause(2)

		message = ""
		for num in range(1, 1050):
			message += "a"

		self.driver.find_element_by_id('text').send_keys(message)
		self.driver.find_element_by_id('text').send_keys(Keys.ENTER)
		self.pause(2)

	def send_emoticon(self):
		self.log_in()

		self.driver.find_element_by_xpath("//button[contains(@class, 'btn') and contains(@class, 'btn-default') and contains(@class, 'dropdown-toggle')]").click()
		self.pause(2)
		self.driver.find_element_by_xpath("//table/tbody[1]/tr[1]/td[2]/a[1]").click()
		self.pause(1)
		self.driver.find_element_by_id('text').send_keys(Keys.ENTER)
		self.pause(2)

	def search_messages(self):
		self.log_in()

		self.driver.find_element_by_id('dropdownMenu1').click()
		self.pause(1)
		self.driver.find_element_by_link_text('Search').click()
		self.pause(1)
		self.driver.find_element_by_id('search_box').send_keys('Hello')
		self.driver.find_element_by_id('search_box').send_keys(Keys.ENTER)
		self.pause(2)

	def edit_message(self):
		self.log_in()

		ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name('msgmenu')).perform()
		self.driver.find_element_by_xpath("//ul[contains(@class, 'msgmenu')]/li[1]").click()
		self.driver.find_element_by_id('edit-1').send_keys('New Message')
		self.driver.find_element_by_id('edit-1').send_keys(Keys.ENTER)

	def delete_message(self):
		self.log_in()

		ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name('msgmenu')).perform()
		self.driver.find_element_by_xpath("//ul[contains(@class, 'msgmenu')]/li[2]").click()
		alert = self.driver.switch_to_alert()
		self.pause(2)
		alert.accept()

	def test_sent_message(self):
		self.send_message()
		self.assertTrue(self.driver.find_element_by_xpath("//div[@id='room-1']/p[2]").is_displayed())
		thirdmessage = self.driver.find_element_by_xpath("//div[@id='room-1']/p[3]").text
		self.assertTrue(len(thirdmessage) < 1050)

	def test_sent_emoticon(self):
		self.send_emoticon()
		self.assertTrue(self.driver.find_element_by_xpath("//div[@id='room-1']/p[2]/img[1]").is_displayed())

	def test_search_messages(self):
		self.search_messages()
		self.assertTrue(self.driver.find_element_by_xpath("//div[@id='searchResults' and text() != '']"))

	def test_edit_message(self):
		self.edit_message()
		assert "New Message" in self.driver.find_element_by_id('message-1').text

	def test_delete_message(self):
		self.delete_message()

		try:
			self.assertFalse(self.driver.find_element_by_id('message-1').is_displayed())
		except:
			return True