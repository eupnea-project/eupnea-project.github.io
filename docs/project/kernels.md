---
prev: false
---

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

The ChromeOS-Eupnea kernel is a slightly modified version of the ChromeOS 5.10 kernel, which itself is a modified
version of the upstream 5.10 Linux kernel with some backported patches from newer kernel versions. The ChromeOS kernel
is the newest kernel used in Chromebooks, despite not being the newest Linux kernel and not even the newest ChromeOS
kernel version (the ChromeOS kernel repo contains 5.15 and even 6.1 branches).

Some devices require the ChromeOS kernel due to better AVS (Intel audio driver used by some Skylake and Kaby Lake
devices) support, although the Mainline kernel should soon receive more AVS support too.

## Mainline-Eupnea kernel

The Mainline kernel is the default Eupnea kernel.
The Mainline-Eupnea kernel is the upstream stable kernel with a custom config. The Mainline kernel has the most
features, although some Chromebooks might experience hardware issues with it and should use the ChromeOS kernel instead.

## Reserve kernel

All Depthboot systems have a reserve kernel which can be used to boot into Depthboot if the main kernel fails to boot.

1. Boot into ChromeOS or use an external media with Depthboot(a cli image is enough).
    1. If on ChromeOS: press <kbd>CTRL</kbd><kbd>ALT</kbd><kbd>T</kbd>, type `shell` and press <kbd>Enter</kbd>.
2. Run `lsblk` to list all connected storage devices
3. Find the internal/external drive. It will be listed as `/dev/sdX` or `/dev/mmcblkX` or `/dev/nvmeXnY`.
    1. Run `sudo dd if=/dev/zero of=/dev/sdX1` if you have a USB and found a drive with the name `/dev/sdX`
    2. OR
    3. Run `sudo dd if=/dev/zero of=/dev/mmcblkXp1`/`sudo dd if=/dev/zero of=/dev/nvmeXnYp1`(NOTICE THE "P") if you have
       an SD-Card or an internal drive and found a drive with the name `/dev/mmcblkX` or `/dev/nvmeXnY`
4. Wait until the command finishes, then restart and boot from the internal/external drive you just modified.
