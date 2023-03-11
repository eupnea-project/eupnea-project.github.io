---
prev: false
next: false

title: Troubleshooting
---
## Depthboot won't Boot From External Media
- Make sure your device is [supported](https://eupnea-linux.github.io/docs/depthboot/supported-devices) (ARM Chromebooks are not supported).

- If your Chromebook beeps, make sure that the [flags](https://eupnea-linux.github.io/docs/depthboot/build-instructions) were set correctly.

- Recreate your Depthboot Image and reflash with the same program you used.

- Use a different External Media (USB, SD Card, etc).

- UEFI and RW_Legacy are not supported by Depthboot.



## Depthboot won't Boot From Internal

- If it won't boot after installing to internal, try reinstalling again.
Try Using a Different Depthboot Image.

- If it won't boot after a eupnea update, try to attempt to use the [backup kernel](https://eupnea-linux.github.io/faq#using-the-backup-kernel).

- If it won't boot due to an unrelated update, backup all files and reinstall Depthboot.

## Using The Backup Kernel

To use the backup kernel, Boot from an External Media containing Depthboot and Open the Terminal.

Run the Following Command:
```shell
lsblk
```
It should list all storage devices connected, and find your internal drive (it doesn't have a mount point and isn't zram).

Find the first partition of your drive, replace the 'placeholder' in the following command with the partition name, and run it.

```shell
dd if=/dev/zero of=/dev/placeholder
```
Wait until the command finishes, then restart and boot from internal.



## Chromebook Shows Recovery Screen
- If it shows the recovery screen, that means that your Chromebook may have exited developer mode.
- You have to reinstall Chrome OS to reinstall Depthboot again.
- If possible, backup all files on your drive on another device.

## Audio Doesnt Work

- Make sure you followed the steps [here](https://eupnea-linux.github.io/docs/depthboot/audio).

## None of these work for me / I need additional support

- Contact the Eupnea OS Team by making a Github Issue or use the official [discord](https://discord.gg/jxXb2PwzYz) or [revolt](https://rvlt.gg/6YxHB2Cz) servers.

