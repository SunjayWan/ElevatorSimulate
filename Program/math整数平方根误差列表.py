from math import sqrt

a,b,c=int(input("a:")),int(input("b:")),int(input("c:"))

for x in range(a,b,c):
    print(sqrt(x)**2-x)
