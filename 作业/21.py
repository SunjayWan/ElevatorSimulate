def statstudent(infname):
    nlist = [0]*5
    textfile = open(infname)
    for line in textfile:
        grade = int(line.split()[1])
        if 0 <= grade < 60:
            nlist[0] += 1
        elif 60 <= grade < 70:
            nlist[1] += 1
        elif 70 <= grade < 80:
            nlist[2] += 1
        elif 80 <= grade < 90:
            nlist[3] += 1
        elif 90 <= grade <= 100:
            nlist[4] += 1
    n = max(nlist)
    print('0~59  ',str(nlist[0]).rjust(n+2),'|','X'*nlist[0],sep = '')
    print('60~69 ',str(nlist[1]).rjust(n+2),'|','X'*nlist[1],sep = '')
    print('70~79 ',str(nlist[2]).rjust(n+2),'|','X'*nlist[2],sep = '')
    print('80~89 ',str(nlist[3]).rjust(n+2),'|','X'*nlist[3],sep = '')
    print('90~100',str(nlist[4]).rjust(n+2),'|','X'*nlist[4],sep = '')
    textfile.close()
statstudent("sun-data.txt")    
    
    
    
    
    

    
    
    
    
    
    
    
#请仿照书上⽤print的⽅式打印直⽅图，直⽅图按照[0, 60), [60, 70), [70, 80), [80, 90), [90, 
#100]的⽅式划分，如果某个区间内有n个学⽣，则输出 (n // 10) 个‘X’。直⽅图中空格数⽬不做
#要求，但需要保证每⼀⾏