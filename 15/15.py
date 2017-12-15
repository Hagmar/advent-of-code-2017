a = int(input().split()[-1])
b = int(input().split()[-1])
tot = 0
for _ in range(40000000):
    a = (a*16807)%2147483647
    b = (b*48271)%2147483647
    if not (a^b)%65536:
        tot += 1
print(tot)
