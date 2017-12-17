from collections import Counter
import sys

ls = sys.stdin.readlines()
d = {}
ns = {}
for l in ls:
    l = l.replace(',','').split()
    p = l[0]
    n = l[1]
    ns[p]=int(n[1:-1])
    ps = l[3:]
    for x in ps:
        d[x] = p

sor = sorted(ls, key=lambda l: len(l.replace(',','').split()[3:]))
w = {}
while sor:
    l_o = sor.pop(0)
    l = l_o.replace(',','').split()
    p = l[0]
    n = int(l[1][1:-1])
    ps = l[3:]
    try:
        bl = list(map(lambda a: w[a], ps))
        w[p] = n + sum(bl)
        if not len(set(bl)) < 2:
            count = Counter(bl)
            v = min(count, key=lambda k: count[k])
            v2 = max(count, key=lambda k: count[k])
            target = next(filter(lambda x: x[1]==v, map(lambda a: (ns[a],w[a]), ps)))
            print(target[0]+v2-v)
            break
    except KeyError:
        sor.append(l_o)

