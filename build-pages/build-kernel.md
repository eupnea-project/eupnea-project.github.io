# Building a custom kernel

* Download the latest pre-compiled Eupnea ChromeOS kernel [here](https://github.com/eupnea-linux/kernel/releases/latest)
* Download the latest pre-compiled Eupnea mainline
  kernel [here](https://github.com/eupnea-linux/mainline-kernel/releases/latest)

## Building the Eupnea ChromeOS kernel

1. Install dependencies:
    * make
    * automake
    * gcc
    * gcc c++
    * kernel development libraries
    * ncurses development library
    * xz utils
    * OpenSSL development libraries
    * GNU bc
    * flex
    * libelf1 development libraries
    * bison
    * binutils

   On debian based systems the dependencies can be installed with:

        sudo apt-get update && sudo apt-get install build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison binutils

2. Clone the kernel repo:

        git clone https://github.com/eupnea-linux/kernel.git && cd kernel

3. Optional: Modify the kernel config in ``kernel-version.conf``.
4. Start the build script: ``python3 ./kernel_build.py kernel-version``.
5. The compiled/compressed files can be found in the root of the cloned repo:
    * bzImage-*version*
    * modules-*version*.tar.xz
    * headers-*version*.tar.xz

## Building the Eupnea mainline kernel

1. Install dependencies:
    * make
    * automake
    * gcc
    * gcc c++
    * kernel development libraries
    * ncurses development library
    * xz utils
    * OpenSSL development libraries
    * GNU bc
    * flex
    * libelf1 development libraries
    * bison
    * binutils

   On debian based systems the dependencies can be installed with:

        sudo apt-get update && sudo apt-get install build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison binutils

2. Clone the kernel repo:

        git clone https://github.com/eupnea-linux/mainline-kernel.git && cd mainline-kernel

3. Optional: Modify the kernel config in ``config-version``
4. Start the build script: ``bash ./build.sh stable`` or ``./build.sh testing`` (testing will take significantly longer
   to build).
5. The compiled/compressed files can be found in the root of the cloned repo:
    * bzImage-*version*
    * modules-*version*.tar.xz
    * headers-*version*.tar.xz

# Installing the kernel

The kernel needs to be signed with a proper rootfs mount PARTUUID passed to it. Copy a kernel.flags file from either
the depthboot repo or the EupneaOS repo and replace the PARTUUID with the one of your rootfs partition. Then sign the
kernel with:

      futility vbutil_kernel --arch x86_64 --version 1 --keyblock /usr/share/vboot/devkeys/kernel.keyblock --signprivate /usr/share/vboot/devkeys/kernel_data_key.vbprivk --bootloader kernel.flags --config kernel.flags --vmlinuz /tmp/depthboot-build/bzImage --pack /tmp/depthboot-build/bzImage.signed

Flash the kernel to the first partition on your usb/SD card with ``dd`` (or similar).

# Disable auto updates

After booting (or via chroot before booting), edit the systemd auto update service unit
file (``/etc/systemd/system/eupnea-update.service``) and comment out the line
with ``ExecStart=/usr/local/bin/manage-kernels --update`` to disable automatic kernel updates.