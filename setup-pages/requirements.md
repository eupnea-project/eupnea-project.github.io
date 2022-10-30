## Requirements: 
* A supported device, see [below](#supported-devices).
* A device to build the image. One of the following:
  * A Chromebook with Crostini enabled(aka "Linux" in settings).
  * A Linux pc/laptop(all distros supported)
  * Windows: [Install WSL](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview).
  * Apple devices support is unknown.
  * Android with Termux is not supported
* Developer mode enabled on your chromebook([How to enable developer mode](https://www.androidauthority.com/how-to-enable-developer-mode-on-a-chromebook-906688/))
* A USB drive or SD-card with at least 8GB of storage. 
* IF not using direct write: 10GB of free space on the builder device

## Supported devices
All 64-bit(x86_64) Intel/AMD Chromebooks are able to at least boot Depthboot. Audio support varies from non-existent to full support.

[Full list of Chromebooks and their CPU Generations](https://mrchromebox.tech/#devices)

### Intel

* Amber Lake, Whiskey Lake (-UE CPUs), and Skylake
  * All peripherals supported, audio may need extra modules
* Apollo Lake, Gemini Lake, Comet Lake, Jasper Lake, Tiger Lake, Alder Lake
  * All peripherals supported

### AMD

* Stoneyridge
  * All peripherals supported except audio
  * (These Chromebooks are unable to handle Windows on custom UEFI firmware)
* Picasso/Dali
  * All peripherals supported except audio(WIP)
