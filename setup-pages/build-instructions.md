## Build instructions:

1. Open a terminal, clone the repo and start the script with this command:
    ```
    git clone --depth=1 https://github.com/eupnea-linux/depthboot-builder; cd depthboot-builder; ./main.py
    ```
2. Follow the instructions inside the terminal.

3. If you chose the image option, flash the image to a USB drive/SD-card using Etcher, Rufus, ``dd`` or any other tool.
    - If you're running this within Crostini, copy depthboot.bin to a folder you can access from ChromeOS's Files App, then [flash](https://www.virtuallypotato.com/burn-an-iso-to-usb-with-the-chromebook-recovery-utility/) it using the Chromebook Recovery Utility extension.
    
4. Make sure you have [enabled developer mode](https://www.androidauthority.com/how-to-enable-developer-mode-on-a-chromebook-906688/)

5. Open the ChromeOS shell by pressing <kbd>CTRL</kbd><kbd>ALT</kbd><kbd>T</kbd>, enter `shell` and press <kbd>Enter</kbd>.  

6. Inside the ChromeOS shell enable USB and Custom Kernel Booting by running:
    ```
    sudo crossystem dev_boot_usb=1; sudo crossystem dev_boot_signed_only=0
    ```

7. Reboot with the USB drive/SD card plugged in and press <kbd>CTRL</kbd><kbd>U</kbd> or select "Boot from external disk". 

After a black screen Depthboot will boot.