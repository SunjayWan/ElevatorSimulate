def my_python(*fname):
    import keyword
    lines = 0
    notelines = 0
    spacelines = 0
    character = 0
    keydic = {}
    def statistics(fname):
        nonlocal lines,notelines,spacelines,character,keydic
        textfile = open(fname)
        for line in textfile:
            lines += 1
            if line.isspace():
                spacelines += 1
            if line.startswith('#'):
                notelines += 1
            else:
                for word in line.split(): 
                    character += len(word)
                    if word in keyword.kwlist:
                        keydic[word] = keydic.get(word,0) + 1
        textfile.close()
    for s in fname:
        statistics(s)
    for i in keyword.kwlist:
        if i not in keydic:
            keydic[i] = 0
    print('you have written',lines,'lines of Python code,in which there are',
          notelines,'notelines,',spacelines,'spacelines,',character,
          'character,The usage of keywords are as follows:',keydic)
            
            
print(my_python('10.py','12.py','13.py'))

    
    