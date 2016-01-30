# -*- coding: utf-8 -*-
'''
    :codeauthor: Felippe Burk

    Return Fibonacci sequence to the Nth number.
'''

def gen(num):
    fibseq = []
    if num == 0:
        fibseq.append(0)
    elif num == 1:
        fibseq.append(1)
    elif num < 0:
        fibseq.append("error: num must be natural number")
    elif num > 1:
        prevnum = 0
        curnum = 1
        for n in range(1, num):
            if n == 1:
                fibseq.append(1)
            fibnum = prevnum + curnum
            fibseq.append(fibnum)
            prevnum = curnum
            curnum = fibnum
    return fibseq
