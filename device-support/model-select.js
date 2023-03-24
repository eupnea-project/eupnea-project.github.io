import jsonAuto from "./devices-list.json";

/** @type {HTMLSelectElement}*/
let selectManufacturer;

/** @type {HTMLSelectElement}*/
let selectModel;

function resetSelects() {
    selectManufacturer = document.getElementById("manufacturer");
    selectModel = document.getElementById("model");
}

function displaySupport({ autogen }) {
    const manufacturer = getSelected(selectManufacturer);
    const modelname = getSelected(selectModel);
    const model = autogen[manufacturer][modelname];

    const codename = model.code_name;
    const boardname = model.family_name;
    const platform = model.cpu_gen;

    const info = `CPU Generation: <b>${platform}</b> <br> Codename: <b>${codename} (${boardname})</b>`;

    const depthbootAvailable = model.supported;
    const audioSupport = model.audio_status;
    const comment = model.comment ?? "N/A";

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

export async function initDeviceSupport() {
    resetSelects();

    const data = {
        autogen: jsonAuto,
    };
    updateSelectOptionsWithKeys(selectManufacturer, data.autogen);

    selectManufacturer.oninput = () => {
        updateModels(data.autogen);
        displaySupport(data);
    };
    selectModel.oninput = () => displaySupport(data);

    updateModels(data.autogen);
    displaySupport(data);
}
