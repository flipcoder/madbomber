#!/usr/bin/gdb -x
set pagination off
set logging file madbomber.txt
set logging on
catch throw
commands
bt
continue
end
run
quit
