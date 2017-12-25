import sys
from collections import defaultdict

tape = defaultdict(int)
i = 0
states = {}
state = input().split()[3][:-1]
diagcs = int(input().split()[5])

for c in 'ABCDEF':
    input()
    s = input().split()[2][:-1]
    states[s] = []
    for cs in [0, 1]:
        input()
        w = int(input().split()[4][:-1])
        d = 1 if input().split()[6] == 'right.' else -1
        ns = input().split()[4][:-1]
        states[s].append((w, d, ns))

for _ in range(diagcs):
    w, d, ns = states[state][tape[i]]
    tape[i] = w
    i += d
    state = ns

print(sum(tape.values()))
