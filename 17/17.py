n = 380
x = [0]
i = 0
for j in range(1, 2018):
    i = (i+n)%len(x)+1
    x.insert(i,j)
print(x[(i+1)%len(x)])
