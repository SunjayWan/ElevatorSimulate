#notice the difference!
a = [[]]*3
a[0].append(0)
b = [[]for i in range (3)]
b[0].append(0)
b[1].append(1)
b[2].append(2)
print(a,b,sep = '\n')

