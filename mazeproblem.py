import tkinter as tk
def mazeproblem():
    
    class CreateMaze1(tk.Frame):
        def __init__(self):
            tk.Frame.__init__(self)
            self._n = 0
            self._m = 0
            self.master.title('Maze problem')
            self.grid()
            self.label = tk.Label(self,text = 'input "n m" to create a maze of same size')
            self.label.grid()
            self.entry = tk.Entry(self)
            self.entry.grid(sticky = tk.EW)
            self.button = tk.Button(self,text = "confirm",command = self._confirm)
            self.button.grid(sticky = tk.EW)
            
        def _confirm(self):
            n,m = self.entry.get().split()
            n = int(n)
            m = int(m)
            self._n = n
            self._m = n
            self.master.destroy()
    a = CreateMaze1()
    a.mainloop()
    m = a._m
    n = a._n
      
    class CreateMaze2(tk.Frame):
        def __init__(self):
            tk.Frame.__init__(self)
            self._m = m
            self._n = n
            self.master.title('Maze problem')
            self.grid()
            self._map = [[0]*m for i in range(n)]
            self._solve = []
            self.label = tk.Label(text = 'create a maze',justify = tk.LEFT)
            self.label.grid(rowspan = 2, columnspan = m, sticky = tk.EW)
            for i in range(n):
                for j in range(m):
                    a = str(i)+'_'+str(j)
                    e = str(i)
                    f = str(j)
                    b = 'self.button'+a+"= tk.Button(self,text='0',command=self._grid"+a+',height=1, width=4)'
                    c = 'self.button'+a+'.grid(row = '+e+',column = '+f+')'
                    exec(b)
                    exec(c)
            self.Button1 = tk.Button(self,text="confirm",command=self._change)
            self.Button1.grid(columnspan = m,sticky = tk.EW)
            self.Button2 = tk.Button(self,text='solve',command=self._solvemaze,state=tk.DISABLED)
            self.Button2.grid(columnspan = m,sticky = tk.EW)
            self.button0_0['text'] = 'start'
            a, b = str(m-1), str(n-1)
            c = "self.button"+a+"_"+b+"['text'] = 'end'"
            exec(c)
            
        def _change(self):
            if self.Button1['text'] == "confirm":
                self.label['text'] = "click 'solve' to"+"\n"+" get the solution"
                self.Button1['state'] = tk.DISABLED
                self.Button2['state'] = tk.NORMAL
                for i in range(n):
                    for j in range(m):
                        a = str(i)+'_'+str(j)
                        b = "self.button"+a+"['state']=tk.DISABLED"
                        exec(b)
                
                
            else:
                self.master.destroy()
                
        def _solvemaze(self):
            maze = self._map
            start = (0,0)
            end = (n-1,m-1)
            def solvemaze(maze,start,end):
                direction = [[0,1],[1,0],[0,-1],[-1,0]]
                solve = []
                def mark(maze,s):
                    maze[s[0]][s[1]] = 2
                def possible(maze,s):
                    if s[0] < 0 or s[0] > n-1:
                        return False
                    if s[1] < 0 or s[1] > m-1:
                        return False
                    return maze[s[0]][s[1]] == 0
                        
                t = start
                solve.append((t,0))
                while len(solve) != 0:
                    t,nxt = solve.pop()
                    for i in range(nxt,4):
                        x = t[0] + direction[i][0]
                        y = t[1] + direction[i][1]
                        nextfoot = (x,y)
                        if nextfoot == end:
                            solve.append((t,i+1))
                            solve.append((nextfoot,i+1))
                            return solve
                        if possible(maze,nextfoot):
                            solve.append((t,i+1))
                            mark(maze,t)
                            solve.append((nextfoot,0))
                            break
                        
                return None
            solve = solvemaze(maze,start,end)
            if solve == None:
                self.label['text'] = "There's no solution to the maze"
                self.Button2["state"] = tk.DISABLED
            else:
                solve = [solve[i][0] for i in range(len(solve))]
                self._solve = solve
                self._print_path()
                self.Button2["state"] = tk.DISABLED
                self.label["text"] = "question solved!"
            self.Button1["text"] = "quit"
            self.Button1["state"] = tk.NORMAL
            
        def _print_path(self):
            path = self._solve
            n = self._n
            m = self._m
            print('\n')
            for i in range(n):
                for j in range(m):
                    a = (i,j)
                    if a in path:
                        b = str(i)+'_'+str(j)
                        c = 'self.button'+b+"['text'] = '*'"
                        exec(c)
    
        for i in range(n):
            for j in range(m):
                a = str(i)+'_'+str(j)
                e = str(i)
                f = str(j)
                b = 'def _grid'+a+'(self):'
                c = 'self._map['+e+']['+f+'] = 1'
                d = 'self.button'+a+"['text']='1'"
                g = b+'\n'+'    '+c+'\n'+'    '+d
                exec(g)
    CreateMaze2().mainloop()
mazeproblem()


    


        
        





                
                    
                
       
    
        

    



        
            
            
    
    
