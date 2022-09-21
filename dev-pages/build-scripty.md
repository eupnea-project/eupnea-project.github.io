# The Eupnea build script

The Eupnea [build script](https://github.com/eupnea-linux/eupnea/blob/main/build.py) is the most important script of Eupnea.
It can either build an image(.img file) or write directly to a USB Stick/SD-card.
* **Building an image:** Most useful for Crostini, as it does not have direct access to USB sticks and therefore cannot format them or write directly. Can also be used to quickly test Eupnea building.
* **Direct write**: 
