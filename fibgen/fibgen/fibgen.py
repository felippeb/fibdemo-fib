# -*- coding: utf-8 -*-
'''
    :codeauthor: Felippe Burk

    Return Fibonacci sequence to the Nth number.
'''

def gen(n):
    fibseq = []
    if n == 0:
        fibseq.append("nil")
    elif n < 0:
        fibseq.append("error: num must be natural number")
    elif n == 1:
        fibseq.append(0)
    elif n == 2:
        fibseq = [0, 1]
    elif n > 2:
        fibseq.append(0)
        prevnum = 0
        curnum = 1
        for num in range(2, n):
            if num == 2:
                fibseq.append(1)
            fibnum = prevnum + curnum
            fibseq.append(fibnum)
            prevnum = curnum
            curnum = fibnum
    return fibseq
