---
prev: false
---

# Glossary

This is an overview of the different terms used in the Eupnea Project documentation and community.

#### The Eupnea Project

An umbrella term for everything related to this Project. It includes Depthboot, all communities (GitHub,
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
of exception catchers, user-friendlier errors, automations, etc. making the process of creating a depthboot image as
easy and quick as possible.

Note: Depthboot refers to both the [Depthboot-builder](https://github.com/eupnea-linux/depthboot-builder) script and all
Chromebooks running the images created by it.

#### Breath

Breath is the original project at https://github.com/cb-linux/breath. It was founded and developed
by [MilkyDeveloper](https://github.com/milkydeveloper) and was active from Apr 2021 until its archival in late Aug 2022.

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
