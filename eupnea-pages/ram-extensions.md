## Ram extensions: swap and zram

It is not recommended to use swap on most Chromebooks, as the high amount of writes will quickly wear out the eMMC
storage which might result in drive failure. An alternative solution is to use zram, which creates a swap-like
partition in RAM by compressing physical RAM to create more virtual RAM. When the data is needed again, it is
decompressed by the CPU. This allows applications to use more RAM than is physically available, but it can come at the
cost of slightly reduced CPU performance.
Both EupneaOS and Depthboot come with zram enabled and configured by default.