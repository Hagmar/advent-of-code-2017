ls = list(map(int, input().strip().split()))

cs = set()
tot = 0
s = tuple(ls)
while s not in cs:
    cs.add(s)
    i_max,n = max(enumerate(ls), key=lambda x:x[1])
    ls[i_max] = 0
    for i in range(1,n+1):
        ls[(i_max+i)%len(ls)] +=1
    tot += 1
    s = tuple(ls)
print(tot)
