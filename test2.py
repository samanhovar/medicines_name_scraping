from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome()

drug_groups = []
group_title = []

driver.get("https://www.darooyab.ir/DrugGroups")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='ahref_Generic']"))
)


# finding all pages of DrugGroups
for medicine in driver.find_elements(By.XPATH, "//a[@class='ahref_Generic']"):
    if medicine.find_elements(By.TAG_NAME, "span"):
        href = medicine.get_attribute("href")
        drug_groups.append(href)
        group_title.append(medicine.text)
        

