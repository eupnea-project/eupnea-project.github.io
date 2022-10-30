# Crostini

## Crostini specific instructions

The Crostini container needs to be started with special privileges to allow for loop devices to be mounted. **These
instructions are mandatory for Crostini.**

## Instructions:

Press <kbd>CTRL</kbd><kbd>ALT</kbd><kbd>T</kbd> to open the ChromeOS terminal, then enter:

```
vmc stop termina; vmc start termina | exit; vmc container termina penguin --privileged true; sleep 5; vmc container termina penguin --privileged true
```

and press <kbd>Enter</kbd>.

Continue to the next page.