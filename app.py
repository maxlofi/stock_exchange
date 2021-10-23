#!/usr/bin/env python3


from bs4 import BeautifulSoup
import requests
import yaml
from datetime import date


URL = "https://www.boursorama.com/cours/1rPOVH/"
results = {}
results["Date"] = date.today().strftime("%d/%m/%Y")


r = requests.get(URL)
soup = BeautifulSoup(r.content, "html.parser")


soup_instruments = soup.find_all("span", class_="c-instrument")[:2]

results["Price"] = float(soup_instruments[0].get_text())
results["Evolution"] = soup_instruments[1].get_text()
with open("res.yaml", "w") as re:
    yaml.dump(results, re)
