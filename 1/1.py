cap = input().strip()
tot = 0
for c in range(len(cap)):
    if cap[c] == cap[(c+1)%len(cap)]:
        tot += int(cap[c])
print(tot)
