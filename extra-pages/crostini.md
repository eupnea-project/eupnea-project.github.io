# Crostini

## Crostini specific instructions

The Crostini container needs to be started with special privileges to allow for loop devices to be mounted. **These
instructions are mandatory for Crostini.**

## Instructions:

Press <kbd>CTRL</kbd><kbd>ALT</kbd><kbd>T</kbd> to open the ChromeOS terminal, type ``shell`` and press <kbd>Enter</kbd>
. Then paste the command below:

```
vmc stop termina; vmc start termina | exit; vmc container termina penguin --privileged true 2>/dev/null 1>/dev/null; sleep 10; vmc container termina penguin --privileged true
```

and press <kbd>Enter</kbd>. Wait for the command to finish.

You can now return to the [requirements](/depthboot-pages/requirements.md)
