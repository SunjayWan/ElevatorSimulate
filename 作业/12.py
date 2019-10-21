def chain(*iterables):
    for i in iterables:
        for j in i:
            yield j
    
def test():
    a = [1,2,3,4,5]
    b = 'abcde'
    c = chain(a,b)
    for i in range(10):
        print(next(c))
test()

