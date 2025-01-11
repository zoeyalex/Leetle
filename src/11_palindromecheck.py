#!/usr/bin/env python

def solve(s):
  s = ''.join(c for c in s if c.isalnum()).lower()
  return s == s[::-1]
