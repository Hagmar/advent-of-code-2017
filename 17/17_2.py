steps = 380
i = 0
x = 0
for j in range(1, 50000001):
    i = (i+steps)%j + 1
    if i == 1:
        x = j
print(x)
