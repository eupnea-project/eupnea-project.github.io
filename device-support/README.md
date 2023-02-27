# File overview

* device-autogen.json: Automatically generated list, scraped
  from https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/
* devices-extra.json: Devices that Google does not have in their list/edit errors from the Google list. Is applied over
  device-autogen.json and combined into devices-list.json.
* devices-list.json: The final list of devices, generated from device-autogen.json and devices-extra.json.
* device-specific.json: Device-specific information, such as audio problems. Also used for manually marking unsupported
  devices.
* family-specific.json: Same as device-specific.json, but for families of devices.
* model-select.js: Json file that is used to generate the model select box on the website.