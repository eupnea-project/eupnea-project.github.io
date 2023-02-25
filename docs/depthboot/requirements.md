# Requirements

* A [supported device](../extra/supported-devices "Eupnea - Supported devices")
* A device to run the script on. **One** of the following:
    * A Chromebook with Crostini enabled(aka "Linux" in settings). **FOLLOW THE INSTRUCTIONS IN
      THE [CROSTINI SECTION](../extra/crostini.md "Eupnea - Crostini instructions")**
    * A Linux pc/laptop(all distros supported)
    * Windows: [Install WSL](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview)
    * MacOS devices are unsupported
    * Non x86_64 devices are incapable of running the builder script without translation layers -> ARM Chromebooks,
      Raspberry Pis and Android devices are not able to build images without translation layers.
* Developer mode enabled on the
  Chromebook ([How to enable developer mode](https://www.androidauthority.com/how-to-enable-developer-mode-on-a-chromebook-906688/))
* A USB drive or SD-card with at least 8GB of storage. A cli image might require even less storage.
* IF not using direct write: 10GB of free storage on the builder device
