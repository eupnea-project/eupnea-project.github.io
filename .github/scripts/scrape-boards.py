import contextlib
import json

import requests
from bs4 import BeautifulSoup

# Create soup object
soup = BeautifulSoup(
    requests.get("https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/").text,
    'html.parser')

devices_table = soup.find_all("table")[2]  # Get the third table on the page

devices_dict = {}

# scan all rows starting from the second row
for table in devices_table.find_all("tr")[1:]:
    row = table.text.split("\n")[2:11]  # get relevant data from the row
    temp_dict = {
        "code_name": row[2],
        "family_name": row[3],
        "arch": row[7],
        "cpu_gen": row[8],
    }
    device_key = row[1].replace(row[0].lower().capitalize(), "").strip()  # remove brand name from device name
    device_key = device_key.replace(row[0].upper(), "").strip()  # remove brand name from device name
    with contextlib.suppress(IndexError):
        if device_key[0] == "-":
            device_key = device_key[1:]
    try:
        devices_dict[row[0].capitalize().strip()][device_key] = temp_dict
    except KeyError:
        devices_dict[row[0].capitalize().strip()] = {device_key: temp_dict}
print(devices_dict)
devices_dict.pop("")  # remove broken entry
with open("./device-support/devices-autogen.json", "w") as f:
    json.dump(devices_dict, f)

# combine autogen and extra into one json file
with open("./device-support/devices-autogen.json", "r") as f:
    autogen = json.load(f)
with open("./device-support/devices-extra.json", "r") as f:
    extra = json.load(f)
merged = {**autogen, **extra}
with open("./device-support/devices-list.json", "w") as f:
    json.dump(merged, f)
