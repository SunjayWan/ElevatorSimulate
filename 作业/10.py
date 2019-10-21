def my_range(*args,**dics):
    if dics:
        raise TypeError("range() does not take keyword arguments")
    for i in args:
        if not isinstance(i,int):
            typei = type(i)
            raise TypeError("'" + repr(typei) + "' object cannot be interpreted as integer")   
    def range_gen(start,stop,step):
        while start < stop:
            yield start 
            start += step
    if len(args) == 1:
        stop = int(args[0])
        return range_gen(0,stop,1)
    if len(args) == 2:
       start = int(args[0])
       stop = int(args[1])
       return range_gen(start,stop,1)
    if len(args) == 3:
        start = int(args[0])       
        stop = int(args[1])
        step = int(args[2])
        return range_gen(start,stop,step)
    if len(args) > 3:
        raise TypeError('range excepted at most 3 arguments, got'+str(len(args)))
    if len(args) == 0:
        raise TypeError('range excepted at most 3 arguments, got 0')
        
        
    