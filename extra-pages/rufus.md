# Rufus issues

Rufus is a utility that helps format and create bootable USB flash drives on Windows.

Unlike other tools Rufus doesn't just copy the iso/img byte by byte to the usb, but instead reads the partition layout
from the provided iso/img files and flashes the usb accordingly.

This is a problem because the Depthboot-builder script doesn't create an iso, but a raw binary file with an unusual
GPT Partition layout. This means that Rufus sometimes messes up the image while flashing it which leads to non-bootable
USB drives/SD-cards.