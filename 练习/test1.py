from math import gcd

def phi(p):
    s = 0
    for i in range(p):
        if gcd(i, p) == 1:
            s += 1
    return s






def mod_inv_builder(p):
    i = phi(p) - 1
    
    def mod_inv(k):
        if gcd(k, p) != 1:
            return 0
        
        nonlocal i
        result = 1
        while i > 0:
            if i % 2:
                result = result * k % p
            i //= 2
            k = k * k % p
        return result
    return mod_inv()










if __name__ == '__main__':
    while True:
        i = input()
        if i == 'end':
            break
        print(mod_inv_builder(int(i)))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        