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

All 64-bit(x86_64) Intel/AMD Chromebooks are able to at least boot Depthboot. Audio support varies from non-existent to
full support.

[Full list of Chromebooks and their CPU Generations](https://mrchromebox.tech/#devices)

### Intel

* Skylake and Kabylake
    * All peripherals supported except audio
* Apollo Lake, Gemini Lake, Comet Lake, Jasper Lake, Tiger Lake, Alder Lake
    * All peripherals supported

### AMD

* Stoneyridge
    * All peripherals supported except audio and gpu framebuffer
* Picasso/Dali
    * All peripherals supported
