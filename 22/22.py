from collections import defaultdict
import sys

def show(ns,xp,yp):
    m = {0:'.', 1:'W', 2:'#', 3:'F'}
    rows = []
    for y in range(-4,4):
        row = []
        for x in range(-4,4):
            c = m[ns[y][x]]
            row.append('['+c+']' if y==yp and x==xp else ' '+c+' ')
        rows.append(row)
    for row in rows:
        print(''.join(row))


tot = 0
nodes = defaultdict(lambda: defaultdict(bool))
nodes = defaultdict(lambda: defaultdict(int))
lines = list(map(lambda x: list(x.strip()), sys.stdin.readlines()))
direct = 0

h = len(lines)
w = len(lines[0])
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        if c == '#':
            nodes[y-h//2][x-w//2] = 2

x = y = 0
move = {
    0: (0,-1),
    1: (1,0),
    2: (0,1),
    3: (-1,0)
}
turn = {
    0: (0,-1),
    1: (1,0),
    2: (0,1),
    3: (-1,0)
}
for _ in range(10000000):
    if nodes[y][x] == 0:
        direct = (direct-1)%4
    elif nodes[y][x] == 1:
        pass
    elif nodes[y][x] == 2:
        direct = (direct+1)%4
    else:
        direct = (direct+2)%4
    #direct = (direct+(1 if nodes[y][x] else -1))%4
    #if not nodes[y][x]:
    if nodes[y][x] == 1:
        tot += 1
    #nodes[y][x] = not nodes[y][x]
    nodes[y][x] = (nodes[y][x]+1)%4
    step = move[direct]
    x += step[0]
    y += step[1]
print(tot)
