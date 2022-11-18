const jsonSrcSpecific = "/device-support/device-specific.json";
const jsonSrcAuto = "/device-support/devices-autogen.json";

/** @type {HTMLSelectElement}*/
const selectManufacturer = document.getElementById("manufacturer");

/** @type {HTMLSelectElement}*/
const selectModel = document.getElementById("model");

async function loadJson(src) {
    const response = await fetch(src);
    const content = await response.json();
    return content;
}

function displaySupport(autogen, specifics) {
    const manufacturer = getSelected(selectManufacturer);
    const modelname = getSelected(selectModel);
    const model = autogen[manufacturer][modelname];

    const codename = model.code_name;
    const boardname = model.family_name;
    const platform = model.cpu_gen;

    const info = `CPU Generation: <b>${platform}</b> <br> Codename: <b>${codename} (${boardname})</b>`;

    const spec = specifics[codename];

    const depthbootAvailable = model.arch === "x86_64";
    const audioSupport = spec?.audio_status ?? "Unknown";
    const comment = spec?.comment ?? "";

    document.getElementById("deviceInfo").innerHTML = info;
    document.getElementById("deviceDepthboot").innerText = depthbootAvailable ? "Yes" : "No";
    document.getElementById("deviceAudio").innerText = audioSupport;
    document.getElementById("deviceComment").innerText = comment;
}

function updateModels(json) {
    const manufacturer = getSelected(selectManufacturer);
    updateSelectOptionsWithKeys(selectModel, json[manufacturer]);
}

/**
 * Replaces the options of a `select` element with the keys of `obj`.
 * @param {HTMLSelectElement} select
 */
function updateSelectOptionsWithKeys(select, obj) {
    for (let i = select.options.length - 1; i >= 0; i--) {
        select.options.remove(i);
    }

    // Insert new option elements from `obj`
    const keys = Object.keys(obj).sort();
    for (const key of keys) {
        const elem = document.createElement("option");
        elem.value = key;
        elem.text = key;
        select.options.add(elem);
    }
}

/** @param {HTMLSelectElement} selectElem */
function getSelected(selectElem) {
    return selectElem.options[selectElem.selectedIndex].value;
}

async function initDeviceSupport() {
    const auto = await loadJson(jsonSrcAuto);
    const specific = await loadJson(jsonSrcSpecific);
    updateSelectOptionsWithKeys(selectManufacturer, auto);

    selectManufacturer.oninput = () => {
        updateModels(auto);
        displaySupport(auto, specific);
    };
    selectModel.oninput = () => displaySupport(auto, specific);

    updateModels(auto);
    displaySupport(auto, specific);
}

initDeviceSupport();