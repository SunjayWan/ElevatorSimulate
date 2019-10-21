print("这是一个简单的互动攻防游戏，双方初始值5血1气，每回合双方各有如下操作：攻击：减弱对方生命，\
防御：抵抗对方攻击，蓄力：提高伤害数值，回血：增加生命值。这些操作分别由指令A B C D表示，来与同伴切磋一下吧！")
def shift(x):
    if x=="A":
        return 1
    if x=="D":
        return 2
    if x=="S":
        return 3
    if x=="w":
        return 4
    else:
        return 0
def shift2(y):
    if y=="J":
        return 1
    if y=="L":
        return 2
    if y=="K":
        return 3
    if y=="I":
        return 4
    else:
        return 0
i = 0
a1,b1,a2,b2 = 5,1,5,1 
while a1>0 and a2>0:
    i=i+1    
    print("round",i)
    print("player1' life",a1,"player1'power",b1)
    print("player2' life",a2,"player2'power",b2,)
    b=int(shift(input("player1' move:")))
    c=int(shift2(input("player2' move:")))
    if not (b and c):
        i = i-1
        print("wrong instruction!")
        continue
    else:
        a1 = a1 - b2*max(0,2 - c)+max(0,1 - (b-2)**2)*max(0,2 - c)+max(0,1 - (b - 4)**2)
        a2 = a2 - b1*max(0,2 - b)+max(0,1-(c - 2)**2)*max(0,2 - b)+max(0,1 - (c - 4)**2)
        b1 = b1 - (b1 - 1)*max(0,1 - (b - 1)**2)+max(0,1 - (b - 3)**2)
        b2 = b2 - (b2 - 1)*max(0,1 - (c - 1)**2)+max(0,1 -(c - 3)**2)
        print('\n'*2 + "Duang!"* 3 + '\n'*2)
 
if a1==0:
    print("player2 win!")
else:
    print("player1 win!")

print("game over!")
        
