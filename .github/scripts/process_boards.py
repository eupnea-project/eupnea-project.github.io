import json
from urllib.request import urlretrieve

parsed_json_list = {}


# recursive function to merge two dictionaries with nested dictionaries
def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            merge_dicts(dict1[key], dict2[key])
        else:
            dict1[key] = value


def parse_device(device: dict, device_name: str, family_name: str) -> None:
    # Extract individual names from device["brandNames"]
    # Remove commas inside brackets
    for i, _device in enumerate(device["brandNames"]):
        start = _device.find("(") + 1
        end = _device.find(")")
        if _device[start:end].find(","):
            device["brandNames"][i] = _device[:start] + _device[start:end].replace(",", "") + _device[end:]
    # Some devices are grouped together with "&" or "," -> Split them to improve UX in the final list
    names_list = [name.strip() for temp_name in device["brandNames"] for name in
                  temp_name.replace(" & ", ",").split(",")]

    # Iterate through names and find the CPU generation based on family_name
    cpu_gen = next(
        (_generation for _generation in board_families if family_name in board_families[_generation]["families"]),
        "Unknown")

    # If CPU generation not found, print a warning
    if cpu_gen == "Unknown":
        print(f"Unknown generation for device: {family_name}")

    # Create temporary device dictionary with relevant information
    for name in names_list:
        temp_device = {
            name.split(" ")[0].strip(): {
                name[name.find(" ") + 1:].strip(): {
                    # if override value exists, use it, else use scraped value
                    "code_name": device_name,
                    "family_name": overrides.get(device_name, {}).get("family_name", family_name),
                    "cpu_gen": overrides.get(device_name, {}).get("cpu_gen", cpu_gen),
                    "supported": overrides.get(device_name, {}).get("supported",
                                                                    board_families[cpu_gen]["arch"] == "x86_64"),
                    "audio_status": overrides.get(device_name, {}).get("audio_status",
                                                                       board_families[cpu_gen]["audio_status"]),
                    "comment": overrides.get(device_name, {}).get("comment", board_families[cpu_gen]["comment"]),
                }
            }
        }

        # Merge the temporary dictionary with the main dictionary
        merge_dicts(parsed_json_list, temp_device)


if __name__ == "__main__":
    # Download recoveries json from chromiumdash
    urlretrieve("https://chromiumdash.appspot.com/cros/fetch_serving_builds?deviceCategory=ChromeOS",
                filename="./devices.json")

    # load downloaded json
    with open("./devices.json", "r") as f:
        devices_json = json.load(f)

    # load families json
    with open("./device-support/board-families.json", "r") as f:
        board_families = json.load(f)

    # load overrides
    with open("./device-support/devices-overrides.json", "r") as f:
        overrides = json.load(f)

    # parse json
    for family in devices_json["builds"]:
        # some device families are devices themselves
        if "brandNames" in devices_json["builds"][family]:
            parse_device(devices_json["builds"][family], family.strip(), family.strip())
        else:
            for device in devices_json["builds"][family]["models"]:
                parse_device(devices_json["builds"][family]["models"][device], device.strip(), family.strip())

    print(json.dumps(parsed_json_list))

    # remove some broken keys + fix some devices
    parsed_json_list.pop("N/A")  # relm has no proper brandName
    parsed_json_list.pop("w/o")  # anahera has a really broken name

    # anahera has a really broken name:
    anahera_fixed = {
        "HP": {
            "Elite c640 14 inch G3 Chromebook (Enterprise)": {
                "code_name": "anahera",
                "family_name": "brya",
                "cpu_gen": "Alder Lake",
                "supported": True,
                "audio_status": "Unknown",
                "comment": ""
            }
        }
    }
    # merge the fixed anahera device with the main dictionary
    merge_dicts(parsed_json_list, anahera_fixed)

    # save fully parsed json
    with open("./device-support/devices-list.json", "w") as f:
        json.dump(parsed_json_list, f)
