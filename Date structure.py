##抽象数据类型的实现
##链表
#class LNode():
#    def __init__(self,elem ,lnext = None):
#        self.elem = elem
#        self.lnext = lnext
#class LinkedListUnderflow(ValueError):
#    pass
#class LList():
#    def __init__(self):
#        self._head = None
#        self._num = 0
#    def is_empty(self):
#        return self._num == 0
#    def pretend(self,elem):
#        self._head = LNode(elem,self._head)
#        self._num += 1
#    def pop(self):
#        if self._num == 0:
#            raise LinkedListUnderflow("is empty!")
#        a = self._head.lnext
#        e = self._head.elem
#        self._head = a
#        self._num -= 1
#        print(e)
#        return e
#    def append(self,elem):
#        if self._head == None:
#            self._head = LNode(elem)
#        else:
#            p = self._head
#            for i in range(self._num):
#                p = p.lnext
#            p.lnext = LNode(elem)
#            self._num += 1
#    def pop_last(self):
#        if self._nun == 0:
#            raise LinkedListUnderflow("is empty!")
#        if self._num == 1:
#            e = self._head.elem
#            self._head = None
#            return e
#        p = self._head
#        for i in range(self._num-1):
#            p = p.lnext
#        e = p._next.elem
#        p._next = None
#        return e
#    def find(self,pred):
#        p = self._head
#        while p is not None:
#            if pred(p._elem):
#                return p.elem
#            p = p.lnext
#        return None
#    def for_each(self,proc):
#        p = self._head
#        while p is not None:
#            proc(p.elem)
#            p = p._lnext
#    def __str__(self):
#        s = ''
#        if self._num == 0:
#            return s
#        p = self._head
#        while p is not None:
#            s = s + str(p.elem)
#            p = p.lnext
#        return s
#llist = LList()
#for i in range(10):
#    llist.append(i)
#    print(llist)
#    
#for i in range(20):
#    llist.pretend(i)
#for i in range(5):
#    llist.pop()

##迷宫问题
#import tkinter as tk
#
#class CreateMaze(tk.Frame):
#    def __init__(self,m,n):
#        tk.Frame.__init__(self)
#        self._m = m
#        self._n = n
#        self.master.title("Create a n*m map")
#        self.grid()
#        self._map = [[0]*m for i in range(n)]
#        self._solve = []
#        self.label = tk.Label(text = 'create a maze')
#        self.label.grid(rowspan = 2, columnspan = m, sticky = tk.EW)
#        for i in range(n):
#            for j in range(m):
#                a = str(i)+str(j)
#                e = str(i)
#                f = str(j)
#                b = 'self.button'+a+"= tk.Button(self,text = '0',command = self._grid"+a+')'
#                c = 'self.button'+a+'.grid(row = '+e+',column = '+f+')'
#                exec(b)
#                exec(c)
#        self.Button1 = tk.Button(self,text = "confirm",command = self._change)
#        self.Button1.grid(columnspan = m,sticky = tk.EW)
#        self.Button2 = tk.Button(self,text = 'solve',command = self._solvemaze)
#        self.Button2.grid(columnspan = m,sticky = tk.EW)
#    def _change(self):
#        self.label['text'] = "click 'solve' to get the solution"
#    def _solvemaze(self):
#        maze = self._map
#        start = (0,0)
#        end = (9,9)
#        def solvemaze(maze,start,end):
#            direction = [[0,1],[1,0],[0,-1],[-1,-1]]
#            solve = []
#            def mark(maze,s):
#                maze[s[0]][s[1]] = 2
#            def possible(maze,s):
#                if s[0] < 0 or s[0] > 9:
#                    return False
#                if s[1] < 0 or s[1] > 9:
#                    return False
#                return maze[s[0]][s[1]] == 0
#                    
#            t = start
#            solve.append((t,0))
#            while len(solve) != 0:
#                t,nxt = solve.pop()
#                for i in range(nxt,4):
#                    x = t[0] + direction[i][0]
#                    y = t[1] + direction[i][1]
#                    nextfoot = (x,y)
#                    if nextfoot == end:
#                        solve.append((t,i+1))
#                        solve.append((nextfoot,i))
#                        return solve
#                    if possible(maze,nextfoot):
#                        solve.append((t,i+1))
#                        mark(maze,nextfoot)
#                        solve.append((nextfoot,0))
#                        break
#            return None
#        solve = solvemaze(maze,start,end)
#        if solve == None:
#            self.label['text'] = "There's no solution to the maze"
#        else:
#            solve = [solve[i][0] for i in range(len(solve))]
#            self._solve = solve
#            self._print_path()
#            
#            
#        
#        
#    def _print_path(self):
#        path = self._solve
#        n = self._n
#        m = self._m
#        print('\n')
#        for i in range(n):
#            for j in range(m):
#                a = (i,j)
#                if a in path:
#                    b = str(i)+str(j)
#                    c = 'self.button'+b+"['text'] = '*'"
#                    exec(c)
#
#    for i in range(10):
#        for j in range(10):
#            a = str(i)+str(j)
#            e = str(i)
#            f = str(j)
#            b = 'def _grid'+a+'(self):'
#            c = 'self._map['+e+']['+f+'] = 1'
#            d = 'self.button'+a+"['text']='1'"
#            g = b+'\n'+'    '+c+'\n'+'    '+d
#            exec(g)
#CreateMaze(10,10).mainloop()





##KMP算法
#def kmp(s,t):
#    n, m = len(t), len(s)
#    i, j = 0, 0
#    def pnext(s):
#        i, k, m = 0, -1,  len(s)
#        pnext = [-1]*m
#        while i < m-1:
#            if k == -1 or s[i] == s[j]:
#                i, k = i+1, k+1
#                pnext[i] = k
#            else:
#                k = pnext[k]
#        return pnext
#            
#    while j < n and i < m:
#        if s[i] == t[j] or i == -1:
#            i += 1
#            j += 1
#        else:
#            i = pnext(i)
#    if i == m:
#        return j-i
#    return -1




        
   
















##八皇后问题
#def nqueens(n):
#    solves = []
#    def check(c,queens):
#        x, y = c[0], c[1]
#        for s in queens:
#            if x == s[0] or y == s[1] or x + y == s[0]+s[1] or x - y == s[0]-s[1]:
#                return False
#        return True
#    queens = []
#    i, j = 0, 0
#    while 0 <= i <= n - 1:
#        if j == n:
#            x,y = queens.pop()
#            i = i - 1
#            j = y + 1
#            if i == 0 and j > n/2:
#                 return solves
#        while 0 <= j <= n-1:
#            if len(queens) == n-1 and check((i,j),queens):
#                queens.append((i,j))
#                print(queens)
#                solves.append(queens)
#                print(solves)
#                x,y = queens.pop()
#                i = i - 1
#                j = y + 1
#            if check((i,j),queens):
#                queens.append((i,j))
#                i += 1
#                j = 0
#                break
#            else:
#                j += 1
#    return solves
#nqueens(8)

a = 8
def f(n):
    b = a+n
    return b
c = f(4)
print(c)
    
    

    




        

        
            
        
        
            
        
        
        
        
    
    
