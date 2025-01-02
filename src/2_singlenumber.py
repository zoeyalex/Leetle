#!/usr/bin/env python
from collections import Counter

def solve(nums):
    return next(num for num, count in Counter(nums).items() if count == 1)
