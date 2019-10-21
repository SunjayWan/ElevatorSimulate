#def pykeys(slist):
#    import keyword
#    keydic = {i:0 for i in keyword.kwlist}
#    def count_keys(s):
#        nonlocal keydic
#        textfile = open(s)
#        for line in textfile:
#            for word in line.split():
#                if word in keyword.kwlist:
#                    keydic[word] = keydic.get(word,0) + 1
#        textfile.close()
#    for i in slist:
#        count_keys(i)
#    return keydic
#a = ['sun1.txt','sun-data.txt','test0.txt']
#print(pykeys(a))


from math import pi
a = list((pi * i * j for j in (1,3,6,7) for i in (14,8,9,11)))
ttable = ([f'{j+1}*{i+1} = {(j+1)*(i+1)}' for j in range(i+1)] for i in range(9))
for k in range(9):
    print(next(ttable))


        
        
    
         
     

    
