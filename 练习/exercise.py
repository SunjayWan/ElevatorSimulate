#def find_dups(list1):
#    a = []
#    for i,j in enumerate(list1):
#        list2 = list1[:]
#        del list2[i]
#        if j in list2 and j not in a:
#            a.append(j)
#    return a

#def prime_facters(n):
#    from math import ceil,sqrt
#    a = []
#    for j in range(2,ceil(sqrt(n))):
#        if n%j == 0:
#            a.append(j)
#            n /= j
#    return a
        

#def squeez(list1,list2):
#    for i in range(len(list2)):
#        list2[i] += 1
#    a = []
#    for j in list1:
#        if j not in list2:
#            a.append(j)
#    return a

#def comp(list1,list2):
#    for i,j in enumerate(list1):
#        for l,k in enumerate(j):
#            if k != list2[i][l]:
#                return False
#    return True

#
#def yang(n):
#    def next_yang(s):
#        s.append(0)
#        b = [1]
#        for i in range(len(s)-1):
#            b.append(s[i] +s[i+1])
#        return b
#    def f(a):
#        d = '1'
#        for i in a[1::]:
#            d += ' ' + str(i)
#        return d
#    a = [1]
#    for i in range(n):
#        print(f(a).center(3*n))
#        b = next_yang(a)
#        a = b

#
#def date(year,num):
#    if not (isinstance(year,int) and isinstance(num,int) and year > 0 and num > 0):
#        return None
#    a = [31,28,31,30,31,30,31,31,30,31,30,31]
#    if (not year % 4 and  year % 100 ) or  not year % 400 :
#        a[1] += 1
#    if num > sum(a):
#        return None
#    m = 1 
#    for i in range(12):
#        if num <= a[i]:
#            return (year,m,num)
#        else:
#            num -= a[i]
#            m += 1
#year, num = map(int,input().split())
#print(date(year, num))




#list1, list2 = [], []
#exec('list1 = ' + input()) 
#exec('list2 = ' + input())
#def squeeze(list1, list2):
#    k = 0
#    list3 = list1[:]
#    for i,j in enumerate(list3):
#        if (j - 1) in list2:
#            del list1[i-k]
#            k += 1
#squeeze(list1, list2) 
#print(list1)       
    
#def remove(text, cset):
#    a = ''
#    for i in text:
#        if i not in cset:
#            a += i
#    return a
#text, cset = input().split('|')
#print(remove(text, cset))    
            

#def anagram(s1, s2):
#    a = sorted(s1)
#    b = sorted(s2)
#    if a == b:
#        return True
#    return False
#s1, s2 = input().split('|')
#print(anagram(s1, s2))


#def rev_pair(slist):
#    result = []
#    for i in slist:
#        if i[::-1] in slist and \
#        (i,i[::-1]) not in result \
#        and (i[::-1],i) not in result:
#            result.append((i,i[::-1]))
#    return result       
#slist = []
#exec('slist=' + input())
#print(rev_pair(slist))


#a = (x**2%15 for x in range(9))
#b = max(a) + min(a)

#text = input()
#def most_frequanct(text):
#    def count(text,x):
#        count = 0
#        for i in text:
#            if i == x:
#                count += 1
#        return count
#    a = []
#    b = []
#    maxa = 0
#    for i in text:
#        n = count(text,i)
#        if i not in b and n > maxa:
#            a = [(i,n)]
#            b = [i]
#            maxa = n
#        if i not in b and n == maxa:
#            b.append(i)
#            a.append((i,n))
#            
#    if len(a) == 1:
#        return a[0]
#    return tuple(a)
#    
#ans = most_frequanct(text)
#
#def cmp(x):
#    return x[0]
#
#if type(ans[0]) != str:
#    ans = sorted(ans,key=cmp)
#print(tuple(ans))



#a = input()
#b = []
#exec('b='+a)
#def dict_intersection(*b):
#    a = {}
#    for x in b:
#        for k in x.keys():
#            if k not in a.keys():
#                a[k] = {x[k]}
#            if k in a.keys():
#                a[k].add(x[k])
#    return a
#ans = dict_intersection(*b)
#
#def cmp(x):
#    return x[0]
#
#ans = list(ans.items())
#ans = sorted(ans, key=cmp)
#for i in range(len(ans)):
#    ans[i] = list(ans[i])
#    ans[i][1] = sorted(list(ans[i][1]))
#print(ans)






#dic_1 = eval(input())
#dic_2 = eval(input())
#
#def cmp(x):
#    return x[0]
#def dict_intersect(dic_1,dic_2):
#    a = {}
#    for i in dic_2.keys():
#        if i in dic_1.keys():
#            a[i] = dic_2[i]
#    return a
#def dict_union(dic_1,dic_2):
#    a = dic_2
#    for i in dic_1:
#        if i not in a.keys():
#            a[i] = dic_1[i]
#    return a
#            
#ans1 = dict_intersect(dic_1,dic_2)
#ans2 = dict_union(dic_1,dic_2)
#ans1 = list(ans1.items())
#ans1 = sorted(ans1, key=cmp)
#print(ans1)
#ans2 = list(ans2.items())
#ans2 = sorted(ans2, key=cmp)
#print(ans2)











#dic=eval(input())
#def rev_dict(dic):
#    a = {}
#    for i,j in dic.items():
#        a[j] = i
#    return a
#def cmp(x):
#   return x[0]       
#ans = rev_dict(dic)
#ans = list(ans.items())
#ans = sorted(ans, key=cmp)
#print(ans)
        
    

#a = input()
#def f(n):
#    return 'class' + str(n)
#dic = {f(n):n*n for n in range(100,201)}
#print (dic[a])

#def count(list2,s):
#        k = 0
#        for i in list2:
#            if i == s:
#                k += 1
#        return k
#def list2dict_count(list1):
#    a = {}
#    for i in list1:
#        a[i] = count(list1,i)
#    return a
#def cmp(x):
#    return x[0]
#
#list1 = input().split()
#ans = list2dict_count(list1)
#ans = list(ans.items())
#ans = sorted(ans, key=cmp)
#print(ans)








    