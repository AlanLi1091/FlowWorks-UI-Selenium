# Load Flowworks Homepage

from selenium import webdriver

base_url = "https://www.flowworks.com"

driver = webdriver.Chrome(executable_path="C:/Users/allan/Desktop/FWUITest/driver/chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get(base_url)

assert "FlowWorks" in driver.title

driver.close()