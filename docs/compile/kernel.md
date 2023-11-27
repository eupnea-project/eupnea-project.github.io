---
prev: false
next: false
---

# 1. Building a custom kernel

* Download the latest pre-compiled Eupnea ChromeOS
  kernel [here](https://github.com/eupnea-project/chromeos-kernel/releases/latest)
* Download the latest pre-compiled Eupnea mainline
  kernel [here](https://github.com/eupnea-project/mainline-kernel/releases/latest)

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
    * dracut

On debian based systems the dependencies can be installed with:

```shell
sudo apt-get update && sudo apt-get install build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison binutils dracut
```

2. Clone the kernel repo:

```shell
git clone https://github.com/eupnea-project/chromeos-kernel.git && cd chromeos-kernel
```

3. Optional: Modify the kernel config in ```kernel.conf```.
4. Optional: Modify the kernel branch in line 12 in ```kernel_build/py```.
5. Start the build script: ```python3 ./kernel_build.py```.
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

```shell
sudo apt-get update && sudo apt-get install build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison binutils
```

2. Clone the kernel repo:

```shell
git clone https://github.com/eupnea-project/mainline-kernel.git && cd mainline-kernel
```

3. Optional: Modify the kernel config in ```kernel.conf```
4. Optional: Modify the kernel version in line 6 in ```build.sh```
5. Start the build script: ```bash ./build.sh```
6. The compiled/compressed files can be found in the root of the cloned repo:
    * bzImage
    * modules.tar.xz
    * headers.tar.xz

# 2. Installing the kernel

1. Sign the kernel and add a cmdline to it.
   > This process can be done automatically with
   the ```install-kernel```[script](https://github.com/eupnea-project/eupnea-utils/blob/main/system-scripts/install-kernel)  
   Run ```/usr/lib/eupnea/install-kernel --help``` to see all available script options.

2. Extract the modules into ```/usr/lib/modules/<insert_version>``` and the headers into
   ```/usr/src/linux-headers-<insert_version>```. Replace insert_version with your kernel version
   > The kernel version can can be read from the bzImage file
   with ```file -bL bzImage | grep -o 'version [^ ]*' | cut -d ' ' -f 2```.
3. Eupnea-systems only: Uninstall all other eupnea-kernel packages with your distros package manager and this
   wildcard: ```eupnea-*-kernel```.  
   Warning: The kernel packages might be reinstalled by an update, which would also overwrite your custom kernel.
