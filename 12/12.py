import sys

lines = sys.stdin.read().strip().replace(',','').split('\n')

d = {}
for line in lines:
    a, _, *b = line.split()
    d[int(a)] = frozenset(map(int,b))

x = set(d[0])
c = set()
tot = 0
for line in lines:
    g = int(line.split()[0])
    if g not in c:
        x = set(d[g])
        while x:
            p = x.pop()
            if p not in c:
                x.update(d[p])
            c.add(p)
        tot += 1
print(len(c))
print(tot)
