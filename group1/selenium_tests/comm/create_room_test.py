from selenium.webdriver.common.keys import Keys
import base_testcase

class CreateRoom(base_testcase.CommonLiveServerTestCase):

	def create_rooms(self):
		self.driver.get('http://127.0.0.1:8000/communication/')

		self.driver.find_element_by_id('username').send_keys(self.super_user_name)
		self.driver.find_element_by_id('password').send_keys(self.super_user_pw)
		self.driver.find_element_by_id('password').send_keys(Keys.ENTER)
		self.pause()

		self.driver.get('http://127.0.0.1:8000/communication/')
		self.driver.find_element_by_xpath("//div[@id='room-list]'/a[1]").click()
		self.driver.find_element_by_id('teamname').send_keys('New Team')
		self.driver.find_element_by_id('saveTeam').click()
		self.pause()

		self.driver.get('http://127.0.0.1:8000/communication/')
		self.driver.find_element_by_xpath("//div[@id='room-list]'/a[1]").click()
		self.driver.find_element_by_id('teamname').send_keys('Newer Team')
		self.driver.find_element_by_id('saveTeam').click()
		self.pause()

	def test_create_room(self):
		self.create_room
		self.assertTrue(self.driver.find_element_by_id('room-2').is_displayed())