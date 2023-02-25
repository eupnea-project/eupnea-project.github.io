# Eupnea kernels

Both EupneaOS and Depthboot use the same precompiled kernel binaries, which are build using GitHub Actions.
The GPL permits distributing binaries, as long as the source code is provided. The following components are precompiled
and distributed:

* A Linux kernel executable (bzImage/vmlinuz)
* A tar archive of the kernel modules
* A tar archive of the kernel headers

The source of the kernel, modules and headers of the kernel executable:

* [ChromeOS kernel](https://chromium.googlesource.com/chromiumos/third_party/kernel)
  -> [ChromeOS Eupnea kernel](https://github.com/eupnea-linux/chromeos-kernel)
* [Mainline Linux kernel](https://github.com/torvalds/linux)
  -> [Mainline Eupnea kernel](https://github.com/eupnea-linux/mainline-kernel)

## ChromeOS-Eupnea kernel

The ChromeOS-Eupnea kernel is a modified version of the ChromeOS 5.10 kernel, which itself is a modified version of the
upstream 5.10 Linux kernel with some backported patches from newer kernel versions. The ChromeOS kernel is the newest
kernel used in Chromebooks, despite not being the newest Linux kernel and not even the newest ChromeOS kernel version (
the ChromeOS kernel repo contains 5.15 and even 6.1 branches).

Some devices require the ChromeOS kernel due to better AVS (Intel audio driver used by some Skylake and Kaby Lake
devices) support, although the Mainline kernel should soon receive more AVS support too.

## Mainline-Eupnea kernel

The Mainline kernel is the default Eupnea kernel.
The Mainline-Eupnea kernel is the upstream stable kernel with a custom config. The Mainline kernel has the most
features, although some Chromebooks might experience hardware issues with it and should use the ChromeOS kernel instead.
