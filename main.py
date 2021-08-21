import requests
import json
import pprint
import pandas as pd

SETTINGS = "settings.json"

def get_data():
    settings = load_settings()
    response = requests.get(
        "https://api.libreview.io/glucoseHistory?numPeriods=5&period=7",
        #"https://api.libreview.io/glucoseHistory?numPeriods=5&period=90",
        headers = {"Authorization": "Bearer {}".format(settings["api_token"])}
    )
    return response.json()

# ====================================================================================================

def load_settings():
    with open(SETTINGS, "r") as f:
        return json.load(f)

# ====================================================================================================

def main():
    data = get_data()
    #pprint.pprint(data)

# ====================================================================================================

if __name__ == "__main__":
    main()
