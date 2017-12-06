import sys


lines = list(map(int, sys.stdin.readlines()))
i = 0
tot = 0

while 0 <= i < len(lines):
    n = lines[i]
    lines[i], i = lines[i]+ (-1 if n>=3 else 1), i + lines[i]
    tot += 1
print(tot)
