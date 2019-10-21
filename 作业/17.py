def all_positive(mlist):
    
    def positive(nlist):
        for i in nlist:
            if i <= 0:
                return False
        return True
    for j in mlist:
        if positive(j):
            return j
    raise ValueError
       
    
def test():
    a = [[-1,2,3],[4,5,6],[7,8,9]]
    b = [[1,2,-3],[4,5,-6],[7,8,9]]
    c = [[1,-2,3],[4,-5,6],[7,-8,9]]
    print(all_positive(a))
    print(all_positive(b))
    print(all_positive(c))
test()