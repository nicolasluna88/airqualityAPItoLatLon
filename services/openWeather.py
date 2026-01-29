import requests

def getAirPollution(lat, lon, config):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": config["openWeather"]["apiKey"]
    }

    r = requests.get(
        config["openWeather"]["url"],
        params=params,
        timeout=10
    )
    r.raise_for_status()
    data = r.json()

    try:
        return data["list"][0]["components"]
    except (KeyError, IndexError):
        return None