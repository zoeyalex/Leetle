#!/usr/bin/env python
from collections import Counter

def solve(nums):
    nums = Counter(nums)
    return max(nums, key=nums.get)
