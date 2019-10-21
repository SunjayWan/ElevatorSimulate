class StackUnderflow(ValueError):
    pass
class Stack():
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
    solves = []
    def check(c,queens):
        x, y = c[0], c[1]
        for s in queens:
            if x == s[0] or y == s[1] or x + y == s[0]+s[1] or x - y == s[0]-s[1]:
                return False
        return True
    queens = Stack()
    i, j = 0, 0
    while 0 <= i <= 7 :
        if j == 8:
             x, y = queens.top()
             queens.pop() 
             i, j = i - 1, y + 1
             if i == 0 and j > 4:
                 return solves
        while 0 <= j <= 7:
            if i == 7 and check((i,j),queens.get()):
                queens.push((7,j))
                print(queens)
                solves.append(queens.get())
                x, y = queens.top()
                queens.pop()
                i, j = i - 1, y + 1
                
            if check((i,j),queens.get()):
                queens.push((i,j))
                i += 1 
                j = 0
                break
            else:
                j += 1
      
    return solves           
        
print(eightqueens_slove())