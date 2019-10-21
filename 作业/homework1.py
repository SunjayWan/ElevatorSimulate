#from math import sqrt,pi,cos
#def calc_area(a,b,c,d,alpha):
#    s=(a+b+c+d)/2
#    alpha=alpha*pi/180
#    f=sqrt((s-a)*(s-b)*(s-c)*(s-d)-a*b*c*d*cos(alpha/2)*cos(alpha/2))
#    return f
#numbers = input()
#a,b,c,d,alpha = numbers.split()
#a = float(a)
#b = float(b)
#c = float(c)
#d = float(d)
#alpha = float(alpha)
#print('%.6f' % calc_area(a,b,c,d,alpha))
#
#
#
#
#from math import sqrt
#def distance(a,b,c,d):
#    return sqrt((a-c)**2+(b-d)**2)
#numbers = input()
#a,b,c,d = numbers.split()
#a = float(a)
#b = float(b)
#c = float(c)
#d = float(d)
#print('%.6f' % distance(a,b,c,d))
#
#
#
##求所有小于n的整除3不整除7的自然数
#def find_nunber1(n):
#    for i in range(1,n+1):
#        if i%3==0 and i%7!=0:
#            print(i)
#def find_number2(n):
#    i = 1
#    while i<=n:
#        if i%3==0 and i%7!=0:
#            print(i)
#        i = i+1
#n = int(input( ))
#find_nunber1(n)
#find_number2(n)
#
#
#
##2.0对逻辑值的充分利用可以简化这个程序
#def find_nunber3(n):
#    for i in range(1,n+1):
#        if not i%3 and i%7:
#            print(i)
#n = int(input( ))
#find_nunber3(n)
#
#
#
#
#
#
#
#            
#def calc_price(a,b,c,d,e):
#    i = 1
#    while i<=d*e:
#        i = i+1
#    return a*e*b/100+c*i
#numbers = input()
#a,b,c,d,e = numbers.split()
#a = float(a)
#b = float(b)
#c = float(c)
#d = float(d)
#e = float(e)
#print('%.1f' % calc_price(a,b,c,d,e))
#
#
##找出1.9999.....9和2.0被Python视为同一个浮点数最少要多少个9
##10**15<2**52<10**16
#i=1
#a="1.9"
#while float(a)!=2.0:
#    a=a+"9"
#    i=i+1
#print(i)
#
#
##可以进行到无穷大的迭代器
#from itertools import count
#for i in count():
#    if float('1.' + '9'*i) == 2.0:
#        break
#print(i)
#
#
#
##从二进制串到十进制数
#c = input()
#num = 0
#for i in c:
#    num = num*2 + int(i)
#print(num)
#    
#
#    
#    
#
#
#
#
##从二进制串到十进制数2.0（用字符串做迭代器）
#bits = input("Input a binary string: ")
#num = 0
#for i in bits:
#    num = num*2 + int(i)         #str可以直接做迭代器，称为“在字符串上循环”
#    
#print("Number of",bits,"is",num)
#
#
#
#
#
#def fact(n):
#    if n==0:
#        return 1
#    else:
#        return n*fact(n-1)
#    
#def power(x,n):
#    if n == 0:
#        return 1
#    else: 
#        return x*power(x,n-1)
#
#
#
#def power(x,n):
#    if n == 0:
#        return 1
#    elif n%2 != 0:
#        return x*power(x,n-1)
#    elif n%2 == 0:
#        return power(x,n/2)*power(x,n/2)
#
#
#
#
#s = input()
#c = input()
#def count(s,c):
#    n = 0
#    for i in s:
#        if i==c:
#            n+=1
#    return n
#print(count(s,c))
#
#
#
#
#s = input()
#c = input()
#def has_no(s,c):
#    n = 0
#    for i in s:
#        if i==c:
#            n=1
#            break
#    return not bool(n)
#print(has_no(s,c))
#
#
#
#s = input()
#w = input()
#def has(s,w):
#    for i in range(len(s)):
#        a = s[i:i+len(w)+2:1]
#        n=0
#        if a==" " + w + " ":
#            n=1
#            break
#    return bool(n)
#print(has(s,w))    
#
#
#
#s = input()
#def print_words(s):
#    s = s + " "
#    b,a = "",""
#    for i in str(s):
#        if i == " ":
#            b = b + a + "\n"
#            a = ''
#        else:
#            a = a + i
#    
#    return b
#print(print_words(s))         
#
#
#
#
#ch = input()
#def myord(c):
#    return ord(c) - 64
#def pyramid(ch): 
#    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#    output=" "*(myord(ch)-1)+"A"
#    for i in range(2,myord(ch)+1):
#        line = alphabet[0:i]
#        output = output+"\n"+' '*(myord(ch)-i)+line+line[-2::-1]
#    return output
#print(pyramid(ch))
#
#
#        
#ch = input()
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#def myord(c):
#    i=1
#    while alphabet[i-1]!=c:
#        i+=1
#    return i  
#def pyramid(ch): 
#    output=""
#    for i in range(myord(ch)+1):
#        line=alphabet[0:i]
#        output = output+' '*(myord(ch)-i)+line+line[-2::-1]+"\n"
#    return output
#print(pyramid(ch))
#
#
#
#
##用递归写字母金字塔
#ch = input()
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#def myord(c):
#    return ord(c) - 64
#def f(n,x):
#    if n<=1:
#        return ' ' * x + 'A'
#    else:
#        b = f(n-1,x+1) + "\n" + ' '*x + alphabet[0:n] + (alphabet[:n])[-2::-1]
#        return b
#def pyramid(ch):
#    m = myord(ch)
#    return f(m,0)
#print(pyramid(ch))
#
#
#
#
#
#
#
#
##递归实例：河内塔问题
#def moveone(sfrom,sto):
#    print('Move a disk form',sfrom,'to',sto)
#    
#def henoi(n,sfrom,sto,sby):
#    if n == 1:
#        moveone(sfrom,sto)
#        return
#    henoi(n-1,sfrom,sby,sto)
#    moveone(sfrom,sto)
#    henoi(n-1,sby,sto,sfrom)
#
#
#def f1(n):
#    if n<3:
#        return n
#    else:
#        return f1(n-1)+f1(n-2)*2+f1(n-3)*3
#def f2(n):
#    if n<3:
#        return n
#    a,b,c = n-int(n),n-int(n)+1,n-int(n)+2
#    k = 2
#    while k<int(n):
#      x,y,z=a,b,c 
#      c = 3*x+2*y+z
#      b = z
#      a = y  
##     a,b,c = b,c,3*a+2*b+c   ####这是一个用于变量迭代更新的语法糖
#      k =k+1
#    return c
#def f3(n):
#    if n<=10:
#        d = f1(n)
#    else:
#        d = f2(n)
#    return d
#x=input()
#if '.'in x:
#    x=float(x)
#    print('%1.5e'%f3(x))
#else:
#    x=int(x)
#    print(f3(x))
#
#
#
#
##拉马努金级数计算圆周率
#def fact(n):
#    b=1
#    for i in range(1,n+1):
#        b*=i
#    return b
#from math import pi,sqrt
#a=1103
#mypi=99*99/2/sqrt(2)/a
#i=1
#while abs(mypi-pi)>10e-14:
#    a=a+fact(4*i)/((fact(i))**4)*(26390*i+1103)/(396**(4*i))
#    mypi=99*99/2/sqrt(2)/a
#    i+=1
#print('%.14f' %mypi)
#
#
#
#
#def f(m):
#    s=0
#    for i in range(1,m+1):
#        if m%i==0:
#            s=s+i
#    return s
#numbers = input()
#a,b = numbers.split()
#a = int(a)
#b = int(b)
#x,y,z = 0,0,0
#for i in range(a,b):
#    if 2*i>f(i):
#        x+=1
#    elif 2*i==f(i):
#        y+=1
#    elif 2*1<f(i):
#        z+=1
#print(x,y,z)
#        
#    
#
#def f(bits):
#    num = 0
#    for i in range(len(bits)):
#        b = bits[i]
#        if b == '.':
#            for k in range(i+1,len(bits)):
#                num = num + int(bits[k])*(2**(i-k))
#            break   
#        num = num*2 + int(b)
#    return '%.5f' %num
#a=''
#while True:
#    b = input()
#    if b!='end':
#        a = a + f(b) +'\n'
#    else:
#        break
#print(a)
#
#
#
#
#
##比较高效的递归计算斐波那契数列的方法
#def fib0(f1,f2,k,n):
#    if k<n:
#        return f1
#    else:return fib0(f2,f1+f2,k+1,n)
#    
#def fib(n):
#    return fib0(0,1,1,n)
#for i in range(17):
#    print(fib(i))
#
#
#
#
#m,n = input().split()
#m=int(m)
#n=int(n)
#def max_collatz(n):
#    Max = n
#    if n ==1:
#        return n
#    while n>1:
#        if n%2 == 0:
#            n = n/2
#            Max = max(Max,n)
#        elif n%2 != 0:
#            n = 3*n+1
#            Max = max(Max,n) 
#    return int(Max)
#            
#def most_collatz(m,n):
#    def count(n):
#        count = 0
#        if n == 1:
#            return 1
#        while n>1:
#            if n % 2 == 0:
#                n = n/2
#                count+=1
#            elif n % 2 != 0:
#                n = 3*n+1
#                count+=1
#        return count
#    counts = count(m)
#    maxi = m
#    for i in range(m,n+1):
#        if count(i)>counts:
#            counts = count(i)
#            maxi = i
#    print(int(maxi),int(counts))
#def find_i_with_biggest_sup_of_collatz(m,n):
#    k = m
#    result = 1
#    for i in range(m,n+1):
#        if max_collatz(i)>result:
#            result = max_collatz(i)
#            k = i
#    print(k,result)
#print(max_collatz(n))
#most_collatz(m,n)
#find_i_with_biggest_sup_of_collatz(m,n)
#        
#
#
#
#m,n = input().split()
#m = int(m)
#n = int(n)
#def drawTian(m,n):
#    def line1(m):
#        print('+'+'-'*m+'+'+'-'*m+'+')
#    def line2(m):
#        print('|'+' '*m+'|'+' '*m+'|')
#    line1(m)
#    for i in range(n):
#        line2(m)
#    line1(m)
#    for i in range(n):
#        line2(m)
#    line1(m)
#drawTian(m,n)       
#    
#
#
#
#m,n = input().split()
#m = int(m)
#n = int(n)        
#def drawboard(m,n) :
#    def line1(m):
#        print('+-'*m+'+')
#    def line2(m):
#        print('| '*m+'|')
#    for i in range(n):
#        line1(m)
#        line2(m)
#    line1(m)
#drawboard(m,n)
#
#
#
#
#
#def checkprime(n):
#    i = 2
#    while i**2 <= n:
#        b = n%i
#        i = i+1 
#        if b == 0:
#            return False
#    return True
#def single_prime_fater(n,i):
#    j = 1
#    while i**j<=n:
#        a = i**j
#        if n%a != 0 or not checkprime:
#            break
#        elif n%a == 0 and checkprime(i):
#            print(i)
#        j+=1
#    
#    
#def prime_fater(n):
#    i = 2
#    while i*i<=n:
#        single_prime_fater(n,i)
#        i+=1
#b = input()
#assert int(b)>0
#prime_fater(int(b))       
#
#    
#
#
#
#
#
##从长度为n的钢条上剪裁的不同方式数目等于不得到某种长度的钢条来进行剪裁的数目，
##加上得到这种长度的钢条来剪裁较短钢条的数目，当钢条长度小于0及尺寸数为0时，认为方式数为0
##而当剩余钢条长度小于3cm时应认为找到了一种剪裁方式
#def length(k):
#    if k == 1:
#        return 5
#    if k == 2:
#        return 8
#    if k == 3:
#        return 17
#    if k == 4:
#        return 28
#def num_cut(k,n):
#    if 0<=n<=3:
#        return 1
#    if k<=0 or n<0:
#        return 0
#    return num_cut(k,n-length(k))+num_cut(k-1,n)
#def steal_cut(n):
#    return num_cut(4,n)
#l,m,n= input().split()
#print(steal_cut(int(l)))
#print(steal_cut(int(m)))
#print(steal_cut(int(n)))
#
#        
#
#    
# 
#
#
#
#
#
#
#from math import sin
#from math import pi
#
#def integ(f, a, b, division):
#    integ = 0
#    for i in range(division):
#        c = a + i*(b-a)/division
#        d = a + (i+1)*(b-a)/division
#        integ = integ + (f(c) + 4*f(c/2+d/2) +f(d))*(d-c)/6
#    return integ
#
#def integrate(f,a,b):
#    div = 20
#    x1 = integ(f, a, b, div)
#    while True:
#        div *= 2
#        x2 = integ(f, a, b, div)
#        if abs((x2 - x1) / x1) < 1e-6:
#            return x2
#        x1 = x2
#print(round(integrate(sin, 0, pi), 6))
#
#
#
#
#from random import random as r
#def test():
#    a = r()
#    b = r()
#    if a*a + b*b <= 1:
#        return True
#    else:
#        return False
#def montecarlo(f,n):
#    count = 0
#    for i in range(n):
#        if f():
#            count = count + 1
#    return count/n
#def montecarlo_pi():
#    n = 100
#    while True:
#        mypi = 4*montecarlo(test,n)
#        if round(mypi,2) == 3.14:
#            return round(mypi,2)
#        n *= 10
#print(montecarlo_pi()) 
#  
#from random import randint as r,seed
#def luck7_one():
#   a,b = r(1,6),r(1,6)
#   if a+b==7:
#       return lambda x:x+4
#   else:
#       return lambda x:x-1
#def test_game(n):
#   seed(10)
#   your_money = 0
#   for i in range (n):
#       your_money = luck7_one()(your_money)
#   if your_money == 0:
#       return 'Yes'
#   else:
#       return 'No'
#print(test_game(1000))
#def lucky7(a,b):
#   seed(10)
#   your_money = a
#   count = 0
##   max_money = a
#   min_money = a
#   while True:
#       money = your_money
#       count += 1
#       your_money = luck7_one()(money)
#       max_money = max(max_money,your_money)
#       min_money = min(min_money,your_money)
#       if your_money >= b or your_money <= 0:
#           print(count,max_money,min_money,)
#           break
#lucky7(100,1000)
#
#
#
#
#
#
#        
##定义函数f，接受0个参数，返回两个函数，一个函数总返回None，
##一个返回上次调用的参数第一个函数的实参，若没有则返回None        
#def f():
#    a = None
#    def setter(x):
#        nonlocal a
#        a = x
#        return None
#    def getter():
#        return a
#        
#    return setter,getter
#s1,g1 = f()
#    
#    
#
##根据年月日参数计算是一年的第几天
#def find_day(year,month,day):
#    a = [31,28,31,30,31,30,31,31,30,31,30,31]
#    if (not year % 4 and year % 100) or not year % 400:
#        a[1] += 1
#    result = 0
#    for i in a[0:month - 1:]:
#        result += i
#    return int(result + day)
#a = input()
#year,month,day = a.split()
#year = int(year)
#month = int(month)
#day = int(day) 
#print(find_day(year,month,day))
#
#
#
#
#
#
#
#def all_positive(nlist):
#    def is_positive(n):
#        return 1 if n>0 else 0
#    for i in nlist:
#        if not is_positive(i):
#            return False
#    return True
#def is_sorted(list1):
#    for i in range(len(list1)-1):
#        if list1[i+1] < list1[i]:
#            return False
#    return True
#          
#def has_duplicate(list1):
#    
#    def has_same(list1,c):
#        for i in list1:
#            if i == c:
#                return True
#        return False
#    if list1 == []:
#        return False
#    for i in list1:
#        if has_same(list1,i):
#            return False
#    return True
#
#
#nlist = []
#list1 = []
#current = 'nlist'
#while True:
#    x = input()
#    if x == 'endnlist':
#        current = 'list1'
#        continue
#    if x == 'endlist1':
#        break
#    if current == 'nlist':
#        nlist.append(float(x))
#    else:
#        list1.append(x)
#
#print(all_positive(nlist))
#print(is_sorted(list1))
#print(has_duplicate(list1))
#
#
#
#
#
#
#
#def find_balance(nlist):
#    def sum_list(nlist):
#        sum0 = 0
#        for i in nlist:
#            sum0 += i
#        return sum0
#    if nlist == []:
#        print (-1)
#    elif len(nlist) == 1:
#        print (0)
#    else:
#        s = sum_list(nlist)
#        sum1 = 0
#        count = 0
#        for i in range(len(nlist)):
#            if sum1 == (s - nlist[i])/2:
#                print(i)
#                count += 1
#            sum1 += nlist[i]
#        if not count:
#            print (-1)
#nlist = []
#while True:
#    x = input()
#    if x=='endlist':
#        break
#    else:
#        nlist.append(int(x))
#find_balance(nlist)
#
#    
#    
#
#
#
#a = []
#a.append(a)
#print(a)
#
#
#
#  
#nlist = []
#exec('nlist = ' + input())
#def accum(nlist):
#    result = [0]*len(nlist)
#    sum0 = 0
#    j = 0
#    for i in nlist:
#        sum0 += i
#        result[j] = sum0
#        j += 1
#    return result
#print(accum(nlist))
#    
#          
#        
#n = int(input())
#def prime_factors(n):
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
#        if flist == [] or p != flist[-1]:
#            flist.append(p)
#        n //= p
#    return flist
#print(prime_factors(n))        
#
#s = []
#exec('s = ' + input())
#def partition(s):
#    def f(a,b,s):
#        sum1,sum2 = 0,0
#        for i in range(a):
#            sum1 += s[i]
#        for i in range(b,len(s)):
#            sum2 += s[i]
#        return abs(sum1 - sum2)
#    result = f(1,len(s)-1,s)
#    output = (1,len(s)-1)
#    for i in range(1,len(s)):
#        j = len(s)-1
#        while j >= i:
#            a = f(i,j,s)
#            if a < result:
#                result = a
#                output = (i,j)
#            j -= 1
#    return output
#print(partition(s))               
#
#
#
#list1 = []
#exec('list1 = ' + input())
#def disjoins(list1):
#    def is_intersection_empty(a,b):
#        if a[1] < b[0] or a[0] > b[1]:
#            return 0
#        return 1
#    list0 = []
#    n = 0
#    list0.append(list1[n])
#    for i in list1[1:]:
#        k = 0
#        for j in list0:
#            k += is_intersection_empty(j,i)
#        if not k:
#            list0.append(i)
#    return list0
#print(disjoins(list1))
#        
#        
#    
#
#
#
#def f(a,b,c,d):
#    return a+b+c+d
#x = 1,2
#y = 3,4
#print(f(*x,*y))
a = [[0]*10 for i in range(10)]
maze = [[1]*12]
for i in range(10):
    b = [1]+a[i]+[1]
    maze.append(b)
maze.append([1]*12)
for i in range(len(maze)):
    print(maze[i])
#
#
#
#
#
#
#
#
#
#
#
#
