print((lambda n,x:x-(x**2-n)%(x//2)-1)(*(lambda n:(n,int(n**0.5)+1))(int(input()))))
