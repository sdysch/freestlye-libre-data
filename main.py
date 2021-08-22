import requests
import json
import pprint
import pandas as pd
import os

SETTINGS = "settings.json"

def get_data():
    response = requests.get(
        "https://api.libreview.io/glucoseHistory?numPeriods=5&period=7",
        #"https://api.libreview.io/glucoseHistory?numPeriods=5&period=90",
        headers = {"Authorization": "Bearer {}".format(get_API_token())}
    )
    return response.json()

# ====================================================================================================

def get_API_token():

    try:
        token = os.environ["LIBREVIEW_API_TOKEN"]
    except:
        print("Please ensure that LIBREVIEW_API_TOKEN environment variable is set. Did you run setup.sh?")
        exit(1)

    return token

# ====================================================================================================

def main():
    data = get_data()
    pprint.pprint(data)

# ====================================================================================================

if __name__ == "__main__":
    main()
