class StackUnderflow(ValueError):
    pass
class Stack():                #先实现一个栈的类
    def __init__(self):
        self._elem = []
    def is_empty(self):
        return self._elem == []
    def top(self):
        if self._elem == []:
            raise StackUnderflow("stack underflow")
        return self._elem[-1]
    def push(self,elem):
        self._elem.append(elem)
    def pop(self):
        if self._elem == []:
            raise StackUnderflow("stack underflow")
        self._elem.pop()
    def __str__(self):
        return str(self._elem)    
    def get(self):
        return self._elem
    
def eightqueens_slove():
    def check(c,queens):        #定义辅助函数检查落子是否合理
        x, y = c[0], c[1]
        for s in queens:
            if x == s[0] or y == s[1] or x + y == s[0]+s[1] or x - y == s[0]-s[1]:
                return False
        return True
    queens = Stack()
    i, j = 0, 0
    while 0 <= i <= 7 :
        if j == 8:             #j=8表示此情况无解，进行回溯
             x, y = queens.top()
             queens.pop() 
             i, j = i - 1, y + 1
        while 0 <= j <= 7:     #每行只有一个皇后，每列上坐标依次增加
            if i == 7 and check((i,j),queens.get()):
                queens.push((7,j))
                print(queens)
                return          
            if check((i,j),queens.get()):  #找到可能的落子点后进行下一行查找
                queens.push((i,j))
                i += 1 
                j = 0
                break
            else:
                j += 1
                
eightqueens_slove()       
