# Depthcharge

Depthcharge is a [U-boot](https://www.denx.de/wiki/U-Boot) based bootloader for Chromebooks. Depthcharge is not a BIOS,
nor is it ever meant to be accessed by the end user. As a result, Depthcharge is basically an embedded-systems
bootloader.

## Issues with depthcharge

* No initramfs support -> Much simpler Linux boot flow but also no initramfs features like full disk encryption
* No bootloader -> no dual booting or other bootloader features
* Unusual GPT partitioning scheme -> [issues with Rufus](/extra-pages/rufus.md)