# File overview

* device-autogen.json: Automatically generated list, created
  from: https://chromiumdash.appspot.com/cros/fetch_serving_builds?deviceCategory=ChromeOS
* device-overrides.json: Used to override values from the auto-generated list, i.e. for device specific comments.
* board-families.json: Contains all generations, their families, audio support status and an optional family-wide comment.
* devices-list.json: The final list of devices, generated from device-autogen.json and devices-extra.json.
* model-select.js: Json file that is used to generate the model select box on the website.