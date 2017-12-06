from collections import defaultdict
from sys import exit


def val(pos, x, y):
    return sum([pos[(x2,y2)] for x2 in [x-1, x, x+1] for y2 in [y-1, y, y+1]]) - pos[pos[(x,y)]]

def check(pos, x, y):
    pos[(x,y)] = val(pos, x, y)
    if pos[(x,y)] > n:
        print(pos[(x,y)])
        exit(0)

n = int(input())
pos = defaultdict(int)

x = y = 0
pos[(x,y)] = 1
side = 2
while True:
    x += 1
    y -= 1
    for _ in range(side):
        y += 1
        check(pos, x, y)
    for _ in range(side):
        x -= 1
        check(pos, x, y)
    for _ in range(side):
        y -= 1
        check(pos, x, y)
    for _ in range(side):
        x += 1
        check(pos, x, y)
    side += 2
