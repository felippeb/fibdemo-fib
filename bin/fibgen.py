#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    :codeauthor: Felippe Burk

    Return Fibonacci sequence to the Nth number.
'''

import sys 
num = int(sys.argv[1])

if num == 0:
    print "well then why did you ask me to run in the first place?"
elif num == 1:
    print "You have input %d. Calculating fibonacci to %d digits:" % (num, num)
    print "1"
elif num < 0:
    print "invalid entry, you will need to enter a positive whole number"
elif num > 1:
    prevnum = 0
    curnum = 1
    print "You have input %d. Calculating fibonacci to %d digits starting at %d:" % (num, num, curnum)
    fibseq = []
    for n in range(1, num):
        fibnum = prevnum + curnum
        fibseq.append(fibnum)
        prevnum = curnum
        curnum = fibnum
for n in fibseq:
    if n == 1:
        print 1,
    print n,
