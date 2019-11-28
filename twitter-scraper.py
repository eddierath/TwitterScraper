import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import subprocess
import sys

twitter_username = input("\n" + "Enter a Twitter handle: " + "\n")
browser = webdriver.Chrome('/Users/eddie/Documents/GitHub/TwitterScraper/chromedriver') # directory of chromedriver
browser.get("https://twitter.com/" + twitter_username)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 10

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)

    no_of_pagedowns-=1

twitter_elm = browser.find_elements_by_class_name("tweet")

for post in twitter_elm:
	username = post.find_element_by_class_name("username")
	if username.text.lower() == "@" + twitter_username.lower():
		tweet = post.find_element_by_class_name("tweet-text")
		print(tweet.text + "\n")
		subprocess.call("say -v Alex -r 220 " + tweet.text, shell=True)
browser.quit()
