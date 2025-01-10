#!/usr/bin/env python

def solve(nums):
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res += 1
        elif num > res:
            break
    return res
