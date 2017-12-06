tot = 0
while True:
    row = input().strip().split()
    l = list(map(int, row))
    for a in l:
        for b in l:
            if a == b:
                continue
            if not a%b:
                tot += a//b
    print(tot)
