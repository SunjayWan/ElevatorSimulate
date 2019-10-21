def sum_mean(s):
    a = []
    n = 1
    for i in s:
        a.append(i)
        s = float(sum(a))
        yield (s,s/n)
        n += 1
def test():
    a = sum_mean([1,2,3,4,5,6,7,8,9])      
    for i in range(9):
       print(next(a))
test()
        