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
        (_generation for _generation in cpu_gen_json if family_name in cpu_gen_json[_generation]["families"]),
        "Unknown")

    # If CPU generation not found, print a warning
    if cpu_gen == "Unknown":
        print(f"Unknown generation for device: {family_name}")

    # Create temporary device dictionary with relevant information
    for name in names_list:
        temp_device = {
            name.split(" ")[0].strip(): {
                name[name.find(" ") + 1:].strip(): {
                    "code_name": device_name.strip(),
                    "family_name": family_name.strip(),
                    "cpu_gen": cpu_gen,
                    "supported": cpu_gen_json[cpu_gen]["arch"] == "x86_64",
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

    # load cpu-generations json
    with open("./cpu_generations.json", "r") as f:
        cpu_gen_json = json.load(f)

    # parse json
    for family in devices_json["builds"]:
        # some device families are devices themselves
        if "brandNames" in devices_json["builds"][family]:
            parse_device(devices_json["builds"][family], family, family)
        else:
            for device in devices_json["builds"][family]["models"]:
                parse_device(devices_json["builds"][family]["models"][device], device, family)

    print(json.dumps(parsed_json_list))

    with open("./devices-autogen.json", "w") as f:
        json.dump(parsed_json_list, f)
    exit()

    # combine autogen and extra into one json file
    with open("./device-support/devices-extra.json", "r") as f:
        extra = json.load(f)
    merge_dicts(parsed_json_list, extra)
    with open("./device-support/devices-list.json", "w") as f:
        json.dump(parsed_json_list, f)
