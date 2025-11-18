import requests
from bs4 import BeautifulSoup
# from test4 import word_list


response = requests.get("https://irc.fda.gov.ir/nfi")
response = requests.get("https://irc.fda.gov.ir/nfi/Search?Term=oma&PageNumber=1&PageSize=10")

with open("index.html", "w") as index:
    index.write(response.text)

# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify)

