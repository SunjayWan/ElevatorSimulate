input("A program to check Fermat put n<=2 to end ")
def check_Fermat(a,b,c,n):
    while a**n+b**n==c**n:
        return"Fermat is wrong"
    else:
        return"I can not find that Fernat is wrong"
while True:
    a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
    n=int(input("n= "))
    if n<=2:
        break
    input(check_Fermat(a,b,c,n))

print("Bye")

        
