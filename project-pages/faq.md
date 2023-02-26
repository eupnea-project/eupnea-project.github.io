# FAQ

### I have UEFI/Custom BIOS installed on my Chromebook
If you have completely replaced your Chromebooks firmware with a custom BIOS/UEFI, you will not be able to boot
Depthboot. You can however still boot EupneaOS.
To be able to boot Depthboot, you will need to revert your firmware to stock.

### I have RW_Legacy installed on my Chromebook
Installation of rw_legacy/alt_fw that can be accessed with ctrl+L/"Select alternate bootloader" does not affect 
your Chromebooks ability to boot Depthboot. Just follow the instructions as usual.

### Will Depthboot/EupneaOS remove my ChromeOS installation?

Only if you choose to do so. Neither Depthboot nor EupneaOS will remove your ChromeOS installation, unless you
explicitly choose to do so.

### When will EupneaOS be ready?

We don't know. We are working on it, but we have no ETA.

### Why is sharing Depthboot images illegal?

The Depthboot base distros all allow image/iso/rootfs sharing, but only in an unmodified form. The Depthboot script
customizes some internal distro behavior (for example it [disables deep sleep](/chromebook-pages/bootlock.md)) and
thereby creates modified images.
To allow modified images to be shared, all trademarked content would have to be removed, i.e. all Distro logos.

### Why is sharing EupneaOS images illegal?

EupneaOS does not have the same restrictions as the Depthboot base distros, as all trademarked content has been removed.
The Eupnea Project disallows sharing of EupneaOS images, to prevent unofficial modded versions from being distributed.
If you want to create a fork of EupneaOS, remove all EupneaOS branding, i.e. the name and logos. 
