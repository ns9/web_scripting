#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Amazon:

	def __init__(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://www.amazon.com")
	
	def open_cart(self):
		cart_button = self.driver.find_element_by_id("nav-cart")
		cart_button.click()

	def close_page(self):
		self.driver.close()


class Ebay:

	def __init__(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://www.ebay.com")
	
	def search(self, search_term):
		search_box = self.driver.find_element_by_id("gh-ac")
		search_button = self.driver.find_element_by_id("gh-btn")
		
		search_box.send_keys(search_term)
		search_button.click()

	def close_page(self):
		self.driver.close()



if __name__== "__main__":
  
	print("opening amazon")
	amazon = Amazon()
	print("opening amazon cart")
	amazon.open_cart()

	print("opening ebay")
	ebay = Ebay()
	print("searching for skis")
	ebay.search("skis")

	time.sleep(10)
	print("closing web pages");
	amazon.close_page()
	ebay.close_page()
	
