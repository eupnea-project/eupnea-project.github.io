/**
 * Because docsify uses a #-history router, global JavaScript identifiers
 * don't get cleared when the same page is visited twice.
 * 
 * As a workaround, the entire script has to be scoped.
 */
function scoped() {
    const jsonSrcAuto = "/device-support/devices-autogen.json";
    const jsonSrcDevice = "/device-support/device-specific.json";
    const jsonSrcFamily = "/device-support/family-specific.json";

    /** @type {HTMLSelectElement}*/
    const selectManufacturer = document.getElementById("manufacturer");

    /** @type {HTMLSelectElement}*/
    const selectModel = document.getElementById("model");

    async function loadJson(src) {
        const response = await fetch(src);
        const content = await response.json();
        return content;
    }

    function displaySupport({ autogen, specDevices, specFamilies }) {
        const manufacturer = getSelected(selectManufacturer);
        const modelname = getSelected(selectModel);
        const model = autogen[manufacturer][modelname];

        const codename = model.code_name;
        const boardname = model.family_name;
        const platform = model.cpu_gen;

        const info = `CPU Generation: <b>${platform}</b> <br> Codename: <b>${codename} (${boardname})</b>`;

        // Find case insensitive key in device-specific.json
        const expcetedKey = codename.toLowerCase();
        let spec = null;
        for (let key in specDevices) {
            if (key.toLowerCase() === expcetedKey) {
                spec = specDevices[key];
                break;
            }
        }

        const depthbootAvailable = model.arch === "x86_64";
        const audioSupport = spec?.audio_status ?? specFamilies[platform] ?? "Unknown";
        const comment = spec?.comment ?? "N/A";

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
        const data = {
            autogen: await loadJson(jsonSrcAuto),
            specDevices: await loadJson(jsonSrcDevice),
            specFamilies: await loadJson(jsonSrcFamily)
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

    initDeviceSupport();

}

scoped();