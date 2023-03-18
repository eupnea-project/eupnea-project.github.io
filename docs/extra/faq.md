---
prev: false
next: false

title: Frequently Asked Questions
---

<script setup>
import FAQEntry from "/components/FAQEntry.vue";
</script>

# FAQ

Frequently asked questions (and answers) regarding the Eupnea Project.

<FAQEntry question="Will Depthboot/EupneaOS remove my ChromeOS installation?">

Only if you choose to do so. Neither Depthboot nor EupneaOS will remove your ChromeOS installation, unless you
explicitly choose to do so.
</FAQEntry>

<FAQEntry question="When will EupneaOS be ready?">

We don't know. We are working on it, but we have no ETA.
</FAQEntry>

<FAQEntry question="What is the difference between the Mainline kernel and the ChromeOS kernel?" link="difference-between-kernels">

Here is a full page comparing the two kernels: [Eupnea Kernels](/docs/project/kernels)
</FAQEntry>

<FAQEntry question="I have UEFI/Custom BIOS installed on my Chromebook">

If you have completely replaced your Chromebooks firmware with a custom BIOS/UEFI, you will not be able to boot
Depthboot. You can however still boot EupneaOS.
To be able to boot Depthboot, you will need to revert your firmware to stock.
</FAQEntry>

<FAQEntry question="I have RW_Legacy installed on my Chromebook">

Installation of rw_legacy/alt_fw that can be accessed with ctrl+L/"Select alternate bootloader" does not affect
your Chromebooks ability to boot Depthboot. Just follow the instructions as usual.
</FAQEntry>

<FAQEntry question="UEFI vs RW_LEGACY vs Depthboot vs EupneaOS?">

Read all pros and ons of each method of booting Linux on a Chromebook [here](/docs/chromebook/firmware-comparison).
</FAQEntry>

<FAQEntry question="Are the Depthboot distros modified?">

Yes, but only the minimal amount of changes required to make them bootable and work properly on Chromebooks (Kernel +
minor configs).  
In addition to installing some packages from the distro's repo, our own repo is added to the distro, which contains the
eupnea-utils and eupnea-system packages (and some others). You can read more about the packages in the respective
eupnea package repos.  
Nothing else is modified, i.e. all distro "quirks" are kept intact (Snap, no Tap-to-click by default on GNOME, etc.).
</FAQEntry>

<FAQEntry question="Which Depthboot distro is the best?">

First off, there are no feasible differences between the distros. They all boot the same 2
kernels ([see above](#difference-between-kernels)), which are
responsible for most of the possible performance differences.
You will have the same "Depthboot experience" on all of them (i.e. the Depthboot scripts/apps will work the same on
every distro).

The differences among the distros are mostly in terms of development philosophy. Here is a brief list of pros and cons:

* Pop!_OS: LTS release (currently)
    * Pros: Based on Ubuntu, but without the Canonical *Quirks* (Snap replaced by flatpak, core packages get updates).
      Developed by System76. Has a customised GNOME desktop.
    * Cons: Based on 22.04 -> not all packages are the latest versions. Has a customised GNOME desktop.
* Ubuntu: LTS release + 6 months release
    * Pros: Most popular distro -> more packages, more support. Developed by Canonical.
    * Cons: Not rolling release -> not all packages are the latest versions. Has some Canonical *Quirks* (i.e. Snap).
* Fedora: 6 month releases
    * Pros: Recent-ish packages (somewhere in the middle between rolling and LTS). Backed by Red Hat.
    * Cons: Has some *Quirks* (i.e. no hardware decoders out-of-the-box, no proper flatpak). DNF is slow out-of-the-box.
* Arch: Rolling release
    * Pros: latest package versions, AUR. Has no corporate backing.
    * Cons: Requires more maintenance, might break more often. Has no corporate backing.
</FAQEntry>

<FAQEntry question="Why is sharing Depthboot images illegal?">

The Depthboot base distros all allow image/iso/rootfs sharing, but only in an unmodified form. The Depthboot script
customizes some internal distro behavior (for example it [disables deep sleep](/docs/chromebook/bootlock)) and
thereby creates modified images.
To allow modified images to be shared, all trademarked content would have to be removed, i.e. all Distro logos.
</FAQEntry>

<FAQEntry question="Why is sharing EupneaOS images illegal?">

EupneaOS does not have the same restrictions as the Depthboot base distros, as all trademarked content has been removed.
The Eupnea Project disallows sharing of EupneaOS images, to prevent unofficial modded versions from being distributed.
If you want to create a fork of EupneaOS, remove all EupneaOS branding, i.e. the name and logos.
</FAQEntry>

<FAQEntry question="Does the Eupnea Project collect any telemetry?">

No, setting up telemetry services is too much work.  
Keep in mind that the distros themselves might collect telemetry and send it to their respective
developers.
</FAQEntry>