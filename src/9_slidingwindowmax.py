#!/usr/bin/env python

def solve(nums, k):
    n = len(nums)
    ret = []
    for i in range(n-k+1):
        tmp = []
        for j in range(k):
            tmp.append(nums[i+j])
        ret.append(max(tmp))
    return ret
