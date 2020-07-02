# KTaNE-cmdexp
A virtual, text-based expert for Keep Talking and Nobody Explodes in Python 3 (ofc)

## Warning! Use at your own discretion!
Using this code in official events, documented speedruns or other competitive situations is, I presume, a very bad idea. This program is more suited to casual play with friends, and I advise you tell anyone you are playing with that you are using this program and gather their opinion first.

Also, see `>>> WARNING: DATA.txt NOT FORMATTED CORRECT!`, the fourth title: I use `exec` in this program. Exec is dangerous. Run at own risk.

### What does it do?
This program can defuse all standard modules. For mazes, functionality is basic: enter one marker and it will tell you which maze to use from the manual, coded from left to right and then top to bottom.

For information on input, enter "h" or "help" in the main menu (">>> ")

### ">>> WARNING: DATA.txt NOT FORMATTED CORRECT!"???
You need to create a file with the same structure as the included `DATA.txt`. In case you wish to open multiple instances of the program, I made it read in global bomb information from that file. It parses it using `exec`: `exec` is dangerous, use at your own risk, blah blah blah. You should therefore define the required variables like python code.

Certain modules are able to be defused without all of the information in that file, and in which case they will work even if the warning is generated. If you try to defuse a module and `DATA.txt` does not contain the required information, the program will either error out or return faulty answers. Most likely the former.

### Useful tips
Colours are expressed as the first letter, except for black in which it is an UPPERCASE 'b'.

See `ktane-symbols.jpg` for what I call the keypads.

Ask the defuser for the first three columns of passwords: that'll leave you with one or two options.

Simon will loop until told to quit by `q`.

You can type the first two letters into the main menu of the module as a shortening.

Who's on first: transmitting information correctly is left to the humans. Type exactly what the button says, use `empty` for an actually blank display.

### TODO
Add full maze functionality.

More intelligent UI parsing.

Remove `exec`.

#### not TODO
Modded
