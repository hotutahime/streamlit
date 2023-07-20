from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

my_name = "kao"


driver = webdriver.Chrome()
driver.get("https://jre-abc.com/wp/afactory/contact/")

driver.find_element(by=By.XPATH , value="//*[@id='post-9857']/div/p[3]/a").click()
time.sleep(1)

driver.find_element(by=By.XPATH , value="/html/body/main/div[2]/div/div/form/div/div[1]/div/div[1]/input").send_keys(my_name)
time.sleep(1)

driver.find_element(by=By.XPATH , value="/html/body/main/div[2]/div/div/form/div/div[3]/div/div[1]/input").send_keys("g@jp")
time.sleep(1)

driver.find_element(by=By.XPATH , value="/html/body/main/div[2]/div/div/form/div/div[4]/div/div[1]/div[3]/label/span[2]").click()
time.sleep(1)

driver.find_element(by=By.XPATH , value="/html/body/main/div[2]/div/div/form/div/div[6]/div/div[1]/div[3]/label/span[2]").click()
time.sleep(1)

driver.find_element(by=By.XPATH , value="/html/body/main/div[2]/div/div/form/div/div[5]/div/div[1]/textarea").send_keys("test")
time.sleep(1)

driver.find_element(by=By.XPATH , value="/html/body/main/div[2]/div/div/form/div/div[7]/div/div[1]/div[2]/label/span[2]").click()
time.sleep(1)