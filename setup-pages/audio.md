# Audio

To enable audio on Depthboot, follow the instructions below:

1. Boot into Depthboot

2. Make sure you are connected to the internet.

- Skylake, Kaby Lake, or Coffee Lake (7th/8th Gen Intel CPU):
    1. Switch to alt kernel by running: ``update-kernel --alt`` in the Terminal.
    2. Run ``setup-audio`` in the Terminal.
    3. Reboot
- Everything else:
    1. Run: `setup-audio` in the Terminal.
    2. Reboot Depthboot

If audio still doesn't work, please open an issue with your device codename and distro.
