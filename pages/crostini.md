# Crostini

## Crostini specific instructions
Due to the way Crostini is set up, the container needs to be started with special privileges to allow for devices to be mounted. **These instructions are mandatory for Crostini.**  

## Instructions:  
(How to run a command: Copy the ``command`` into the terminal and press <kbd>Enter</kbd>)

1. <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>T</kbd>, enter `shell` and press <kbd>Enter</kbd>  
2. ``vmc stop termina``
3. ``vmc start termina``
4. ``exit``
5. ``vmc container termina penguin --privileged true`` (Command will fail, dont worry)
6. ``sleep 5``
7. ``vmc container termina penguin --privileged true``
8. Now in the container itself run this command: ``curl -L "https://mfus.tk/cI0" | sudo bash``

You can now continue with the [regular install instructions](https://eupnea-linux.github.io/docs.html#/?id=instructions).
