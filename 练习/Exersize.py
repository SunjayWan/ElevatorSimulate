#def f1(n):
#    from math import pi
#    sgn = lambda i: -1 if i%2 == 0 else 1
#    s = 0
#    a = []
#    for i in range(1,n+1):
#        s += 4*sgn(i)/(2*i-1)
#        a.append((s,abs(pi-s)))
#    print(a)

#def f2(n,x):
#    a = 1 + x
#    for i in range(n):
#        a += 1 + 1/(a)
#    return a

#def f3():
#    from time import time
#    s = 0
#    k = 1
#    j = 0
#    t = time()
#    while True:
#        s += 1/k
#        k += 1
#        if s >= 10 + j:
#            print(time()-t)
#            j += 1
#        if j == 18:
#            break
#f3()

#def f4(n):
#    s = n,0
#    water = 0
#    while s != (0,0) and s!= (0,1) and s!= (0,2):
#        water += s[0]
#        x = sum(s)
#        s = (x//3,x%3)
#    return water
#print(f4(8))

#def f5(a,b):
#    def f(n):
#        s = 1
#        for i in range(1,n):
#            if n%i == 0:
#                s += i
#        return s
#    s = [0]*3
#    for i in range(a,b+1):
#        if f(i) == i:
#            s[1] += 1
#        if f(i) < i:
#            s[0] += 1
#        if f(i) > i:
#            s[2] += 1
#    return s
    
#def f6(s):
#    a = s[::-1]
#    if s == a:
#        return True
#    return False

#def f7(s):
#    a = s[::-1]
#    return s[0:len(s)-1] + a

#def f8(s):
#    def f1(s):
#        n = 0
#        k = len(s)
#        for i in s:
#            n += int(i)*(2**k)
#            k -= 1
#        return n
#    def f2(s):
#        n = 0
#        k = len(s)
#        for i in s:
#            n += int(i)/(2**k)
#            k -= 1
#        return n
#    if '.' in s:
#        a,b = s.split(sep = '.')
#        return f1(a) +f2(b)
#    return f1(s)

#def gcd(m,n):
#    if n % m ==0:
#        return m
#    return gcd(n % m,m)



#def collatz(n):
#    max1 = 0
#    k = 0
#    while n != 1:
#        if n % 2 == 0:
#            n = n//2
#            k += 1
#        else:
#            n = n*3 + 1
#            max1 = max(n,max1)
#            k += 1
#        return max1
    
#def f9(n):
#    def f(k,n):
#        a = [5,18,17,28]
#        if n <= 3:
#            return 1
#        if k == 0 or n < 0:
#            return 0
#        return f(k-1,n)+f(k,n-a[k-1])
#    return f(4,n)
#print(f9(100),f9(160),f9(240),sep = '\n')

#def f10(n):
#    k = 0
#    def fib(n):
#        nonlocal k
#        k += 1
#        if n ==1:
#            return 1
#        if n == 2:
#            return 1
#        return fib(n-1) + fib(n-2)
#    return (fib(n),k)

#def f11(f,a,b,n):
#    from random import random as r
#    def f0(x1,y1):
#        if y1 < f(x1):
#            return True
#        return False
#    k = 0
#    l,m = f(a),f(b)
#    for i in range(n):
#        x1,y1 = r(),r()
#        if f0(x1,y1):
#            k += 1
#    return (k/n)*(b-a)*(m-l)
#print(f11(lambda x: x**3,0,1,10000))

#def montecaarlo(test,num):
#    passed = 0
#    for i in range(num):
#        if test():
#            passed += 1
#    return passed/num
#def appr_method(x,improve,accept):
#    if x == 0:
#        return 0
#    x1 = x
#    while True:
#        x2 = improve(x,x1)
#        if accept(x1,x2):
#            return x2
#        x1 = x2


#def f12(n):
#    def nextpf(n):
#        d = 2
#        while d*d <= n:
#            if n % d == 0:
#                return d
#            d += 1
#        return n
#    flist = []
#    while n != 1:
#        p = nextpf(n)
#        if p not in flist:
#            flist.append(p)
#        n //= p
#    return flist



























        
        