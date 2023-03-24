---
prev: false
next: false

title: Troubleshooting
---

**DISCLAIMER: IF YOU GET AN ERROR/DO NOT GET A SUCCESS MESSAGE WHILE RUNNING ANY SCRIPT FROM THE EUPNEA PROJECT, PLEASE
REPORT IT ON GITHUB/DISCORD/REVOLT.**

## Depthboot won't boot for the first time

1. Make sure your device is [supported](/docs/depthboot/supported-devices).

2. Make sure [developer mode](https://www.androidauthority.com/how-to-enable-developer-mode-on-a-chromebook-906688/) is
   enabled.

3. Make sure you are **<font size="3">NOT</font>** trying to boot
   via [UEFI](/docs/extra/faq#i-have-uefi-custom-bios-installed-on-my-chromebook)
   or [RW_LEGACY](/docs/extra/faq#i-have-rw-legacy-installed-on-my-chromebook). You need to use Ctrl+U or select "Boot
   from external media" in the boot menu.

4. If the Chromebook beeps when pressing ctrl+U, make sure that
   the [crossflags in STEP 5](/docs/depthboot/build-instructions) were set correctly.

5. Rebuild the Depthboot image and reflash it to another external media(USB, SD Card, etc).

## Depthboot won't boot after an update

1. Immediately report the issue on GitHub/Discord/Revolt.
2. [Use the reserve kernel](/docs/project/kernels#reserve-kernel) to boot into Depthboot.

## Chromebook shows recovery screen

If you see the recovery screen, that means that your Chromebook may have exited developer mode. Reinstall Chrome OS and
re-enable developer mode before reinstalling Depthboot.
