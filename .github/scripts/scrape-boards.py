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
    temp_dict = {}
    row = table.text.split("\n")[2:11]  # get relevant data from the row
    temp_dict["code_name"] = row[2]
    temp_dict["family_name"] = row[3]
    temp_dict["arch"] = row[7]
    temp_dict["cpu_gen"] = row[8]
    device_key = row[1].replace(row[0].lower().capitalize(), "").strip()  # remove brand name from device name
    device_key = device_key.replace(row[0].upper(), "").strip()  # remove brand name from device name
    if device_key.startswith("-"):
        device_key = device_key[1:]
    try:
        devices_dict[row[0].capitalize().strip()][device_key] = temp_dict
    except KeyError:
        devices_dict[row[0].capitalize().strip()] = {device_key: temp_dict}
print(devices_dict)
devices_dict.pop("")  # remove broken entry
with open("./device-support/devices-autogen.json", "w") as f:
    json.dump(devices_dict, f)
