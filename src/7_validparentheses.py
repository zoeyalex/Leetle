#!/usr/bin/env python

def solve(s):
    stack = []
    parentheses = {')': '(', ']': '[', '}':'{'}
    for par in s:
        if par in parentheses.values():
            stack.append(par)
        elif par in parentheses:
            if stack and stack[-1] == parentheses[par]:
                stack.pop()
            else:
                return False
    return not stack
