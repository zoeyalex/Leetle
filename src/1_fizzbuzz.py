#!/usr/bin/env python

def solve(n):
    ret = []
    for i in range(1, n+1):
        cur = ''
        if i % 3 == 0:
            cur += 'Fizz'
        if i % 5 == 0:
            cur += 'Buzz'
        ret.append(cur or i)
    return ret
