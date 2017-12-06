print(sum(map(lambda l:len(set(l.split()))==len(l.split()),__import__('sys').stdin.read().strip().split('\n'))))
