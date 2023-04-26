# Glossary

This is an overview of the different terms used in the Eupnea Project documentation and community.

#### The Eupnea Project

An umbrella term for everything related to this Project. It includes EupneaOS, Depthboot, all communities (GitHub,
Discord, Revolt, Reddit) and all developers.  
Note: [Breath](#breath) and [cb-linux](https://github.com/cb-linux/) are not part of [the
Eupnea Project](#the-eupnea-project).

#### Depthboot

[Depthboot-builder](https://github.com/eupnea-linux/depthboot-builder) is a fork of [Breath](#breath) that creates
bootable images for *almost* all 64-bit Chromebooks. Multiple [distros](#distribution) and [DEs](#desktop-environment)
are supported.
[Breath](#breath) was rewritten into Python3 by Apacelus, due to developer preference (Python has a much more
human-readable syntax and better ways to interact with the user). At its core the script is "just" a very fancy wrapper
for about 150 bash calls.
Depthboot was written with user-friendliness as the main goal (which is what Breath was lacking) and has a huge amount
of exception catchers, user-friendly errors, automations, etc. making the process of creating a depthboot image as easy
as possible.

Note: Depthboot refers to both the [Depthboot-builder](https://github.com/eupnea-linux/depthboot-builder) script and all
Chromebooks running the images created by it.

#### EupneaOS

EupneaOS is a Fedora based operating system optimized to run on *almost* all 64-bit Chromebooks. It features a custom (
KDE based) ChromeOS style desktop and native Android app support, as well as tweaks to make the system more
user-friendly.  
While most of the tweaks from EupneaOS are available (or can be added post-install) in a Fedora + KDE Depthboot
system, EupneaOS has the advantage of being available as a prebuilt img, as well as featuring many extra system tweaks
from the Eupnea Project.  
EupneaOS can also be booted on UEFI/RW_L Chromebooks (non Chromebook devices are **NOT** supported)

#### Eupnea

An umbrella term for [EupneaOS](#eupneaos) and [Depthboot](#depthboot). It Was used as the name for Depthboot in the
early development stages (pre v1.0)

#### Desktop Environment

Aka DE. Refers to the gui part of a system, as well as apps and frameworks used by
it.  
[Which DE is the best?](/faq#which-desktop-enviroment-de-is-the-best)

#### Distribution

Aka distro. Refers to the base system used. The base system includes the package manager, the update philosophy and
other (mostly) user abstracted aspects.  
[Which distro is the best?](/faq#which-depthboot-distro-is-the-best)

[Are the Depthboot distros modified?](/faq#are-the-depthboot-distros-modified)  
Note: [EupneaOS](#eupneaos) is a modified [Fedora](https://www.fedoraproject.org/) fork.