print("Program to calculate root(s) of quadratic equetion")
print("aX**2+bX+c=0")
print("print\"a=0\" to end")
from math import sqrt

while True:
    a=float(input("a="))
    if a==0:
        break
    b=float(input("b="))
    c=float(input("c="))
    s=b**2-4*a*c
    if s>0:
        print("two roots:",(-b+sqrt(s))/2/a,(-b-sqrt(s))/2/a)
    elif s==0:
        print("one root:",-b/2/a)
    else:
        print("The equation has no roots")

print("Bye!")
