lines = list(map(lambda l: tuple(map(int, l.split(':'))), __import__('sys').stdin.readlines()))
print(next(i for i in range(10**7) if all(map(lambda x: (i+x[0])%((x[1]-1)*2), lines))))
