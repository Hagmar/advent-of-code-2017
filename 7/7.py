import sys

ls = sys.stdin.read().rstrip().split('\n')
d = {}

for l in ls:
    l = l.replace(',','').split()
    p = l[0]
    ps = l[3:]
    for x in ps:
        d[x] = p

p = list(d.keys())[0]
while True:
    try:
        p = d[p]
    except:
        print(p)
        break
