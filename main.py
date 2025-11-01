from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome()

drug_groups = []

driver.get("https://www.darooyab.ir/DrugGroups")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='ahref_Generic']"))
)


# finding all pages of DrugGroups
for medicine in driver.find_elements(By.XPATH, "//a[@class='ahref_Generic']"):
    if medicine.find_elements(By.TAG_NAME, "span"):
        href = medicine.get_attribute("href")
        drug_groups.append(href)


# writing all drug names both in farsi and english to csv files
for group in drug_groups:
    driver.get(group)

    medicines = []

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='ahref_Generic']"))
    )

    farsi_medicine = driver.find_elements(By.XPATH, "//a[@class='ahref_Generic']")
    english_medicine = driver.find_elements(
        By.XPATH, "//a[@class='ahref_Generic EnglishNumericFont']"
    )

    for fa, en in zip(farsi_medicine, english_medicine):
        if fa.text != "" or en.text != "":
            medicines.append([fa.text, en.text])

    df = pd.DataFrame(medicines)
    file_id = group.rstrip("/").split("/")[-1]
    filename = f"medicines_{file_id}.csv"
    df = pd.DataFrame(medicines)
    df.to_csv(filename, index=False)
