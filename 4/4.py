import sys


tot =  0
for l in sys.stdin.readlines():
    l = l.split()
    if len(set(l)) == len(l):
        tot += 1
print(tot)
