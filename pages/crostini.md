# Crostini

## Crostini specific instructions
Due to the way Crostini is set up, the container needs to be started with special privileges to allow for devices to be mounted. **These instructions are mandatory for Crostini.**  

## Instructions:  
Press <kbd>CTRL</kbd><kbd>ALT</kbd><kbd>T</kbd> to open the ChromeOS terminal. Then run the following commands(To run a command, copy the ``command`` into the terminal and press <kbd>Enter</kbd>):

1. ``vmc stop termina``
2. ``vmc start termina``
3. ``exit``
4. ``vmc container termina penguin --privileged true`` (Command will fail, dont worry)
5. Wait for 5 seconds
6. ``vmc container termina penguin --privileged true``

You can now continue with the [regular install instructions](/?id=instructions).
