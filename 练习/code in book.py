##无穷生成器
#def fibs_infgen():
#    f0,f1 = 0, 1
#    while True:
#        yield f0
#        f0,f1 = f1,f1 + f0
#fibs = fibs_infgen()
#for i in range(20):
#    print(next(fibs))
#    
#def circular(seq):
#    i = 0
#    while True:
#        yield seq[i]
#        i += (i + 1) % len(seq)
#
#def inf_name(s):
#    count = 0
#    while True:
#        yield str(s) + str(count)
#        count += 1
#        
#        
##取得文件中的浮点数
#def get_float(fname):
#    infile = open(fname)
#    while True:
#        line = infile.readline()
#        if not line:
#            break
#        infile.close()
#        for s in line.split():
#            yield float(s)
#            
#def read_floats(fname):
#    nlist = []
#    infile = open(fname)
#    crt = 0
#    
#    def next_float():
#        nonlocal nlist,crt
#        if crt == len(nlist):
#            line = infile.readline()
#            if not line:
#                infile.close()
#                return None
#            nlist = line.split()
#            crt = 0
#        crt += 1
#        return float(nlist[crt - 1])
#    
#    return next_float


#
#def fibs_closure():
#    f0, f1 = 0, 1
#    i = 1
#    
#    def generator():
#        nonlocal f0,f1,i
#        while True:
#            tmp = f0
#            f0, f1 = f1, f1 + f0
#            i += 1
#            return tmp
#    return generator
#fibs = fibs_closure()
#for i in range(20):
#    print(fibs())
    


##生成无素数序列
#def prime():
#    plist = [2]
#    yield 2
#    cn = 3
#    def is_prime(cn):
#        for p in plist:
#            if cn % p == 0:
#                return False
#            if p*p > cn:
#                return True
#    while True:
#        if is_prime(cn):
#            yield cn
#            plist.append(cn)
#        cn += 2
            


##生成银行账户对象
#def account(user,init = 0):
#    def despoist(v):
#        nonlocal amount,history,user_name
#        amoint += v
#        history.append(("despoist",v))
#        print(user_name,"desposing",v,"done)
#    def withdrew(v):
#        nonlocal amount,history,user_name
#        if  v > amount:
#            print('No enough money in account.')
#            return
#        history.append(('withdrew',v))
#        amount -= v
#        print(user_name,"withdrew",v,"done")
#    def dispatcher(command,v):
#        if command == 'name':
#            return user_name
#        elif command == 'history':
#            return history[:]
#        elif command == amount:
#            return amount
#        elif command = "despoist":
#            return despoist(v)
#        elif command = "withdrew":
#            return withdrew(v)
#        else:
#            return "Not understood"
#  
#    
#    user_name = user
#    amount = init
#    history = [init]
#    print('Account for',user,"created,with initially",str(amount)+'.')
#    
#    return dispatcher


##异常处理
#def summary_datafile(fname):
#    try:
#        datafile = open(fname)
#    except OSError:
#        print('File cannot open:',frame)
#        raise
#    
#    num = 0
#    errnum = 0
#    accum = 0.0
#    
#    for line in datafile:
#        for s in line:
#            try:
#                x = float(s)
#                accum += x
#                num += 1
#            except ValueError:
#                errnum += 1
#    datafile.close()
#    
#    return (num,errnum,accum)
#
#
#if __name__ == '__main__':
#    num = 0
#    errnum =0
#    accum = 0.0 
#    while True:
#        frame = input("Next file name (None to quit)")
#        if frame == "None":
#            print(num,errnum,accum)
#            break
#        try:
#            n,e,a = summary_datafile(fname)
#            num += u
#            errnum += e
#            accum += a
#        except OSError as mag:
#            print("Details:",msg.args)



##用表完成斐波那契数列的递归计算
#def fibs(n):
#    fib = [-1]*(n+2)
#    fib[0] = 0
#    fib[1] = 1
#    def fib0(k):
#        if fib[k] != -1:
#            return fib[k]
#        fib[k] = fib0(k-1) + fib0(k-2)
#        return fib[k]
#    return fib0(n)
#            
#for i in range(50):
#    print(fibs(i))








