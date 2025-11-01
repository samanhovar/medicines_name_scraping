from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

pages = ["DrugGroups", "HerbalMedicines", "DrugHerbal"]


driver = webdriver.Chrome()

medicines = []

driver.get("https://www.darooyab.ir/" + pages[-1])

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
df.to_csv("medicines.csv", index=False)
