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
    * deb-pkg
    * netpbm
    * imagemagick (provides mogrify command)

   On debian based systems the dependencies can be installed with:

        sudo apt update && sudo apt install build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison binutils

2. Clone the kernel repo: ``git clone https://github.com/eupnea-linux/kernel.git && cd kernel``
3. Optional: Modify the kernel config, in either ``kernel.conf`` or ``kernel-alt.conf``if you are building the alt
   kernel
4. Start the build script: ``./kernel_build.py``
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
    * Flex
    * libelf1 development libraries
    * bison
    * binutils
    * deb-pkg
    * netpbm
    * imagemagick

2. Clone the kernel repo: ``git clone https://github.com/eupnea-linux/kernel.git && cd kernel``
3. Optional: Modify the kernel config in ``.config``
4. Start the build script: ``./build.sh``
5. The compiled/compressed files can be found in the root of the cloned repo:
    * bzImage-*version*
    * modules-*version*.tar.xz
    * headers-*version*.tar.xz