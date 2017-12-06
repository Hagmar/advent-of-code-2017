print(sum(map(lambda x: int(x[0]), filter(lambda x: x[0]==x[1], (lambda x: zip(x, x[1:]+x[0]))(input().strip())))))
