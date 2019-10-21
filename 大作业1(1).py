#定义电梯类，属性有电梯的运行状态，负载人员情况，含有一个优先队列来记录电梯要去往的楼层
#定义人员类，属性包括人所在的楼层和要前往的楼层，人员等待的时间，保存在这个类的类变量中
#定义楼层类（按钮类），对每个楼层生成一个类对象，每秒钟各个楼层对象向电梯发送指令，楼层类中定义一个队列保存等待的人员
#初始化电梯，停留在一层，每秒钟各个楼层向电梯发送指令，电梯得到指令修改其内部的优先队列和运行状态。
#若电梯所在楼层与优先队列顶的元素相同，电梯停下，间隔固定的秒数后再运行，在此期间各楼层依然可以对电梯发出指令
#每个楼层随机生成人员的队列（两个，上下不同的方向），电梯停下时弹出队列中元素入电梯，直到电梯达到满负荷或队列空
#关于电梯队列的优先级：每个人是一个三元组，所在楼层，去往楼层，上下方向，上下方向与电梯运行方向相同优先级高
#与当前楼层越近优先级越高
#要定义一个每层楼按钮的类，电梯每次只会向一个方向运行到没有人为止，这时再读取各层楼发出的指令，先进先出，应该是一个队列
#电梯空时电梯接到指令前往某一楼层，重设运行方向，然后开始人员入电梯



import random as r
class QueneUnderflow():
    pass
class Quene():
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0]*init_len
        self._head = 0
        self._num = 0
    def is_empty(self):
        return self._num == 0
    def peek(self):
        if self._num == 0:
            raise QueneUnderflow
        return self._elems(self._head)
    def dequene(self):
        if self._num == 0:
            raise QueneUnderflow
        e = self._elems[self._head]
        self._head = (self._head+1)%self._len
        self._num -= 1
        return e
    def enquene(self,e):
        if self._num == self._len:
            self.__extend
        self._elems[(self._head+self._num)%self._len] = e
        self._num += 1
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self.elems[(self.head+i)%self._len]
            self._elems, self._head = new_elems, 0

class PrioQueneError():
    pass
class PrioQuene():
    def __init__(self, elist=[]):
        self._elems = list(elist)
        
    def is_empty(self):
        return not self._elems
    def peek(self):
        if self.is_empty():
            raise PrioQueneError
        return self._elems[0]
    def enquene(self, e):
        self._elems.append(None)
        self.siftup(e,len(self._elem)-1)
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e
    def dequene(self):
        if self.is_empty:
            raise PrioQueneError
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e,0,len(elems))
        return e0
    def siftdown(self,e,begin,end):
        elems, i, j = self._elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e
time = 100  
a = 0
b = 50 
n = 5    
class Passenger():
    s = 0
    time = time
    def __init__(self, lift):
        self._start = r.randint(1,n)#所在楼层
        self._end = self._genend()#目的楼层
        self.direction = lambda start,end: -1 if start > end else 1 (start,end)#上楼1，下楼-1
        self._lift = lift#指定电梯（在单电梯系统中可以不需要）
        self._order
        self._arrivetime = Passenger.time + 1#初始化为时间范围之外
        if Passenger.s < Passenger.time:
            Passenger.s = Passenger.s + (r.random() * (b - a) + a)
            self._arrivetime = Passenger.s
        self._leavetime = None#上电梯的时间
    def _genend(self):
        t = r.randint(1,n)
        while t == self._start:
            t = r.randint(1,n)
        return t
    def __lt__(self,other):
        direction = self.lift._direction
        if direction > 0:
            return self._end < other._end
        if direction < 0:
            return self._end > other._end
    def _order(self):
        order = (self._start,self._direction)
        self._lift._orderquene.enquene(order)
    @classmethod
    def _gentime(cls):
        while cls.s < cls.time:
            t = r.random()*(b-a)+a
            cls.s += t
            yield cls.s

class Lift():
    def __init__(self, speed, lmax):
        self._direction = 0
        self._speed = speed
        self._max = lmax
        self._passengerquene = PrioQuene()#乘客队列
        self._orderquene = Quene()#命令队列
        self._condition = (1, 1)#现在的楼层和下一个要到达的楼层
        self._floor = []
        for i in range(1,lmax+1):
            i = str(i)
            self._floor.append(Floor(i))

def genpassenger(seconds, lift):
    a = Quene()
    def genpassenger0():
        while True:
            yield Passenger(lift)
    g = genpassenger0()
    p = next(g)
    a.enquene(p)
    while p._arrivetime < seconds:
        p = next(g)
        a.enquene(p)
    return a
        
class Floor():
    def __init__(self,m):
        if m == 1:
            self._upquene = PrioQuene()
        if m == n:
            self._downquene = PrioQuene()
        else:
            self._downquene = PrioQuene()
            self._upquene = PrioQuene()
        
    

time = 1000  
a = 0
b = 50 
lmax = 5
speed = 3
def simulift():
    lift = Lift(speed,lmax)
    allpassenger = genpassenger(time, lift)
    
    seconds = 0
    def openthedoor(lift):
        pass
    def updatecondition(lift):
        pass
    while seconds < time:
#        work of the system
        
        
        
        
        
        updatecondition(lift)
        
        if lift._passengerquene.is_empty and not lift._orderquene.is_empty:
            a = lift._orderquene.peek
            b = lift._condition[0]
            if a == b:
                openthedoor()
            elif a > b:
                lift._direction = -1
                lift._condition[1]  = a[0]
            elif a < b:
                lift._direction = 1
                lift._condition[1] = a[0]
        if not lift._passengerquene.is_empty and lift._condition[0]==lift._condition[1]:
            if lift._floor[lift._condition[0]].state == 1 or lift._passengerquene.peek._end:
                openthedoor()
            
                
            
        
        s+1
    return None
    
    

    
#电梯每秒钟要干的事情：
        #如果电梯静止，读取指令队列的第一个元素，设定方向，开始运行
        #如果电梯非空，且到达某一楼层，取乘客队列第一个元素和此楼层的呼叫状态，检查是否应该停下，若否，电梯正常运行
        #若电梯开门，修改楼层状态，修改运行方向，先下后上，检查堆顶元素的目标楼层，对应的人员全部弹出，
        #然后检查从这一层与电梯运行方向相同的队列，依次弹出，入堆。电梯重新开始运行，总时间加上电梯开门的时长
#每秒钟系统要做的事：
        #记录电梯又运行了一秒，更新电梯的楼层状态
        #检查此时的时间戳是否与乘客队列顶端的元素时间一致，若一致则将其弹出，存入对应楼层的等待队列
        #产生新的楼层指令，若有，判断是否在电梯的运行路径上，若在，标记楼层呼叫状态
        #若不在电梯此时的运行路径上，则存入指令队列，等待电梯之后访问
#欠缺：一个判断电梯是否运行到新的楼层的管理系统
       

        
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
            
                                                                                                                    
        
        
        
        
        
        
        
