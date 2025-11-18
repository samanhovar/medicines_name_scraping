import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://www.darooyab.ir/"
drug_groups_page = "DrugGroups"

drug_groups = []
group_title = []


# read web page
response = requests.get(base_url + drug_groups_page)
soup = BeautifulSoup(response.text, "html.parser")


# finding all pages of DrugGroups
for medicine in soup.select('a[class="ahref_Generic"]'):
    if medicine.find("span"):
        href = medicine.get("href")
        drug_groups.append(href)
        group_title.append(medicine.get_text(strip=True))


# writing all drug names both in farsi and english to csv files
for i, group in enumerate(drug_groups):
    response = requests.get(base_url + group)
    soup = BeautifulSoup(response.content, "html.parser")


    medicines = []
    medicines.append(group_title[i])


    farsi_med = soup.select('a[class="ahref_Generic"]')
    english_med = soup.select('a[class="ahref_Generic EnglishNumericFont"]')

    
    for fa, en in zip(farsi_med, english_med):
        if fa.get_text() != "" and en.get_text() != "":
            medicines.append([fa.get_text(), en.get_text()])



    df = pd.DataFrame(medicines)
    file_id = group.rstrip("/").split("/")[-1]
    filename = f"medicines_{file_id}.csv"
    df.to_csv(filename, index=False, header=False)
    break
