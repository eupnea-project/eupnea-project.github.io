## Building the ChromeOS Kernel

The [image build script](https://github.com/eupnea-linux/eupnea/blob/main/build.py) of Eupnea downloads two precompiled binaries:

* The Linux Kernel Executable (vmlinuz/bzImage)
* A Tar Archive of the kernel modules

These binaries are compiled using Github Actions and require a powerful computer and at least an hour of compilation. The GPL permits distributing binaries, as long as you give the source code of them. The source of the kernel and modules is [here](https://chromium.googlesource.com/chromiumos/third_party/kernel).
