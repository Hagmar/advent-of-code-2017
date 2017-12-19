import sys
tot = 0

def step(x,y,d):
    if d == 0:
        y += 1
    elif d == 1:
        y -= 1
    elif d == 2:
        x += 1
    elif d == 3:
        x -= 1
    return x,y

lines = sys.stdin.readlines()
y = 0
x = lines[0].index('|')
d = 0
s = []
last = 'x'
while True:
    c = lines[y][x]
    if c == ' ':
        break
    tot += 1
    if c not in {'|','-','+'}:
        s.append(c)
    if c == '+':
        if last == '|':
            if lines[y][x+1] == '-':
                d = 2
            else:
                d = 3
            last = '-'
        elif last == '-':
            if lines[y+1][x] == '|':
                d = 0
            else:
                d = 1
                last = '|'
    else:
        last = c
    x,y = step(x,y,d)
print(''.join(s))
print(tot)
