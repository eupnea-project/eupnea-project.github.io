# Bootlock

When the lid closes or the system is idle for a long time, Linux distributions tend to sleep to S1. This triggers an NVRAM reset and forces the chromebook to boot into an operating system with an officially signed kernel (only ChromeOS has one). Once booted into ChromeOS, one can re-enable USB and unsigned kernel booting to boot Eupnea again.

This is really problematic as going into sleep doesn't properly work and if ChromeOS has been wiped, one cannot re-enable USB and Unsigned kernel booting without it.

To fix this, the systemd config file for power and sleep had to be overriden to sleep to S3. Sleeping to S3 is slightly less power efficient, but prevents the aforementioned NVRAM reset.
