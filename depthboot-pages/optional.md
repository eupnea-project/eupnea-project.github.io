# Optional features

## Install to internal storage

This will wipe ChromeOS(or any other installed OS) from the internal drive. It will always be possible
to [restore ChromeOS using a recovery USB](https://support.google.com/chromebook/answer/1080595?hl=en) afterwards.

It's recommended to [set up audio](/depthboot-pages/audio.md) and confirm all hardware is working correctly(touchpad,
touchscreen, speakers) before proceeding.

To install to internal storage, run: ``install-to-internal`` in a terminal.

## ZRAM

Due to most Chromebook running on eMMC storage, it is not recommended to use swap as the high amount of writes will wear
out the storage faster. Instead, ZRAM can be used to create a swap-like partition in RAM.
ZRAM works by compressing the physical RAM, thereby creating more virtual RAM. When the data is needed again, it is
decompressed by the cpu. This allows applications to use more RAM than physically available, but comes at the cost of
slight CPU performance.

The commands below will create 6GB of memory compressed to 2GB:

**WIP, commands below are broken!**

1. ~~``sudo modprobe zram``~~
2. ~~``SIZE=6144 # change the size here for more/less virtual ram``~~
3. ~~``sudo echo $(($SIZE*1024*1024)) > /sys/block/zram0/disksize``~~
4. ~~``sudo mkswap /dev/zram0``~~
5. ~~``sudo swapon /dev/zram0 -p 10``~~

## Fan control(ectool):

WIP  
(Copy the ectool from a ChromeOS iso for now)

