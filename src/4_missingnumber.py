#!/usr/bin/env python

def solve(nums):
    return sum(range(0, len(nums) + 1)) - sum(nums)
