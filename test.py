from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/allan/Desktop/FWUITest/driver/chromedriver.exe")
base_url = "https://www.flowworks.com"
user_name = "alanli"
user_password = "DC9kt10&2A8#"
driver.get(base_url)
loginButton = driver.find_element_by_id("menu-item-781")
loginButton.click()
usernameInput=driver.find_element_by_id("txtUsername")
usernameInput.send_keys(user_name)