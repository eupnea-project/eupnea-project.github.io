# 1. Building a custom kernel

* Download the latest pre-compiled Eupnea ChromeOS
  kernel [here](https://github.com/eupnea-linux/chromeos-kernel/releases/latest)
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

        git clone https://github.com/eupnea-linux/chromeos-kernel.git && cd chromeos-kernel

3. Optional: Modify the kernel config in ``kernel.conf``.
4. Optional: Modify the kernel branch in line 12 in ``kernel_build.py``.
5. Start the build script: ``python3 ./kernel_build.py``.
6. The compiled/compressed files can be found in the root of the cloned repo:
    * bzImage
    * modules.tar.xz
    * headers.tar.xz

7. Proceed to [installing the kernel](#_2-installing-the-kernel).

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

3. Optional: Modify the kernel config in ``kernel.conf``
4. Optional: Modify the kernel version in line 6 in ``build.sh``
5. Start the build script: ``bash ./build.sh``
6. The compiled/compressed files can be found in the root of the cloned repo:
    * bzImage
    * modules.tar.xz
    * headers.tar.xz

# 2. Installing the kernel

The kernel needs to be signed with a proper rootfs mount PARTUUID passed to it. Copy a kernel.flags file from either
the depthboot repo (repo_root/configs/cmdline) or the EupneaOS repo and replace the PARTUUID with the one of your rootfs
partition. You can find the PARTUUID of your rootfs partition with ``blkid -o value -s PARTUUID /dev/your_root_mount``.
Then sign the kernel with:

      futility vbutil_kernel --arch x86_64 --version 1 --keyblock /usr/share/vboot/devkeys/kernel.keyblock --signprivate /usr/share/vboot/devkeys/kernel_data_key.vbprivk --bootloader /path/to/kernel.flags --config /path/to/kernel.flags --vmlinuz /path/to/bzImage --pack ./bzImage.signed

Flash the kernel to the first partition on your usb/SD card with ``dd`` (or similar).
