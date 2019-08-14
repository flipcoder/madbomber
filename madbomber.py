#!/usr/bin/env python2

import sys
import subprocess
import select
import time

f = open("madbomber.txt", "w")

proc = subprocess.Popen(["gdb", sys.argv[1]],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE
)

args = ' ' + ' '.join(sys.argv[2:])
proc.stdin.write('set pagination off\ncatch throw\nrun%s\n' % args)
poll = select.poll()
poll.register(proc.stdout, select.POLLIN)
t = time.clock()
stoplines= [
    "(gdb) No stack.\n",
    "(gdb) The program is not being run.\n",
    "Couldn\'t get registers: No such process.\n"
]
while True:
    r = poll.poll(0)
    if r:
        line = proc.stdout.readline()
        if line in stoplines:
            proc.kill()
            break
        print(line[:-1])
        f.write(line)
        t = time.clock()
    else:
        now = time.clock()
        if now - t > 0.01:
            proc.stdin.write('bt\nc\n')
            t = now

