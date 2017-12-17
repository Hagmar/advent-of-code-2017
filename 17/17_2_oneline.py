print(__import__('functools').reduce(lambda s,n: ((s[0]+s[1])%n+1, s[1], s[2] if (s[0]+s[1])%n else n), range(1,50000001), (0,int(input()),0))[2])
