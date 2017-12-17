import sys
tot = 0

lengths = map(int, input().split(','))
l = list(range(256))
i = 0
ss = 0

for length in lengths:
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
print(l[0]*l[1])
