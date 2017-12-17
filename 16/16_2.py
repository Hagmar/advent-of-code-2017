import sys

ss = input().split(',')
s = 'abcdefhgijklmnop'
seq = [s]
x = list(s)
for i in range(1,1000000001):
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
    s = ''.join(x)
    if s in seq:
        print(seq[1000000000%i])
        break
    seq.append(s)
