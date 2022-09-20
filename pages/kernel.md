## Building the ChromeOS Kernel

The [image build script](https://github.com/eupnea-linux/eupnea/blob/main/build.py) of Eupnea downloads two precompiled binaries:

* The Linux Kernel Executable (vmlinuz/bzImage)
* A Tar Archive of the kernel modules

These binaries are compiled using Github Actions and require a powerful computer and at least an hour of compilation. The GPL permits distributing binaries, as long as you give the source code of them. The source of the kernel and modules is [here](https://chromium.googlesource.com/chromiumos/third_party/kernel).

### Requirements
The following must be installed in order to successfully build the kernel:
* linux-generic (headers)
* bison (parser, replacement for yacc)
* flex (lexical scanner)
* libelf-dev (for Ubuntu; possibly libelf-devel or elfutils-libelf-devel for other distros)
* imagemagick (provides mogrify command)
* libssl-dev (supports openssl development)

### Kernel build script
In the kernel folder, you should run the `build.sh` for a guided kernel build.

### Manually(not recommended)
1. Clone the repository with git by running:
```bash
git clone --branch chromeos-5.10 --depth=1 https://chromium.googlesource.com/chromiumos/third_party/kernel.git
cd kernel
```

2. Download the kernel `.config` file, and update it, by running:
```bash
wget https://raw.githubusercontent.com/cb-linux/breath/main/kernel.conf -O .config
make olddefconfig
```

3. Compile the kernel by running:
```bash
make -j$(nproc)
```

The `bzImage` should be located in `arch/x86/boot/bzImage`.

Running `make -j$(nproc) modules_install INSTALL_MOD_PATH=[DIRECTORY]`, and then compressing the `[DIRECTORY]` should give you the compressed modules.
