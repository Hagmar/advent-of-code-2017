import sys

gar = input()
garbage = ignore = False
c = tot = g = i = 0
while i < len(gar):
    if gar[i] == '!':
        ignore = True
        i += 1
    elif gar[i] == '>':
        garbage = False
    elif not garbage:
        if gar[i] == '<':
            garbage = True
        elif gar[i] == '{':
            g += 1
        elif gar[i] == '}':
            tot += g
            g -= 1
    else:
        c += 1
    i += 1
print(tot)
print(c)
