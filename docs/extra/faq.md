---
prev: false
next: false

title: Frequently Asked Questions
---

# FAQ

Frequently asked questions (and answers) regarding the Eupnea Project.

## Will Depthboot/EupneaOS remove my ChromeOS installation?

Only if you choose to do so. Neither Depthboot nor EupneaOS will remove your ChromeOS installation, unless you
explicitly choose to do so.

## When will EupneaOS be ready?

We don't know. We are working on it, but we have no ETA.

## What is the difference between the Mainline kernel and the ChromeOS kernel?

Here is a full page comparing the two kernels: [Eupnea Kernels](/docs/project/kernels)

## How do I use the backup kernel?

To use the backup kernel, Open the Terminal and run this command.

```shell
lsblk
```

Find the first partition name on the drive you want to use the backup kernel on, replace the 'placeholder' in the following command with the partition name, and run it.

```shell
dd if=/dev/zero of=/dev/placeholder
```

## I have UEFI/Custom BIOS installed on my Chromebook

If you have completely replaced your Chromebooks firmware with a custom BIOS/UEFI, you will not be able to boot
Depthboot. You can however still boot EupneaOS.
To be able to boot Depthboot, you will need to revert your firmware to stock.

## I have RW_Legacy installed on my Chromebook

Installation of rw_legacy/alt_fw that can be accessed with ctrl+L/"Select alternate bootloader" does not affect
your Chromebooks ability to boot Depthboot. Just follow the instructions as usual.

## UEFI vs RW_LEGACY vs Depthboot vs EupneaOS?

Read all pros and ons of each method of booting Linux on a Chromebook [here](/docs/chromebook/firmware-comparison).

## Are the Depthboot distros modified?

Yes, but only the minimal amount required to make them bootable and work properly on Chromebooks (Kernel + minor
configs).  
In addition to installing some packages from the distro's repo, our own repo is added to the distro, which contains the
eupnea-utils and eupnea-system packages (and some others). You can read more about the packages in the respective
repos.  
Nothing else is modified, i.e. all distro "quirks" are kept intact (Snap, no Tap-to-click by default on GNOME, etc.).

## Why is sharing Depthboot images illegal?

The Depthboot base distros all allow image/iso/rootfs sharing, but only in an unmodified form. The Depthboot script
customizes some internal distro behavior (for example it [disables deep sleep](/docs/chromebook/bootlock)) and
thereby creates modified images.
To allow modified images to be shared, all trademarked content would have to be removed, i.e. all Distro logos.

## Why is sharing EupneaOS images illegal?

EupneaOS does not have the same restrictions as the Depthboot base distros, as all trademarked content has been removed.
The Eupnea Project disallows sharing of EupneaOS images, to prevent unofficial modded versions from being distributed.
If you want to create a fork of EupneaOS, remove all EupneaOS branding, i.e. the name and logos.

## Does the Eupnea Project collect any telemetry?

No, setting up telemetry services is too much work.  
Keep in mind that the distros themselves might collect telemetry and send it to their respective
developers.
