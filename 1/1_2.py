cap = input().strip()
tot = 0
l = len(cap)
for c in range(l):
    if cap[c] == cap[(c+(l//2))%l]:
        tot += int(cap[c])
print(tot)
