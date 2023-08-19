import requests


def stateName(zipcode: int | str) -> str | None:
    BASE_URL = "https://api.zippopotam.us/us/"
    URL = BASE_URL + str(zipcode)
    response = requests.get(URL)
    json_response = response.json()
    try:
        # state = json_response["places"][0]["state"]
        state = json_response
    except KeyError:
        return None
    return state


if __name__ == "__main__":
    print(stateName(27247))  # North Carolina
    print(stateName(65043))  # Missouri
