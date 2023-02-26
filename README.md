# The Eupnea Project

Welcome to the Eupnea Project wiki. We are a small dev team that focuses on running Linux on Chromebooks.

## Depthboot

Depthboot is a builder script that creates a bootable USB drive/SD-card that can be booted on any 64-bit Chromebook. It
supports common Linux distributions(Pop!_OS, Ubuntu, Arch and Fedora) and a variety of the most popular desktop
environments.  
Due to licensing restraints, Depthboot cannot be distributed as an iso. Instead, it has to be build locally.

[Build a Depthboot image](docs/depthboot/requirements.md)

## EupneaOS

The Eupnea Project develops a custom Linux distribution based on [Fedora](https://getfedora.org/) called EupneaOS. It's
designed to imitate the look of ChromeOS and is the recommended way of upgrading your Chromebook. It is designed to
replicate most features of ChromeOS, but without any limitations.

[Download precompiled EupneaOS image](https://eupnea-linux.github.io)

## Depthboot vs EupneaOS vs Crostini vs Crouton vs RW_LEGACY vs UEFI

This is a small pros and cons summary of the different methods of running Linux on Chromebooks. It should help
you decide which method is best for you.

* Depthboot
    * Pros:
        * Can be used on any 64-bit Chromebook
        * Offers Pop!_OS, Ubuntu, Arch and Fedora as a base
        * Offers Gnome, KDE, XFCE, LXDE, Deepin, Budgie and a desktopless version as desktop environments
    * Cons:
        * Can only be used on 64-bit Chromebooks with depthcharge
        * Has to be built locally
        * May take a long time to build on weaker Chromebooks


* EupneaOS
    * Pros:
        * Based on a stable distro: Fedora
        * Comes with a customized KDE desktop environment, which eases the transition from ChromeOS
        * Offers precompiled images for depthcharge and UEFI/RW_LEGACY
    * Cons:
        * No deskop environment choice
        * No distro choice

* RW_Legacy:
    * Pros:
        * Can boot all generic Linux isos
    * Cons:
        * No audio support out of the box
        * Not all hardware may work correctly
        * Not available on all Chromebooks

* UEFI:
    * Pros:
        * Can boot all generic Linux isos
        * Removes coreboot -> ability to autoboot Linux without user interaction
    * Cons:
        * Not available on all Chromebooks
        * Requires unscrewing the Chromebook or buying a special cable
        * Slight chance of bricking the Chromebook