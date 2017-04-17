from selenium.webdriver.common.keys import Keys
import base_testcase

class RoomFunctions(base_testcase.CommonLiveServerTestCase):

	def send_message(self):
		self.log_in()

		self.driver.find_element_by_id('text').send_keys('Hi there')
		self.driver.find_element_by_id('text').send_keys(Keys.ENTER)
		self.pause(2)

	def test_sent_message(self):
		self.send_message()
		self.assertTrue(self.driver.find_element_by_xpath("//div[@id='room-1']/p[2]").is_displayed())