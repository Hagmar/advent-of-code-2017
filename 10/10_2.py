import functools, sys

bytes = list(map(ord, input())) + [17,31,73,47,23]
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

print(''.join(map(lambda x: '{:02x}'.format(x), ns)))
