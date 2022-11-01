# Crostini

## Crostini specific instructions

The Crostini container needs to be started with special privileges to allow for loop devices to be mounted. **These
instructions are mandatory for Crostini.**

## Instructions:

Press <kbd>CTRL</kbd><kbd>ALT</kbd><kbd>T</kbd> to open the ChromeOS terminal. Paste the following commands one by one
and press <kbd>ENTER</kbd> after each one:

1. ``vmc stop termina``
2. ``vmc start termina``
3. ``exit``
4. ``vmc container termina penguin --privileged true`` (Command will fail, dont worry)
5. ``sleep 5``
6. ``vmc container termina penguin --privileged true``

You can now return to the [requirements](/setup-pages/requirements.md)