from collections import defaultdict
import sys

ls = sys.stdin.readlines()
regs = defaultdict(int)
m = 0
for l in ls:
    a, b, c, _, *cond = l.split()
    s = 'regs["{}"] {} {}'.format(*cond)
    if eval(s):
        c = int(c)
        regs[a] += c if b=='inc' else -c
        m = max(m, regs[a])
print(m)
