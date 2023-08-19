from typing import Final, List
from datetime import timedelta
from dataclasses import dataclass
from requests_cache import CachedSession

BASE_URL: Final[str] = "https://api.zippopotam.us/us/"

session = CachedSession(
    cache_name="cache/zipcode_cache", backend="sqlite", expire_after=timedelta(days=30)
)


def stateName(zipcode: int | str) -> str | None:
    URL = BASE_URL + str(zipcode)
    response = session.get(URL)
    try:
        json: dict = response.json()
        state: str = json["places"][0]["state"]
        return state
    except Exception as e:
        print(f"{response.status_code}: {response.reason}\n{e}")
        return None


if __name__ == "__main__":
    print(stateName(27247))  # North Carolina
    print(stateName(65043))  # Missouri
