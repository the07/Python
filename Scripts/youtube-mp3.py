from urllib import *
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

song = str(input('Enter the name of the song - '))
url = 'https://www.youtube.com/'

driver = webdriver.Firefox()

driver.get(url)
assert "youtube" not in driver.title

elem = driver.find_element_by_name("search_query")
elem.send_keys(song)
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source
