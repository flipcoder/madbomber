#!/usr/bin/env python2

import sys
import subprocess
import select
import time

f = open("madbomber.txt", "w")

proc = subprocess.Popen(["gdb", sys.argv[1]],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE
)

proc.stdin.write('set pagination off\ncatch throw\nrun\n')
poll = select.poll()
poll.register(proc.stdout, select.POLLIN)
t = time.clock()
while True:
    r = poll.poll(0)
    if r:
        line = proc.stdout.readline()
        if line == "(gdb) No stack.\n":
            proc.kill()
            break
        elif line == "(gdb) The program is not being run.\n":
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

