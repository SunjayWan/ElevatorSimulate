#求平方根的算法误差比较
from math import sqrt
def mysqrt(x):
    guess=1.0
    while abs(guess*guess-x)>1e-8:
              guess=(guess+x/guess)/2
    return guess
a,b,c=int(input("a:")),int(input("b:")),int(input("c:"))
for n in range(a,b,c):
    f=abs(mysqrt(n)-sqrt(n))
    print(f)
for y in range(a,b,c):
    g=0
    f=abs(mysqrt(y)-sqrt(y))
    g=g+f
print("the average error:",g/((b-a+1)//c))
