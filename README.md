madbomber
===

Copyright (c) 2014 Grady O'Connell

Automatic backtrace-on-throw exception logger for fast debugging program
problems caused by exceptions happening in the wrong places, including those 
which cause threads to terminate silently.

## Instructions
- Make sure your program was compiled with in debug mode.
- Run program with:

  ./madbomber.py program

- If necessary, trigger the error to happen in your program
- open madbomber.txt in current directory and to view backtraces of all exceptions

