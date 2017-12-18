import sys
from collections import defaultdict

lines = sys.stdin.readlines()

layers = {}
for l in lines:
    a, b = list(map(int,l.split(':')))
    layers[a] = b

i = 0
while True:
    caught = False
    for k,v in layers.items():
        if not (i+k)%((v-1)*2):
            caught = True
            break
    if not caught:
        print(i)
        break
    i += 1
