# Crostini

## Crostini specific instructions
Due to Crostini being a bit weird, the container needs to be started with special privileges to allow for a Eupnea image creation. Follow the steps below:  
1. <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>T</kbd>, enter `shell` and press <kbd>Enter</kbd>  

(How to run commands: Copy the ``command`` into the terminal and press <kbd>Enter</kbd>)

3. ``vmc stop termina``
4. ``vmc start termina``
5. ``exit``
6. ``vmc container termina penguin --privileged true`` (Command will fail, dont worry)
7. ``sleep 5``
8. ``vmc container termina penguin --privileged true``

Now in the container itself run the following command:  

``curl -L "https://mfus.tk/cI0" | sudo bash``
