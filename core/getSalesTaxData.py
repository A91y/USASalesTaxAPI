from bs4 import BeautifulSoup
import pandas as pd
from requests_cache import CachedSession
from getZip import stateName

session = CachedSession(
    cache_name="cache/salestaxdata_cache", backend="sqlite", expire_after=60*3
)


def extractSalesTaxData() -> pd.core.frame.DataFrame:
    taxData = []
    URL = r"https://salestaxusa.com/#salestaxusa"
    page = session.get(URL)
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


def clean_state_name(stateName: str) -> str:
    formatted = []
    stateName = stateName.split(" ")
    for i in stateName:
        formatted.append(i.capitalize())
    stateName = " ".join(formatted)
    return stateName


def searchByState(state: str) -> pd.core.frame.DataFrame:
    df = extractSalesTaxData()
    df = df[df["state"].str.contains(state, case=False)]
    return df


def searchByZipcode(zipcode: int | str) -> pd.core.frame.DataFrame:
    df = searchByState(clean_state_name(stateName(zipcode)))
    return df


if __name__ == "__main__":
    # a = searchByState("North Carolina")
    a = searchByZipcode(27247)
    print(a)
