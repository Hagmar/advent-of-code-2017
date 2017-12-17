import sys
from string import ascii_lowercase

ss = input().split(',')
x = list(ascii_lowercase[:16])
for s in ss:
    if s[0] == 's':
        n = int(s[1:])
        x = x[-n:] + x[:-n]
    elif s[0] == 'x':
        a,b = map(int, s[1:].split('/'))
        x[a], x[b] = x[b], x[a]
    elif s[0] == 'p':
        a,b = s[1:].split('/')
        a = x.index(a)
        b = x.index(b)
        x[a], x[b] = x[b], x[a]

print(''.join(x))
