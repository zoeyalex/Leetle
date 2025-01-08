#!/usr/bin/env python

def solve(nums, target):
    seen = {}
    for idx, num in enumerate(nums):
        match = target - num
        if match in seen:
            return [seen[match], idx]
        seen[num] = idx
    return []
