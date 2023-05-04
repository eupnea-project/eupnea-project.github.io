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
            name.split(" ")[0].strip().lower().capitalize(): {  # capitalize only the first letter of brand name
                name[name.find(" ") + 1:].strip(): {
                    # if override value exists, use it, else use scraped value
                    "code_name": device_name,
                    "family_name": overrides.get(device_name, {}).get("family_name", family_name),
                    "cpu_gen": overrides.get(device_name, {}).get("cpu_gen", cpu_gen),
                    "supported": overrides.get(device_name, {}).get("supported",
                                                                    board_families[cpu_gen]["arch"] == "x86_64"),
                    "audio_status": overrides.get(device_name, {}).get("audio_status",
                                                                       board_families[cpu_gen]["audio_status"]),
                    "comment": overrides.get(device_name, {}).get("comment", "N/A"),
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
    parsed_json_list.pop("N/a")  # relm is an unknown device
    parsed_json_list.pop("Consumer")  # expresso (the device, not the family) is an unknown device
    parsed_json_list.pop("Education")  # enguarde (the device, not the family) is an unknown device
    parsed_json_list.pop("W/o")  # anahera has a really broken name
    parsed_json_list.pop("100e")  # missing the lenovo brand at the beginning -> wrong sorting
    parsed_json_list.pop("Cx1101cma")  # missing asus brand at the beginning -> wrong sorting
    parsed_json_list.pop("Cx1400fka")  # missing asus brand at the beginning -> wrong sorting
    parsed_json_list.pop("Cx1500fka")  # missing asus brand at the beginning -> wrong sorting

    # manually fix some devices
    # anahera has a really broken name:
    fixed_devices = {
        "Hp": {
            "Elite c640 14 inch G3 Chromebook (Enterprise)": {
                "code_name": "anahera",
                "family_name": "brya",
                "cpu_gen": "Alder Lake",
                "supported": True,
                "audio_status": "Unknown",
                "comment": ""
            },
            # these devices names overlap -> separate them
            "Chromebook x360 14c (10th gen)": {
                "audio_status": "Full",
                "code_name": "dragonair",
                "comment": "N/A",
                "cpu_gen": "Cometlake-U",
                "family_name": "hatch",
                "supported": True
            },
            "Chromebook x360 14c (11th gen)": {
                "audio_status": "Full",
                "code_name": "eldrid",
                "comment": "N/A",
                "cpu_gen": "TigerLake-UP3",
                "family_name": "volteer",
                "supported": True
            }
        },
        # These Lenovo cbs are missing the Lenovo brand at the beginning -> wrong sorting
        "Lenovo": {
            "100e Chromebook Gen 3": {
                "audio_status": "Full",
                "code_name": "bookem",
                "comment": "N/A",
                "cpu_gen": "Jasper Lake",
                "family_name": "dedede",
                "supported": True
            },
            "100e Chromebook Gen 2": {
                "audio_status": "Unsupported",
                "code_name": "treeya",
                "comment": "N/A",
                "cpu_gen": "Stoney Ridge",
                "family_name": "grunt",
                "supported": True
            }
        },
        # These Asus cbs are missing the Lenovo brand at the beginning -> wrong sorting
        "Asus": {
            "Chromebook Cx1101cma": {
                "audio_status": "Full",
                "code_name": "apele",
                "comment": "N/A",
                "cpu_gen": "Gemini Lake",
                "family_name": "octopus",
                "supported": True
            },
            "Chromebook CX1400fka": {
                "audio_status": "Full",
                "code_name": "galtic360",
                "comment": "N/A",
                "cpu_gen": "Jasper Lake",
                "family_name": "dedede",
                "supported": True
            },
            "Chromebook CX1500fka": {
                "audio_status": "Full",
                "code_name": "galith360",
                "comment": "N/A",
                "cpu_gen": "Jasper Lake",
                "family_name": "dedede",
                "supported": True
            }
        },
        "Samsung": {}  # add Samsung here, so we can add devices to it later
    }

    # remove old Chromebook x360 14c entry
    parsed_json_list["Hp"].pop("Chromebook x360 14c")

    # move all IdeaPads to Lenovo
    for device in parsed_json_list["Ideapad"]:
        fixed_devices["Lenovo"][f"IdeaPad {device}"] = parsed_json_list["Ideapad"][device]
    # move all ThinkPads to Lenovo
    for device in parsed_json_list["Thinkpad"]:
        fixed_devices["Lenovo"][f"ThinkPad {device}"] = parsed_json_list["Thinkpad"][device]
    # remove ideaPads and ThinkPads
    parsed_json_list.pop("Ideapad")
    parsed_json_list.pop("Thinkpad")

    # some HP cbs are missing the HP brand at the beginning -> wrong sorting
    for device in parsed_json_list["Chromebook"]:
        fixed_devices["Hp"][f"Chromebook {device}"] = parsed_json_list["Chromebook"][device]
    parsed_json_list.pop("Chromebook")  # remove broken entry

    # Some Galaxy cbs are missing the Samsung brand at the beginning -> wrong sorting
    for device in parsed_json_list["Galaxy"]:
        fixed_devices["Samsung"][f"Galaxy {device}"] = parsed_json_list["Galaxy"][device]
    parsed_json_list.pop("Galaxy")  # remove broken entry

    # merge the fixed devices with the main dictionary
    merge_dicts(parsed_json_list, fixed_devices)

    # save fully parsed json
    with open("./device-support/devices-list.json", "w") as f:
        json.dump(parsed_json_list, f, indent=2, sort_keys=True)
