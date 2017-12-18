steps = input().split(',')
s = {'n': (0,1), 's': (0,-1), 'ne': (1,0.5), 'nw': (-1,0.5), 'se': (1,-0.5), 'sw': (-1,-0.5)}
x = y = 0

m = 0
for step in steps:
    dx, dy = s[step]
    x += dx
    y += dy
    m = max(m, abs(x)+max(0,abs(y)-abs(x)/2))

x, y = abs(x), abs(y)
y = max(0, y-x/2)
tot = x + y
print(tot)
print(m)
