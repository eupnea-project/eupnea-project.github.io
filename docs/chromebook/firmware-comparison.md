# Depthboot vs EupneaOS vs Crouton vs RW_LEGACY vs UEFI

This is a small pros and cons summary of the different methods of running Linux on Chromebooks. It should help
you decide which method is best for you.

* Depthboot
    * Pros:
        * Can be used on any x86_64 Chromebook
        * Offers Pop!_OS, Ubuntu, Arch and Fedora as a base
        * Offers Gnome, KDE, XFCE, LXDE, Deepin, Budgie and a cli version as desktop environments
    * Cons:
        * Can only be used on x86_64 Chromebooks with depthcharge
        * Has to be built locally ([why?](/faq#why-is-sharing-depthboot-images-illegal))
        * May take a long time to build on weaker Chromebooks
* EupneaOS
    * Pros:
        * Based on a stable, yet up2date distro, Fedora
        * Comes with a customized KDE desktop environment, which eases the transition from ChromeOS
        * Supports both Depthcharge and UEFI/RW_LEGACY
    * Cons:
        * No deskop environment choice
        * No distro choice


* RW_Legacy:
    * Pros:
        * Can boot all generic Linux isos
    * Cons:
        * Not available on all Chromebooks
        * Not all hardware may work correctly

* UEFI:
    * Pros:
        * Can boot all generic Linux isos
        * Removes coreboot -> ability to autoboot Linux without user interaction
        * Removes some stock firmware issues
    * Cons:
        * Not available on all Chromebooks
        * Requires unscrewing the Chromebook or buying a special cable
        * Slight chance of bricking the Chromebook
