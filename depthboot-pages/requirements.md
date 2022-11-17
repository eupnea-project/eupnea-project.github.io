# Requirements

* A supported device, see [below](#supported-devices)
* A device to run the script on. **One** of the following:
    * A Chromebook with Crostini enabled(aka "Linux" in settings). **FOLLOW THE INSTRUCTIONS IN
      THE [CROSTINI SECTION](/extra-pages/crostini.md)**
    * A Linux pc/laptop(all distros supported)
    * Windows: [Install WSL](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview)
    * MacOS devices are unsupported
    * Android with Termux is not supported. (Might be possible with root)
* Developer mode enabled on the
  Chromebook([How to enable developer mode](https://www.androidauthority.com/how-to-enable-developer-mode-on-a-chromebook-906688/))
* A USB drive or SD-card with at least 8GB of storage
* IF not using direct write: 10GB of free storage on the builder device

## Supported devices

<label>
  Manufacturer
  <select id="manufacturer"></select>
</label>
<label>
  Model
  <select id="model"></select>
</label>

<i id="deviceInfo"></i>

Can boot Depthboot: <b id="deviceDepthboot"></b><br>
Audio support: <b id="deviceAudio"></b><br>
Other issues: <span id="deviceComment"></span>

<script src="device-support.js"></script>