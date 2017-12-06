print(sum(map(lambda x: max(x)-min(x), map(lambda x: list(map(int, x.split())), __import__('sys').stdin.read().rstrip().split('\n')))))
