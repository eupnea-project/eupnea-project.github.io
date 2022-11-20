# Eupnea kernels

Both EupneaOS and Depthboot use the same precompiled kernel binaries, which are build using GitHub Actions and require a
lot of processing power and at least an hour of compilation. The GPL permits distributing binaries, as long as the
source code is provided. The following components are precompiled and distributed:

* A Linux kernel executable (bzImage)
* A tar archive of the kernel modules
* A tar archive of the kernel headers

The source of the kernel, modules and headers of the kernel executable:

* [ChromeOS kernel](https://chromium.googlesource.com/chromiumos/third_party/kernel)
  -> [ChromeOS Eupnea kernel](https://github.com/eupnea-linux/chromeos-kernel)
* [Mainline Linux kernel](https://github.com/torvalds/linux)
  -> [Mainline Eupnea kernel](https://github.com/eupnea-linux/mainline-kernel)

## Kernel types

There are 5 different kernel types that can be used in Depthboot and EupneaOS:

* ChromeOS
    * Stable(chromeos-5.10):
        * Newest kernel used in Chromebooks, although it is pretty old by mainline kernel standards. Provides the best
          compatibility for Chromebooks, although it might not have the newest features(although Google does backport
          some).
    * Experimental(chromeos-5.15):
        * A more recent kernel, but not actively used on any Chromebooks. It is unclear why Google is developing this
          kernel if its not used by any device and moreover will be soon superseded by the 6.0 kernel.
    * Alternative(chromeos-5.10):
        * An older chromeos 5.10 kernel branch, which provides more compatibility for older devices, as the newer
          branches of the same kernel broke audio support for some devices.
* Mainline
    * Mainline:
        * Latest stable linux kernel with some Chromebook patches applied. Provides the newest features, but might not
          work on all devices.
    * Mainline-testing:
        * Latest mainline linux kernel with some Chromebook patches applied. Provides the newest features, but might not
          work on all devices. Might be unstable.