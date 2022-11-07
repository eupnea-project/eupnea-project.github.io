## Eupnea kernels

Both EupneaOS and Depthboot use the same precompiled kernel binaries, which are build using GitHub Actions and require a
lot of processing power and at least an hour of compilation. The GPL permits distributing binaries, as long as the
source code is provided. The following components are precompiled and distributed:

* A Linux kernel executable (bzImage)
* A tar archive of the kernel modules
* A tar archive of the kernel headers

The source of the kernel, modules and headers of the kernel executable:

* [ChromeOS kernel](https://chromium.googlesource.com/chromiumos/third_party/kernel)
  -> [ChromeOS Eupnea kernel](https://github.com/eupnea-linux/kernel)
* [Mainline Linux kernel](https://github.com/torvalds/linux)
  -> [Mainline Eupnea kernel](https://github.com/eupnea-linux/mainline-kernel)

