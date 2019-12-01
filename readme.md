Juno-DS-Sysex
=============

A Python script that simply prints some useful sysex messages to change
modes and parameters of a Roland Juno-DS keyboard.

The script outputs the following:
```
Sound Mode:
Patch:   F0 41 10 00 00 3A 12 01 00 00 00 00 7F F7
Perform: F0 41 10 00 00 3A 12 01 00 00 00 01 7E F7
GM1:     F0 41 10 00 00 3A 12 01 00 00 00 02 7D F7
GM2:     F0 41 10 00 00 3A 12 01 00 00 00 03 7C F7
GS:      F0 41 10 00 00 3A 12 01 00 00 00 04 7B F7

Transpose:
Transpose -5: F0 41 10 00 00 3A 12 01 00 00 12 3B 32 F7
Transpose -4: F0 41 10 00 00 3A 12 01 00 00 12 3C 31 F7
Transpose -3: F0 41 10 00 00 3A 12 01 00 00 12 3D 30 F7
Transpose -2: F0 41 10 00 00 3A 12 01 00 00 12 3E 2F F7
Transpose -1: F0 41 10 00 00 3A 12 01 00 00 12 3F 2E F7
Transpose 0: F0 41 10 00 00 3A 12 01 00 00 12 40 2D F7
Transpose 1: F0 41 10 00 00 3A 12 01 00 00 12 41 2C F7
Transpose 2: F0 41 10 00 00 3A 12 01 00 00 12 42 2B F7
Transpose 3: F0 41 10 00 00 3A 12 01 00 00 12 43 2A F7
Transpose 4: F0 41 10 00 00 3A 12 01 00 00 12 44 29 F7
Transpose 5: F0 41 10 00 00 3A 12 01 00 00 12 45 28 F7
Transpose 6: F0 41 10 00 00 3A 12 01 00 00 12 46 27 F7
```

The script contains a function to calculate checksums and the functions that
create the above sequences are useful to understand the keyboard's sysex
scheme.

