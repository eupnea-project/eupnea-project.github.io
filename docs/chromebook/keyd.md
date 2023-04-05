# Keyboard layout (keyd)

The Depthboot installer preinstalls keyd packages, which are build from rvaiya's [keyd](https://github.com/rvaiya/keyd)
repo. They keyd code itself is unmodified, but the packages include a libinput quirks file, which prevents the keyboard
from working when in tablet mode (this file was removed from the upstream project) and the various chromebook keyboard
layouts.

There are multiple keyd config files, which are located in `/usr/share/eupnea/keyboard-layouts/` and symlinked to
`/etc/keyd/base.conf`. These can be switched with the `/usr/lib/eupnea/set-keymap` script. The layouts all produce the
same results, which are documented below.

* Normal mode (i.e. Without holding any keys):
    * Search key behaves like the Super (aka windows) key (same as in ChromeOS)
    * Top row keys are mapped to their respective functions (varies between Chromebooks)
* Holding the Search(super) key:
    * Super + top row key results in the respective F-key F1-F12
    * To execute f-key shortcuts, hold super then press the rest of the shortcut as normal. For example, to press
      alt+f4: hold super, then press alt+f4 (without releasing Super).
* ChromeOS shortcuts:
    * alt + backspace: delete
    * alt + brightness up/down: increase/decrease keyboard backlight (if supported by Chromebook)
    * ctrl + alt + backspace: does the same as ctrl + alt + delete on normal Laptops