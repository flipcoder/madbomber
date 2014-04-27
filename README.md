madbomber
===

Copyright (c) 2014 Grady O'Connell

Backtrace-on-throw exception logger for debugging C++ programs.

Useful in tracking down problems caused by exceptions happening in unexpected
places, including those which cause threads to terminate silently.

*ALL* exceptions (including both caught and uncaught) are backtraced and logged
upon the initial throw, so no exception shall escape your oversight.
In most situations, this means you should be looking at the bottom of the 
resultant logs for the most relevant details.

## Requirements
- a C++ program to debug
- gdb
- Python 2.7

## Instructions
- Make sure your program was compiled in debug mode, as you would with gdb.
- Run program with:

    ./madbomber.py program
    
- If necessary, trigger the error to happen in your program
- open madbomber.txt in current directory and to view backtraces of all exceptions

