from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import os
ESTE_DIR= os.path.abspath('.')
PROFILE_DIR= ESTE_DIR+'/_browser_profile'

browser= None

def get_browser(quiereVisible= False):
	global browser
	if browser is None:
		chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

		chrome_options = Options()
		options = [
				"--disable-gpu",
				"--window-size=1920,1200",
				"--ignore-certificate-errors",
				"--disable-extensions",
				"--no-sandbox",
				"--disable-dev-shm-usage",
				"user-data-dir="+PROFILE_DIR, #A: Path to your chrome profile
		]

		if not quiereVisible:
			options.append("--headless")

		for option in options:
				chrome_options.add_argument(option)

		browser= webdriver.Chrome(service=chrome_service, options=chrome_options)

	return browser

def free_browser(a_browser=None):
	global browser
	a_browser= a_browser or browser
	a_browser.quit()
	if a_browser==browser:
		browser= None
