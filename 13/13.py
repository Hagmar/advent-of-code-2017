import sys
from collections import defaultdict

lines = sys.stdin.readlines()

layers = {}
scanners = {}
for l in lines:
    a, b = list(map(int,l.split(':')))
    layers[a] = b
    scanners[a] = 0

delay = sev = 0
packet = -1
direct = defaultdict(bool)
for _ in range(max(layers.keys())+1):
    packet += 1
    if packet in scanners and scanners[packet] == 0:
        sev += packet*layers[packet]
    for k,i in scanners.items():
        i += 1 if not direct[k] else -1
        scanners[k] = i
        if i == layers[k]-1 or not i:
            direct[k] = not direct[k]
print(sev)
