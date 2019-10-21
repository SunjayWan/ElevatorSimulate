#开发环境：Spyder(python3.6)
def issubsequence(s,t):
    s = list(s.split('，'))                          #将模式串按时间切分
    def get_next(s):
        i,k,p = 0,-1,len(s)
        pnext = [-1]*p
        while i < p - 1:
            if s[i] == s[k] or k == -1:
                i += 1
                k += 1
                if s[i] == s[k]:
                    pnext[i] = pnext[k]
            else:
                k = pnext[k]
        return pnext
    pnext = [get_next(s[i]) for i in range(len(s))]  #得到每个事件对应字符串的next表
    k, j, n = 0, 0, len(t)                           #j为标准串的下标，无回溯的匹配
    m,i,c,p = len(s[k]),0,s[k],pnext[k]              #一个一个事件匹配，记录成功地个数
    while j < n and i < m:
        if i == -1 or t[j] == c[i]:
            j, i = j + 1, i + 1
        else:
            i = p[i]
        if i == m:
            k += 1
            if k == len(s):
                return True
            m,i,c,p = len(s[k]),0,s[k],pnext[k]     #每匹配成功一个事件后更新与模式串有关的所有变量
    return False



if __name__ == "__main__":
    
    s1 = '买Amazon股票，买Facebook股票，买Amazon股票，买Google股票'
    s2 = '买Amazon股票，买Facebook股票，买Facebook股票，买Google股票'
    t = '买Microsoft股票，买Amazon股票，买Facebook股票，买Amazon股票，买Google股票'
    print(issubsequence(s1,t))
    print(issubsequence(s2,t))
    

        
    
    
    
    
    
    


    