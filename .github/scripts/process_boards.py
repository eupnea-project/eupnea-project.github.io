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
    print(device["brandNames"])
    names_list = []
    for temp_name in device["brandNames"]:
        names_list.extend(iter(temp_name.split(",")))
    for name in names_list:
        cpu_gen = ""
        for _generation in cpu_gen_json:
            if family_name in cpu_gen_json[_generation]["families"]:
                cpu_gen = _generation
                break
        if not cpu_gen:
            print(f"Unknown generation for device: {family_name}")
            cpu_gen = "Unknown"
        temp_device = {
            name.split(" ")[0].strip(): {
                name[name.find(" ") + 1:].strip(): {
                    "code_name": device_name.strip(),
                    "family_name": family_name.strip(),
                    # all x86_64 devices are generally supported. Special cases are handled in the devices-extra file
                    "cpu_gen": cpu_gen,
                    "supported": cpu_gen_json[cpu_gen]["arch"] == "x86_64",
                }
            }
        }
        merge_dicts(parsed_json_list, temp_device)


if __name__ == "__main__":
    # Download recoveries json from chromiumdash
    urlretrieve("https://chromiumdash.appspot.com/cros/fetch_serving_builds?deviceCategory=ChromeOS",
                filename="./devices.json")

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

    exit()

    with open("./device-support/devices-autogen.json", "w") as f:
        json.dump(parsed_json_list, f)

    # combine autogen and extra into one json file
    with open("./device-support/devices-extra.json", "r") as f:
        extra = json.load(f)
    merge_dicts(parsed_json_list, extra)
    with open("./device-support/devices-list.json", "w") as f:
        json.dump(parsed_json_list, f)
