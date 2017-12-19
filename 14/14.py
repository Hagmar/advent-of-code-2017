import sys, functools
from collections import defaultdict
tot = 0


def knot(s):
    bytes = list(map(ord,s)) + [17,31,73,47,23]
    l = list(range(256))
    i = 0
    ss = 0

    for _ in range(64):
        for length in bytes:
            if 1 < length <= len(l):
                stop = i+length
                end = min(len(l), stop)
                part1 = l[i:stop]
                part2 = l[0:stop-end]

                sublist = (part1 + part2)[::-1]
                l[i:stop] = sublist[0:len(part1)]
                l[0:stop-end] = sublist[len(part1):]
            i = (i + ss + length)%len(l)
            ss += 1

    ns = []
    for i in range(16):
        sublist = l[i*16:i*16+16]
        n = functools.reduce(lambda x,y: x^y, sublist)
        ns.append(n)

    return ''.join(map(lambda x: '{:02x}'.format(x), ns))

key = input()

tot = 0
grid = []
for i in range(128):
    s = '{}-{}'.format(key, i)
    h = knot(s)
    bits = ''.join(map(lambda c: '{:04b}'.format(int(c,16)), h))
    tot += len(list(filter(lambda x: x=='1', bits)))
    grid.append(bits)

print(tot)

def walk(x,y,reg,n,grid):
    visited = set()
    left = {(x,y)}
    while left:
        x,y = left.pop()
        if (x,y) not in visited:
            reg[y][x] = n
            for x2,y2 in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= x2 < 128 and 0 <= y2 < 128:
                    if grid[y2][x2] == '1':
                        if (x2, y2) not in visited:
                            left.add((x2,y2))
        visited.add((x,y))


reg = defaultdict(lambda: defaultdict(int))
n = 0
for y in range(128):
    for x in range(128):
        if grid[y][x] == '1':
            if not reg[y][x]:
                n += 1
                walk(x,y,reg,n,grid)
print(n)
