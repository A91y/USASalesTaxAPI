import requests
from bs4 import BeautifulSoup
import pandas as pd

def extractSalesTaxData() -> pd.core.frame.DataFrame:
    taxData = []
    URL = r"https://salestaxusa.com/#salestaxusa"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    datatable = soup.find_all("table", class_="tablepress")
    rows = datatable[0].find_all("tr")
    for row in rows[1:]:
        datalist = row.find_all("td")
        stateData = {
        "state": datalist[1].text.strip(),
        "combined_rate": datalist[2].text.strip(),
        "local_rate": datalist[3].text.strip(),
        "state_rate": datalist[4].text.strip(),
        "population": datalist[5].text.strip()
        }
        taxData.append(stateData)
    df = pd.DataFrame(taxData)
    return df
