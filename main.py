from bs4 import BeautifulSoup
import requests

# HTML from File
# with open("index.html", "r") as f:
# 	doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all("p")[0]

# print(tags.find_all("b"))

# HTML from Website
url = "https://www.newegg.ca/intel-core-i9-12th-gen-core-i9-12900k-alder-lake-lga-1700-desktop-cpu-processor/p/N82E16819118339?Item=N82E16819118339"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")
parent = prices[0].parent
print(parent)