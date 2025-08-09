import json

import requests

token = ""
with open("hamsat.token", "r") as f:
    token = f.read().strip()

response = requests.get(
    "https://hams.at/api/alerts/upcoming", headers={"Authorization": "Bearer " + token}
)

if response.status_code == 200:
    output = response.text[:600]
    print(f"{output}...\n\n")
    for activation in response.json()["data"]:
        print(
            f"{activation['callsign']} \
            {activation['aos_at']} \
            {activation['satellite']}"
        )
