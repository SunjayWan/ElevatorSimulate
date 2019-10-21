#list2 = list((x for x in list1 if list.count(x) > 1))
#(x for x in list1[y] for y in len(list1))
#list(list(list1[y][x] for y in range(len(list1[x])) for x in range(len(list1))))
#list()


#list(set(x))
#[z for y in x for z in y]
#[[x[j][i] for i in range(len(x))] for j in range(len(x[i]))]
#[x[i]]
#zip(*[iter(x)]*2)


#[x for y in z forx in y]
#(x[j][i] for i in range(len(x)) for j in range(len(x[i])))
#[[x[i] + x[i+1]]for i in range(1,len(x),2)]


#list1 = [[1,2,3],[4,5,6],[7,8,9]]
#a = list(([list1[j][i] for j in range(len(list1[i]))] for i in range(len(list1))))
#print(a)

#class Countable:
#    count = 0
#    def __init__(self,cls):
#        count += 1
#    @classmethod
#    def get_count(cls):
#        return Countable.count
#a = Countable(cls)
#print(Countable.get_count())
