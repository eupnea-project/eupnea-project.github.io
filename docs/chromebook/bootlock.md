---
prev: false
---

# Sleep bootlock

When the lid is closed or the system is idle for a long time, Linux distributions tend to sleep to S3(Suspend-to-RAM).
On a Chromebook this triggers an NVRAM reset and forces the Chromebook to boot into an operating system with an
officially signed kernel(only ChromeOS has one). It is not possible to re-enable USB and unsigned kernel booting without
booting into ChromeOS(neither Depthboot nor EupneaOS(except on UEFI) can be booted without those flags).

To fix this, the systemd config file for power and sleep is overwritten to sleep to S0. Sleeping to S0 is slightly
less power efficient, but prevents the aforementioned NVRAM reset.

Note: This behavior is only present when booting from USB/SD-card. If you boot from internal storage, the NVRAM reset
will not trigger.

External sleep states [here](https://www.kernel.org/doc/Documentation/power/states.txt).