tot = 0
while True:
    row = input().strip().split()
    l = list(map(int, row))
    m = max(l)
    m2 = min(l)
    tot += m-m2
    print(tot)
