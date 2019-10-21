print("rogram to calculate area of triangle")
print("print a=0 to end")
from math import sqrt

while True:
    a=float(input("Length of edge a:"))
    if a==0:
        break
    b=float(input("Length of edge b:"))
    c=float(input("Length of edge c:"))

    if a>0 and b>0 and c>0 and\
       a+b>c and a+c>b and c+b>a:
        s=(a+b+c)/2
        area=sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of the triangle:", area)
    else:
        print("a,b,c do not form a triangle!")

print("Bye!")        
