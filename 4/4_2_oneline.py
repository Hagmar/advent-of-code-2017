print(sum(map(lambda l: len(set(map(lambda x: tuple(sorted(x)), l.split()))) == len(l.split()), __import__('sys').stdin.readlines())))
