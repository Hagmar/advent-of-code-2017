import sys


lines = list(map(int, sys.stdin.read().strip().split('\n')))
i = 0
tot = 0

while 0 <= i < len(lines):
    lines[i], i = lines[i]+1, i + lines[i]
    tot += 1
print(tot)
