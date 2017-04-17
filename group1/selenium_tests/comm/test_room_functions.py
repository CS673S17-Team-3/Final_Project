from selenium.webdriver.common.keys import Keys
import base_testcase

class RoomFunctions(base_testcase.CommonLiveServerTestCase):

	def create_rooms(self):
		self.log_in();

		self.driver.find_element_by_xpath("//div[@id='room-list']/a[1]").click()
		self.pause(2)
		self.driver.find_element_by_id('teamname').send_keys('New Team')
		self.driver.find_element_by_id('saveTeam').click()
		self.pause(2)

		self.driver.find_element_by_xpath("//div[@id='room-list']/a[1]").click()
		self.pause(2)
		self.driver.find_element_by_id('teamname').send_keys('Newer Team')
		self.driver.find_element_by_id('saveTeam').click()
		self.pause(2)

	def edit_room_name(self):
		self.log_in();

		self.driver.find_element_by_id('dropdownMenu1').click()
		self.pause(1)
		self.driver.find_element_by_link_text('Edit Team').click()
		self.pause(2)
		self.driver.find_element_by_id('teamname').send_keys('Edited Team')
		self.driver.find_element_by_id('saveTeam').click()
		self.pause(2)

	def delete_room(self):
		self.log_in();

		self.driver.find_element_by_id('dropdownMenu1').click()
		self.pause(1)
		self.driver.find_element_by_link_text('Edit Team').click()
		self.pause(2)
		self.driver.find_element_by_id('deleteButton').click()
		self.pause(2)
		alert = self.driver.switch_to_alert()
		self.pause(2)
		alert.accept()
		self.pause()

	def test_create_room(self):
		self.create_rooms()
		self.assertTrue(self.driver.find_element_by_link_text('Newer Team').is_displayed())

	def test_edit_room_name(self):
		self.edit_room_name()
		self.assertTrue(self.driver.find_element_by_link_text('Edited Team').is_displayed())

	def test_delete_room(self):
		self.delete_room()

		try:
			self.assertFalse(self.driver.find_element_by_id('room-1').is_displayed())
		except:
			return True
