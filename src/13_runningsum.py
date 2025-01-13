#!/usr/bin/env python

def solve(nums):
  ret = []
  cur_sum = 0
  for num in nums:
    cur_sum += num
    ret.append(cur_sum)
  return ret
