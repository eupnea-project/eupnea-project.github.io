# Crostini

## Crostini specific instructions

The Crostini container needs to be started with special privileges to allow for loop devices to be mounted. **These
instructions are mandatory for Crostini.**

## Instructions:

Press <kbd>CTRL</kbd><kbd>ALT</kbd><kbd>T</kbd> to open the ChromeOS terminal, type ``shell`` and press <kbd>Enter</kbd>
, then paste the command below:

- If you get an error about `shell` not being a command:
  [Enable developer mode](https://www.androidauthority.com/how-to-enable-developer-mode-on-a-chromebook-906688/) and
  try again.
- If you get `LXD was configured to only allow unprivileged containers`:
    - [Discord issue post](https://discord.com/channels/994245999822381076/1037455727310155846)
    - [Google IssueTracker issue](https://issuetracker.google.com/issues/259361701)

```
vmc stop termina; vmc start termina | exit; vmc container termina penguin --privileged true 2>/dev/null 1>/dev/null; sleep 10; vmc container termina penguin --privileged true
```

and press <kbd>Enter</kbd>. Wait for the command to finish.

You can now return to the [requirements](/depthboot-pages/requirements.md)