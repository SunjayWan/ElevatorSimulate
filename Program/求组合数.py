print("A progran to calculate combinatorial number__C(m,n),")
print(" print m>n or m<0 or n<0 to end")
def jiecheng(n):
    x = 1
    for s in range(1,n+1):
        x =x*s
    return x

while True:
    m=int(input("m="))
    n=int(input("n="))

    a=jiecheng(n)
    b=jiecheng(m)
    c=jiecheng(n-m)
    if m>n or m<0 or n<0:
        break
    if m==n:
        print("The combinatorial number is 1")
    else:
        d=int(a//b//c)
        print("The combinatorial number is",d)


print("Bye!")
        
    
    
    
