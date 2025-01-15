#!/usr/bin/env pythno

def solve(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
