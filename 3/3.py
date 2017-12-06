n = int(input())
x = int(n**0.5)+1
left = (x**2-n)%(x-1)
print(x-1 - (left % ((x-1)//2)))
