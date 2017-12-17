from collections import defaultdict
import sys

ls = sys.stdin.readlines()
regs = defaultdict(int)
for l in ls:
    a, b, c, _, *cond = l.split()
    s = 'regs["{}"] {} {}'.format(*cond)
    if eval(s):
        c = int(c)
        regs[a] += c if b=='inc' else -c
print(max(regs.values()))
