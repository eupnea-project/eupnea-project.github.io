---
prev: false
next: false

title: Troubleshooting
---
## Depthboot Wont Boot From Externel Media
Make sure you device is [supported](https://eupnea-linux.github.io/docs/depthboot/supported-devices) (ARM Chromebooks are not supported).

If your Chromebook beeps, make sure that the [flags](https://eupnea-linux.github.io/docs/depthboot/build-instructions) were set correctly.

Recreate your Depthboot Image and reflash with the same program you used.

Use a different Externel Media (USB, SD Card, etc).

UEFI and RW_Legacy are not supported by depthboot.



## Depthboot Wont Boot From Internel

If it wont boot after installing to internel, try reinstalling again.
Try Using a Different Depthboot Image.

If it wont boot after an eupnea update, try to attempt to use the backup kernel.


## Using Backup Kernel


To use the backup kernel, Boot from an Externel Media containing Depthboot and Open the Terminal.
Dont mount your Internel Drive,

Run the Following Command:
```shell
lsblk
```
It should list all storage devices connected, find your internel drive (it doesnt have a mount point and isnt zram).

Find the first partition of your drive, replace the 'placeholder' in the following command with the partition name, and run it.

```shell
dd if=/dev/zero of=/dev/placeholder
```
Wait until the command finishes, then restart and boot from internel.

If it broke due to an unrealated update, backup all files and reinstall depthboot.



## Chromebook Shows Recovery Screen
If it shows the recovery screen, that means that your Chromebook may have exited developer mode.
You have to reinstall chrome os to reinstall depthboot again.
If possible, backup all files of your drive on an another device.



## None of these work for me

Contact the Eupnea OS Team by making a Github Issue or use the official [discord](https://discord.gg/jxXb2PwzYz) or [revolt](https://rvlt.gg/6YxHB2Cz) servers.
